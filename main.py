import os
import shutil
sorter = os.environ.get('sorting')

IgnoreDownTypes = 'oad,tmp'
IgnoreFileTypes = 'exe,msi,apk,.gz,tar,gin,zip'

def print_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            print(os.path.join(directory, filename))
            continue
        else:
            continue




def sort(dir):
    for f in os.listdir(dir):
        FileExtension = f[-3:]
        if IgnoreDownTypes.find(FileExtension) != -1:
            continue
        elif IgnoreFileTypes.find(FileExtension) != 1:
            shutil.move(sorter+f,eg.globals.jobpath+f)
            print eg.globals.jobpath+f
        elif IgnoreFileTypes.find(FileExtension) != -1:
            shutil.move(sorter+f,'C:\\Users\\Dan.Edens\\Downloads\\')
            print ("Transfer to Programs complete")



if __name__ == '__main__':
    print_files(sorter)

