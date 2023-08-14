import numpy as np
new_drug_data = [10, 12, 8, 15, 11, 9, 13, 14, 10, 12]
placebo_data = [5, 7, 4, 8, 6, 3, 7, 6, 4, 9]
mean_new_drug = np.mean(new_drug_data)
std_new_drug = np.std(new_drug_data)
mean_placebo = np.mean(placebo_data)
std_placebo = np.std(placebo_data)
n_new_drug = len(new_drug_data)
n_placebo = len(placebo_data)
se_new_drug = std_new_drug / np.sqrt(n_new_drug)
se_placebo = std_placebo / np.sqrt(n_placebo)
confidence_interval_new_drug = (mean_new_drug-1.96*se_new_drug,mean_new_drug+1.96*se_new_drug)
confidence_interval_placebo = (mean_placebo-1.96*se_placebo,mean_new_drug+1.96*se_placebo)
print("95% Confidence Interval for Mean Reduction in Blood Pressure (New Drug):", confidence_interval_new_drug)
print("95% Confidence Interval for Mean Reduction in Blood Pressure (Placebo):", confidence_interval_placebo)