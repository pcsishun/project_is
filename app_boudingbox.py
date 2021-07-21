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


iterate = 0
indexTextArea_info = [] 


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
        iterate = iterate + 1 
        if level == 5:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),1)

        if level == 4:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
    
        print(iterate,'index', i,'level', level, 'page_num', page_num,'block_num', block_num,'par_num', par_num,'line_num'
        , line_num,'word_num', word_num,'left', x,'top', y,'width', w,'height',h , 'Word predict = ', word)


        # [ index, x, y, w, h, มี BB หรือไม่, มีคำหรือไม่, BB นั้นจะใช้หรือไม่ใช้]
        if word != "" or word != " ":
            indexTextArea_info.append([i, x, y, w, h, 1, 1, word])

        elif  word  == "" or word == " ":
            indexTextArea_info.append([i, x, y, w, h, 1, 0, word])

  


print(indexTextArea_info)
cv2.imshow("window", img)
cv2.waitKey(0)

 
# for i, word in enumerate(image_data['text']):
#     x = image_data['left'][i]
#     y = image_data['top'][i]
#     w = image_data['width'][i]
#     h = image_data['height'][i]



#     ## คำ
#     if word != " " and word != "":
#         if  x  > 80 and y > 34 and w+x < 200 and h+y < 200:
#             print('Word not use:', word, ' ', x, ' ', y, ' ', x+w, ' ', y+h)
#         else:
#             print('word:',word ,' ',x, ' ', y, ' ',   x+w, ' ', y+h)
#             cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),1)
        
#     else:
#         ###########################
#         ######### Debug ###########
#         ###########################

#         #cv2.rectangle(img, (60, 221), (221, 255), (255,50,255), 2) ## Not use 
#         cv2.rectangle(img, (57, 0), (227, 218), (255,50,255), 3) ## Logo

# #   x=80 y=34 w=139 h=200
#         ## BB testing debug 
#         cv2.rectangle(img, (80, 34), (200, 200), (50,255,255), 3) # img test4.jpg


#         ## ผู้โอน กับ เลขบัญชีผู้โอน 
#         cv2.rectangle(img, (313, 472), (593, 498), (255,50,255), 3) ## ชื่อผู้โอน 
#         cv2.rectangle(img, (312, 528), (480, 546), (255,50,255), 3) ## เลขบัญชีผู้โอน


#         cv2.rectangle(img, (313, 472), (593, 546), (0,255,0), 3) ## Not use BB 
        
#         ## ผูุ้รับโอน กับ เลขบัญชีผู้รับโอน 
#         cv2.rectangle(img, (313, 588), (644, 634), (255,50,255), 3) ## ชื่อรับผู้โอน 
#         cv2.rectangle(img, (312, 652), (476, 670), (255,50,255), 3) ## เลขบัญชีผู้โอน 

#         cv2.rectangle(img, (313, 588), (644, 670), (0,255,0), 3) ## Not use BB 

#         ###########################
#         ###########################
#         ###########################

#         if x not in notUseArea_X and y not in notUseArea_Y and x+w not in notUseArea_W and y+h not in notUseArea_H:
#             print("BB :",word ,' ',x, ' ', y, ' ', x+w, ' ', y+h)
#             cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,50), 2)
#             # cv2.rectangle(img, (64, 287), (545, 358), (255,0,50), 2) ## Scan to pay
#             # cv2.rectangle(img, (67, 365), (405, 397), (255,0,50), 2) ## TimeStamp
            
 
            
            
 
# cv2.imshow("window", img)
# cv2.waitKey(0)