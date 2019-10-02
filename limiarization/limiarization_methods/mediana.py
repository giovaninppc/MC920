def mediana(img):
    size = 15 # n*n
    out = img

    for x in range(0, img.shape[0]):

        if x % 20 == 0:
            print('.', end = '', flush = True)

        for y in range(0, img.shape[1]):
            pixel = out[x][y]
            T = limit(img, x, y, size)
            if pixel >= T:
                out[x][y] = 255
            else:
                out[x][y] = 0
    return out

def limit(img, x, y, size):
    list = []

    for index_x in range(x - int(size / 2), x + int(size / 2)):
        for index_y in range(y - int(size / 2), y + int(size / 2)):
            if index_x >= 0 and index_x < img.shape[0] and index_y >= 0 and index_y < img.shape[1]:
                list.append(img[index_x][index_y])

    sortedList = sorted(list)
    n = len(sortedList)
    middle = int(n / 2)

    if n % 2 == 0:
    	mediana = (sortedList[middle + 1] + sortedList[middle + 2]) / 2
    else:
    	mediana = sortedList[middle+1]*1

    return mediana
