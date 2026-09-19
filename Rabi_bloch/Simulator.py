import math
import torch

class RabiBlochSimulator:
    """
    Macroscopic Bloch-vector toy model.

    State is (Mx, My, Mz). Drive and detuning produce precession.
    This is a computational model, not a physical quantum-device simulator.
    """

    def __init__(self, dt=0.01, damping=0.02, device="cpu"):
        self.dt = dt
        self.damping = damping
        self.device = device

    def run(self, omega=0.14, detuning=0.0, phase=0.0,
            duration=100.0, initial=None, drive_axis="x"):
        steps = int(duration / self.dt)
        if initial is None:
            m = torch.tensor([0.0, 0.0, 1.0], dtype=torch.float64, device=self.device)
        else:
            m = torch.tensor(initial, dtype=torch.float64, device=self.device)

        history = torch.empty((steps, 3), dtype=torch.float64, device=self.device)
        t = torch.arange(steps, dtype=torch.float64, device=self.device) * self.dt

        for k in range(steps):
            tk = t[k]
            drive = omega * torch.cos(0.0 * tk + phase)

            if drive_axis == "x":
                h = torch.tensor([drive, 0.0, detuning], dtype=torch.float64, device=self.device)
            elif drive_axis == "y":
                h = torch.tensor([0.0, drive, detuning], dtype=torch.float64, device=self.device)
            else:
                raise ValueError("drive_axis must be 'x' or 'y'.")

            dm = torch.cross(h, m, dim=0) - self.damping * m
            m = m + self.dt * dm
            norm = torch.linalg.vector_norm(m)
            if norm > 0:
                m = m / norm
            history[k] = m

        return t.cpu(), history.cpu()

def spectral_purity(signal: torch.Tensor) -> float:
    x = signal - signal.mean()
    spec = torch.abs(torch.fft.rfft(x))
    if len(spec) <= 2 or float(spec.sum()) == 0:
        return 0.0
    power = spec[1:] ** 2
    return float(power.max() / (power.sum() + 1e-12))

def contrast(signal: torch.Tensor) -> float:
    return float(signal.max() - signal.min())

def dominant_frequency(signal: torch.Tensor, dt: float) -> float:
    x = signal - signal.mean()
    spec = torch.abs(torch.fft.rfft(x))
    if len(spec) <= 2:
        return 0.0
    idx = 1 + int(torch.argmax(spec[1:]))
    freqs = torch.fft.rfftfreq(len(x), d=dt)
    return float(freqs[idx])
