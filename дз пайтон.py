import matplotlib.pyplot as plt
from data_module import generate_data

X, Y = generate_data()

plt.plot(X, Y, marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of Y vs X')
plt.grid(True)

plt.show()

