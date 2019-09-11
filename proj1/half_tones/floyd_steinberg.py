def FloydSteinberg(img, error: int, x, y, z):
    if checkRange(x + 1, y, img):
        img[x+1][y][z] = img[x+1][y][z] + (7/16) * error
    if checkRange(x, y + 1, img):
        img[x][y+1][z] = img[x][y+1][z] + (5/16) * error
    if checkRange(x + 1, y + 1, img):
        img[x+1][y+1][z] = img[x+1][y+1][z] + (1/16) * error
    if checkRange(x - 1, y + 1, img):
        img[x-1][y+1][z] = img[x-1][y+1][z] + (3/16) * error

def checkRange(x, y, img) -> bool:
    '''
    Check if an position x y belongs to the inside of the matrix
    '''
    if x >= 0 and x < img.shape[0] and y >= 0 and y < img.shape[1]:
        return True
    return False
