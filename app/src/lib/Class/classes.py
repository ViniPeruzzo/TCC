import os


class Img:
    _img_list = []
    _path = os.getcwd()
    #_import_folder_name = ""

    def __init__(self):
        pass
    def read_imports(self):
        print(self._path)
