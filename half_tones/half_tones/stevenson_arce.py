from half_tones.check_range import *

def StevensonArce(img, error: int, x, y, z):
    if checkRange(x + 2, y, img):
        img[x+2][y][z] = img[x+2][y][z] + (32/200) * error
    if checkRange(x - 3, y + 1, img):
        img[x-3][y+1][z] = img[x-3][y+1][z] + (12/200) * error
    if checkRange(x - 1, y + 1, img):
        img[x-1][y+1][z] = img[x-1][y+1][z] + (26/200) * error
    if checkRange(x + 1, y + 1, img):
        img[x+1][y+1][z] = img[x+1][y+1][z] + (30/200) * error
    if checkRange(x + 3, y + 1, img):
        img[x+3][y+1][z] = img[x+3][y+1][z] + (16/200) * error
    if checkRange(x - 2, y + 2, img):
        img[x-2][y+2][z] = img[x-2][y+2][z] + (12/200) * error
    if checkRange(x , y + 2, img):
        img[x][y+2][z] = img[x][y+2][z] + (26/200) * error
    if checkRange(x + 2, y + 2, img):
        img[x+2][y+2][z] = img[x+2][y+2][z] + (12/200) * error
    if checkRange(x - 3, y + 3, img):
        img[x-3][y+3][z] = img[x-3][y+3][z] + (5/200) * error
    if checkRange(x - 1, y + 3, img):
        img[x-1][y+3][z] = img[x-1][y+3][z] + (12/200) * error
    if checkRange(x + 1, y + 3, img):
        img[x+1][y+3][z] = img[x+1][y+3][z] + (12/200) * error
    if checkRange(x + 3, y + 3, img):
        img[x+3][y+3][z] = img[x+3][y+3][z] + (5/200) * error
