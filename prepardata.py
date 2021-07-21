import cv2
from pytesseract import  pytesseract # download tesseract here https://tesseract-ocr.github.io/tessdoc/Downloads.html 
from pytesseract import Output
import os 

pytesseract.tesseract_cmd = r'C:\\Program Files\Tesseract-OCR\tesseract.exe' ## change path 


## โหลดรูปมาจัดทำให้อย่ในรูปแบบของ black and white 
img_convert = cv2.imread('./image_krungsri/test_1.jpg') # img paths  

# convert into gray scale.
gray_scale = cv2.cvtColor(img_convert,cv2.COLOR_RGB2GRAY)
# convert gray scale to black and with by using threshold.
thresh, img_black_white  = cv2.threshold(gray_scale, 120, 240, cv2.THRESH_BINARY)
# Save image 
cv2.imwrite('useImage.jpg', img_black_white)


img = cv2.imread('./useImage.jpg')
image_data = pytesseract.image_to_data(img, output_type=Output.DICT, lang="eng+tha")


def eslipType_krungsri (data):

    preType = []
    preType2 = []
    slipType = []

    for i, word in enumerate(data['text']):
        x = image_data['left'][i]
        y = image_data['top'][i]
        if 50 < x < 600 and 270 < y < 360:
            preType.append(word)
    
    for i in preType:
        if i == "Scan":
            type_slip = "Scan"
            slipType.append(type_slip)
            break
        elif  i == "QR":
            type_slip = "QR"
            slipType.append(type_slip)
            break

    if not slipType:
        type_slip = "TF"
        slipType.append(type_slip)

    return slipType

iterate = 0
eslipType = eslipType_krungsri(image_data)
print(eslipType)


## Word and BB not use ## 
Data_QR = []
Data_Scan = []
Data_TF = []
Data_Logo = []
Data_Payment_type = []
Data_bb_notuses = []

## Word and BB use ## 
Data_word = []
Data_BB = []


for i, word in enumerate(image_data['text']):
    x = image_data['left'][i]
    y = image_data['top'][i]
    w = image_data['width'][i]
    h = image_data['height'][i]
    line_num = image_data['line_num'][i]
    block_num = image_data['block_num'][i]
    level = image_data['level'][i]
    par_num = image_data['par_num'][i]
    word_num = image_data['word_num'][i]
    page_num = image_data['page_num'][i]


    if level == 4 or level == 5:

        ## Data_Logo
        if 40 < x < 230 and 220 < y < 255:
            cv2.rectangle(img, (230, 255), (40,220), (255,50,255), 1)
            Data_Logo.append([x, y , w, h, word])
            # print("Not use A: ",x, y, w, h, word)
            print('\n')

        ## Data_Payment_type
        if 50 < x < 600 and 270 < y < 360:
            cv2.rectangle(img, (600, 360), (50,270), (255,50,255), 1)
            Data_Payment_type.append([x, y , w, h, word])
            # print("Not use B: ",x, y, w, h, word)
            print('\n')

        ## Data_Scan
        if eslipType[0] == "Scan":
            
            if 100 < x < 700 and 570 < y < 700: 
                cv2.rectangle(img, (800, 700), (100, 570), (255,50,255), 1)
                Data_Scan.append([x, y , w, h, word])
                # print("Not use C: ",x, y, w, h, word)
            print('\n')              

        ## Data_TF
        if eslipType[0] == "TF":
            
            if 100 < x < 700 and 570 < y < 700: 
                cv2.rectangle(img, (800, 700), (100, 570), (255,50,255), 1)
                Data_TF.append([x, y , w, h, word])
                # print("Not use C: ",x, y, w, h, word)
            print('\n')

        ## Data_QR
        if eslipType[0] == "QR":
            
            if 100 < x < 700 and 570 < y < 920: 
                cv2.rectangle(img, (800, 920), (100, 570), (255,50,255), 1)
                Data_QR.append([x, y , w, h, word])
                # print("Not use C: ",x, y, w, h, word)
            print('\n')
        
        ## Data_BB
        if level == 5:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),1)
            Data_BB.append([x, y, w, h, word])
            # print("word use:",x, y, w, h, word)
            print('\n')

        ## Data_word
        if level == 4:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
            Data_word.append([x, y, w, h, word])
            # print("BB use:",x, y, w, h, word)
            print('\n')

    ## Data_bb_notuses
    else:
        Data_bb_notuses.append([x, y, w, h, word])
        # print("BB Not uses:",x, y, w, h, word)
        print('\n')
        
    iterate = iterate + 1
    
 
## Not use 

print("Data_QR",'\n')
print(Data_QR,'\n')

print("Data_Scan",'\n')
print(Data_Scan,'\n')

print("Data_TF",'\n')
print(Data_TF,'\n')

print("Data_Logo",'\n')
print(Data_Logo,'\n')

print("Data_Payment_type",'\n')
print(Data_Payment_type,'\n')

print("Data_bb_notuses",'\n')
print(Data_bb_notuses,'\n')

print('\n')

##  use 
print("Data_word",'\n')
print(Data_word,'\n')

print("Data_BB",'\n')
print(Data_BB)
 
cv2.imshow("window", img)
cv2.waitKey(0)

 