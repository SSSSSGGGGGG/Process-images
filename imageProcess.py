# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:28:11 2024

@author: SG
"""

import numpy as np
import matplotlib.pyplot as plt



im=plt.imread("0.0.tif")
im1=im[:,:,1] # green channel
# plt.imshow(im1)
im45withlabel=im1[1000:1700,0:700]
im_45withlabel=im1[0:700,1220:1920]

im45=im45withlabel[200:700,200:700]
im_45=im_45withlabel[180:680,200:700] # adjust these arraies to make the light in the center
plt.subplot(2, 2, 1)
plt.imshow(im45withlabel)
plt.title('+45')
plt.subplot(2, 2, 2)
plt.imshow(im_45withlabel)
plt.title('-45')
plt.subplot(2, 2, 3)
plt.imshow(im45)
plt.title('+45')
plt.subplot(2, 2, 4)
plt.imshow(im_45)
plt.title('-45')


def calIntensity(row, col,x,y,r,pol):
    count=0
    sumintensity=0 # for sum work here it should be 0
    for i in range(rows):  
        for j in range(cols):
            distance_squared = (i - x0) ** 2 + (j - y0) ** 2
            if distance_squared < r ** 2:
                if pol=="45":
                    sumintensity += im45[i, j]
                    
                else:
                    sumintensity += im_45[i, j]
                count+=1
                    
    print(f"The sum of the intensity id {sumintensity} and the number of the pixel is {count} ")
    print(f"Then the average of the intensity is {sumintensity/count:.2f}")
    
print("For +45")
rows, cols = np.shape(im45)
x0,y0=rows/2,cols/2 
r=20
cal45=calIntensity(rows, cols, x0, y0, r,"45")
print("For -45")
rows_45, cols_45 = np.shape(im_45)
x0_45,y0_45=rows_45/2,cols_45/2 
cal_45=calIntensity(rows_45, cols_45, x0_45, y0_45, r,"-45")
