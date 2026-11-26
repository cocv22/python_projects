import numpy as np
import matplotlib.pyplot as plt
from measurements import measure

plus_state = (1/np.sqrt(2))*np.array([1, 1], dtype=complex)
results = []
theoretical_probability = np.abs(plus_state[0])**2

shots = int(input("Give a sample size(Greater than 0): "))
if shots <= 0:
    raise ValueError("Invalid sample size")

for _ in range(shots):
    results.append(measure(plus_state))
    
one_count = results.count(1)
zero_count = results.count(0)

one_frequency = one_count/len(results)
zero_frequency = zero_count/len(results)

sample_sizes = [10, 100, 1000]
observed_results = [0.7, 0.52, 0.505]

plt.plot(sample_sizes, observed_results, marker="o", label="Frequency Of Outcome 0")
plt.title("Observed Measured Frequency vs. Sample Size")
plt.ylim(0, 1)
plt.axhline(y=theoretical_probability, label="Theoretical Probability", color="red")
plt.xlabel("Sample Sizes")
plt.ylabel("Observed Frequency of Outcome 0")
plt.legend()
plt.show()

# Hypothesis:
# As the sample size increases, the observed measurement
# frequencies should generally approach the theoretical probability.

# Results:
# The results supported my hypothesis.
# From 10 to 1000 shots, the absolute deviation decreased
# from 20 percentage points to 0.5 percentage points.

# Conclusion:
# The simulator produced results consistent with the
# Law of Large Numbers for measurements of the plus state.
# Although larger samples generally provide more reliable
# estimates, they do not guarantee smaller deviations
# in every individual experiment.