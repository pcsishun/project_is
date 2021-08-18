import cv2
from pytesseract import  pytesseract # download tesseract here https://tesseract-ocr.github.io/tessdoc/Downloads.html 
from pytesseract import Output
import numpy as np
import pandas as pd
import os 

pytesseract.tesseract_cmd = r'C:\\Program Files\Tesseract-OCR\tesseract.exe' ## change path 

#################################################################################
#################################################################################
#################################################################################
#################################################################################


def findWord(data):
    for i in data:
        print(i)

def eslipType_krungsri(data):

    preType = []
    preType2 = []
    slipType = []
    eslipTypeArray = ['Scan','QR']

    for word in data['text']:
        if word == "Scan":
            preType.append('Scan')
            break
        elif word == "QR":
            preType.append('QR')
            break
    
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

    range_data = len(data_img)

    CC = []
    if range_data == 11 and type_slip == "QR":
        correct_data = ""
        for i,word in enumerate(data_img):
            if i == 3:
                correct_data = correct_data + word
                # print("A",i,word, correct_data)
            if i == 4:
                
                correct_data = correct_data + word
                # print("B",i,word, correct_data)
                CC.append(correct_data)
            if i != 3 and i != 4:
                # print("C",i,word)
                CC.append(word)

    elif range_data == 8 and type_slip == "TF":
        correct_data = ""
        for i,word in enumerate(data_img):
            if i == 3:
                correct_data = correct_data + word
                # print("A",i,word, correct_data)
            if i == 4:
                
                correct_data = correct_data + word
                # print("B",i,word, correct_data)
                CC.append(correct_data)
            if i != 3 and i != 4:
                # print("C",i,word)
                CC.append(word)

    elif range_data == 9 and type_slip == "Scan":
        correct_data = ""
        for i,word in enumerate(data_img):
            if i == 3:
                correct_data = correct_data + word
                # print("A",i,word, correct_data)
            if i == 4:
                
                correct_data = correct_data + word
                # print("B",i,word, correct_data)
                CC.append(correct_data)
            if i != 3 and i != 4:
                # print("C",i,word)
                CC.append(word)
    return CC; 


def tagLabelToData(eslipType, data_overall_image):

    data_with_label = []
    passing = 0
    eslipType = eslipType[0]

    for i,data in enumerate(data_overall_image):
        
        level = data[0]
        page_num = data[1]
        block_num = data[2]
        par_num = data[3]
        line_num = data[4]
        word_num = data[5]
        x = data[6]
        y = data[7]
        w = data[8]
        h = data[9]
        not_use_logo = data[10]
        word = data[11]
        
        if data[10] == 1:
            label = 0 
            data_with_label.append([eslipType, level, page_num, block_num, par_num, line_num, word_num, x, y ,w, h, not_use_logo, word,  label])
        
        elif data[10] == 0:
            label_categorical = [["1",1], ["2",2], ["3",3], ["4",4], ["5",5], ["6",6], ["7",7], ["8",8], ["9",9], ["10",10], ["11",11], ["12",12], 
            ["13",13], ["14",14], ["15",15], ["16",16], ["17",17], ["18",18], ["19",19], ["20",20]]
            alert = []
            
            if data[0] == 4:
                label = 0
                # print(passing)
                # print("data[0] == 4: ",[eslipType, level, page_num, block_num, par_num, line_num, word_num, x, y ,w, h, not_use_logo, word,  label])
                data_with_label.append([eslipType, level, page_num, block_num, par_num, line_num, word_num, x, y ,w, h, not_use_logo, word,  label])
                    
            elif data[0] == 5:
                label = label_categorical[passing][1]
                # print(passing)
                # print("data[0] == 5: ",[eslipType, level, page_num, block_num, par_num, line_num, word_num, x, y ,w, h, not_use_logo, word,  label])
                data_with_label.append([eslipType, level, page_num, block_num, par_num, line_num, word_num, x, y ,w, h, not_use_logo, word,  label])
                alert.append(1)
                    
            try:
                # print(alert[0])
                try:
                    data_overall_image[i + 1][0]
                    # print(data[0], data_overall_image[i+1][0])
                    if data[0] == 5 and data_overall_image[i + 1][0] == 4:
                        # print("Try: ",data[0], data_overall_image[i + 1][0])
                        passing = passing + 1
                        # print("passing",passing)
                except :
                    # print("Over array")
                    pass
            except :
                # print("No alert")
                pass

    return data_with_label


def departDataOfImage(image_data):

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

    countingArray = []
    perfectArray = []
    
    string_a = ""
    passingRemark = 0

    for i, word in enumerate(image_data['text']):
        x = image_data['left'][i]
        y = image_data['top'][i]
        w = image_data['width'][i]
        h = image_data['height'][i]
    
        arrayLogoStop = ['01','02','03','04','05','06','07','08',
        '09','10','11','12','13','14','15','16',
        '17','18','19','20','21','22','23','24',
        '25','26','27','28','29','30','31']
        
        # print(passingRemark)
        if passingRemark == 0:
            if word in arrayLogoStop:
                image_data['logoWord'].append(0)
                passingRemark = passingRemark + 1
            
            elif word not in arrayLogoStop:
                image_data['logoWord'].append(1)

        elif passingRemark > 0:
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

        # data_overall_image.append([level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, word])


        if level == 4 or level == 5:

            ## Data_BB
            if level == 4 and not_use_logo != 1:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),1)
                Data_BB.append([level, page_num, block_num, par_num, line_num, word_num,x, y, w, h, word])
                BB_level_4_5.append([level, page_num, block_num, par_num, line_num, word_num,x, y, w, h, word])
                data_overall_image.append([level, page_num, block_num, par_num, line_num, word_num,x, y, w, h, not_use_logo, word])
                # print("word use:",x, y, w, h, word)

            ## Data_word
            if level == 5 and not_use_logo != 1:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),1)
                Data_word.append([level, page_num, block_num, par_num, line_num, word_num,x, y, w, h, word])
                BB_level_4_5.append([level, page_num, block_num, par_num, line_num, word_num,x, y, w, h, word])
                data_overall_image.append([level, page_num, block_num, par_num, line_num, word_num,x, y, w, h, not_use_logo, word])
                # print("BB use:",x, y, w, h, word)
            else:
                data_overall_image.append([level, page_num, block_num, par_num, line_num, word_num,x, y, w, h, not_use_logo, word])
    

        else:
            Data_bb_notuses.append([level, page_num, block_num, par_num, line_num, word_num,x, y, w, h, word])

    for i in BB_level_4_5:
        if i[0] == 4:
            if string_a == "":
                countingArray.append(string_a)
            else:
                countingArray.append(string_a)
                string_a = ""

        if i[0] == 5:
            string_a = string_a + i[10]


    for i in countingArray:
        if i != "" and i != " " and i != "  ":
            perfectArray.append(i)

    # print(image_data)
    # print(len(image_data['logoWord']))
    # print(len(image_data['text']))
    return perfectArray, countingArray, BB_level_4_5, data_overall_image



def finishCreateLabel(data_with_label, perfectArray, eslipType):

    arrayLabelName = ["Timing", "Name", "Account", "Amount", "RefCode"]
    rangeArray = len(perfectArray)
    finishData = []

    # print('rangeArray:', rangeArray)

    for index, arrays in enumerate(data_with_label):


        arrayType = arrays[0]
        level = arrays[1]
        page_num = arrays[2]
        block_num = arrays[3]
        par_num = arrays[4]
        line_num = arrays[5]
        word_num = arrays[6]
        x = arrays[7]
        y = arrays[8]
        w = arrays[9]
        h = arrays[10]
        not_use_logo = arrays[11]
        word = arrays[12]
        tagingRow = arrays[13]

        
        if eslipType[0] == "QR":

            if rangeArray == 11:
                # arrayLabelName = ["Timing", "Name", "Account", "Amount", "RefCode"]
                if arrays[13] == 1:
                    labeldata = arrayLabelName[0]
                    indexLabel = 1
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])
                
                elif arrays[13] == 2:
                    labeldata = arrayLabelName[1]
                    indexLabel = 2
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 3:
                    labeldata = arrayLabelName[2]
                    indexLabel = 3
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 9:
                    labeldata = arrayLabelName[3]
                    indexLabel = 4
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 11:
                    labeldata = arrayLabelName[4]
                    indexLabel = 5
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])
                
                else:
                    labeldata = "NotUse"
                    indexLabel = 0
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

    
            elif rangeArray == 10:
                # arrayLabelName = ["Timing", "Name", "Account", "Amount", "RefCode"]
                if arrays[13] == 1:
                    labeldata = arrayLabelName[0]
                    indexLabel = 1
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])
                
                elif arrays[13] == 2:
                    labeldata = arrayLabelName[1]
                    indexLabel = 2
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 3:
                    labeldata = arrayLabelName[2]
                    indexLabel = 3
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 8:
                    labeldata = arrayLabelName[3]
                    indexLabel = 4
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 10:
                    labeldata = arrayLabelName[4]
                    indexLabel = 5
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                else:
                    labeldata = "NotUse"
                    indexLabel = 0
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

            else:
                # print("error")
                break

        elif eslipType[0] == "Scan":
            if rangeArray == 8:
                # arrayLabelName = ["Timing", "Name", "Account", "Amount", "RefCode"]
                if arrays[13] == 1:
                    labeldata = arrayLabelName[0]
                    indexLabel = 1
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])
                
                elif arrays[13] == 2:
                    labeldata = arrayLabelName[1]
                    indexLabel = 2
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 3:
                    labeldata = arrayLabelName[2]
                    indexLabel = 3
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 6:
                    labeldata = arrayLabelName[3]
                    indexLabel = 4
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 8:
                    labeldata = arrayLabelName[4]
                    indexLabel = 5
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])
                
                else:
                    labeldata = "NotUse"
                    indexLabel = 0
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

    
            elif rangeArray == 9:
                # arrayLabelName = ["Timing", "Name", "Account", "Amount", "RefCode"]
                if arrays[13] == 1:
                    labeldata = arrayLabelName[0]
                    indexLabel = 1
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])
                
                elif arrays[13] == 2:
                    labeldata = arrayLabelName[1]
                    indexLabel = 2
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 3:
                    labeldata = arrayLabelName[2]
                    indexLabel = 3
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 7:
                    labeldata = arrayLabelName[3]
                    indexLabel = 4
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 9:
                    labeldata = arrayLabelName[4]
                    indexLabel = 5
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                else:
                    labeldata = "NotUse"
                    indexLabel = 0
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

            else:
                # print("error")
                break

        elif eslipType[0] == "TF":
            if rangeArray == 8:
                # arrayLabelName = ["Timing", "Name", "Account", "Amount", "RefCode"]
                if arrays[13] == 1:
                    labeldata = arrayLabelName[0]
                    indexLabel = 1
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])
                
                elif arrays[13] == 2:
                    labeldata = arrayLabelName[1]
                    indexLabel = 2
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 3:
                    labeldata = arrayLabelName[2]
                    indexLabel = 3
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 7:
                    labeldata = arrayLabelName[3]
                    indexLabel = 4
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 9:
                    labeldata = arrayLabelName[4]
                    indexLabel = 5
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])
                
                else:
                    labeldata = "NotUse"
                    indexLabel = 0
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

    
            elif rangeArray == 7:
                # arrayLabelName = ["Timing", "Name", "Account", "Amount", "RefCode"]
                if arrays[13] == 1:
                    labeldata = arrayLabelName[0]
                    indexLabel = 1
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])
                
                elif arrays[13] == 2:
                    labeldata = arrayLabelName[1]
                    indexLabel = 2
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 3:
                    labeldata = arrayLabelName[2]
                    indexLabel = 3
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 6:
                    labeldata = arrayLabelName[3]
                    indexLabel = 4
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                elif arrays[13] == 8:
                    labeldata = arrayLabelName[4]
                    indexLabel = 5
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

                else:
                    labeldata = "NotUse"
                    indexLabel = 0
                    finishData.append([arrayType, level, page_num, block_num, par_num, line_num, word_num, x, y, w, h, not_use_logo, word, tagingRow, labeldata, indexLabel])

            else:
                # print("error")
                break
    
    return finishData 
    


def autoLabel(data_with_finish_label):
    start_operate = True
    dataNew = []
    areaData = []
    label_use = []
    string_con = ""
    for iterate,data_array in enumerate(data_with_finish_label):

        if start_operate == True :
            if data_array[1] == 5:
                # print('if data_array[1] == 5: ',data_array)
                string_con += data_array[12]
                label_use.append(data_array[14])
                if data_with_finish_label[iterate-1][1] == 4:
                    for iterate2 in data_with_finish_label[iterate-1]:
                        areaData.append(iterate2)

            if data_array[1] == 4 and string_con != "":
                # print('data_array[1] == 4 and string_con != "":', data_array)
                areaData.append(string_con)
                areaData.append(label_use[0])
                dataNew.append(areaData)
                string_con = ""
                areaData = []
                label_use = []
    
    return dataNew


def countingWord(data_concat_word):

    arrayOfAscii = []
    arrayOfNumber = ['1','2','3','4','5','6','7','8','9','0']
    chatSymbol = []
    countingLang = []

    for code in range(ord('a'), ord('z') + 1):
        arrayOfAscii.append(chr(code))


    for i in data_concat_word:

        CountEng = 0
        CountTha = 0
        CountNum = 0
        CountSym = 0
        textDetectLang = i[16]

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

def dataTopandas(dataBeforeCount, texCount, files):
    dataNew = []
    array1D = []
    for iterate, data in enumerate(dataBeforeCount):
        counttext = texCount[iterate]
        array1D.append('krungsri')
        for j in data:
            array1D.append(j)
        
        for j in counttext:
            array1D.append(j)

        array1D.append(files)
        dataNew.append(array1D)
        array1D = []

    return dataNew
 

#################################################################################
#################################################################################
#################################################################################
#################################################################################
 
 

path_of_dir = 'D://project_openCV/project_OCR_eslip/image_krungsri'
csvPath = 'D://project_openCV/project_OCR_eslip/csv'

featureName = ['Bank','ESlip_Type', 'level', 'page_num', 'block_num', 'par_num', 'line_num',
 'word_num','left','top', 'width', 'height', 'label_index', 'per_word', 'index_order', 
 'old_label','old_index', 'word', 'label', 'CEng', 'CTha', 'CNum', 'CSym', 'SlipID']

ext = ('.jpg', '.png')
countStr = 0

dataFrame = []

for iterate,files in enumerate(os.listdir(path_of_dir)):

    if files.endswith(ext):
        # print(files)
        img_convert = cv2.imread('./image_krungsri/'+files) # img paths  
        gray_scale = cv2.cvtColor(img_convert,cv2.COLOR_RGB2GRAY)
        thresh, img_black_white  = cv2.threshold(gray_scale, 120, 240, cv2.THRESH_BINARY)
        cv2.imwrite('useImage.jpg', img_black_white)
        img = cv2.imread('./useImage.jpg')
        image_data = pytesseract.image_to_data(img, output_type=Output.DICT, lang="eng+tha")
        
        data_of_image = departDataOfImage(image_data)
        data_overall_image = data_of_image[3]
        perfectArray = data_of_image[0]
        countingArray = data_of_image[1]
        
        eslipType = eslipType_krungsri(image_data)
        CC = concatStringData(perfectArray, eslipType[0])
        data_with_label = tagLabelToData(eslipType, data_overall_image)
        data_with_finish_label = finishCreateLabel(data_with_label, perfectArray, eslipType)
        dataBeforeCount = autoLabel(data_with_finish_label)
        texCount = countingWord(dataBeforeCount)
        
        try:
            finsih_array = dataTopandas(dataBeforeCount, texCount, files)

            for i in finsih_array:
                dataFrame.append(i)
            print('Success:', files)
            
        except:
            print('error:', files)
         
df = pd.DataFrame(dataFrame, columns= featureName)
df.to_csv('data_krungsri.csv')


 
##################################################
##################################################
##################################################