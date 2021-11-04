from skimage import io
import kernel
import util
from convolution import convolute

if __name__ == '__main__':
  img_urls = [
    'https://www.dropbox.com/s/updljye8v80pipg/building.jpg?dl=1', 
    'https://www.dropbox.com/s/lcoqk6btwll8dbg/noisy.jpg?dl=1'
  ]

  kernels = [
    kernel.sobel_edges_kernel_1,
    kernel.sobel_edges_kernel_2,
    kernel.prewitt_edges_kernel_1,
    kernel.prewitt_edges_kernel_2,
    kernel.avg_3x3_kernel,
    kernel.avg_5x5_kernel,
    kernel.create_gaussian_kernel(sigma=1),
    kernel.create_gaussian_kernel(sigma=3),
    kernel.create_gaussian_kernel(sigma=5)
  ]

  for img_url in img_urls:
    try:
      img = util.read_image(img_url)

      for k in kernels:
        improved_img = convolute(img, k)
        
        io.imshow(img)
        io.show()
        io.imshow(improved_img)
        io.show()

        # TODO plot side-by-side comparision
        
    except Exception as e:
      print(e)
