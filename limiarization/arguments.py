import argparse
from limiarization_methods import *

class LimiarizationMethod():
    def __init__(self, name: str, method):
        self.name = name
        self.method = method

class Arguments():
    def __init__(self, imagePath: str, limiarization: LimiarizationMethod):
        self.imagePath = imagePath
        self.imageName = imagePath.replace('.pgm', '').replace('/', '-')
        self.limiarizationMethods = limiarization

def setupArguments() -> Arguments:
    argParser = argparse.ArgumentParser(description = 'Arguments for the Image processing')
    argParser.add_argument('input_image_path', help = 'The path to image file to be processed')
    argParser.add_argument('-g', '--global_method', help='Apply global limiarization', action='store_true')
    argParser.add_argument('-b', '--bernsen', help='Apply Bernsen limiarization', action='store_true')

    args = argParser.parse_args()
    image_path = args.input_image_path

    limiarizations = []

    if args.global_method:
        limiarizations.append(LimiarizationMethod('Global', globalLimiarization))
    if args.bernsen:
        limiarizations.append(LimiarizationMethod('Bernsen', bernsen))

    return Arguments(image_path, limiarizations)
