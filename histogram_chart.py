import matplotlib.pyplot as plt

data = [7,879,25,154,78,23,2,1,4,8,96,5,3,2,5,8,8,99,5,21]

plt.hist(data,bins=5, color='purple', edgecolor='black')

plt.title('Histogram')

plt.show()

