import numpy as np

alpha = 1
beta = 0

X = np.array([[0, 1], [1, 0]], dtype=complex)
H = (1/np.sqrt(2))*np.array([[1, 1], [1, -1]], dtype=complex)

state_zero = np.array([alpha, beta], dtype=complex)

h_state_zero = H @ state_zero
h_twice_state = H@h_state_zero
h_state_zero_prob = np.abs(h_state_zero)**2

def check_normalization(state):
    probabilities = np.abs(state)**2
    total_probability = np.sum(probabilities)
    
    return np.isclose(total_probability, 1)

print(check_normalization(h_state_zero))

print(h_state_zero)
print(h_state_zero_prob)
