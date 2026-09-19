from dataclasses import dataclass

@dataclass
class HolodeckConfig:
    n_nodes: int = 33
    dt: float = 0.05
    epsilon: float = 0.02
    magnetic_mix: float = 0.22
    geom_strength: float = 0.055
    seed: int = 7
  
