import pandas as pd
import matplotlib.pyplot as plt
import ast
from datetime import datetime

# Read the CSV file
data = pd.read_csv('FINALUS1 copy.csv')

# Convert the strings of lists to actual lists
for column in data.columns:
    data[column] = data[column].apply(lambda x: ast.literal_eval(x))

# Create a list of all dates in the range from January to July
start_date = datetime(2021, 1, 1)
end_date = datetime(2021, 7, 31)
all_dates = pd.date_range(start=start_date, end=end_date)

# Create a list to store occurrences for each topic
all_occurrences = []

# Populate the occurrences list
for index, row in data.iterrows():
    month_counts = []
    for month in row:
        month_count = {}
        for day in month:
            if day in month_count:
                month_count[day] += 1
            else:
                month_count[day] = 1
        month_counts.append(month_count)
    all_occurrences.append(month_counts)

# Convert occurrences to a list of counts for each date for each topic
all_counts_by_date = [{date: [] for date in all_dates} for _ in range(len(all_occurrences))]
for topic_index, topic_occurrences in enumerate(all_occurrences):
    for month_index, month_count in enumerate(topic_occurrences, start=1):
        for day, count in month_count.items():
            date = datetime(2021, month_index, day)
            all_counts_by_date[topic_index][date].append(count)

# Calculate the total count for each date for each topic
all_total_counts = [[sum(counts) for counts in counts_by_date.values()] for counts_by_date in all_counts_by_date]

# Plot the line graph for each topic
plt.figure(figsize=(10, 6))
for topic_index, total_counts in enumerate(all_total_counts, start=1):
    plt.plot(all_dates, total_counts, marker='o', label=f'Topic {topic_index}')

plt.title('Occurrences of Dates Across Months')
plt.xlabel('Date')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
