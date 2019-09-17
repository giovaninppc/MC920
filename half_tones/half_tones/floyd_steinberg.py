from half_tones.check_range import *

def FloydSteinberg(img, error: int, x, y, z):
    if checkRange(x + 1, y, img):
        img[x+1][y][z] = img[x+1][y][z] + (7/16) * error
    if checkRange(x, y + 1, img):
        img[x][y+1][z] = img[x][y+1][z] + (5/16) * error
    if checkRange(x + 1, y + 1, img):
        img[x+1][y+1][z] = img[x+1][y+1][z] + (1/16) * error
    if checkRange(x - 1, y + 1, img):
        img[x-1][y+1][z] = img[x-1][y+1][z] + (3/16) * error
