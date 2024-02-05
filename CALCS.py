import pandas as pd
import statistics
import numpy as np
import scipy.stats as stats

df = pd.read_csv('FINAL_RESULTS.csv')

topic_list = df["topic"]
countries = df["country"]
percentage_june = df["percentage june"]
percentage_july = df["percentage july"]
percentage_august = df["percentage august"]
percentage_september = df["percentage september"]
percentage_october = df["percentage october"]


tweet1 = [percentage_june[0],percentage_july[0],percentage_august[0],percentage_september[0],percentage_october[0]]
print(statistics.stdev([percentage_june[1],percentage_july[1]]))
print(statistics.stdev([percentage_august[1],percentage_september[1],percentage_october[1]]))
# Create the data for two groups
group1 = np.random.rand(25)
group2 = np.random.rand(20)
# Calculate the sample variances
variance1 = np.var(group1, ddof=1)
variance2 = np.var(group2, ddof=1)
# Calculate the F-statistic
f_value = variance1 / variance2
# Calculate the degrees of freedom
df1 = len(group1) - 1
df2 = len(group2) - 1
# Calculate the p-value
p_value = stats.f.cdf(f_value, df1, df2)
# Print the results
print('Degree of freedom 1:',df1)
print('Degree of freedom 2:',df2)
print("F-statistic:", f_value)
print("p-value:", p_value)

tweet2 = [percentage_june[2],percentage_july[2],percentage_august[2],percentage_september[2],percentage_october[2]]
tweet3 = [percentage_june[3],percentage_july[3],percentage_august[3],percentage_september[3],percentage_october[3]]
tweet4 = [percentage_june[4],percentage_july[4],percentage_august[4],percentage_september[4],percentage_october[4]]
tweet5 = [percentage_june[5],percentage_july[5],percentage_august[5],percentage_september[5],percentage_october[5]]
tweet6 = [percentage_june[6],percentage_july[6],percentage_august[6],percentage_september[6],percentage_october[6]]

tweet7 = [percentage_june[7],percentage_july[7],percentage_august[7],percentage_september[7],percentage_october[7]]
tweet8 = [percentage_june[8],percentage_july[8],percentage_august[8],percentage_september[8],percentage_october[8]]
tweet9 = [percentage_june[9],percentage_july[9],percentage_august[9],percentage_september[9],percentage_october[9]]
tweet10 = [percentage_june[10],percentage_july[10],percentage_august[10],percentage_september[10],percentage_october[10]]
tweet11 = [percentage_june[11],percentage_july[11],percentage_august[11],percentage_september[11],percentage_october[11]]
tweet12 = [percentage_june[12],percentage_july[12],percentage_august[12],percentage_september[12],percentage_october[12]]
tweet13 = [percentage_june[13],percentage_july[13],percentage_august[13],percentage_september[13],percentage_october[13]]

tweet14 = [percentage_june[14],percentage_july[14],percentage_august[14],percentage_september[14],percentage_october[14]]
tweet15 = [percentage_june[15],percentage_july[15],percentage_august[15],percentage_september[15],percentage_october[15]]
tweet16 = [percentage_june[16],percentage_july[16],percentage_august[16],percentage_september[16],percentage_october[16]]
tweet17 = [percentage_june[17],percentage_july[17],percentage_august[17],percentage_september[17],percentage_october[17]]