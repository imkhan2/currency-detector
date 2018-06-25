import glob
from skimage.io import *
import numpy as np
#file=glob.glob(r"D:\dol.jpg")[0]
#im=imread(file)
def tobinary(im):
	im2=[]
	for i in range(len(im)):
		a=[]
		for j in range(len(im[i])):
			x=(im[i][j][0]/3+im[i][j][1]/3+im[i][j][2]/3)
			x=x/255
			if x>=0.0015:
				a.append(255)
			else:
				a.append(0)
		im2.append(a)
	im2=np.array(im2)
	return im2
'''from skimage.exposure import *
im4=equalize_hist(im)
im5=tobinary(im4)
imsave("D:\seg.jpg",im5)'''