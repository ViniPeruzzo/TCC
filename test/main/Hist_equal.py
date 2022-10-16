from matplotlib.pyplot import cla
import numpy as np
import cv2
import os


img = cv2.imread('C:/Users/vinic/Projetos_Python/TCC/test/images/18.JPG')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = hsv_img[:,:,0], hsv_img[:,:,1], hsv_img[:,:,2],

clahe = cv2.createCLAHE(clipLimit=6.0, tileGridSize=(200,200))
v = clahe.apply(v)

hsv_img = np.dstack((h,s,v))

rgb = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)



cv2.imwrite('C:/Users/vinic/Projetos_Python/TCC/test/images/test.jpg',rgb)
#cv2.waitKey(0)
#cv2.destroyAllWindows()