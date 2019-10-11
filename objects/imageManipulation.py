from skimage.color import rgb2gray
from skimage.filters import roberts, sobel


def convert_to_grayscale(img):
    return rgb2gray(img)


def detectEdge(img):
    return sobel(img)
