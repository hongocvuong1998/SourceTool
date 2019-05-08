import os

def Rename(src,first_name,file_format):
    list_file=os.listdir(src)

    for i in range(len(list_file)):
        file_dst=src+'/'+first_name + str(i)+file_format
        file_src=src+'/'+list_file[i]
        os.rename(file_src,file_dst)
        print(file_src)

Rename("/home/vuonghn/Downloads/Data_Pneumonia/chest_xray/val/PNEUMONIA","PNEUMONIA_",".jpg")

