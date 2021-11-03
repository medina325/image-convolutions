import numpy as np

sobel_edges_kernel_1 = np.array([
  [-1, -2, -1],
  [0, 0, 0],
  [1, 2, 1]
])

sobel_edges_kernel_2 = np.array([
  [-1, 0, 1],
  [-2, 0, 2],
  [-1, 0, 1]
])

prewitt_edges_kernel_1 = np.array([
  [-1, 0, 1],
  [-1, 0, 1],
  [-1, 0, 1]
])

prewitt_edges_kernel_2 = np.array([
  [1, 1, 1],
  [0, 0, 0],
  [-1, -1, -1]
])

avg_3x3_kernel = np.ones((3,3))

avg_5x5_kernel = np.ones((5,5))

def create_gaussian_kernel(sigma):
  size = sigma*3 + 1
  pass