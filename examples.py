from matplotlib import pyplot as plt
import util
import kernel
from convolution import convolute

img_urls = [
  'https://www.dropbox.com/s/updljye8v80pipg/building.jpg?dl=1', 
  'https://www.dropbox.com/s/lcoqk6btwll8dbg/noisy.jpg?dl=1',
  'https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png'
]
def smoothing_lena():
  lena = util.read_image(img_urls[2])

  kernels = [
    kernel.avg_3x3_kernel,
    kernel.avg_5x5_kernel,
    kernel.create_gaussian_kernel(sigma=1),
    kernel.create_gaussian_kernel(sigma=3)
  ]

  kernel_names = [
    '3x3 Average Kernel',
    '5x5 Average Kernel',
    'Gaussian Kernel (sigma=1)',
    'Gaussian Kernel (sigma=3)'
  ]
  
  convoluted_imgs = [convolute(lena, kernel) for kernel in kernels]

  util.plot_comparisions(lena, convoluted_imgs, kernel_names, 'smoothing')


def smoothing_images():
  noisy_img = util.read_image(img_urls[1])

  kernels = [
    kernel.avg_3x3_kernel,
    kernel.avg_5x5_kernel,
    kernel.create_gaussian_kernel(sigma=1),
    kernel.create_gaussian_kernel(sigma=3)
  ]

  kernel_names = [
    '3x3 Average Kernel',
    '5x5 Average Kernel',
    'Gaussian Kernel (sigma=1)',
    'Gaussian Kernel (sigma=3)'
  ]

  convoluted_imgs = [convolute(noisy_img, kernel) for kernel in kernels]

  util.plot_comparisions(noisy_img, convoluted_imgs, kernel_names, 'smoothing_results')


def detecting_edges():
  building_img = util.read_image(img_urls[0])

  kernels = [
    kernel.sobel_edges_kernel_1,
    kernel.sobel_edges_kernel_2,
    kernel.prewitt_edges_kernel_1,
    kernel.prewitt_edges_kernel_2
  ]

  kernel_names = [
    'Sobel Kernel 1',
    'Sobel Kernel 2',
    'Prewitt Kernel 1',
    'Prewitt Kernel 2'
  ]
  
  convoluted_imgs = [convolute(building_img, kernel) for kernel in kernels]

  util.plot_comparisions(building_img, convoluted_imgs, kernel_names, 'edges_results')

