import numpy as np
from states import check_normalization, check_states
from gates import apply_gate, check_unitary, H, X

alpha = 1
beta = 0

state_zero = np.array([alpha, beta], dtype=complex)

M = (1/np.sqrt(2))*np.array([[1, 1], [1, 1]], dtype=complex) #False nonunitary gate for testing
invalid_state = np.array([.3, .4], dtype=complex) #Invalid state for testing
A = np.array([[1, 0], [1, 1], [0, 0]], dtype=complex)
#print(check_unitary())

h_state_zero = apply_gate(state_zero, H)
h_twice_state = apply_gate(h_state_zero, H)

h_twice_prob = np.abs(h_twice_state)**2
h_state_zero_prob = np.abs(h_state_zero)**2

print("Normalization:", check_normalization(state_zero))
print("State comparison:", check_states(state_zero, h_twice_state))
