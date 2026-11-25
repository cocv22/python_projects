import numpy as np
import matplotlib.pyplot as plt
from gates import H, apply_gate
from states import check_normalization

initial_state = np.array([1, 0], dtype = complex)
transformed_state = apply_gate(initial_state, H)
print(check_normalization(transformed_state))

probabilities = np.abs(transformed_state)**2
outcomes = ["0", "1"]

#Plot creation
plt.bar(outcomes, probabilities)
plt.title("Probability of outcomes in a zero state after applying H gate.")
plt.xlabel("Measurement Outcomes")
plt.ylabel("Probability")
plt.ylim(0, 1)
plt.show()

#Hypothesis:
#If H is applied to a zero state it shall become a plus state.

#Results:
#This simulator was able to calculate the 50-50 probability that comes with a plus state.
#It also verified normalization thorugh the check_normalization function.

#Conclusion:
#Results did indeed support the hypothesis, demonstrating that when applying an H gate to a zero state.
#It will then return a plus state.
#To be clear, the graph itself doesn't specify the phase, only the calculated probability of either state in a computational plane.
