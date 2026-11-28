import numpy as np
from states import check_normalization

def measure(state, collapse=False):
    if not check_normalization(state):
        raise ValueError("Ensure the state is normalized to do further computations.")
    
    probabilities = np.abs(state)**2
    outcome = np.random.choice(a=[0, 1], p=probabilities)
    
    if collapse:
        collapsed_state = np.zeros_like(state)
        collapsed_state[int(outcome)] = 1
        
        return int(outcome), collapsed_state
        
    return int(outcome)

if __name__ == '__main__':
    one_state = np.array([0, 1], dtype=complex)
    zero_state = np.array([1, 0], dtype=complex)
    plus_state = (1/np.sqrt(2))*np.array([1, 1], dtype=complex)
    unequal_state = np.array([np.sqrt(3)/2, 1/2], dtype=complex)
    
    first_outcome, collapsed_state = measure(unequal_state, collapse=True)
    expected_state = zero_state if first_outcome == 0 else one_state
    
    assert np.allclose(expected_state, collapsed_state)
    print(first_outcome)
    
    second_outcome = measure(collapsed_state)
    print(second_outcome)
    assert first_outcome == second_outcome
    
    print("Unequal state test passed")
    
    outcome, c_state = measure(one_state, collapse=True)
    assert outcome == 1 and np.allclose(c_state, one_state)
    
    print("Basis state est passed")