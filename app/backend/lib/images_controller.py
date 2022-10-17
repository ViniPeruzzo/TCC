
import gc
import os 
import cv2
import numpy
from PIL import Image
from .coco_anott import *

class Train_Images:
    image_path = '/app/backend/dir/Imagens_anotadas_coco/train'
    app_path = ''
    complete_path = ''

    Global_Train_Images=[]


    def __init__(self, path):
        self.app_path = path
        self.complete_path = f"{self.app_path}{self.image_path}"
        img_list = []
        annotation: list

        x=[]
        for path in os.listdir(self.complete_path):
            if path.count('.jpg') != 0:
                x = [(cv2.imread(f'{self.complete_path}/{path}')),str(path)]
                img_list.append(x)
            if path.count('.json') != 0:
                an = COCO(f'{self.complete_path}/{path}')
                annotation = an.Read_Anott()
        

        for x_1 in annotation:
            aux = [x_1[0], x_1[1], x_1[2], x_1[3]]

            for y in img_list:
                if y[1] == aux[1]:
                    aux.append(y[0])
                    pass
            
            aux.append(x_1[4])
            self.Global_Train_Images.append(aux)
        
        
    def Show_img(self, num: int):

        img_list_aux = self.Global_Train_Images[num]

        img_aux = img_list_aux[4]
        annot_aux = img_list_aux[5]

        for x in annot_aux:
            ann_x = x[3][0]
            ann_y = x[3][1]
            ann_w = int(x[3][2])
            ann_h = int(x[3][3])
            cv2.line(img_aux,(ann_x,ann_y),(ann_x + ann_w,ann_y),(0,0,255), 3)
            cv2.line(img_aux,(ann_x + ann_w,ann_y),(ann_x + ann_w,ann_y + ann_h),(0,0,255), 3)
            cv2.line(img_aux,(ann_x + ann_w,ann_y + ann_h),(ann_x,ann_y + ann_h),(0,0,255), 3)
            cv2.line(img_aux,(ann_x,ann_y + ann_h),(ann_x,ann_y),(0,0,255), 3)

        im_pil = Image.fromarray(cv2.cvtColor(img_aux, cv2.COLOR_BGR2RGB))
        im_pil.show()


class Val_Images:
    image_path = '/app/backend/dir/Imagens_anotadas_coco/valid'
    app_path = ''
    complete_path = ''

    Global_Train_Images=[]


    def __init__(self, path):
        self.app_path = path
        self.complete_path = f"{self.app_path}{self.image_path}"
        img_list = []
        annotation: list

        x=[]
        for path in os.listdir(self.complete_path):
            if path.count('.jpg') != 0:
                x = [(cv2.imread(f'{self.complete_path}/{path}')),str(path)]
                img_list.append(x)
            if path.count('.json') != 0:
                an = COCO(f'{self.complete_path}/{path}')
                annotation = an.Read_Anott()
        

        for x_1 in annotation:
            aux = [x_1[0], x_1[1], x_1[2], x_1[3]]

            for y in img_list:
                if y[1] == aux[1]:
                    aux.append(y[0])
                    pass
            
            aux.append(x_1[4])
            self.Global_Train_Images.append(aux)
        
        
    def Show_img(self, num: int):

        img_list_aux = self.Global_Train_Images[num]

        img_aux = img_list_aux[4]
        annot_aux = img_list_aux[5]

        for x in annot_aux:
            ann_x = x[3][0]
            ann_y = x[3][1]
            ann_w = int(x[3][2])
            ann_h = int(x[3][3])
            cv2.line(img_aux,(ann_x,ann_y),(ann_x + ann_w,ann_y),(0,0,255), 3)
            cv2.line(img_aux,(ann_x + ann_w,ann_y),(ann_x + ann_w,ann_y + ann_h),(0,0,255), 3)
            cv2.line(img_aux,(ann_x + ann_w,ann_y + ann_h),(ann_x,ann_y + ann_h),(0,0,255), 3)
            cv2.line(img_aux,(ann_x,ann_y + ann_h),(ann_x,ann_y),(0,0,255), 3)

        im_pil = Image.fromarray(cv2.cvtColor(img_aux, cv2.COLOR_BGR2RGB))
        im_pil.show()



class Test_Images:
    image_path = '/app/backend/dir/Imagens_anotadas_coco/test'
    app_path = ''
    complete_path = ''

    Global_Train_Images=[]


    def __init__(self, path):
        self.app_path = path
        self.complete_path = f"{self.app_path}{self.image_path}"
        img_list = []
        annotation: list

        x=[]
        for path in os.listdir(self.complete_path):
            if path.count('.jpg') != 0:
                x = [(cv2.imread(f'{self.complete_path}/{path}')),str(path)]
                img_list.append(x)
            if path.count('.json') != 0:
                an = COCO(f'{self.complete_path}/{path}')
                annotation = an.Read_Anott()
        

        for x_1 in annotation:
            aux = [x_1[0], x_1[1], x_1[2], x_1[3]]

            for y in img_list:
                if y[1] == aux[1]:
                    aux.append(y[0])
                    pass
            
            aux.append(x_1[4])
            self.Global_Train_Images.append(aux)
        
        
    def Show_img(self, num: int):

        img_list_aux = self.Global_Train_Images[num]

        img_aux = img_list_aux[4]
        annot_aux = img_list_aux[5]

        for x in annot_aux:
            ann_x = x[3][0]
            ann_y = x[3][1]
            ann_w = int(x[3][2])
            ann_h = int(x[3][3])
            cv2.line(img_aux,(ann_x,ann_y),(ann_x + ann_w,ann_y),(0,0,255), 3)
            cv2.line(img_aux,(ann_x + ann_w,ann_y),(ann_x + ann_w,ann_y + ann_h),(0,0,255), 3)
            cv2.line(img_aux,(ann_x + ann_w,ann_y + ann_h),(ann_x,ann_y + ann_h),(0,0,255), 3)
            cv2.line(img_aux,(ann_x,ann_y + ann_h),(ann_x,ann_y),(0,0,255), 3)

        im_pil = Image.fromarray(cv2.cvtColor(img_aux, cv2.COLOR_BGR2RGB))
        im_pil.show()

    def Return_img(self):
        return self.Global_Train_Images
