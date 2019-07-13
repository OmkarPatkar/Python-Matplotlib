from matplotlib import pyplot as plt 

#to check the available styles
#print(plt.style.available)

#plt.style.use('seaborn')

#for comic style
plt.xkcd()

# Median Developer Salaries by Age
ages = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Median Python Developer Salaries by Age

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages, py_dev_y, color = 'b', marker = 'o', label = 'Python')


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages, js_dev_y, color = 'red', linewidth = 3, label = 'JavaScript')

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages, dev_y, color = 'k', linestyle = '--', marker = '.', label = 'all devs')


plt.title('Median Salaries (USD) by Age')
plt.xlabel('ages')
plt.ylabel('Median Salaries USD')
plt.legend()
#for padding issues
plt.tight_layout()

plt.grid(True)
plt.savefig('comic.png')

plt.show()