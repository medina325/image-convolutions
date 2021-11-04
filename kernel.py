import math
import numpy as np
from util import get_index

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

avg_3x3_kernel = np.ones((3,3)) / 9

avg_5x5_kernel = np.ones((5,5)) / 25

# TODO turn into generator
def create_gaussian_kernel(sigma):
  def gaussian_pixel(sigma, x, y):    
    return (1 / (2*np.pi*sigma*sigma)) * math.exp(-(x*x + y*y) / (2*sigma*sigma))

  order = 3*sigma + 2
  center = order//2
  center_idx = (center, center)
  
  gaussian_kernel = np.zeros((order,order))
  for x in range(-center, center+1):
      for y in range(-center, center+1):
          i_idx = get_index(center_idx, (x,y))
          
          gaussian_kernel[i_idx] = gaussian_pixel(sigma, x, y)
      
  return gaussian_kernel / np.sum(gaussian_kernel)
  