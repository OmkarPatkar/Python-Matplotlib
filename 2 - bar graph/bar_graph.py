import numpy as np
from matplotlib import pyplot as plt

#styling the graph
plt.style.use('seaborn')

# Median Developer Salaries by Age
ages = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

#creating a range of values(list) using ages
x_indexes = np.arange(len(ages))

#creating width for bar
width = 0.25

# Median Python Developer Salaries by Age

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indexes - width, py_dev_y, color = '#89DA59', width = width, label = 'Python')

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes, js_dev_y, color = '#F98866', width = width, label = 'JavaScript')

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_indexes + width, dev_y, color = '#80BD9E', width = width, label = 'all devs')

#to get the correct values on the axis 
plt.xticks(ticks = x_indexes, labels = ages)
plt.title('Median Salaries (USD) by Age')
plt.xlabel('ages')
plt.ylabel('Median Salaries USD')
plt.legend()
#for padding issues
plt.tight_layout()

plt.grid(True)
plt.savefig('bar.png')

plt.show()
