Reproducibility

Reproducibility is a core design requirement of the MTFS Holodeck.

The purpose of this repository is not only to demonstrate interesting simulator behavior, but to make it possible for another researcher to determine how a result was produced, under what conditions it appeared, and whether it survives independent repetition.

Experimental results should therefore be treated as configuration-dependent observations rather than universal conclusions.

---

Environment

The current computational environment is based on:

- Python 3.10+
- PyTorch
- NumPy

Exact package versions should be recorded in the project environment and requirements files as the implementation matures.

---

Determinism and Experimental Recording

Every reported experiment should record enough information to reconstruct the experimental conditions.

At minimum, this includes:

- random seed
- simulator parameters
- controller parameters
- timestep
- trajectory count
- initial conditions
- action schedule
- observation configuration
- evaluation horizon
- control/sham condition
- relevant stopping or termination criteria

When stochastic components are introduced, their sources of randomness should be explicitly identified.

A result without its corresponding configuration should be considered incomplete.

---

Seeds and Initial Conditions

Random seeds should be treated as part of the experimental specification.

Where possible, experiments should distinguish between:

training seeds
validation seeds
held-out evaluation seeds

Initial conditions should also be recorded rather than generated implicitly.

This helps prevent a result from appearing reproducible simply because the same favorable starting conditions were accidentally reused.

---

Recommended Evaluation Protocol

Learned Predictors

For learned prediction models, train/test separation should occur at the trajectory or seed level, not at the individual time-point level.

Preferred

Trajectory 1 ───────► TRAIN
Trajectory 2 ───────► TRAIN
Trajectory 3 ───────► TRAIN

Trajectory 4 ───────► TEST
Trajectory 5 ───────► TEST

Avoid

Same trajectory
      ↓
randomly split individual time points
      ↓
TRAIN + TEST

Random time-point splitting can allow highly correlated neighboring observations from the same trajectory to appear in both sets, producing an overly optimistic estimate of generalization.

---

Parameter Holdout

Where computationally feasible, evaluation should also hold out parameter combinations, not only random trajectories.

For example:

Training
├── Parameter set A
├── Parameter set B
└── Parameter set C

Held-out evaluation
└── Parameter set D

This provides a stronger test of whether a learned relationship reflects a general feature of the simulator rather than memorization of a particular configuration.

---

Prediction Metrics

For binary prediction tasks, report:

- ROC-AUC
- base rate
- calibration
- sample count
- prediction horizon

Where appropriate, additional metrics such as precision-recall performance should also be reported, particularly when the event being predicted is relatively uncommon.

Metrics should be accompanied by the underlying evaluation protocol so that apparently different results can be compared meaningfully.

---

Controls

Experiments involving intervention should retain appropriate controls.

At minimum, the project recommends considering:

- passive control
- matched intervention control
- sham intervention
- outside-window control
- held-out seeds
- parameter perturbations

Controls should be designed to test plausible alternative explanations rather than simply provide a comparison condition.

The causal-window experiments demonstrate why this matters: an initially promising result can change when a hidden scheduling or duty-cycle difference is removed.

---

Reproducible Experimental Record

Each major experiment should ideally produce a record containing:

Experiment ID
Date / version
Code revision
Random seed(s)
Simulator configuration
Controller configuration
Initial conditions
Timestep
Trajectory count
Action schedule
Control condition
Evaluation metrics
Raw results
Summary statistics
Known limitations

This creates a chain from:

Code
  ↓
Configuration
  ↓
Trajectory
  ↓
Measurement
  ↓
Analysis
  ↓
Reported result

The objective is to make that chain inspectable.

---

Current Status

The repository is currently a clean research architecture for migrating and organizing the existing MTFS Holodeck experiments.

The reusable numerical modules are intentionally compact.

The historical experiments, results, controls, and negative findings are kept conceptually separate from the reusable simulator architecture so that future researchers can distinguish:

what the framework is

from

what a particular experiment happened to produce.

As the project develops, the reproducibility layer will expand to include versioned configurations, standardized experiment runners, saved seeds and initial conditions, automated result summaries, and machine-readable experiment metadata.

---

Reproducibility Principle

The goal is not merely:

«"Can I run my experiment again?"»

The stronger question is:

«"Can another researcher determine exactly what I did, reproduce the conditions, challenge the result, and potentially prove me wrong?"»

That standard is central to the MTFS Holodeck research process.
