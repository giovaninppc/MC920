from arguments import *
from fileManipulation import *
from PIL import Image
import numpy as np
import os
import math
import matplotlib.pyplot as plt


args = setupArguments()
k = int(args.component_number)
path = args.input_image_path
output = args.output_path if args.output_path != None else 'compressed.png'

img = Image.open(path)
imgProperties = openImage(path)

outimg = np.zeros(imgProperties.shape)

# For each color channel
for channel in range(0,3):
    imgmat = np.array(list(img.getdata(band = channel)), float)
    imgmat.shape = (img.size[1], img.size[0])
    imgmat = np.matrix(imgmat)

    U, S, Vt = np.linalg.svd(imgmat) # single value decomposition
    for i in range(k):
        cmpimg = np.matrix(U[:, :i]) * np.diag(S[:i]) * np.matrix(Vt[:i,:])
        morphed = (cmpimg).astype(np.uint8)
        result = Image.fromarray(morphed)

    result.save('c' + str(channel) + '.png')

redChannel = openImage('c0.png')
blueChannel = openImage('c1.png')
greenChannel = openImage('c2.png')


for i in range(0, outimg.shape[0]):
    for j in range(0, outimg.shape[1]):
        outimg[i][j][0] = redChannel[i][j]
        outimg[i][j][1] = blueChannel[i][j]
        outimg[i][j][2] = greenChannel[i][j]


os.remove('c0.png')
os.remove('c1.png')
os.remove('c2.png')

saveImage(output, outimg)

sizeIn = float(os.path.getsize(path))/1000
sizeOut = float(os.path.getsize(output))/1000
print("Original Image (%0.2f Kb)" %sizeIn)
print("Compressed Image (%0.2f Kb)" %sizeOut)
print("Comopression factor (p): %.3f" %(sizeOut/sizeIn))

rmse = 0.0
for i in range(0,outimg.shape[0]):
    for j in range(0,outimg.shape[1]):
        for k in range(0,outimg.shape[2]):
            rmse += (imgProperties[i][j][k] - outimg[i][j][k]) ** 2
rmse /= (outimg.shape[0] * outimg.shape[1] *outimg.shape[2])
rmse = math.sqrt(rmse)

print('RMSE: %.3f' %rmse)
