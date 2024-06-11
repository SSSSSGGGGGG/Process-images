# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:28:11 2024

@author: SG
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib as mpl

mpl.rcParams['font.size'] = 20

os.chdir("C:/Users/Laboratorio/scitificCalculation/imageHub/b")
im=plt.imread("0.tif")
im1=im[:,:,2] # green channel
# plt.imshow(im1)
# im45withlabel=im1[1000:2000,0:1050]
# im_45withlabel=im1[0:950,1220:2170]

# im45=im45withlabel[110:610,100:600]
# im_45=im_45withlabel[120:620,100:600] # adjust these arraies to make the light in the center
leftP=im1[0:2048,0:1223]
rightP=im1[0:2048,1224:2448]

im_0=leftP[565:625,540:600] #g=leftP[615:665,645:690], r=leftP[625:715,670:760]
im_45=leftP[1590:1650,540:600] #g=leftP[1640:1690,645:690], r=leftP[1650:1740,670:760]

im_n45=rightP[565:625,540:600] #b=rightP[565:625,540:600]
im_90=rightP[1590:1650,540:600] #b=rightP[1590:1650,540:600]


plt.figure(1,figsize=(10, 10))
plt.subplot(2, 2, 4)
plt.imshow(im_90,vmin=0,vmax=256,cmap='hot')
plt.title('90')
plt.colorbar()
plt.minorticks_on()
plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')

plt.subplot(2, 2, 1)
plt.imshow(im_0,vmin=0,vmax=256,cmap='hot')
plt.title('0')
plt.colorbar()
plt.minorticks_on()
plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')

plt.subplot(2, 2, 3)
plt.imshow(im_45,vmin=0,vmax=256,cmap='hot')
plt.title('+45')
plt.colorbar()
plt.minorticks_on()
plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')

plt.subplot(2, 2, 2)
plt.imshow(im_n45,vmin=0,vmax=256,cmap='hot')
plt.title('-45')
plt.colorbar()
plt.minorticks_on()
plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')

plt.figure(2,figsize=(10, 10))
plt.imshow(im1,vmin=0,vmax=256,cmap='hot')
plt.title('left')
plt.colorbar()
plt.minorticks_on()
plt.grid(which='minor',linestyle=':', linewidth='0.1', color='gray')

def calIntensity(row, col,x,y,r,pol):
    count=0
    sumintensity=0 # for sum work here it should be 0
    for i in range(rows):  
        for j in range(cols):
            distance_squared = (i - x0) ** 2 + (j - y0) ** 2
            if distance_squared < r ** 2:
                if pol=="45":
                    sumintensity += im_45[i, j]
                    
                else:
                    sumintensity += im_n45[i, j]
                count+=1
                    
    print(f"The sum of the intensity id {sumintensity} and the number of the pixel is {count} ")
    print(f"Then the average of the intensity is {sumintensity/count:.2f}")
    
print("For +45")
rows, cols = np.shape(im_45)
x0,y0=rows/2,cols/2 
r=20
cal45=calIntensity(rows, cols, x0, y0, r,"45")
print("For -45")
rows_45, cols_45 = np.shape(im_n45)
x0_45,y0_45=rows_45/2,cols_45/2 
cal_45=calIntensity(rows_45, cols_45, x0_45, y0_45, r,"-45")
