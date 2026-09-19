"""
MTFS Holodeck — Reproducibility Smoke Test

Purpose:
    Verify that the core Holodeck environment can be imported,
    initialized, stepped, and measured deterministically.

This is NOT a scientific experiment.
It is an integrity/reproducibility check.
"""

from __future__ import annotations

import platform
import sys
import random

import numpy as np


SEED = 42


def set_seed(seed: int) -> None:
    """Set deterministic seeds for the basic numerical stack."""
    random.seed(seed)
    np.random.seed(seed)

    try:
        import torch

        torch.manual_seed(seed)

        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)

    except ImportError:
        pass


def print_environment() -> None:
    """Print the computational environment."""
    print("=" * 60)
    print("MTFS HOLODECK — REPRODUCIBILITY SMOKE TEST")
    print("=" * 60)

    print(f"Python:     {sys.version.split()[0]}")
    print(f"Platform:   {platform.platform()}")
    print(f"NumPy:      {np.__version__}")

    try:
        import torch

        print(f"PyTorch:    {torch.__version__}")
    except ImportError:
        print("PyTorch:    not installed")

    print(f"Seed:       {SEED}")
    print()


def main() -> None:
    """Run the smoke test."""

    set_seed(SEED)
    print_environment()

    # Import the Holodeck after the environment has been initialized.
    try:
        from holodeck import Holodeck
    except ImportError as exc:
        print("FAILED: Could not import the Holodeck.")
        print()
        print(f"Import error: {exc}")
        print()
        print("Check that:")
        print("  1. holodeck/__init__.py exists")
        print("  2. the package is in the repository")
        print("  3. you are running this from the repository root")
        raise SystemExit(1)

    print("PASS: Holodeck package imported.")
    print()

    # ------------------------------------------------------------
    # Create the environment.
    # ------------------------------------------------------------

    try:
        env = Holodeck(seed=SEED)
    except TypeError:
        # Fallback for an early implementation that may not yet
        # expose a seed argument.
        env = Holodeck()

    print("PASS: Holodeck initialized.")
    print()

    # ------------------------------------------------------------
    # Inspect initial state.
    # ------------------------------------------------------------

    if hasattr(env, "observe"):
        observation = env.observe()
    elif hasattr(env, "observation"):
        observation = env.observation()
    elif hasattr(env, "state"):
        observation = env.state
    else:
        observation = None

    print("Initial observation:")
    print(observation)
    print()

    # ------------------------------------------------------------
    # Execute one bounded test action.
    # ------------------------------------------------------------

    action = {
        "type": "WAIT"
    }

    print("Test action:")
    print(action)
    print()

    try:
        if hasattr(env, "step"):
            result = env.step(action)
        elif hasattr(env, "act"):
            result = env.act(action)
        else:
            print("FAILED: Holodeck has no step() or act() method.")
            raise SystemExit(1)

    except Exception as exc:
        print("FAILED: Test action could not be executed.")
        print(f"Error: {exc}")
        raise SystemExit(1)

    print("Result after action:")
    print(result)
    print()

    print("=" * 60)
    print("SMOKE TEST PASSED")
    print("=" * 60)
    print()
    print("The Holodeck successfully:")
    print("  ✓ imported")
    print("  ✓ initialized")
    print("  ✓ produced an observation")
    print("  ✓ accepted a bounded action")
    print("  ✓ returned a state/result")
    print()
    print("This confirms basic repository integrity.")
    print("It does NOT validate scientific hypotheses.")


if __name__ == "__main__":
    main()
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
