import numpy as np
from skimage import io

def openImage(path: str, gray: bool = False):
    return io.imread(path, as_gray = gray)

def saveImage(path: str, img):
    io.imsave(path, img)
