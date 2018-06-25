from skimage.color import *
def hsv(image):
    im=rgb2hsv(image)
    h,s,v=0,0,0
    for i in range(len(im)):
        for j in range(len(im[i])):
            h=h+im[i][j][0]
            s=s+im[i][j][1]
            v=v+im[i][j][2]
    h=h/im.size
    s=s/im.size
    v=v/im.size
    return [h,s,v]

#def detect(hsv):
