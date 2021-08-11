import os

path_of_dir = 'D://project_openCV/project_OCR_eslip/image_krungsri'
ext = ('.jpg', '.png')
countStr = 0

for files in os.listdir(path_of_dir):
    if files.endswith(ext):
        scr = path_of_dir + '/' + files
        crateName = path_of_dir
        crateName = crateName+'/'+"F"+ str(countStr) + ".jpg" ## Change name here 
        os.rename(scr, crateName)
        countStr += 1
    else:
        continue