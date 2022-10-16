import gc
import json

class COCO:
    file: json
    annot = []

    def __init__(self, path):
        f = open(path)
        self.file = json.load(f)

        cat = self.cat_load()
        img = self.img_load()
        ann = self.ann_load()

        for x_img in img:
            aux = [x_img[0], x_img[1], x_img[2], x_img[3]]
            aux_ann = []
            for x_ann in ann:
                if x_ann[1] == x_img[0]:
                    aux1 = [x_ann[0], x_ann[2]]
                    for x_cat in cat:
                        if x_cat[0] == aux1[1]:
                            aux1.append(x_cat[1])
                            pass
                    aux1.append(x_ann[3])
                    aux1.append(x_ann[4])
                    aux_ann.append(aux1)
            aux.append(aux_ann)
            self.annot.append(aux)

    def cat_load(self):
        lt = []
        for x in self.file["categories"]:
            lt.append([x["id"], x["name"], x["supercategory"]])
        return lt

    def img_load(self):
        lt = []
        for x in self.file["images"]:
            lt.append([x["id"], x["file_name"], x["height"], x["width"]])
        return lt
    
    def ann_load(self):
        lt = []
        for x in self.file["annotations"]:
            lt.append([x["id"], x["image_id"], x["category_id"], x["bbox"], x["area"]])
        return lt

    def Read_Anott(self):
        return self.annot





