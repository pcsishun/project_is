import cv2
from pytesseract import  pytesseract # download tesseract here https://tesseract-ocr.github.io/tessdoc/Downloads.html 
from pytesseract import Output

pytesseract.tesseract_cmd = r'C:\\Program Files\Tesseract-OCR\tesseract.exe' ## change path 
img = cv2.imread('./image_krungsri/test_1.jpg') # img path 2 

image_data = pytesseract.image_to_data(img, output_type=Output.DICT, lang="eng+tha")


for i, word in enumerate(image_data['text']):
    x = image_data['left'][i]
    y = image_data['top'][i]
    w = image_data['width'][i]
    h = image_data['height'][i]

    notUseArea_X = [60,97,85,0]
    notUseArea_Y = [221,36,140,170,0]
    notUseArea_W = [221,188,199,137,870]
    notUseArea_H = [255,127,194,1882]

    if word != " " and word != "":
        print('word:',word ,' ',x, ' ', y, ' ', x+w, ' ', y+h)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),1)
        
    else:

        #cv2.rectangle(img, (60, 221), (221, 255), (255,50,255), 2) ## Not use 
        cv2.rectangle(img, (57, 0), (227, 218), (255,50,255), 3) ## Logo

        cv2.rectangle(img, (313, 472), (593, 498), (255,50,255), 3) ## ชื่อผู้โอน 
        cv2.rectangle(img, (312, 528), (480, 546), (255,50,255), 3) ## เลขบัญชีผู้โอน


        cv2.rectangle(img, (313, 472), (593, 546), (0,255,0), 3) ## Not use BB 

        if x not in notUseArea_X and y not in notUseArea_Y and x+w not in notUseArea_W and y+h not in notUseArea_H:
            print("BB :",word ,' ',x, ' ', y, ' ', x+w, ' ', y+h)
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,50), 2)
            # cv2.rectangle(img, (64, 287), (545, 358), (255,0,50), 2) ## Scan to pay
            # cv2.rectangle(img, (67, 365), (405, 397), (255,0,50), 2) ## TimeStamp
            
 
            
            
 
cv2.imshow("window", img)
cv2.waitKey(0)