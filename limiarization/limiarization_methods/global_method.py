def globalLimiarization(img):
    output = img
    output[output < 50] = 0
    output[output >= 50] = 255
    return output
