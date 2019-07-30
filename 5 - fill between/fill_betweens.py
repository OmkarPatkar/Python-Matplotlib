import pandas as pd
from matplotlib import pyplot as plt

#styling the graph
plt.style.use('seaborn')

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color = '#444444',
		linestyle = '--', label = 'All_Devs')

plt.plot(ages, py_salaries, label = 'Python')

overall_median = 57287

plt.fill_between(ages, py_salaries, overall_median, alpha = 0.25,
				where = (py_salaries > overall_median), label = 'above avg', interpolate = True)

plt.fill_between(ages, py_salaries, overall_median, alpha = 0.45,
				where = (py_salaries <= overall_median), label = 'below avg',color = 'orange', interpolate = True)

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.savefig('fill_1.png')
plt.show()
