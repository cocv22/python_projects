import numpy as np
from states import check_normalization

X = np.array([[0, 1], [1, 0]], dtype=complex)
H = (1/np.sqrt(2))*np.array([[1, 1], [1, -1]], dtype=complex)

def check_unitary(gate):
    con_gate = gate.conj().T
    finalized_gate = con_gate@gate
    
    size = finalized_gate.shape
    I = np.eye(size[0], size[1], dtype=complex)
    
    return np.allclose(con_gate@gate, I)

def apply_gate(state, gate):
    if not check_normalization(state) or not check_unitary(gate):
        raise ValueError("Please enter a normalized state and an unitary gate for further computation.")
    
    return gate @ state

print(check_unitary(X))