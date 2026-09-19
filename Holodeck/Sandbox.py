import torch
from .config import HolodeckConfig
from .geometry import toroidal_positions
from .types import Node, SandboxState, ActionType
from .magnetic_dipole import MagneticDipoleDynamics
from .observations import make_observation
from .safety import ActionSafetyGate

class MTFSHolodeck:
    def __init__(self, config=None):
        self.cfg = config or HolodeckConfig()
        self.rng = torch.Generator().manual_seed(self.cfg.seed)
        positions = toroidal_positions(self.cfg.n_nodes)
        moments = torch.randn((self.cfg.n_nodes, 3), generator=self.rng)
        moments /= torch.linalg.vector_norm(moments, dim=1, keepdim=True) + 1e-8
        energies = torch.ones(self.cfg.n_nodes) * 0.27
        phases = torch.zeros(self.cfg.n_nodes)

        self.state = SandboxState([
            Node(positions[i], moments[i], float(energies[i]), float(phases[i]))
            for i in range(self.cfg.n_nodes)
        ])
        self.dynamics = MagneticDipoleDynamics(
            dt=self.cfg.dt,
            mix=self.cfg.magnetic_mix,
            geom_strength=self.cfg.geom_strength,
            generator=self.rng,
        )
        self.gate = ActionSafetyGate()
        self.last_energy = None
        self.last_kappa = None

    def observe(self):
        obs = make_observation(
            self.state,
            previous_energy=self.last_energy,
            previous_kappa=self.last_kappa,
            epsilon=self.cfg.epsilon,
        )
        self.last_energy = obs["energy"]
        self.last_kappa = obs["kappa"].clone()
        return obs

    def step(self, action=ActionType.WAIT, magnitude=0.0):
        if not self.gate.validate(action, magnitude):
            raise ValueError("Action rejected by safety gate.")

        positions = torch.stack([n.position for n in self.state.nodes])
        moments = torch.stack([n.moment for n in self.state.nodes])
        energies = torch.tensor([n.energy for n in self.state.nodes])
        phases = torch.tensor([n.phase for n in self.state.nodes])

        if action == ActionType.PULSE_FIELD:
            energies += 0.5 * magnitude
        elif action == ActionType.INSERT_CATALYST:
            energies *= 0.8
            phases += 0.2 * magnitude
        elif action == ActionType.CHANGE_TOPOLOGY:
            self.state.topology_openings = max(0, min(3, self.state.topology_openings + (1 if magnitude > 0 else -1)))
        elif action == ActionType.MEASURE:
            pass

        positions, moments, energies, phases = self.dynamics.step(
            positions, moments, energies, phases
        )

        for i, node in enumerate(self.state.nodes):
            node.position = positions[i]
            node.moment = moments[i]
            node.energy = float(energies[i])
            node.phase = float(phases[i])

        self.state.time += 1
        return self.observe()
