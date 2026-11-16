import numpy as np

# Task 1: Define the state |0>

alpha = 1
beta = 0

state_zero = np.array([alpha, beta], dtype=complex)

# Task 3: Calculate the measurement
# probabilities for your states

prob_zero = np.abs(alpha)**2
prob_one = np.abs(beta)**2

# Task 4: Verify that the probabilities

def check_normalization(state):
    probabilities = np.abs(state)**2
    total_probability = np.sum(probabilities)
    
    return np.isclose(total_probability, 1)

X = np.array([[0, 1], [1, 0]], dtype=complex)

new_state = X @ state_zero

print(check_normalization(new_state))

print("Og state: ", state_zero)
print("New state: ", new_state)