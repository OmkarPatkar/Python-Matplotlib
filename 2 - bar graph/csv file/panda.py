import csv
import pandas as pd
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

#styling the graph
plt.style.use('seaborn')

#read the csv file
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang:
	language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])

#to get the most used programming language on top
languages.reverse()
popularity.reverse()

#barh - to get the horizontal bar graph
plt.barh(languages, popularity)

plt.title("Most Popular Programming Languages")
plt.xlabel("Number of People")
plt.ylabel("Programming Languages")

plt.tight_layout()
plt.savefig('panda_barh.png')

plt.show()