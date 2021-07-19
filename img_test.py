import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

import cv2
 

def position_img(img):
    Himg, Wimg, _ = img.shape
    boxes = tess.image_to_boxes(img, lang= "eng+tha")
    #print(boxes)
    for iteration_,i in enumerate(boxes.splitlines()):
        i = i.split()
        #print(iteration_, i)
        x,y,w,h = int(i[1]),int(i[2]),int(i[3]),int(i[4])

             ## Show rectangle 
             ## #print("Character: {}, X-axis {}, y-axis {}, hight {}, width {}".format(i[0], x, y, w, h))
        convert_x, convert_y, convert_w, convert_h =   (x), (Himg - y), (w), (Himg- h)
        print(i[0],convert_x, convert_y, convert_w, convert_h)

         



image_path = cv2.imread('./project_OCR_eslip/image/test2.jpg')
position_img(image_path)
 