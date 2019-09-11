import argparse
from half_tones import *

class HalfTones():
    def __init__(self, name, distribution):
        self.name = name
        self.distribution = distribution

class Arguments():
    def __init__(self, imagePath: str, halfTones):
        self.imagePath = imagePath
        self.imageName = imagePath.replace('.png', '').replace('/', '-')
        self.halfTones = halfTones

def setupArguments() -> Arguments:
    argParser = argparse.ArgumentParser(description='Arguments for the Image processing')
    argParser.add_argument('input_image_path', help='The path to image file to be processed')
    argParser.add_argument('-fs', '--floyd_steinberg', help='Make floyd steinberg transformation', action='store_true')

    args = argParser.parse_args()
    image_path = args.input_image_path

    halfTones = []

    if args.floyd_steinberg:
        halfTones.append(HalfTones("Floyd-Steinberg", FloydSteinberg))

    return Arguments(image_path, halfTones)
