import torch
from .geometry import curvature_proxy

def bounded_separation(dg: float, de: float, eps: float = 0.02) -> float:
    return float((dg - de) / (dg + de + eps))

def magnetic_coherence(moments: torch.Tensor) -> float:
    n = len(moments)
    if n < 2:
        return 1.0
    dots = moments @ moments.T
    mask = ~torch.eye(n, dtype=torch.bool, device=moments.device)
    return float(dots[mask].mean())

def make_observation(state, previous_energy=None, previous_kappa=None, epsilon=0.02):
    positions = torch.stack([n.position for n in state.nodes])
    moments = torch.stack([n.moment for n in state.nodes])
    energies = torch.tensor([n.energy for n in state.nodes])
    phases = torch.tensor([n.phase for n in state.nodes])

    kappa = curvature_proxy(positions)
    energy = float(energies.sum())
    geom_activity = 0.0 if previous_kappa is None else float(torch.linalg.vector_norm(kappa - previous_kappa))
    energy_activity = 0.0 if previous_energy is None else abs(energy - previous_energy)

    return {
        "energy": energy,
        "geometry": positions.flatten(),
        "coherence": float(torch.linalg.vector_norm(moments.mean(0))),
        "phase": float(phases.mean()),
        "kappa": kappa,
        "attractor": float(1.0 / (1.0 + energies.std())),
        "information": float(state.topology_openings / 3.0),
        "magnetic_coherence": magnetic_coherence(moments),
        "geometric_activity": geom_activity,
        "energy_activity": energy_activity,
        "separation_score": bounded_separation(geom_activity, energy_activity, epsilon),
    }
