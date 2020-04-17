import glob
import os
import csv
import shutil
import re
pattern = re.compile(r'^(\d+)(?::([0-5]?\d)(?::([0-5]?\d))?)?$')

ALLOWED_EXTENSIONS = {
    'mp4', 'm4a', 'm4v', 'f4v', 'f4a', 'm4b', 'm4r', 'f4b', 'mov',
    '3gp', '3gp2', '3g2', '3gpp', '3gpp2',
    'ogg', 'oga', 'ogv', 'ogx',
    'wmv', 'wma',
    'avi',
    'mpg',
    'flv',
    'webm',
    'mkv',
    'ts'
}
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def allowed_time(time):
    match = pattern.match(time)
    if not match:
        return False
    else:
        return True


# prefix = '/media/huyvt/DATA/adtech/dataset18/Data_video/Data/16+/Sexy Dance/'
prefix = '/home/vuonghn/Downloads/vccorp/3D'
list_file = set()

count = 0
for root, dirs, files in os.walk(prefix):
    files.sort()
    # print(files)
    for fileName in files:
        path = os.path.join(root, fileName)
        fileNameCSV = os.path.splitext(path)[0] + '.csv'
        if not allowed_file(path) or os.path.exists(fileNameCSV):
            continue
        print(path)
        count+=1
        print('start = 00:00')
        start_time = '00:00'
        list_rs = []
        
        is_end = False
        while(True):
            while True:
                time = input("time(if end is \'end\'): ")
                if (time == 'end'):
                    is_end = True
                    break
                elif (allowed_time(time)):
                    break
                else:
                    print('time eror')
            end_time = time
            if is_end:
                break
            while True:
                try:
                    label = int(input("label (0: binh_thuong, 1: 16+, 2: 18+, 3 is unknow): "))
                    if (label >= 0 and label < 4):
                        break
                    else:
                        print('Don\'t have label is: ',label)
                except:
                    print('Input is not interger')
            
            if label != 3:
                list_rs.append([start_time, end_time, label])
                
            start_time = end_time

        out = open(fileNameCSV, mode='w')
        csv_writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line in list_rs:
            csv_writer.writerow(line)


print('count: ',count)
