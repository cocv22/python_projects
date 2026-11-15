import numpy as np

# Mini Quantum Simulator
# Phase 1: Quantum state representation

# Task 1: Define the state |0>

alpha = 1
beta = 0

state_zero = np.array([alpha, beta], dtype=complex)

#print(state_zero)
# Task 2: Define the state |1>

alpha = 0
beta = 1

state_one = np.array([alpha, beta], dtype=complex)

#print(state_one)

# Task 3: Calculate the measurement
# probabilities for your states

state_one = np.array([0,1], dtype=complex)

alpha = state_one[0]
beta = state_one[1]

prob_zero = np.abs(alpha)**2
prob_one = np.abs(beta)**2

print("Probability of 0:", prob_zero)
print("Probability of 1:", prob_one)

# Task 4: Verify that the probabilities
# for each state sum to 1