import cv2
from pytesseract import  pytesseract  
from pytesseract import Output
import numpy as np
import pandas as pd
import os 

pytesseract.tesseract_cmd = r'C:\\Program Files\Tesseract-OCR\tesseract.exe' ## change path 


def imgToWordKBank(image_data):

    dataConcat = []
    stringCon = ""

    dataCreateIndex = []
    dataCleanLevel = []
    array2D = [] 

    indexCreator = 0

    level = []
    page_num = []
    block_num = []
    par_num  = []
    line_num  = []
    left = []
    top = [] 
    width = []  
    height = []
    text = []

    for data in image_data:
        if data == "level":
            for element in image_data[data]:
                level.append(element)
        if data == "page_num":
            for element in image_data[data]:
                page_num.append(element)
        if data == "block_num":
            for element in image_data[data]:
                block_num.append(element)
        if data == "par_num":
            for element in image_data[data]:
                par_num.append(element)
        if data == "line_num":
            for element in image_data[data]:
                line_num.append(element)
        if data == "left":
            for element in image_data[data]:
                left.append(element)
        if data == "top":
            for element in image_data[data]:
                top.append(element)
        if data == "width":
            for element in image_data[data]:
                width.append(element)
        if data == "height":
            for element in image_data[data]:
                height.append(element)
        if data == "text":
            for element in image_data[data]:
                text.append(element)
    
    for iterate, element in enumerate(level):
        array2D.append([
            element,
            page_num[iterate],
            block_num[iterate],
            page_num[iterate],
            line_num[iterate],
            left[iterate],
            top[iterate],
            width[iterate],
            height[iterate],
            text[iterate],
        ])

    for usinglevel in array2D:
        if usinglevel[0] == 4 or usinglevel[0] == 5:
            dataCleanLevel.append(usinglevel)
        
    for iterate,data in enumerate(dataCleanLevel):
        storage = []
        try:
            if data[0] == 4 and dataCleanLevel[iterate+1][0] == 5:
                indexCreator += 1
        except:
            pass

        if indexCreator > 0 and data[0] == 5:
            for element in data:
                storage.append(element)   
            storage.append(indexCreator)
            dataCreateIndex.append(storage)

        else:
            for element in data:
                storage.append(element)
            storage.append(0)
            dataCreateIndex.append(storage)

    storage = []
    for iterate ,data in enumerate(dataCreateIndex):

        if data[0] == 5:
            stringCon += data[9]

        if dataCreateIndex[iterate - 1][0] == 4:
            for  element in dataCreateIndex[iterate - 1]:
                storage.append(element)
                

        if data[0] == 4 and stringCon != "":
            storage.append(stringCon)
            storage.append(dataCreateIndex[iterate - 1][10])
            dataConcat.append(storage)
            stringCon = ""
            storage = []
            

    return dataConcat


def countingWord(dataConcat):

    arrayOfAscii = []
    arrayOfNumber = ['1','2','3','4','5','6','7','8','9','0']
    chatSymbol = []
    countingLang = []

    for code in range(ord('a'), ord('z') + 1):
        arrayOfAscii.append(chr(code))

    for i in dataConcat:

        CountEng = 0
        CountTha = 0
        CountNum = 0
        CountSym = 0
        textDetectLang = i[11]

        for j in textDetectLang:
            if j.isalpha():
                j = j.lower()
                if j in arrayOfAscii:
                    CountEng += 1
                    # print(j, 'Eng')
                else:
                    CountTha += 1
                    # print(j, 'Tha')

            elif j in arrayOfNumber:
                CountNum += 1
                # print(j, "Num")
                
            else:
                CountSym += 1
                # print(j,'Sym')
        
        countingLang.append([CountEng, CountTha, CountNum, CountSym])

    return countingLang

def addCounting(dataNew, countlang):
    data = []
    for iterate,element in enumerate(dataNew):
        store = []
        for i in element:
            store.append(i)
        for j in countlang[iterate]:
            store.append(j)
        data.append(store)

    return data

path_kbank = "./image_kbank/K0.jpg"
path_Krungsri = "./image_krungsri/E6.jpg"


#########################################################
#########################################################
#########################################################

path_of_dir = 'D://project_openCV/project_OCR_eslip/testdata'

featureName = ['Bank', 'level', 'page_num', 'block_num', 'par_num', 'line_num',
 'left','top', 'width', 'height', 'per_word', 'index_order', 'word', 'indexlabel', 'CEng', 'CTha', 'CNum', 'CSym', 'SlipID']

# files = 'K1.jpg'
ext = ('.jpg', '.png')
countStr = 0

dataFrame = []

for iterate,files in enumerate(os.listdir(path_of_dir)):
    if files.endswith(ext):

        img_convert = cv2.imread(path_Krungsri)
        #########################################################

        gray_scale = cv2.cvtColor(img_convert,cv2.COLOR_RGB2GRAY)
        thresh, img_black_white  = cv2.threshold(gray_scale, 120, 240, cv2.THRESH_BINARY)
        cv2.imwrite('extractorImg.jpg', img_black_white)
        img = cv2.imread('./extractorImg.jpg')
        image_data = pytesseract.image_to_data(img, output_type=Output.DICT, lang="eng+tha")
        #########################################################

        dataConcat = imgToWordKBank(image_data)
        countlang = countingWord(dataConcat)
        data = addCounting(dataConcat, countlang)

        bankname = ""

        try:
            store = []
            for i in data:
                if files[0] == 'E':
                    store.append('krungsri')
                    bankname = 'krungsri'
                elif files[0] == 'K':
                    store.append('Kbank')
                    bankname = 'Kbank'

                for j in i:
                    store.append(j)
                store.append(files)
                dataFrame.append(store)
                store = []

            print('Success:', files, 'Bank Name:', bankname)
        except:
            print('Error:', files, 'Bank Name:', bankname)
            pass
                
df = pd.DataFrame(dataFrame, columns= featureName)
df.to_csv('dataTest.csv')