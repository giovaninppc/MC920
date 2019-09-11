from half_tones.check_range import *

def JJN(img, error: int, x, y, z):
    if checkRange(x+1, y, img):
        img[x+1][y][z] = img[x+1][y][z] + (7/48) * error
    if checkRange(x+2, y, img):
        img[x+2][y][z] = img[x+2][y][z] + (5/48) * error
    if checkRange(x-2, y+1, img):
        img[x-2][y+1][z] = img[x-2][y+1][z] + (3/48) * error
    if checkRange(x-1, y+1, img):
        img[x-1][y+1][z] = img[x-1][y+1][z] + (5/48) * error
    if checkRange(x, y+1, img):
        img[x][y+1][z] = img[x][y+1][z] + (7/48) * error
    if checkRange(x+1, y+1, img):
        img[x+1][y+1][z] = img[x+1][y+1][z] + (5/48) * error
    if checkRange(x+2, y+1, img):
        img[x+2][y+1][z] = img[x+2][y+1][z] + (3/48) * error
    if checkRange(x-2, y+2, img):
        img[x-2][y+2][z] = img[x-2][y+2][z] + (1/48) * error
    if checkRange(x-1, y+2, img):
        img[x-1][y+2][z] = img[x-1][y+2][z] + (3/48) * error
    if checkRange(x, y+2, img):
        img[x][y+2][z] = img[x][y+2][z] + (5/48) * error
    if checkRange(x+1, y+2, img):
        img[x+1][y+2][z] = img[x+1][y+2][z] + (3/48) * error
    if checkRange(x+2, y+2, img):
        img[x+2][y+2][z] = img[x+2][y+2][z] + (1/48) * error
