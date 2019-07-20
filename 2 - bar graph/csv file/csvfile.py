import csv
import numpy as np
from matplotlib import pyplot as plt

#styling the graph
plt.style.use('seaborn')

#read the csv file
with open('data.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)

#get the first row
	row = next(csv_reader)
	print(row)

#to get the languages from the csv file use the key LanguagesWorkedWith,
#and use the split method to separate the values 
#it'll return a list
	print(row['LanguagesWorkedWith'].split(';'))