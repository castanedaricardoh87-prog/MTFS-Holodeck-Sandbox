from dataclasses import dataclass, field
from enum import Enum, auto
import torch

class ActionType(Enum):
    PULSE_FIELD = auto()
    INSERT_CATALYST = auto()
    CHANGE_TOPOLOGY = auto()
    MEASURE = auto()
    WAIT = auto()

@dataclass
class Node:
    position: torch.Tensor
    moment: torch.Tensor
    energy: float
    phase: float
    active: bool = True

@dataclass
class Observation:
    energy: float
    geometry: torch.Tensor
    coherence: float
    phase: float
    kappa: torch.Tensor
    attractor: float
    information: float
    magnetic_coherence: float
    geometric_activity: float
    energy_activity: float
    separation_score: float

@dataclass
class SandboxState:
    nodes: list[Node]
    time: int = 0
    topology_openings: int = 3
    field: torch.Tensor = field(default_factory=lambda: torch.zeros(3))
  
