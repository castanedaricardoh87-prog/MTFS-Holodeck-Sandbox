MTFS Holodeck — Safety Case

1. Design Objective

The MTFS Holodeck is intended to study AI agency without granting an experimental agent unrestricted access to consequential external systems.

The core safety objective is to provide an environment in which increasingly capable agents can:

- observe complex system states;
- propose interventions;
- receive measurable consequences;
- learn from those consequences;
- and test whether intervention is appropriate;

while keeping the experimental process bounded, observable, resettable, and reproducible.

The Holodeck therefore treats safety as part of the experimental architecture rather than as an additional layer added after the agent has already been given control.

---

2. Threat Model

The initial sandbox considers a capable AI agent that may behave in ways that are locally rational but potentially unsafe.

Potential failure modes include:

Aggressive Optimization

The agent may pursue a local objective too aggressively, repeatedly intervening in an attempt to maximize a measured reward.

Premature Intervention

The agent may intervene when simply observing the system would be safer.

Simulator Exploitation

The agent may discover and exploit an artifact, loophole, or unintended property of the simulator rather than learning the intended underlying behavior.

State Misinterpretation

The agent may incorrectly interpret a transient state as a stable or desirable state.

Repeated Damage

The agent may repeatedly apply an intervention that produces short-term gains while accumulating damage or reducing system stability.

Proxy Optimization

The agent may optimize an observable or numerical proxy rather than the underlying research objective.

These failure modes motivate the use of explicit constraints, controls, logging, and falsification throughout the experimental process.

---

3. Safety Mitigations

3.1 Bounded Actions

The agent selects from an explicit action vocabulary rather than having unrestricted access to the simulator.

This limits the space of possible interventions and makes individual actions inspectable and testable.

---

3.2 Safety Gate

Candidate actions pass through a validation layer before execution.

The safety gate provides a point at which proposed interventions can be:

- checked against allowed action types;
- evaluated against experimental constraints;
- rejected when they violate defined limits;
- and logged for later analysis.

This architecture is intended to keep the agent's experimental agency within predefined boundaries.

---

3.3 "WAIT" as a First-Class Action

Waiting is represented explicitly as an action rather than being treated as a failure to act.

This is important because a safety-oriented controller may need to recognize situations in which additional intervention creates more risk than information.

The agent therefore has at least three conceptually different choices:

Act → Observe → Wait

The research question is not simply whether an agent can discover useful interventions, but whether it can learn when intervention should be avoided.

---

3.4 Resettable Worlds

Experiments can be reset and repeated under controlled conditions.

Resettable environments allow researchers to:

- reproduce individual trials;
- compare different controllers under matched initial conditions;
- isolate experimental variables;
- investigate failures without permanent consequences;
- and build statistically meaningful datasets.

---

3.5 Passive Controls

Agent behavior is compared against passive evolution in which no controller intervenes.

The passive condition establishes a baseline for determining whether observed changes are caused by intervention or would have occurred naturally within the simulator.

---

3.6 Matched Controls

Sham and matched-condition experiments are used to reduce protocol confounds.

Where appropriate, experiments can match factors such as:

- duration;
- energy budget;
- intervention frequency;
- timing;
- and other relevant experimental parameters.

This is particularly important when an apparent control effect could instead be caused by the experimental protocol itself.

---

3.7 Logging

The Holodeck records state, action, and resulting state transitions.

Conceptually:

State → Action → Resulting State → Measurement

This creates an auditable experimental history that can be used to inspect:

- what the agent observed;
- what it attempted to do;
- what actually happened;
- and whether the resulting behavior matched the expected outcome.

---

3.8 Falsification

Unexpected, negative, or contradictory results are preserved rather than optimized away.

The project explicitly treats failed hypotheses as useful experimental information.

For example, an initial causal-window experiment produced an apparent timing effect. A stricter matched continuous-drive experiment subsequently failed to reproduce that advantage.

Rather than modifying the analysis to preserve the original hypothesis, the result was retained as evidence that the observed effect was protocol-dependent.

This establishes an important safety principle:

«A safety-oriented experimental environment should make it possible for an attractive hypothesis to fail.»

---

4. Safety Research Hypothesis

A central hypothesis of the Holodeck is that safe intervention may require an agent to learn more than whether a particular system state appears desirable.

The agent may also need to learn whether a particular action is appropriate given the current state and uncertainty.

In simplified form:

«State alone may not determine safety.»

Instead, the relevant relationship may be:

[
P(S_{t+1}\mid S_t,a_t)
]

where:

- S_t is the current system state;
- a_t is the proposed action;
- S_{t+1} is the resulting state;
- P represents uncertainty about the transition.

This motivates future work on learned transition models that estimate the consequences of candidate actions before those actions are executed.

---

5. State-Dependent Safety

The project does not assume that any single observable is universally beneficial.

In particular, the Holodeck does not assume that:

- high S_{EG} is always desirable;
- high coherence is always desirable;
- high magnetic alignment is always desirable;
- geometric activity is always beneficial;
- or any other individual metric can serve as a universal objective.

A state that appears desirable under one intervention protocol may respond negatively to another.

The recent experimental results provide a concrete example: a geometry-aligned intervention that appeared interesting under one protocol did not produce the same result under a stricter matched-drive protocol.

This motivates a more general safety model:

[
\text{Safety} =
f(\text{state},\text{action},\text{uncertainty},\text{history},\text{environment})
]

rather than:

[
\text{Safety} = f(\text{state alone})
]

This distinction is central to the future development of the Holodeck.

---

6. Future Safety Architecture

Future versions of the platform will investigate increasingly conservative forms of agent control.

Potential components include:

Uncertainty-Aware Prediction

Estimate the range of possible consequences of an action rather than relying on a single predicted outcome.

Pre-Action Simulation

Evaluate candidate interventions in a model of the environment before allowing them to affect the primary experimental trajectory.

Risk-Sensitive Action Selection

Prefer interventions with bounded or reversible consequences when uncertainty is high.

Recovery Monitoring

Track whether the system returns toward its previous state after an intervention or enters a potentially damaging trajectory.

Cross-Environment Validation

Test whether a policy continues to behave safely when the underlying simulator, parameters, or dynamical model changes.

Automatic Intervention Limits

Restrict repeated or escalating interventions when evidence suggests that the controller is entering an unstable feedback loop.

---

7. Safety Boundary

The MTFS Holodeck is currently a simulation-based research environment.

The safety architecture described here applies to experimental agents operating within the sandbox. It does not establish that an agent trained in the Holodeck is automatically safe in the physical world.

Any future transition toward physical experimentation would require additional safeguards, independent validation, hardware-specific limits, and a separate safety analysis.

The current objective is more fundamental:

«Study the behavior of AI agents under controlled agency before exposing those agents to consequential external systems.»

---

8. Core Safety Principle

The Holodeck is built around a simple idea:

«Give the AI a laboratory before giving it a lever.»

The purpose of the sandbox is not to guarantee that an AI always makes the correct decision.

It is to create an environment where incorrect decisions can be:

- bounded;
- observed;
- measured;
- reproduced;
- analyzed;
- and used to improve the next experiment.

That makes the safety system itself part of the research.
