from holodeck.sandbox import MTFSHolodeck
from holodeck.types import ActionType

world = MTFSHolodeck()
obs = world.observe()

print("MTFS Holodeck smoke test")
print("nodes:", world.cfg.n_nodes)
print("initial energy:", round(obs["energy"], 4))
print("initial S_EG:", round(obs["separation_score"], 4))

for _ in range(10):
    obs = world.step(ActionType.WAIT)

print("final energy:", round(obs["energy"], 4))
print("final S_EG:", round(obs["separation_score"], 4))
print("OK")
