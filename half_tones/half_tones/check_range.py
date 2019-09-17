def checkRange(x, y, img) -> bool:
    if x >= 0 and x < img.shape[0] and y >= 0 and y < img.shape[1]:
        return True
    return False
