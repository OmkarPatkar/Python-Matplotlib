from matplotlib import pyplot as plt

#styling the graph
plt.style.use('seaborn')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

plt.stackplot(minutes, player1, player2, player3,
			 labels = ["player1", "player2", "player3"])

plt.legend(loc=(0.07, 0.85))

plt.title('Stack Plot')
plt.tight_layout()
plt.savefig('Stack0.png')

plt.show()