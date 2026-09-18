# MTFS-Holodeck-Sandbox
A Geometric Reality Sandbox for Safe AI Experimentation
MTFS Holodeck is an experimental, open-source sandbox for studying how AI agents can safely observe, experiment with, and control complex dynamical systems without direct access to the real world.
Give the AI a laboratory before giving it a lever.
The current prototype combines a constrained magnetic-dipole environment with structured state observation and a macroscopic Rabi–Bloch test layer.
Research focus
Safe exploration
Bounded intervention
State-dependent control
Learning when to WAIT
Energy–geometry separation
Experimental falsification
Reproducible AI-agent experiments
Important scientific boundary
The magnetic-dipole and Rabi–Bloch components are computational models. Results in this repository describe behavior within the implemented simulator; they are not claims of a new physical law, quantum advantage, or physical quantum-computing device.
Architecture
┌─────────────────────┐
                  │       AI AGENT      │
                  │  Observe → Reason   │
                  │     → Choose        │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │    SAFETY GATE      │
                  │ Bound / Validate /  │
                  │      Reject         │
                  └──────────┬──────────┘
                             │
                             ▼
          ┌──────────────────────────────────┐
          │           MTFS HOLODECK          │
          │                                  │
          │ Magnetic dipoles + geometry      │
          │ fields + phase + topology       │
          └────────────────┬─────────────────┘
                           │
                           ▼
                  ┌─────────────────────┐
                  │ OBSERVATION ENGINE  │
                  │ E G C Φ κ A I M     │
                  │ + Δstate metrics    │
                  └──────────┬──────────┘
                             │
                             ▼
                       STATE + ΔSTATE
                             │
                             └──────────► AI
Repository layout
MTFS-HoloDeck/
├── README.md
├── requirements.txt
├── LICENSE
├── GRANT_SUMMARY.md
├── SAFETY_CASE.md
├── EXPERIMENTAL_RESULTS.md
├── REPRODUCIBILITY.md
├── ROADMAP.md
├── FUTURE_RESEARCH.md
├── holodeck/
│   ├── __init__.py
│   ├── config.py
│   ├── types.py
│   ├── geometry.py
│   ├── magnetic_dipole.py
│   ├── observations.py
│   ├── safety.py
│   ├── sandbox.py
│   └── agent.py
├── rabi_bloch/
│   ├── __init__.py
│   └── simulator.py
├── experiments/
│   ├── run_smoke_test.py
│   └── run_rabi_bloch.py
└── results/
    └── .gitkeep
Quick start
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python experiments/run_smoke_test.py
python experiments/run_rabi_bloch.py
The skeleton is intentionally small. The goal is to provide a clean research foundation into which the existing MTFS Holodeck experiments can be migrated without obscuring the experimental record.
Core observation
The sandbox tracks a structured state:
[ S = [E,G,C,\Phi,\kappa,A,I,M] ]
and distinguishes energetic activity from geometric activity:
[ D_E = |\Delta E|,\qquad D_G = ||\Delta\kappa|| ]
with the bounded separation score:
[ S_{EG} = \frac{D_G-D_E}{D_G+D_E+\epsilon}. ]
The 9:1 regime is an operational simulator-defined regime, not a physical constant.
Research philosophy
If an experiment produces an exciting result, try to break it.
The project therefore emphasizes:
passive baselines
matched controls
sham windows
held-out seeds
parameter sweeps
ablations
explicit limitations
reproducibility
falsification
The Holodeck should be capable of discovering that an apparently useful intervention is actually harmful or protocol-dependent.
Current research milestones
Prototype 1 — Sandbox
Constrained actions, toroidal geometry, observations, and state transitions.
Prototype 4 — Magnetic-dipole substrate
Interacting magnetic moments, fields, energy, geometry, phase, curvature proxies, and coherence.
Prototype 5A — Blind detection
Passive trajectories showed detectable precursors to strong energy–geometry separation.
Prototype 5B — Protective control
A minimal WATCH/minimal-intervention policy preserved long-lived geometry-dominant behavior, while random/aggressive intervention shortened and disrupted those episodes.
Causal-window experiments
A first gated-drive experiment appeared to show a geometry-timing advantage relative to a sham window. A stricter continuous-drive experiment removed the scheduling confound and reversed that result.
That negative result is retained as part of the scientific record.
Current question
Instead of assuming:
high S_EG → intervene
the project now asks:
observed state + proposed action → state-dependent consequence
This is the basis for future conservative model-based control.
Author
Ricardo Humberto Castañeda
Independent AI Researcher & Lead Architect, MTFS Project
