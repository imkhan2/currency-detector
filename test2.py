import glob
from skimage import color, data
from skimage.io import *
import numpy as np
from scipy.signal import *
from skimage.exposure import *
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from skimage.restoration import *
from binarize import *
from skimage.filters import gaussian
file=glob.glob(r"D:\images\dol.jpg")[0]
image=imread(file)
#im3=gaussian(image,sigma=2)
im4=rgb2gray(image)
psf=np.ones((7,7))*0.9
im5 = convolve2d(im4, psf, 'same')	
deconvolved_img = wiener(im5, psf,100)
deconvolved_img=equalize_hist(deconvolved_img)
imsave(r"D:\deconvolved_img.jpg",deconvolved_img)
thresh_img=threshold_otsu(deconvolved_img)
binary=deconvolved_img>thresh_img
for i in range(len(binary)):
	for j in range(len(binary[0])):
		if binary[i][j]==True:
			deconvolved_img[i][j]=0
		else:
			deconvolved_img[i][j]=1

imsave(r"D:\deconvolved_img.jpg",deconvolved_img)
