import numpy as np
import matplotlib.pyplot as plt

# Let's create a mock self-similarity matrix.
# Typically, this would be computed from your data.
size = 50  # Assuming a 50x50 matrix
np.random.seed(0)  # Seed for reproducibility
data = np.random.rand(size, size)

# Making the matrix symmetric to simulate self-similarity
similarity_matrix = (data + data.T) / 2
np.fill_diagonal(similarity_matrix, 1)  # Self-similarities are max

# Plotting the heatmap
plt.figure(figsize=(6, 5))
plt.imshow(similarity_matrix, cmap='hot', interpolation='nearest')
plt.title('Self-similarity matrix of the GCFs')
plt.colorbar()  # To show the color scale
plt.xlabel('GCFs')
plt.ylabel('GCFs')
plt.tight_layout()  # Adjust the layout
plt.show()
