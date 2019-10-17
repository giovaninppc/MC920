from skimage.color import rgb2gray
from skimage.filters import roberts, sobel
from skimage.measure import label, regionprops

def convert_to_grayscale(img):
    return rgb2gray(img)


def detectEdge(img):
    return sobel(img)



def labelImage(img):
    label_image, number_of_objects = label(img, return_num = True)
    regions = regionprops(label_image)

    return label_image, number_of_objects, regions



def extractRegions(img):
    return regionprops(img)
