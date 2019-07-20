import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

#styling the graph
plt.style.use('seaborn')

#read csv file
with open('data.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)

#to count the itteration of each item
	language_counter = Counter()

	for row in csv_reader:
		language_counter.update(row['LanguagesWorkedWith'].split(';'))

#print most common languages
print(language_counter.most_common(15))

languages = []
popularity = []

for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])

print(languages)
print(popularity)

#to get the most used programming language on top
languages.reverse()
popularity.reverse()

#barh - to get the horizontal bar graph
plt.barh(languages, popularity)

plt.title("Most Popular Programming Languages")
plt.xlabel("Number of People")
plt.ylabel("Programming Languages")

plt.tight_layout()
plt.savefig('count.png')

plt.show()