import cv2
from pytesseract import  pytesseract # download tesseract here https://tesseract-ocr.github.io/tessdoc/Downloads.html 
from pytesseract import Output
import os 

pytesseract.tesseract_cmd = r'C:\\Program Files\Tesseract-OCR\tesseract.exe' ## change path 

 ## Scan == 8 
 ## QR == 10 
 ## TF == 7 

## โหลดรูปมาจัดทำให้อย่ในรูปแบบของ black and white 
img_convert = cv2.imread('./image_krungsri/test3.jpg') # img paths  

# convert into gray scale.
gray_scale = cv2.cvtColor(img_convert,cv2.COLOR_RGB2GRAY)
# convert gray scale to black and with by using threshold.
thresh, img_black_white  = cv2.threshold(gray_scale, 120, 240, cv2.THRESH_BINARY)
# Save image 
cv2.imwrite('useImage.jpg', img_black_white)


img = cv2.imread('./useImage.jpg')
image_data = pytesseract.image_to_data(img, output_type=Output.DICT, lang="eng+tha")

def findWord(data):
    for i in data:
        print(i)

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


def concatStringData(data_img, type_slip):
    print(data_img)
    print(type_slip)
    range_data = len(data_img)
    print(range_data)
    CC = []
    if range_data == 11 and type_slip == "QR":
        correct_data = ""
        for i,word in enumerate(data_img):
            if i == 3:
                correct_data = correct_data + word
                print("A",i,word, correct_data)
            if i == 4:
                
                correct_data = correct_data + word
                print("B",i,word, correct_data)
                CC.append(correct_data)
            if i != 3 and i != 4:
                print("C",i,word)
                CC.append(word)

    elif range_data == 8 and type_slip == "TF":
        correct_data = ""
        for i,word in enumerate(data_img):
            if i == 3:
                correct_data = correct_data + word
                print("A",i,word, correct_data)
            if i == 4:
                
                correct_data = correct_data + word
                print("B",i,word, correct_data)
                CC.append(correct_data)
            if i != 3 and i != 4:
                print("C",i,word)
                CC.append(word)

    elif range_data == 9 and type_slip == "Scan":
        correct_data = ""
        for i,word in enumerate(data_img):
            if i == 3:
                correct_data = correct_data + word
                print("A",i,word, correct_data)
            if i == 4:
                
                correct_data = correct_data + word
                print("B",i,word, correct_data)
                CC.append(correct_data)
            if i != 3 and i != 4:
                print("C",i,word)
                CC.append(word)
    return CC; 


iterate = 0
eslipType = eslipType_krungsri(image_data)


## Word and BB not use ## 
Data_bb_notuses = []

## Word and BB use ## 
Data_word = []
Data_BB = []

 

## Overall data in image ## 
data_overall_image = []

## Check BB level 4 and 5 ## 
BB_level_4_5 = []

## Create new dict key 
image_data["logoWord"] = []


for i, word in enumerate(image_data['text']):
    x = image_data['left'][i]
    y = image_data['top'][i]
    w = image_data['width'][i]
    h = image_data['height'][i]

    if 0 < x < 650 and 0 < y < 357:
        image_data['logoWord'].append(1)
    else:
        image_data['logoWord'].append(0)
 



        

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
    not_use_logo = image_data['logoWord'][i]

    data_overall_image.append([level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, word])


    if level == 4 or level == 5:

        ## Data_BB
        if level == 4 and not_use_logo != 1:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),1)
            Data_BB.append([level, page_num, block_num, par_num, line_num, word_num,x, y, w, h, word])
            BB_level_4_5.append([level, page_num, block_num, par_num, line_num, word_num,x, y, w, h, word])
            # print("word use:",x, y, w, h, word)

        ## Data_word
        if level == 5 and not_use_logo != 1:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),1)
            Data_word.append([level, page_num, block_num, par_num, line_num, word_num,x, y, w, h, word])
            BB_level_4_5.append([level, page_num, block_num, par_num, line_num, word_num,x, y, w, h, word])
            # print("BB use:",x, y, w, h, word)

    ## Data_bb_notuses
    else:
        Data_bb_notuses.append([level, page_num, block_num, par_num, line_num, word_num,x, y, w, h, word])


        
    iterate = iterate + 1


print('\n')
print("Level 4 and 5")
AA = []
BB = []
CC = []
string_a = ""

for i in BB_level_4_5:
    if i[0] == 4:
        if string_a == "":
            AA.append(string_a)
        else:
            AA.append(string_a)
            string_a = ""

    if i[0] == 5:
        string_a = string_a + i[10]


for i in AA:
    if i != "" and i != " " and i != "  ":
        BB.append(i)

##################

CC = concatStringData(BB, eslipType[0])


if len(CC) == 0:
    print(eslipType)
    print("BB: ",BB, len(BB))
elif len(CC) > 0:
    print(eslipType)
    print("CC: ",CC, len(CC))
 
############

 ## Scan == 8 
 ## QR == 10 
 ## TF == 




 

# print('\n')
# ## overall element in data image 
# print('data_overall_image', '\n')
# for i in data_overall_image:
#     print(i)


# print(image_data)
# find word ## 
# findWord(image_data)
 



cv2.imshow("window", img)
cv2.waitKey(0)


