def bernsen(img):
    size = 10 # n*n
    out = img

    for x in range(0, img.shape[0]):

        if x % 20 == 0:
            print('.', end = '', flush = True)

        for y in range(0, img.shape[1]):
            T = limit(img, x, y, size)
            if out[x][y] >= T:
                out[x][y] = 255
            else:
                out[x][y] = 0

    return out


def limit(img, x, y, size):
    min = 256
    max = -1

    for index_x in range(x - int(size / 2), x + int(size / 2)):
        for index_y in range(y - int(size / 2), y + int(size / 2)):
            if index_x >= 0 and index_x < img.shape[0] and index_y >= 0 and index_y < img.shape[1]:
                value = img[index_x][index_y]
                if value < min:
                    min = value
                if value > max:
                    max = value

    return (min + max) / 2
