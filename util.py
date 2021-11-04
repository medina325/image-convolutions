from skimage import io

def read_image(url):
  return io.imread(url, as_gray=True)

def get_index(i1: tuple, i2: tuple) -> tuple:
  '''Element wise addition of 2 tuples'''
  return tuple(map(lambda x,y: x + y, i1, i2))