from half_tones.check_range import *

def Stucki(img, error: int, x, y, z):
    if checkRange(x+1, y, img):
        img[x+1][y][z] = img[x+1][y][z] + (8/42) * error
    if checkRange(x+2, y, img):
        img[x+2][y][z] = img[x+2][y][z] + (4/42) * error
    if checkRange(x-2, y+1, img):
        img[x-2][y+1][z] = img[x-2][y+1][z] + (2/42) * error
    if checkRange(x-1, y+1, img):
        img[x-1][y+1][z] = img[x-1][y+1][z] + (4/42) * error
    if checkRange(x, y+1, img):
        img[x][y+1][z] = img[x][y+1][z] + (8/42) * error
    if checkRange(x+1, y+1, img):
        img[x+1][y+1][z] = img[x+1][y+1][z] + (4/42) * error
    if checkRange(x+2, y+1, img):
        img[x+2][y+1][z] = img[x+2][y+1][z] + (2/42) * error
    if checkRange(x-2, y+2, img):
        img[x-2][y+2][z] = img[x-2][y+2][z] + (1/42) * error
    if checkRange(x-1, y+2, img):
        img[x-1][y+2][z] = img[x-1][y+2][z] + (2/42) * error
    if checkRange(x, y+2, img):
        img[x][y+2][z] = img[x][y+2][z] + (4/42) * error
    if checkRange(x+1, y+2, img):
        img[x+1][y+2][z] = img[x+1][y+2][z] + (2/42) * error
    if checkRange(x+2, y+2, img):
        img[x+2][y+2][z] = img[x+2][y+2][z] + (1/42) * error
