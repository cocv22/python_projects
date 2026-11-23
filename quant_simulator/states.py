import numpy as np

def check_states(original_state, altered_state):
    return np.allclose(original_state, altered_state)
    
def check_normalization(state):
    probabilities = np.abs(state)**2
    total_probability = np.sum(probabilities)
    
    return np.isclose(total_probability, 1)