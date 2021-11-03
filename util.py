from skimage import io

def read_image(url):
  return io.imread(url, as_gray=True)
  