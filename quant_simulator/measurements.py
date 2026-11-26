import numpy as np
from states import check_normalization

def measure(state):
    if not check_normalization(state):
        raise ValueError("Ensure the state is normalized to do further computations.")
    
    probabilities = np.abs(state)**2
    outcome = np.random.choice(a=[0, 1], p=probabilities)
    
    return int(outcome)

if __name__ == '__main__':
    zero_state = np.array([1, 0], dtype=complex)
    result = measure(zero_state)

    print(result)