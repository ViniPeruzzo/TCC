#%%
from lib.images_controller import *
import os 
import psutil
import cv2
from PIL import Image



#tr = Train_Images(os.getcwd())
#tr.Show_img(5)
#del(tr)
#gc.collect()


#val = Val_Images(os.getcwd())
#val.Show_img(5)
#del(val)
#gc.collect()



tes = Test_Images(os.getcwd())
img = tes.Return_img()


img_orig = img[0]

img_height = img_orig[2]
img_width = img_orig[3]
img_scale = 0.5




print(img_orig)






