import cv2
import pytesseract # download tesseract here https://tesseract-ocr.github.io/tessdoc/Downloads.html 
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' ## change path 

# frame = cv2.imread('./project_OCR_eslip/image/test2.jpg') # img path 
frame = cv2.imread('./image_bkk/test2.jpg') # img path 2 


Himg, Wimg,_ = frame.shape
boxes = pytesseract.image_to_boxes(frame, lang="tha+eng") #lang thai and english

for i in boxes.splitlines():
     i = i.split(' ')
    
     x,y,w,h = int(i[1]),int(i[2]),int(i[3]),int(i[4])

     ## create text area
     cv2.rectangle(frame, (235,5),(55,260),(0,0,255),2)

     ## create text 
     cv2.rectangle(frame, (x,Himg - y), ( w, Himg - h), (225,50,20), 2)
     # cv2.putText(frame,i[0], (x, Himg-y),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
     print(i[0], x, Himg - y, w, Himg - h)

cv2.imshow("ressult", frame)


cv2.waitKey(0)
cv2.destroyAllWindows()

