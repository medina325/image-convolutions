import numpy as np
from util import get_index

def idx_is_valid(width, height, x, y):
  return 0 <= x < width and 0 <= y < height

# TODO transform into generator
def convolute_pixel(image, idx, kernel):
  w, h = image.shape
  n, _ = kernel.shape
  center = n // 2
  center_idx = (center, center)
  
  convoluted_pixel = 0
  for kx in range(-center, center+1):
    for ky in range(-center, center+1):
      i_idx = get_index(idx, (kx,ky))
      k_idx = get_index(center_idx, (kx,ky))
      
      convoluted_pixel += image[i_idx] * kernel[k_idx] if idx_is_valid(w, h, *i_idx) else 0
  
  return convoluted_pixel

def convolute(img, kernel):   
  convoluted_image = np.zeros(img.shape, dtype=np.uint8)
  w, h = img.shape
  
  for x in range(w):
    for y in range(h):
      convoluted_image[(x,y)] = convolute_pixel(img, (x,y), kernel)
  
  return np.array(convoluted_image)