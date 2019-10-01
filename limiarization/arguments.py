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
    argParser.add_argument('-n', '--niblack', help='Apply Niblack limiarization', action='store_true')
    argParser.add_argument('-c', '--contrast', help='Apply Contrast limiarization', action='store_true')
    argParser.add_argument('-avg', '--media', help='Apply Average limiarization', action='store_true')
    argParser.add_argument('-med', '--mediana', help='Apply Mediana limiarization', action='store_true')
    argParser.add_argument('-sp', '--sauvola', help='Apply Sauvola-Pietaksinen limiarization', action='store_true')

    args = argParser.parse_args()
    image_path = args.input_image_path

    limiarizations = []

    if args.global_method:
        limiarizations.append(LimiarizationMethod('Global', globalLimiarization))
    if args.bernsen:
        limiarizations.append(LimiarizationMethod('Bernsen', bernsen))
    if args.niblack:
        limiarizations.append(LimiarizationMethod('Niblack', niblack))
    if args.contrast:
        limiarizations.append(LimiarizationMethod('Contrast', contrast))
    if args.media:
        limiarizations.append(LimiarizationMethod('Media', average))
    if args.mediana:
        limiarizations.append(LimiarizationMethod('Mediana', mediana))
    if args.sauvola:
        limiarizations.append(LimiarizationMethod('Sauvola e Pietaksinen', sauvola))

    return Arguments(image_path, limiarizations)
