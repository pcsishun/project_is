import os

path_of_dir = 'D://project_openCV/project_OCR_eslip/Eslip'
ext = ('.jpg', '.png')

# os.remove('D://project_openCV/project_OCR_eslip/Eslip/receipt_20200605131424(1).png')

for files in os.listdir(path_of_dir):
    if files.endswith(ext):
        if len(files) >= 28:
            delete_path = path_of_dir+'/'+ files
            print(delete_path)
            os.remove(delete_path)
 