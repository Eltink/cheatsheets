import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2)

# First subplot
ax1.plot(x, y1)
ax1.set_title('Quadratic')

# Second subplot
ax2.plot(x, y2)
ax2.set_title('Linear')

# Plot multiple lines
plt.plot(x, y1, label='Quadratic')
plt.plot(x, y2, label='Linear')

plt.plot(X, Y, label='Data', marker='o')
    linewidth, alpha (transparency), marker, linestyle
    nao tem hold on pq sempre adiciona, nao sobrescreve
    
plt.grid(True)

# Turn on minor ticks
plt.minorticks_on()

# Turn on the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5')

plt.xlim(0, np.inf) # Set x-axis limits with padding
plt.yscale('log') # Set y-axis to logarithmic scale

# Save the plot to a file
plt.savefig('line_plot.png')

# Customize ticks
plt.xticks([1, 2, 3, 4, 5], ['One', 'Two', 'Three', 'Four', 'Five'])

plt.show()

fig.clear()
plt.close("all")


### Python vector handling
import numpy as np

# Create a sample vector
vector = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Crop the vector to include elements from index 2 to 5 (exclusive)
cropped_vector = vector[2:5]            # Output: [3 4 5]

# Access the element at index 2
element = vector[2]

# Access elements at indices 1, 3, and 4
elements = vector[[1, 3, 4]]            # Output: [20 40 50]

# Select elements greater than 25
selected_elements = vector[vector > 25] # Output: [30 40 50]

# Select elements from index 1 to 3 (exclusive)
sliced_vector = vector[1:3]             # Output: [20 30]

# Concatenate the vectors
concatenated_vector = np.concatenate((vector1, vector2))

def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
