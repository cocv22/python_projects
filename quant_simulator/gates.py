import numpy as np
from states import check_normalization

X = np.array([[0, 1], [1, 0]], dtype=complex)
H = (1/np.sqrt(2))*np.array([[1, 1], [1, -1]], dtype=complex)

def check_unitary(gate):
    I = np.eye(2, dtype=complex)
    con_gate = gate.conj().T
    
    return np.allclose(con_gate@gate, I)

def apply_gate(state, gate):
    if not check_normalization(state) or not check_unitary(gate):
        print("Please enter a normalized state and an unitary gate for further computation.")
        return None
    
    return gate @ state