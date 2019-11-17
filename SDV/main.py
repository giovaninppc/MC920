from arguments import *
from fileManipulation import *
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt


args = setupArguments()
k = int(args.component_number)
path = args.input_image_path
output = args.output_path if args.output_path != None else 'compressed.png'

img = Image.open(path)

size = float(os.path.getsize(path))/1000
print("Size(dimension): ",img.size)
print("Original Image (%0.2f Kb):" %size)

# For each color channel
for i in range(0,2):
    imggray = img.convert('LA')
    imgmat = np.array( list(imggray.getdata(band = 0)), float)
    imgmat.shape = (imggray.size[1], imggray.size[0])
    imgmat = np.matrix(imgmat)
    # plt.figure()
    # plt.imshow(imgmat, cmap = 'gray')
    # plt.title("Image after converting it into the Grayscale pattern")
    # plt.show()

    U, S, Vt = np.linalg.svd(imgmat) #single value decomposition
    for i in range(k):
        cmpimg = np.matrix(U[:, :i]) * np.diag(S[:i]) * np.matrix(Vt[:i,:])
        # plt.imshow(cmpimg, cmap = 'gray')
        # title = " Image after =  %s" %i
        # plt.title(title)
        # plt.show()
        result = Image.fromarray((cmpimg ).astype(np.uint8))
    result.save(output)
