import torch

class MagneticDipoleDynamics:
    """Small, research-oriented magnetic-dipole toy dynamics."""

    def __init__(self, dt=0.05, mix=0.22, geom_strength=0.055, generator=None):
        self.dt = dt
        self.mix = mix
        self.geom_strength = geom_strength
        self.generator = generator or torch.Generator().manual_seed(7)

    def step(self, positions, moments, energies, phases):
        # Pairwise alignment signal.
        dots = moments @ moments.T
        n = len(moments)
        eye = torch.eye(n, device=moments.device, dtype=torch.bool)
        alignment = dots.masked_fill(eye, 0.0)

        # Local magnetic force proxy.
        diff = positions[:, None, :] - positions[None, :, :]
        dist2 = (diff * diff).sum(-1) + 0.08
        force_mag = alignment / dist2
        force = (force_mag[..., None] * (-diff)).sum(1)

        # Geometric restoring/active term.
        prev_ = torch.roll(positions, 1, 0)
        next_ = torch.roll(positions, -1, 0)
        curvature_force = self.geom_strength * (next_ - 2 * positions + prev_)

        positions = positions + self.dt * (force + curvature_force)

        # Conservative energy diffusion.
        neighbor = 0.5 * (torch.roll(energies, 1) + torch.roll(energies, -1))
        energies = energies + self.mix * (neighbor - energies) * self.dt

        # Moment rotation/noise proxy.
        moments = moments + 0.01 * torch.randn(
            moments.shape, generator=self.generator, device=moments.device
        )
        moments = moments / (torch.linalg.vector_norm(moments, dim=1, keepdim=True) + 1e-8)

        phases = phases + 0.1 * torch.linalg.vector_norm(moments, dim=1) * self.dt

        return positions, moments, energies, phases

