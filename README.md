MTFS Holodeck

A Geometric Reality Sandbox for Safe AI Experimentation

Give the AI a laboratory before giving it a lever.

MTFS Holodeck is an experimental, open-source research environment for studying how AI agents can observe, reason about, experiment within, and control complex dynamical systems without giving them direct access to consequential real-world systems.

The central idea is simple:

«Before an AI system is trusted with powerful actions in the real world, give it a bounded world in which its decisions can be observed, measured, challenged, and safely rejected.»

The Holodeck provides that world.

Instead of allowing an experimental agent to immediately manipulate external infrastructure, the agent operates inside a constrained computational environment with:

- explicit state representation
- bounded actions
- safety validation
- deterministic and reproducible experiments
- passive baselines
- matched controls
- intervention logging
- state-transition measurements
- falsification experiments
- held-out seeds and parameter sweeps

The goal is not to make an AI agent powerful by removing constraints.

The goal is to study whether an agent can become useful while remaining constrained, observable, and willing to do nothing when intervention is not justified.

---

Why a Holodeck?

Many AI-control experiments focus on whether an agent can accomplish an objective.

MTFS Holodeck adds another question:

«Can the agent recognize when acting is unnecessary, harmful, premature, or unsupported by the observed state?»

This creates a different experimental target.

Instead of:

Observe → Act → Reward

the Holodeck investigates:

Observe
   ↓
Estimate state
   ↓
Evaluate possible consequences
   ↓
Safety gate
   ↓
ACT / WAIT / REJECT
   ↓
Measure resulting state
   ↓
Compare prediction with reality

The environment is deliberately designed so that inaction is a legitimate action.

That makes it possible to study conservative AI behavior experimentally rather than assuming that more intervention is better.

---

What is MTFS?

MTFS is the broader research architecture behind the Holodeck.

The Holodeck is one experimental implementation of that architecture: a Geometric Reality Sandbox in which information, state, geometry, dynamics, observation, and intervention can be studied together.

The current implementation uses a computational magnetic-dipole substrate because it provides a useful combination of:

- interacting components
- field-dependent behavior
- emergent structure
- energy changes
- geometric changes
- coherence
- phase relationships
- transient regimes
- controllable perturbations

This makes it possible to ask questions that are difficult to study with a simple static benchmark.

---

Current Research Question

The project began with a simple hypothesis:

High energy–geometry separation
            ↓
       intervene

Experiments have made that assumption more complicated.

The current research question is:

Observed state + proposed action
            ↓
   predicted consequence
            ↓
      safety evaluation
            ↓
       ACT / WAIT
            ↓
      observed consequence

In other words:

«Can an AI learn that the correct intervention depends on the state and the predicted consequence of the action—not simply on the presence of an interesting regime?»

This is the foundation for future conservative, model-based control experiments.

---

Experimental Environment

The current Holodeck prototype contains a constrained dynamical environment based on interacting magnetic dipoles.

The simulated substrate can represent:

- magnetic moments
- particle positions
- interaction energies
- external fields
- phase
- geometric structure
- curvature/activity proxies
- magnetic coherence
- attractor-like behavior
- controlled perturbations

The agent does not receive unrestricted access to the simulator.

Actions pass through a safety layer that can:

1. validate an action
2. enforce bounds
3. reject invalid interventions
4. record the decision
5. return the resulting state

This allows the experiment to distinguish between:

what the agent wanted to do

and

what the environment actually allowed it to do.

---

Core State Representation

The Holodeck tracks a structured state:

[
S = [E,G,C,\Phi,\kappa,A,I,M]
]

where the current implementation represents quantities associated with:

- E — energy
- G — geometric state/activity
- C — coherence
- Φ — phase
- κ — curvature/geometric structure proxy
- A — attractor-related state
- I — information/interaction measure
- M — magnetic coherence

The exact interpretation of individual observables is implementation-dependent and documented in the simulator.

The important architectural principle is that the environment does not reduce its state to a single scalar reward.

It exposes a structured state that allows the agent's decisions to be evaluated against multiple dimensions of system behavior.

---

Energy vs. Geometry

One of the central experimental ideas is to distinguish energetic activity from geometric activity.

The current implementation defines:

[
D_E = |\Delta E|
]

and

[
D_G = ||\Delta\kappa||
]

A bounded separation score is then:

[
S_{EG} =
\frac{D_G-D_E}
{D_G+D_E+\epsilon}
]

This provides a normalized way to describe situations in which geometric change is large relative to energetic change.

The project refers to one experimentally observed regime as the 9:1 regime, where geometric activity substantially exceeds energetic activity.

Important limitation

9:1 is an operational simulator-defined regime.

It is not being proposed as a universal physical constant or a newly discovered physical law.

The purpose of the metric is to create a measurable experimental regime that can be reproduced, challenged, and potentially falsified.

---

The Safety Architecture

The Holodeck separates the AI agent from the underlying dynamical system.

┌──────────────────────────────┐
│           AI AGENT           │
│                              │
│       Observe → Reason       │
│             ↓                │
│          Propose             │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         SAFETY GATE          │
│                              │
│   Bound → Validate → Reject  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         MTFS HOLODECK        │
│                              │
│ Magnetic dipoles             │
│ Fields                       │
│ Geometry                     │
│ Phase                        │
│ Controlled perturbations     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      OBSERVATION ENGINE      │
│                              │
│ E G C Φ κ A I M              │
│ Δstate metrics               │
└──────────────┬───────────────┘
               │
               ▼
        STATE + ΔSTATE
               │
               └──────────► AI

This architecture makes the state transition a first-class experimental object.

The question is not simply:

«What did the agent do?»

It is:

«What changed because the agent did it?»

---

Experimental Philosophy

The project follows a deliberately adversarial research philosophy:

«If an experiment produces an exciting result, try to break it.»

A promising result is treated as the beginning of an investigation, not the end.

Experiments therefore emphasize:

- passive baselines
- matched controls
- sham windows
- held-out random seeds
- parameter sweeps
- ablation studies
- alternative explanations
- temporal controls
- negative results
- explicit limitations
- reproducibility
- falsification

The Holodeck should be capable of demonstrating that an apparently useful intervention:

- does nothing
- is harmful
- only works under specific conditions
- depends on timing
- is explained by a confound
- fails under a control condition
- or disappears when the experiment is made more rigorous

Those outcomes are scientifically valuable.

---

Research Milestones

Prototype 1 — Sandbox

Established the initial constrained environment:

- bounded actions
- toroidal/geometric environment
- structured observations
- state transitions
- experimental action loop

The purpose was to establish the basic agent → safety → environment → observation architecture.

---

Prototype 4 — Magnetic-Dipole Substrate

Introduced a richer dynamical substrate containing interacting magnetic moments.

The environment tracks quantities associated with:

- magnetic interactions
- fields
- energy
- geometry
- phase
- coherence
- curvature/activity
- emergent structure

This provided a more complex environment in which state-dependent behavior could be studied.

---

Prototype 5A — Blind Detection

Prototype 5A tested whether naturally occurring strong energy–geometry separation could be detected without allowing the detector to use future information.

The experiment found measurable predictive structure in passive trajectories.

In particular, geometric activity and magnetic coherence contributed detectable information about future strong-separation events.

The result is therefore framed as:

«The simulator contains measurable precursors to certain dynamical regimes.»

It is not framed as proof that the same relationship exists in physical magnetic systems.

---

Prototype 5B — Protective Control

Prototype 5B investigated whether a minimal-intervention policy could preserve long-lived geometry-dominant episodes.

The experiment compared passive behavior with intervention strategies, including more aggressive/random intervention.

The resulting observations motivated a shift away from treating high separation as an automatic command to intervene.

The important lesson is architectural:

«Detection of an interesting state is not equivalent to justification for intervention.»

---

Causal-Window Experiments

The project then tested whether geometry-related timing could be used to influence a macroscopic Rabi–Bloch-style signal within the simulator.

An initial gated-drive experiment produced a result that appeared to favor geometry-timed intervention relative to a sham condition.

Rather than treating that result as confirmation, the experiment was redesigned.

A stricter continuous-drive experiment removed an important scheduling confound.

The result changed.

The apparent advantage disappeared and the measured relationship reversed.

This negative result is intentionally retained.

It is an important part of the experimental record because it demonstrates the project's intended methodology:

Interesting result
      ↓
Identify possible confound
      ↓
Strengthen experimental control
      ↓
Repeat experiment
      ↓
Result changes
      ↓
Retain the failure

The project does not require every hypothesis to survive.

It requires the experiments to survive attempts to falsify them.

---

Rabi–Bloch Layer

The Holodeck includes a computational Rabi–Bloch test layer for studying whether macroscopic observables can exhibit structured oscillatory behavior under controlled driving.

This layer is used as an experimental measurement framework inside the simulator.

It is not presented as a physical quantum computer.

Likewise, the current results do not establish quantum advantage or a new quantum-mechanical effect.

The purpose is to create another structured dynamical signal against which state-dependent control hypotheses can be tested.

---

Scientific Boundary

This distinction is fundamental to the repository.

«The magnetic-dipole and Rabi–Bloch components are computational models.»

Results in this repository describe behavior produced by the implemented simulator and experimental protocols.

They should not be interpreted as claims of:

- a new physical law
- demonstrated quantum advantage
- a physical quantum-computing device
- experimentally verified quantum control
- a universal relationship between energy and geometry
- or direct evidence that simulator behavior transfers to physical systems

The value of the project is currently in the experimental architecture, control methodology, measurements, and falsifiable computational results.

Physical validation would require separate experiments with appropriate instrumentation and controls.

---

Why WAIT Matters

Most agent environments treat action as the natural expression of intelligence.

MTFS Holodeck treats WAIT as an explicit decision.

An agent may observe a system entering an unusual regime and still decide:

The evidence is insufficient.
WAIT.

That decision can then be evaluated experimentally.

This creates a useful safety question:

«Can an AI learn to distinguish between a state that is interesting and a state that actually justifies intervention?»

That distinction becomes increasingly important as AI systems move from producing information toward controlling processes.

---

Future Direction: Predictive Consequence

The long-term direction is not simply:

State → Action

but:

State
  ↓
Candidate Action
  ↓
Predicted ΔState
  ↓
Safety / Uncertainty Check
  ↓
ACT or WAIT
  ↓
Actual ΔState
  ↓
Prediction Error

This creates a feedback loop in which the agent can be evaluated on more than task completion.

It can also be evaluated on:

- prediction accuracy
- intervention necessity
- intervention cost
- state stability
- recovery
- unintended consequences
- uncertainty calibration
- ability to abstain

This is where the Holodeck could become a useful testbed for conservative model-based AI control.

---

Repository Structure

MTFS-HoloDeck/
│
├── README.md
├── requirements.txt
├── LICENSE
│
├── GRANT_SUMMARY.md
├── SAFETY_CASE.md
├── EXPERIMENTAL_RESULTS.md
├── REPRODUCIBILITY.md
├── ROADMAP.md
└── FUTURE_RESEARCH.md
│
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
│
├── rabi_bloch/
│   ├── __init__.py
│   └── simulator.py
│
├── experiments/
│   ├── run_smoke_test.py
│   └── run_rabi_bloch.py
│
└── results/
    └── .gitkeep

The repository is intentionally compact.

The goal is to establish a clean research foundation into which the existing MTFS experiments can be migrated while keeping the experimental history visible and reproducible.

---

Quick Start

python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

Run the basic environment test:

python experiments/run_smoke_test.py

Run the Rabi–Bloch experiment:

python experiments/run_rabi_bloch.py

Additional experiments and result-generation scripts will be added as the repository is expanded.

---

Reproducibility

The project is being developed around reproducible computational experiments.

Where practical, experiments should document:

- random seeds
- simulator configuration
- parameter values
- action policies
- observation definitions
- control conditions
- evaluation metrics
- experiment duration
- number of trajectories
- exclusion criteria
- statistical summaries
- generated results

A result that cannot be reproduced should be treated as provisional.

---

Road Ahead

The next generation of the Holodeck will focus on state-dependent consequence prediction.

Potential directions include:

1. Model-based control

Predict the effect of candidate actions before executing them.

2. Conservative intervention

Penalize unnecessary interventions and reward successful abstention.

3. Uncertainty-aware control

Allow the agent to explicitly represent:

I don't know.

4. Counterfactual simulation

Test:

What would happen if I act?

without immediately committing the real environment to that action.

5. Intervention replay

Compare the predicted trajectory with the trajectory that actually occurred.

6. Safety stress testing

Deliberately construct situations where:

- aggressive action appears attractive
- the obvious action is harmful
- waiting is optimal
- observations are ambiguous
- the system changes faster than expected
- an intervention produces an unexpected side effect

7. Physical validation

Only after computational hypotheses are sufficiently robust should selected mechanisms be considered for physical experimentation.

---

The Bigger Idea

MTFS Holodeck is not an attempt to give an AI unrestricted power.

It is an attempt to build the experimental space between intelligence and power.

A capable agent should have somewhere to:

- explore
- make mistakes
- encounter uncertainty
- test hypotheses
- experience consequences
- learn when intervention fails
- learn when waiting is preferable
- and have every decision measured

before those same behaviors are connected to systems where mistakes have real-world consequences.

The Holodeck is therefore intended as a research instrument for studying AI agency under controlled conditions.

The central experimental principle is:

«Don't ask only whether an AI can act. Ask whether it can understand the consequences of acting—and recognize when it should not.»

---

Author

Ricardo Humberto Castañeda
Independent AI Researcher & Lead Architect, MTFS Project

---

Status

Experimental / Research Prototype

This repository is an active research project. APIs, experiments, metrics, and interpretations may change as new experiments attempt to reproduce, refine, or falsify earlier results.

Scientific claims should be interpreted according to the documented simulator, experimental protocol, controls, and limitations.Prototype 1 — Sandbox
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
