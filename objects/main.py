from skimage.color import rgb2gray
from file_manipulation import *
from arguments import *
from imageManipulation import *
import math
import matplotlib.pyplot as plt

def main():
    args = setupArguments()

    img = openImage(args.imagePath)
    name = args.imageName

    # Edges
    grayscale = convert_to_grayscale(img)
    saveImage('out/gray-' + name + '.png', grayscale)
    extractEdges(grayscale, name)
    grayscale = openImage('out/gray-' + name + '.png', True)

    # Label
    labeled, numberOfObjects, regions = labelObjects(grayscale, name)

    fig, ax = plt.subplots()
    ax.imshow(labeled, cmap=plt.cm.gray)

    # Output
    print('número de regiões' + str(numberOfObjects))

    i = 0
    for props in regions:
        print('Região {}: \tárea: {}\tperímetro: {}\texcentricidade: {}\tsolidez: {}'
        .format(i, props.area, props.perimeter, props.eccentricity, props.solidity))
        i += 1


def extractEdges(img, name):
    sobelConverted = detectEdge(img)
    saveImage('out/edges-' + name + '.png', sobelConverted)


def labelObjects(img, name):
    labeled, numberOfObjects, regions = labelImage(img)
    saveImage('out/labeled-' + name + '.png', labeled)
    return img, numberOfObjects, regions

if __name__ == '__main__':
    main()
