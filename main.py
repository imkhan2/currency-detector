from input import *
from binarize import *
from filter import *
from data import *
from colordetect import *
import math
#from segment import *
from skimage.filters import threshold_otsu

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
    imsave("D:\images\seg.jpg",im3)
    return im3

def main(image):
    image=filter(image)
    image2=seg(image)
    asp=aspect(image2)
    col=hsv(image)
    ans="null"
    for curr in aspectr.keys():
        if abs(asp-aspectr[curr])<=0.1:
            x=(color[curr][0]-col[0])*(color[curr][0]-col[0])+(color[curr][1]-col[1])*(color[curr][1]-col[1])+(color[curr][2]-col[2])*(color[curr][2]-col[2])
            y=math.sqrt(x)
            if(y<=0.01):
                ans=curr
                break
    else:
        ans="Not Found"
    return ans