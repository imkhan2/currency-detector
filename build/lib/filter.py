from skimage.filters import gaussian

def filter(image):
    im=gaussian(image,sigma=0.4,multichannel=False)
    return im

def aspect(image):
    return (image[0].size * image[0].size) / (3 * image.size)

