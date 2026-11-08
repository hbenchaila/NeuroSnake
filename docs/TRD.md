# 1. Interface: 
reset(), step(action) -> (reward, done, info), get_state() -> (11,), render(). Actions are {0: straight, 1: right, 2: left}.

# 2. Feature order: 
danger straight, right, left; direction up, down, left, right; food left, right, up, down.

# 3. Network: 
W1 (11,256), b1 (256), W2 (256,3), b2 (3). He init for the ReLU layer, small init for the output. Huber loss (δ=1) on the taken action only, averaged over the batch.

# 4. Target: 
y = r if terminal, else r + γ·max Q_target(s′). Timeouts (step limit) are truncations, not terminals.

# 5. Starting hyperparameters (to be tuned from observed results, not promises): 
γ=0.95, buffer 50k, batch 64, ε from 1.0 to 0.01, target sync every 500 steps, step limit 100×length. SGD for equivalence tests; Adam (manual in NumPy) for training, to be confirmed on Day 6.

# 6. Seeding: 
one master seed in a saved JSON config, deriving env, NumPy, PyTorch and Python RNGs separately.

# 7. Tolerances: 
NumPy vs PyTorch in float64 with rtol=1e-8; finite-difference check with central differences, relative error below 1e-6.

# 8. Evaluation: 
ε=0, 100 fixed evaluation episodes, 3 training seeds, report mean, median, std and 95% CI, with training and evaluation metrics kept separate.

# 9. Layout change: 
one shared replay_memory.py; folders created only when first used.