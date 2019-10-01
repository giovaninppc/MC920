import numpy as np

def contrast(img):
    size = 7 # n*n
    out = img

    for x in range(0, img.shape[0]):

        if x % 20 == 0:
            print('.', end = '', flush = True)

        for y in range(0, img.shape[1]):
            pixel = out[x][y]
            min, max = limit(img, x, y, size)
            if abs(pixel - min) < abs(pixel - max):
                out[x][y] = 0
            else:
                out[x][y] = 255
    return out

def limit(img, x, y, size):
    min = 256
    max = -1

    for index_x in range(x - int(size / 2), x + int(size / 2)):
        for index_y in range(y - int(size / 2), y + int(size / 2)):
            if index_x >= 0 and index_x < img.shape[0] and index_y >= 0 and index_y < img.shape[1]:
                if img[index_x][index_y] > max:
                    max = img[index_x][index_y]
                if img[index_x][index_y] < min:
                    min = img[index_x][index_y]

    return (min, max)
