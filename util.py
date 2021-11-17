from skimage import io
import matplotlib.pyplot as plt

def read_image(url):
  return io.imread(url, as_gray=True)

def get_index(i1: tuple, i2: tuple) -> tuple:
  '''Element wise addition of 2 tuples'''
  return tuple(map(lambda x,y: x + y, i1, i2))

def plot_comparisions(original_img, conv_imgs, conv_img_titles, operation='results'):
    if len(conv_imgs) != len(conv_img_titles):
      raise Exception("Quantidade de imagens não é a mesma que de títulos")

    total_subplots = len(conv_imgs)
    n_cols = 3
    n_rows = total_subplots // n_cols
    n_rows += total_subplots % n_cols

    fig = plt.figure(figsize=(20,10))

    ax = fig.add_subplot(n_rows, n_cols, 1)
    ax.set_title('Original Image')
    ax.imshow(original_img, cmap='gray')

    for i in range(len(conv_imgs)):
      ax = fig.add_subplot(n_rows, n_cols, i+2)
      ax.set_title(conv_img_titles[i])
      ax.imshow(conv_imgs[i], cmap='gray')

    plt.savefig(f'{operation}.jpg')
    plt.show()
    

