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
    argParser.add_argument('-fs', '--floyd_steinberg', help='Make Floyd-Steinberg transformation', action='store_true')
    argParser.add_argument('-sa', '--stevenson_arce', help='Make Stevenson and Arce transformation', action='store_true')
    argParser.add_argument('-b', '--burkes', help='Make Burkes transformation', action='store_true')
    argParser.add_argument('-si', '--sierra', help='Make Sierra transformation', action='store_true')
    argParser.add_argument('-st', '--stucki', help='Make Stucki transformation', action='store_true')
    argParser.add_argument('-jjn', '--jarvas_judice_ninke', help='Make Jarvas Judice and Ninke transformation', action='store_true')
    argParser.add_argument('-all', '--all', help='Make all transformations to specified image', action='store_true')

    args = argParser.parse_args()
    image_path = args.input_image_path

    halfTones = []

    if args.floyd_steinberg or args.all:
        halfTones.append(HalfTones("Floyd-Steinberg", FloydSteinberg))
    if args.stevenson_arce or args.all:
        halfTones.append(HalfTones("Stevenson and Arce", StevensonArce))
    if args.burkes or args.all:
        halfTones.append(HalfTones("Burkes", Burkes))
    if args.sierra or args.all:
        halfTones.append(HalfTones("Sierra", Sierra))
    if args.stucki or args.all:
        halfTones.append(HalfTones("Stucki", Stucki))
    if args.jarvas_judice_ninke or args.all:
        halfTones.append(HalfTones("Jarvas Judice and Ninke", JJN))

    if len(halfTones) == 0:
        print('You gotta tell which half tone transformation you want to use. Check --help for help.')

    return Arguments(image_path, halfTones)
