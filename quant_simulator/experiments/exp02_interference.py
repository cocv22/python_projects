import numpy as np
from gates import H, apply_gate
from states import check_normalization

plus_state = (1/np.sqrt(2))*np.array([1, 1], dtype=complex)
minus_state = (1/np.sqrt(2))*np.array([1, -1], dtype=complex)

print(check_normalization(minus_state))
print(check_normalization(plus_state))

transformed_plus = apply_gate(plus_state, H)
