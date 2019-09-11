import imageio

def openImage(path):
    img = imageio.imread(path)
    return img

def saveImage(path, image):
    imageio.imsave(path, image)
