from lib.images_controller import *
import os 
import psutil



#tr = Train_Images(os.getcwd())
#tr.Show_img(5)
#del(tr)
#gc.collect()


val = Val_Images(os.getcwd())
val.Show_img(5)
del(val)
gc.collect()



tes = Test_Images(os.getcwd())
tes.Show_img(5)
del(tes)
gc.collect()

