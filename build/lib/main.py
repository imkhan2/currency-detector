from input import *
from binarize import *
from filter import *
from data import *
from colordetect import *
import math

def main(image):
    image=filter(image)
    asp=aspect(image)
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
        ans="not found"
    return ans