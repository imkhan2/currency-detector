from skimage.segmentation import *
import glob
from skimage.io import *
from skimage.color import *
from skimage.filters import threshold_otsu
import numpy
import filter
#file=glob.glob(r"D:\dol2.jpg")[0]
#im=imread(file)
'''im2=felzenszwalb(im)
a=[]
for i in range(len(im)):
    b=[]
    for j in range(len(im[0])):
        if im2[i][j]>0:
            b.append(im[i][j])
    a.append(b)
im3=numpy.array(a)
#imsave("D:\seg.jpg",im3)
print(im3)
print(a)
from skimage.exposure import *
im4=equalize_hist(im)
imsave("D:\seg.jpg",im4)'''
def seg(im):
    im2=rgb2grey(im)
    val=threshold_otsu(im2)
    mask=im2<val
    x1,x2,x3,x4=-1,-1,-1,-1
    for i in range(len(mask)):
        for j in range(len(mask[0])):
            if mask[i][j]==False and x1==-1:
                x1=i
                x2=j
                break
    for i in range(len(mask)-1,-1,-1):
        for j in range(len(mask[0])-1,-1,-1):
            if mask[i][j]==False and x3==-1:
                x3=i
                x4=j
                break
    im3=im2[x1:x3,x2:x4]
    return im3
