def globalLimiarization(img):
    output = img
    output[output < 128] = 0
    output[output >= 128] = 255
    return output
