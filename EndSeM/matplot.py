import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='s', linestyle='--', color='g', label='Sample Data')

plt.title('Matplotlib')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()