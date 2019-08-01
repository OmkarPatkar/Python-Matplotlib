#to show the relatioship between two sets of values and see if they are co-related
#co-relation b/w likes and views
#ratio of likes and dislikes

import pandas as pd
from matplotlib import pyplot as plt

#styling the graph
plt.style.use('seaborn')

#loading data from a csv file
data = pd.read_csv('data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

#s for size of the marker
#c for color of the marker
#cmap changes the color of the marker
#marker is used to change the pointer
plt.scatter(view_count, likes, c = ratio, cmap = 'summer',
			edgecolor='black', linewidth=1, alpha=0.65)

#colormap legend
cbar = plt.colorbar()
cbar.set_label('likes / dislikes ratio')

#to plot in logarithmic scale
plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')


plt.tight_layout()
plt.savefig('scatter1.png')
plt.show()