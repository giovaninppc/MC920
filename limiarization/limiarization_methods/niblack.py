import numpy as np

def niblack(img):
    size = 7 # n*n
    out = img

    for x in range(0, img.shape[0]):

        if x % 20 == 0:
            print('.', end = '', flush = True)

        for y in range(0, img.shape[1]):
            T = limit(img, x, y, size)
            if img[x][y] >= T:
                out[x][y] = 255
            else:
                out[x][y] = 0
    return out

def limit(img, x, y, size):
    k = 1
    list = []
    for index_x in range(x - int(size / 2), x + int(size / 2)):
        for index_y in range(y - int(size / 2), y + int(size / 2)):
            if index_x >= 0 and index_x < img.shape[0] and index_y >= 0 and index_y < img.shape[1]:
                list.append(img[index_x][index_y])

    return stdev(list) + k * average(list)

def stdev(obj):
    return np.std(obj)

def average(obj):
    return sum(obj)/len(obj)
