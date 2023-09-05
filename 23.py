import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
# Generate sample data
np.random.seed(0)
control_group = np.random.normal(loc=50, scale=10, size=100)
treatment_group = np.random.normal(loc=55, scale=10, size=100)
# Perform t-test
t_statistic, p_value = ttest_ind(control_group, treatment_group)
# Create box plot
plt.boxplot([control_group, treatment_group], labels=['Control', 'Treatment'])
plt.ylabel('Outcome')
plt.title('Box Plot of Control and Treatment Groups')

# Annotate p-value
plt.annotate(f'p-value = {p_value:.4f}', xy=(0.5, 0.05), xycoords='axes fraction', ha='center')

# Show the plot
plt.show()
