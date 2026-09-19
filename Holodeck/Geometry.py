import torch

def toroidal_positions(n: int, R: float = 2.0, r: float = 0.7) -> torch.Tensor:
    """Simple toroidal route used by the prototype."""
    t = torch.arange(n, dtype=torch.float32)
    theta = 2 * torch.pi * t / n
    phi = theta
    x = (R + r * torch.cos(phi)) * torch.cos(theta)
    y = (R + r * torch.cos(phi)) * torch.sin(theta)
    z = r * torch.sin(phi)
    return torch.stack([x, y, z], dim=1)

def curvature_proxy(positions: torch.Tensor) -> torch.Tensor:
    """Discrete local curvature/activity proxy, not differential mean curvature."""
    prev_ = torch.roll(positions, 1, 0)
    next_ = torch.roll(positions, -1, 0)
    second = next_ - 2 * positions + prev_
    return torch.linalg.vector_norm(second, dim=1)
  
