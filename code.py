import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

data = pd.read_csv("StudentsPerformance.csv")
finalData = data["reading score"].tolist()

mean = sum(finalData) / len(finalData)
std_dev = statistics.stdev(finalData)
median = statistics.median(finalData)
mode = statistics.mode(finalData)

first_std_dev_start, first_std_dev_end = mean-std_dev, mean+std_dev
second_std_dev_start, second_std_dev_end = mean-(2*std_dev), mean+(2*std_dev)
third_std_dev_start, third_std_dev_end = mean-(3*std_dev), mean+(3*std_dev)

fig = ff.create_distplot([finalData], ["reading scores"], show_hist=False)
fig.show()

list_of_data_within_1_std_dev = [result for result in finalData if result > first_std_dev_start and result < first_std_dev_end]
list_of_data_within_2_std_dev = [result for result in finalData if result > second_std_dev_start and result < second_std_dev_end]
list_of_data_within_3_std_dev = [result for result in finalData if result > third_std_dev_start and result < third_std_dev_end]
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(std_dev))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_dev)*100.0/len(finalData)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_dev)*100.0/len(finalData)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_dev)*100.0/len(finalData)))