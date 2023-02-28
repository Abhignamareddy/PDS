import pandas as pd
from scipy.stats import ttest_ind

# Load the raw data CSV file
raw_data = pd.read_csv("/Users/chethanmallavarapu/Downloads/ABHIGNA/raw_data.csv")

# Filter the data based on Grip Strength > 20
clean_data = raw_data[raw_data['Grip Strength'] > 20]

# Save the clean data to a new file
clean_data.to_csv("/Users/chethanmallavarapu/Downloads/ABHIGNA/clean_data.csv", index=False)

# Load the clean data CSV file
clean_data = pd.read_csv("/Users/chethanmallavarapu/Downloads/ABHIGNA/clean_data.csv")

# Perform t-test for Grip Strength between Frailty groups
frailty_1 = clean_data[clean_data['Frailty'] == 'Y']['Grip Strength']
frailty_0 = clean_data[clean_data['Frailty'] == 'N']['Grip Strength']
t_test_result = ttest_ind(frailty_1, frailty_0)

# Save the t-test result to a file
with open("/Users/chethanmallavarapu/Downloads/ABHIGNA/results/test.txt", 'w') as f:
    f.write(str(t_test_result))
