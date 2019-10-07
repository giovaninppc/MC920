import numpy as np
from skimage import io

def openImage(path: str):
    return io.imread(path)
