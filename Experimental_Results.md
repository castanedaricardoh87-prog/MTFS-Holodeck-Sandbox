Experimental Results

This document records the current computational results of the MTFS Holodeck experiments.

The results below describe the behavior of the implemented simulator under the stated parameterizations and experimental protocols. They are not claims that the same relationships have been demonstrated in physical systems.

A central principle of the project is to preserve negative and confounding results alongside positive observations.

---

1. Geometry-Dominant Regime

Passive trajectories were analyzed for episodes in which the simulator entered the operational 9:1 energy–geometry regime.

Observed results

Measure| Result
Distinct high-9:1 episodes| 59
Trajectories| 30
Mean episodes / trajectory| 1.97
Mean persistence| 20.2 steps
Median persistence| 10 steps
90th percentile persistence| 50 steps
Maximum persistence| 65 steps
Approx. time in regime| 60%

These measurements indicate that geometry-dominant episodes can arise naturally in the passive simulator and can persist for substantial periods.

Interpretation

The result establishes that the operational regime is sufficiently common and persistent to support controlled intervention experiments.

It does not establish that a corresponding 9:1 relationship is a universal physical phenomenon.

The 9:1 designation is defined by the simulator's metrics and parameterization.

---

2. Protective Control

Prototype 5B tested whether a minimal-intervention strategy could preserve geometry-dominant episodes.

The controller used hysteresis to avoid repeatedly entering and exiting the regime because of small fluctuations.

Hysteresis thresholds

[
\text{Enter: } S_{EG} \geq 0.78
]

[
\text{Exit: } S_{EG} < 0.62
]

Results

Condition| Mean Persistence| Episodes / Trajectory| Median Episode| Damage Events| Mean M
Passive| 36.5| 1.04| 35.5| 0.0| 0.612
Protective| 36.4| 1.08| 34.5| 0.0| 0.611
Random| 9.7| 5.17| 1.6| 1.8| 0.412
Aggressive| 5.2| 4.21| 1.0| 1.8| 0.431

Observation

Within this simulator and experimental configuration:

- Passive and protective conditions produced very similar persistence.
- Random intervention produced substantially shorter episodes.
- Aggressive intervention produced the shortest episodes.
- Random and aggressive conditions also produced damage events in the recorded experiments.
- Mean magnetic coherence was lower under the random and aggressive conditions.

Interpretation

The protective policy did not demonstrate that intervention improved the underlying regime.

Instead, its behavior was approximately comparable to passive operation while avoiding the fragmentation observed under the more disruptive intervention strategies.

This supports a narrower conclusion:

«Minimal intervention can preserve behavior that would otherwise be disrupted by unnecessary intervention.»

It does not establish that intervention is beneficial whenever S_{EG} is high.

---

3. Blind Detection — Prototype 5A

Prototype 5A tested whether naturally occurring strong energy–geometry separation could be predicted from passive trajectories.

The detector was evaluated at horizons of approximately 1–5 steps ahead.

Base rates

Horizon| Base Rate
1 step| 7.5%
2 steps| 8.8%
3 steps| 9.2%
4 steps| 10.2%
5 steps| 10.6%

Best single-feature AUC

Horizon| AUC
1 step| 0.779
2 steps| 0.799
3 steps| 0.782
4 steps| 0.765
5 steps| 0.722

The strongest single-feature results were approximately in the 0.72–0.80 AUC range across the tested horizons.

Interpretation

The passive trajectories contain measurable information that can help distinguish upcoming strong-separation events from the background trajectory.

This is evidence for detectability within the simulator.

It is not evidence that the detected features represent a universal physical precursor.

The results remain preliminary and require:

- larger trajectory sets
- trajectory-level validation
- held-out seeds
- additional parameterizations
- feature ablations
- stronger temporal controls

before stronger conclusions can be drawn.

---

4. Initial Causal-Window Experiment

The next experiment asked whether the detected geometry-related state could be used to time a controlled drive.

The initial experiment compared geometry-timed modulation with outside-window and sham conditions.

Initial results

Condition| Contrast| Purity| Fidelity Proxy
Geometry window| 1.988| 0.352| 0.700
Outside window| 1.606| 0.562| 0.943
Sham window| 1.992| 0.234| 0.466

The geometry-versus-sham comparison initially appeared promising because the geometry-window condition produced a higher fidelity proxy than the sham condition.

However, inspection of the protocol identified an important issue:

«The outside-window comparison contained a drive-duty-cycle confound.»

Therefore, the initial result could not cleanly distinguish a geometry-dependent effect from differences in when and how often the drive was applied.

Scientific response

Rather than treating the result as confirmation, the experiment was redesigned to remove this confound.

---

5. Refined Continuous-Drive Experiment

The refined experiment used:

- a continuous baseline drive
- identical small modulation
- matched energy budgets
- geometry-based timing
- sham modulation

This removed the earlier scheduling/duty-cycle ambiguity.

Results

Condition| Contrast| Purity| Fidelity Proxy
Baseline| 1.997| 0.830| 1.657
Sham modulation| 1.997| 0.652| 1.302
Geometry modulation| 1.995| 0.474| 0.946

The geometry-modulated condition did not reproduce the apparent advantage observed in the initial geometry-window experiment.

Instead, under the stricter continuous-drive protocol, the geometry modulation produced lower purity and lower fidelity proxy than both the baseline and sham-modulation conditions.

---

6. Within-Geometry Correlations

Additional analysis was performed within the geometry-modulation condition.

Observed correlations included:

Quantity| Correlation
Mean S_{EG} vs. fidelity proxy| r \approx -0.47
Mean S_{EG} vs. purity| r \approx -0.48
Persistence T_S vs. fidelity proxy| r \approx -0.24
Persistence T_S vs. purity| r \approx -0.24

These relationships are descriptive correlations within the tested simulator configuration.

They should not be interpreted as establishing causation.

The negative direction also demonstrates why simply identifying a high-S_{EG} state is insufficient to determine whether an intervention will produce a desirable outcome.

---

7. Falsification / Boundary Result

The refined continuous-drive experiment is an important result precisely because it weakened the earlier interpretation.

The sequence was:

Initial experiment
        ↓
Geometry-timed result appears promising
        ↓
Potential duty-cycle confound identified
        ↓
Protocol redesigned
        ↓
Continuous drive + matched energy
        ↓
Previous advantage does not survive

The earlier geometry-timing result is therefore retained in the research record, but it is not treated as evidence of a robust causal advantage.

This is an intentional feature of the project.

A result that disappears under stronger controls is still useful because it identifies the boundary of the current hypothesis.

---

8. What the Experiments Currently Support

Taken together, the current experiments support several narrower observations within the simulator:

1. Geometry-dominant episodes occur

The passive system naturally produces measurable periods in which geometric activity substantially exceeds energetic activity according to the operational S_{EG} metric.

2. These episodes can persist

The observed episodes are sufficiently persistent to make them experimentally accessible.

3. Passive trajectories contain predictive information

Prototype 5A found detectable precursors to upcoming strong-separation events.

4. Unnecessary intervention can be disruptive

Random and aggressive intervention fragmented geometry-dominant episodes in the tested configuration.

5. Minimal intervention can preserve passive-like behavior

The protective policy produced persistence close to the passive condition.

6. High separation alone does not justify intervention

The causal-window experiments provide an important warning against treating S_{EG} as a direct intervention trigger.

---

9. What the Experiments Do Not Establish

The current evidence does not establish:

- a universal 9:1 physical law
- a new physical relationship between energy and geometry
- quantum advantage
- a physical quantum-computing mechanism
- that geometry-timed intervention improves Rabi–Bloch behavior
- that S_{EG} is a universal control variable
- that simulator results transfer directly to physical systems
- that correlation between an observation and an outcome establishes causation

These remain open questions requiring further computational testing and, where justified, eventual physical validation.

---

10. Current Scientific Conclusion

The experiments do not support the simple control rule:

[
\boxed{\text{high }S_{EG}\Rightarrow\text{better intervention outcome}}
]

Instead, the results motivate a more conservative hypothesis:

[
\boxed{
(\text{observed state},\text{proposed action})
\Rightarrow
\text{state-dependent response}
}
]

The important shift is from state-triggered intervention to consequence-aware control.

The next stage of MTFS Holodeck research will therefore investigate whether an agent can:

1. observe the current state,
2. propose a candidate action,
3. predict the resulting state transition,
4. estimate uncertainty and risk,
5. choose ACT or WAIT,
6. execute only within the safety envelope,
7. compare predicted and observed consequences,
8. update its model.

That turns the Holodeck from a system for asking:

«"What state is the system in?"»

into a system for asking:

«"Given this state, what will happen if I act—and is acting justified at all?"»

This is the current central control problem of the MTFS Holodeck.
