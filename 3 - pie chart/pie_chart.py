from matplotlib import pyplot as plt

#styling the graph
plt.style.use('seaborn')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

#to pop out specific item 
explode = [0, 0, 0, 0.1, 0]

#use startangle to adjust the angle of the pie chart
#use autopct to show the percentage values
#use wedgeprops to give border to the pie chart

plt.pie(slices, labels= labels, explode = explode, shadow = True,
		startangle = 90, autopct = '%1.1f%%',
		 wedgeprops={'edgecolor' : 'black'})

plt.title("Pie Chart")
plt.tight_layout()
plt.savefig('pie_chart.png')
plt.show()
