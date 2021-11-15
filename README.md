# Image Convolutions
Small project that implements the convolution operation between an image and variety of kernels.

## Kernels
The current list of kernels are:

- Sobel's edge detectors
- Prewitt's edge detectors
- Average (Smoothing)
- Gaussian

## TODO
Current implementation is very naive and poorly optimized. Hence a small list of improvements to be made:
- Use Python Generators whenever possible
- Use vectorized/parallel operations from numpy
- Use Cython for unavoidable pixel-by-pixel for loops
