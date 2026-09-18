MTFS Holodeck — Grant Summary

«MTFS Holodeck is an open-source experimental sandbox for studying safe AI agency: an AI can observe a complex dynamical world, propose bounded interventions, measure consequences, and learn when not to act without experimenting directly on the real world.»

---

1. The Problem

As AI systems become increasingly agentic, safety research needs environments where agents can explore the consequences of their actions without requiring irreversible experimentation in the real world.

The central research question is:

«Can an AI learn state-dependent intervention policies while its actions remain bounded, observable, reversible, and experimentally testable?»

The MTFS Holodeck approaches this question by giving an AI agent a controlled experimental environment in which actions, observations, consequences, and failures can be measured systematically.

---

2. The Proposed Solution

The MTFS Holodeck is a computational research sandbox built around a constrained interaction loop:

AI Agent → Safety Validation → Bounded Action → Simulated World → Observation → Measurement → Learning

Rather than allowing an agent unrestricted control, the Holodeck limits the actions available to the agent and records the resulting state transitions.

This creates a laboratory-like environment in which researchers can investigate:

- when an intervention is useful;
- when an intervention is harmful;
- when the system should wait;
- whether apparent control effects survive stricter experimental controls;
- and whether policies learned in one environment transfer to another.

---

3. What Has Already Been Built

The current prototype includes the following components.

Environment and Dynamics

- Constrained action types
- Magnetic-dipole dynamical substrate
- Toroidal/geometric state representation
- Energy and geometry activity measurements
- Coherence measurements
- Magnetic orientation alignment
- Phase measurements
- Attractor measurements
- Local geometric/curvature measurements

AI Interaction and Safety

- Bounded action space
- Safety validation
- Explicit observation interface
- Intervention logging
- Passive baseline conditions
- Random-control conditions
- Protective-control conditions
- Aggressive-control conditions
- "WAIT" as a legitimate action

Experimental Infrastructure

- Persistent-regime detection
- Energy–geometry separation metrics
- Blind short-horizon detection experiments
- Rabi–Bloch dynamical testing
- Matched causal-window controls
- Sham controls
- Explicit falsification experiments

The goal is not simply to demonstrate that an agent can intervene.

The goal is to determine when intervention should occur, when it should not occur, and whether apparent benefits survive controlled experimentation.

---

4. Preliminary Experimental Evidence

The current simulator has produced persistent high-S_{EG}, geometry-dominant episodes.

The operational separation metric is designed to distinguish changes in geometry from changes in scalar energy. In the current experiments, these episodes represent periods in which geometric activity remains substantial while energy activity remains comparatively small.

Persistent-Regime Control

A protective "WATCH" policy was tested against passive, random, and aggressive intervention conditions.

The results showed:

- The passive system maintained long-lived high-S_{EG} episodes.
- The protective "WATCH" policy preserved episode persistence at approximately passive levels.
- Random intervention substantially shortened persistent episodes.
- Aggressive intervention also shortened persistent episodes.
- Random and aggressive intervention reduced the separation state and produced measurable recovery periods.

These results support a limited conclusion:

«In the current simulator, recognizing a geometry-dominant state and avoiding unnecessary intervention can preserve that state, while indiscriminate intervention can disrupt it.»

This is a state-preservation result—not yet a general claim that the system has learned an optimal controller.

---

5. Blind Detection

Blind detection experiments tested whether observations available to the agent contain measurable precursors to strong energy–geometry separation.

The experiments found detectable short-horizon predictive signal at horizons of approximately 1–5 simulation steps.

This provides evidence that the observation space contains information that can be used to distinguish approaching separation events.

Importantly, this experiment was conducted separately from the intervention policy experiments.

That separation helps distinguish:

Detection

from

Control.

The current evidence supports the former more strongly than the latter.

---

6. Causal-Window Testing and Falsification

An initial causal-window experiment produced an apparent timing effect in which intervention aligned with geometry-dominant states appeared different from comparison conditions.

Rather than treating this as confirmation, the experiment was subjected to a stricter control.

A refined continuous-drive experiment:

- matched the baseline and modulation energy budgets;
- matched total experimental duration;
- used real geometry windows;
- used matched-length sham windows;
- compared modulation against an unmodulated baseline.

Under the stricter protocol, the earlier apparent advantage did not generalize.

In fact, geometry-aligned modulation produced lower spectral-purity and fidelity-proxy values than the baseline condition under that parameterization.

Why This Result Matters

This negative result is part of the research contribution.

The sandbox prevented an attractive early observation from automatically becoming a control rule.

Instead, the experimental process revealed that the observed effect was protocol-dependent.

This leads to a revised research hypothesis:

«The consequence of an intervention may depend jointly on the state of the system and the type, timing, amplitude, and phase of the intervention.»

The Holodeck is therefore designed not merely to discover useful interventions, but also to discover when seemingly useful interventions are unsafe, ineffective, or protocol-dependent.

---

7. Safety Thesis

The Holodeck is designed around several safety principles.

Bounded Actions

The AI cannot issue arbitrary commands to the underlying system. Its action space is explicitly defined.

Action Validation

Proposed actions pass through a safety layer before being applied to the simulated environment.

Reversible Experiments

Experiments can be reset and repeated under controlled conditions.

Explicit Observations

The agent receives a defined observation space rather than unrestricted access to the underlying simulator.

Intervention Logging

Actions and resulting state transitions are recorded for analysis and reproducibility.

Passive Baselines

Experiments include conditions in which the system evolves without intervention.

Sham Controls

Control conditions are designed to distinguish genuine state-dependent effects from effects caused by the experimental protocol itself.

Falsification

Hypotheses are deliberately tested under increasingly strict controls rather than accepted solely because an initial experiment produces an interesting result.

"WAIT" as an Action

The agent is explicitly allowed to refrain from intervening.

This is central to the safety objective.

A safe agent should not merely learn:

«"What can I do?"»

It should also learn:

«"When should I do nothing?"»

Separation Between Simulation and Reality

The current Holodeck is a simulation environment. It does not directly control physical systems.

This separation allows potentially risky intervention strategies to be investigated before consideration of any real-world deployment.

---

8. Funding Objective

Funding would support the transition from an experimental prototype into a more robust, reproducible research platform.

Primary Uses of Funding

- Robustify the sandbox architecture
- Expand reproducibility infrastructure
- Run larger controlled experiments
- Develop learned state-transition models
- Develop uncertainty-aware intervention policies
- Strengthen safety gates and action validation
- Conduct cross-environment transfer experiments
- Build public documentation
- Maintain open-source releases
- Produce standardized experimental datasets and benchmarks

---

9. Expected Deliverables

Near Term

Reproducible Benchmark Suite

A collection of standardized experiments for evaluating detection, intervention, persistence, and safety behavior.

Documented Observation/Action API

A clear interface defining what the AI can observe and what actions it can request.

Baseline Controllers

Reference implementations including passive, random, protective, and other bounded control policies.

Intervention-Response Dataset

Structured records connecting:

state → action → consequence → recovery

Experiment Dashboards

Tools for inspecting trajectories, interventions, energy–geometry separation, coherence, and other experimental measurements.

---

Medium Term

Learned State-Transition Model

A model capable of estimating how candidate actions may change the simulated environment.

Uncertainty-Aware Controller

A controller that accounts for uncertainty rather than treating every predicted consequence as certain.

Conservative Action-Selection Policy

A policy designed to prefer low-risk or reversible actions when uncertainty is high.

Cross-Environment Evaluation

Testing whether learned behaviors remain valid when the underlying environment or dynamical model changes.

---

Long Term

The long-term objective is a reusable research platform for studying safe exploration and intervention by increasingly capable AI agents.

The platform could provide a controlled intermediate environment between purely passive AI observation and consequential real-world agency.

The broader research vision is:

«Give the AI a laboratory before giving it a lever.»

---

10. Scientific Boundary

MTFS Holodeck is experimental research software.

Its physics-inspired models are used as simulation substrates for AI-safety experiments. They are not presented as independently validated physical or quantum technologies.

Likewise, observed behavior within the simulator should be interpreted as evidence about the modeled computational system—not automatically as evidence that the same behavior exists in nature.

Future work may investigate additional physical models, computational substrates, and potentially quantum-inspired information-processing concepts, but those investigations will remain subject to the same requirements for controlled experimentation, reproducibility, and falsification.

---

11. Research Philosophy

The MTFS Holodeck is built around a simple principle:

«Interesting results should become stronger through attempts to disprove them, not through increasingly favorable experiments.»

The purpose of the platform is therefore not to guarantee that an AI discovers a useful intervention.

It is to create an environment in which the AI and the researcher can discover:

- what works;
- what fails;
- what is uncertain;
- what is protocol-dependent;
- when intervention causes damage;
- and when the safest action is to wait.

That makes the Holodeck both an experimental platform and a framework for studying responsible AI agency before real-world consequences are involved.
