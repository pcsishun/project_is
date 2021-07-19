import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

from PIL import Image
import cv2


def img_ocr(path):

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 
    thresh = 200 
    img_binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]
    path_save = './image_kbank/rescale_img.jpg'
    cv2.imwrite(path_save,img_binary) 


    img_g = Image.open(path_save)
    text = tess.image_to_string(img_g, lang="tha") 
    array_text = list(text.split("\n"))
    
    array_drop_blank = []

    for i in array_text:
        if i != "" and i != " " and i != "  ":
            array_drop_blank.append(i)


    return array_drop_blank

def debug_depart_element_list(array_list):
    for iters, string_e in enumerate(array_list):
        print('{}. element: {}'.format(iters + 1, string_e))
    print('\n')
    


def position_img(img):
    Himg, Wimg, _ = img.shape
    print(Himg, '\n')
    print(Wimg)

    
path = './image_kbank/42884.jpg'

arra_ystring = img_ocr(path)
debug_depart_element_list(arra_ystring)

# print("Kbank: ",arra_ystring,'\n')
# print("Array Count: ", len(arra_ystring))


 
 
 

 
 