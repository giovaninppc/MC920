from skimage.color import rgb2gray
from file_manipulation import *
from arguments import *
from imageManipulation import *
import math
import matplotlib.pyplot as plt

small_area = 1500
medium_area = 3000

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

    areas = []
    # Output
    print('número de regiões' + str(numberOfObjects))

    i = 0
    for props in regions:
        print('Região {}: \tárea: {}\tperímetro: {}\texcentricidade: {}\tsolidez: {}'
        .format(i, props.area, props.perimeter, props.eccentricity, props.solidity))
        i += 1

        if props.area < small_area:
            areas.append(0)
        elif props.area < medium_area:
            areas.append(1)
        else:
            areas.append(2)

    # Objects area histogram
    plt.hist(areas, bins=32)
    plt.show()

def extractEdges(img, name):
    sobelConverted = detectEdge(img)
    saveImage('out/edges-' + name + '.png', sobelConverted)


def labelObjects(img, name):
    labeled, numberOfObjects, regions = labelImage(img)
    saveImage('out/labeled-' + name + '.png', labeled)
    return img, numberOfObjects, regions

if __name__ == '__main__':
    main()
