#to show the relatioship between two sets of values and see if they are co-related

import pandas as pd
from matplotlib import pyplot as plt

#styling the graph
plt.style.use('seaborn')

#x & y axis points
x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

#intensity of the marker according to the value
colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

#defining size for the marker
sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
          538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

#s for size of the marker
#c for color of the marker
#cmap changes the color of the marker
#marker is used to change the pointer
plt.scatter(x, y, s = sizes, c = colors, cmap = 'Blues',
			edgecolor='black', linewidth=1, alpha=0.65,
			marker ='*')

#colormap legend 
cbar = plt.colorbar()
cbar.set_label('Satisfaction')

plt.tight_layout()
plt.savefig('scatter.png')
plt.show()