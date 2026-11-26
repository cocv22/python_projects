import numpy as np
import matplotlib.pyplot as plt
from gates import H, apply_gate
from states import check_normalization

plus_state = (1/np.sqrt(2))*np.array([1, 1], dtype=complex)
minus_state = (1/np.sqrt(2))*np.array([1, -1], dtype=complex)

print("Minus state normalized:", check_normalization(minus_state))
print("Plus state normalized:", check_normalization(plus_state))

transformed_plus = apply_gate(plus_state, H)
print("Transformed plus state:", transformed_plus)

transformed_minus = apply_gate(minus_state, H)
print("Transformed minus state:", transformed_minus)

plus_probabilities = np.abs(transformed_plus)**2
minus_probabilities = np.abs(transformed_minus)**2

print("Plus state probabilities after H:", plus_probabilities)
print("Minus state probabilities after H:", minus_probabilities)

labels = ["plus 0", "plus 1", "minus 0", "minus 1"]
combined_probabilities = np.concatenate((plus_probabilities, minus_probabilities))
print(combined_probabilities)

plt.bar(labels, combined_probabilities)
plt.title("Understanding the effect of quantum interference")
plt.xlabel("Initial state and measured outcome")
plt.ylabel("Measurement Probability")
plt.ylim(0, 1)
plt.show()

#Hypothesis:
#If H was applied to the two states I had originally predicted a difference in state.
#Despite having equal probability, their relative amplitudes were different.

#Results:
#The results supported my hypothesis.
#Hadamard acts directly on complex probability amplitudes,
#producing different interference patterns for the two states.
#H|+> = |0>, resulting in probabilities [1, 0].
#H|-> = |1>, resulting in probabilities [0, 1].
#Despite identical initial measurement probabilities,
#their different relative phases produced different outcomes.

#Conclusion:
#Relative phase dictates the way a gate may alter a state, despite having equal probability.