import os
import cv2
def Rename(src,first_name,file_format):
    list_file=os.listdir(src)

    for i in range(len(list_file)):
        file_dst=src+'/'+first_name + str(i)+file_format
        file_src=src+'/'+list_file[i]
        os.rename(file_src,file_dst)
        print(file_src)

def RemoveFile(src):
    list_file=os.listdir(src)
    for i in range(len(list_file)):
        file_src=src+'/'+list_file[i]
        img=cv2.imread(file_src)
        print(type(img))
        if str(type(img)) != "<class 'numpy.ndarray'>":
            os.remove(file_src)
            continue


root="/home/vuonghn/Downloads/ALL/all"

list_folder=os.listdir(root)

for i in range(len(list_folder)):
        folder=root+'/'+list_folder[i]
        # Rename(folder,"img_",".jpg")
        RemoveFile(folder)    



