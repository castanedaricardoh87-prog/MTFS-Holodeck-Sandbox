from rabi_bloch.simulator import (
    RabiBlochSimulator, spectral_purity, contrast, dominant_frequency
)

sim = RabiBlochSimulator(dt=0.01, damping=0.02)

cases = [
    ("resonant-x", dict(omega=0.14, detuning=0.0, phase=0.0, drive_axis="x")),
    ("resonant-y", dict(omega=0.14, detuning=0.0, phase=0.0, drive_axis="y")),
    ("detuned-x", dict(omega=0.14, detuning=0.35, phase=0.0, drive_axis="x")),
]

for name, params in cases:
    t, m = sim.run(duration=100.0, **params)
    mz = m[:, 2]
    print(
        name,
        "contrast=", round(contrast(mz), 4),
        "purity=", round(spectral_purity(mz), 4),
        "dom_freq=", round(dominant_frequency(mz, sim.dt), 4),
    )
