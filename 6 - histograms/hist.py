import pandas as pd
from matplotlib import pyplot as plt

#styling the graph
plt.style.use('seaborn')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
ages = data['Age']

#bins are created in the graph to store values
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#log = True for huge dataset
plt.hist(ages, bins = bins, edgecolor = 'black', log = True)

#calculated the median from the data
median_age = 29

#axvline(axes vertical line) 
plt.axvline(median_age, label = 'Age Median',
			color = 'red', alpha = 0.45, linewidth = 2)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()
plt.savefig('histogram.png')

plt.show()
