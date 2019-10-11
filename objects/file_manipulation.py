import numpy as np
from skimage import io

def openImage(path: str):
    return io.imread(path)

def saveImage(path: str, img):
    io.imsave(path, img)
