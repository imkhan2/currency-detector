
import glob
from skimage.io import *
from binarize import *

def input(file):
    #file=glob.glob(r"")[0]
    im=imread(file)
    im2=tobinary(im)
    return im