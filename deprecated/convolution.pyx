import cython
import numpy as np
# cimport numpy as np
from util import get_index

def idx_is_valid(width, height, x, y):
  return 0 <= x < width and 0 <= y < height

# def convolute_pixel(image, idx, kernel):
cpdef double convolute_pixel(double[:,:] img, size_t idx, double[:,:] kernel):
  cdef size_t w, h, n, center, i_idx, k_idx, coin, xoin, oin, toin
  cdef double convoluted_pixel = 0

  w = img.shape[0]
  h = img.shape[1]
  n = kernel.shape[0]

  center = n // 2
  center_idx = (center, center)
  
  for kx in range(-center, center+1):
    for ky in range(-center, center+1):
      i_idx = get_index(idx, (kx,ky))
      k_idx = get_index(center_idx, (kx,ky))
      coin, xoin = i_idx
      oin, toin = k_idx
      
      convoluted_pixel += img[coin][xoin] * kernel[oin][toin] if idx_is_valid(w, h, *i_idx) else 0
  
  return convoluted_pixel

@cython.boundscheck(False)
cpdef double[:,:] convolute(double[:,:] img, double[:,:] kernel):
  cdef size_t x, y, w, h

  w = img.shape[0]
  h = img.shape[1]
  cdef double[:,:] convoluted_image = np.zeros((w,h), dtype=np.double)

  # convoluted_image = np.zeros((w,h), dtype=np.double64)
  
  for x in range(w):
    for y in range(h):
      convoluted_image[x][y] = convolute_pixel(img, (x,y), kernel)
  
  return convoluted_image
