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
    


def extractingArea(data_with_finish_label):

    area_record_data = []

    for i,data in enumerate(data_with_finish_label):
        try:
            if data[14] != data_with_finish_label[i +1][14]:
                if data_with_finish_label[i +1][14] == "Timing":
                    area_record_data.append(["Area", 
                    data[7], 
                    data[8], 
                    data[9], 
                    data[10],
                    "Timing"])
                elif data_with_finish_label[i +1][14] == "Name":
                    area_record_data.append(["Area", 
                    data[7], 
                    data[8], 
                    data[9], 
                    data[10],
                    "Name"])
                elif data_with_finish_label[i +1][14] == "Account":
                    area_record_data.append(["Area", 
                    data[7], 
                    data[8], 
                    data[9], 
                    data[10],
                    "Account"])
                elif data_with_finish_label[i +1][14] == "Amount":
                    area_record_data.append(["Area", 
                    data[7], 
                    data[8], 
                    data[9], 
                    data[10],
                    "Amount"])
                elif data_with_finish_label[i +1][14] == "RefCode":
                    area_record_data.append(["Area", 
                    data[7], 
                    data[8], 
                    data[9], 
                    data[10],
                    "RefCode"])
        except :
            pass
    
    return area_record_data


def data_area_word(data_with_finish_label, data_extractingArea):

    data_record_use = []
    data_concat_word = [] ## return 
    count_loop = 0

    for i in data_with_finish_label:
        if i[14] != "NotUse":
            for j,selectionArea in enumerate(data_extractingArea):
                if selectionArea[5] == i[14]:
                    # print(i[14], data_extractingArea[j][5])
                    data_record_use.append([i[0],
                    i[1],
                    i[2],
                    i[3],
                    i[4],
                    i[5],
                    data_extractingArea[j][1],
                    data_extractingArea[j][2],
                    data_extractingArea[j][3],
                    data_extractingArea[j][4],
                    i[12],
                    i[14]])

    for i in data_record_use:
        
        stringCon = ""

        if i[11] == "Timing" and count_loop == 0:
            for j in data_record_use:
                if j[11] == "Timing":
                    stringCon = stringCon + j[10]
    

            data_concat_word.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], stringCon, i[11]])
            count_loop += 1
        


        if i[11] == "Name"  and count_loop == 1:
            for j in data_record_use:
                if j[11] == "Name":
                    stringCon = stringCon + j[10]


            data_concat_word.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], stringCon, i[11]])
            count_loop += 1


        if i[11] == "Account" and count_loop == 2:
            for j in data_record_use:
                if j[11] == "Account":
                    stringCon = stringCon + j[10]


            data_concat_word.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], stringCon, i[11]])
            count_loop += 1


        if i[11] == "Amount" and count_loop == 3:
            for j in data_record_use:
                if j[11] == "Amount":
                    stringCon = stringCon + j[10]

            data_concat_word.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], stringCon, i[11]])
            count_loop += 1


        if i[11] == "RefCode" and count_loop == 4:
            for j in data_record_use:
                if j[11] == "RefCode":
                    stringCon = stringCon + j[10]

            data_concat_word.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], stringCon, i[11]])
            count_loop += 1

    return data_concat_word


def countingWord(data_concat_word):

    arrayOfAscii = []
    arrayOfNumber = ['1','2','3','4','5','6','7','8','9','0']
    chatSymbol = []
    countingLang = []

    for code in range(ord('a'), ord('z') + 1):
        arrayOfAscii.append(chr(code))
    
    # print(arrayOfAscii)

    for i in data_concat_word:

        CountEng = 0
        CountTha = 0
        CountNum = 0
        CountSym = 0
        textDetectLang = i[10]

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


def arrayWithCount_Final(data_concat_word, texCount, fileName):
    arrayPreToPandas = []
    ErrorFile = []

    try:
        for i, word in enumerate(data_concat_word):
            for j in word:
                # print(j)
                arrayPreToPandas.append(j) 
            for c in texCount[i]:
                # print(c)
                arrayPreToPandas.append(c)
        
            arrayPreToPandas.append(fileName)

        arrayPreToPandas = np.array(arrayPreToPandas)
        arrayPreToPandas = arrayPreToPandas.reshape(5,17)
        print('Sucess:', fileName)

        
    except:
        print('error picture:', fileName, '\n')
        print('array error:', arrayPreToPandas)
        ErrorFile.append(fileName)
        pass


        
    return arrayPreToPandas

 

#################################################################################
#################################################################################
#################################################################################
#################################################################################

path_of_dir = 'D://project_openCV/project_OCR_eslip/image_krungsri'
csvPath = 'D://project_openCV/project_OCR_eslip/csv'

featureName = ['ESlip_Type', 'level', 'page_num', 'block_num', 'par_num', 'line_num',
 'left','top', 'width', 'height', 'word', 'label', 'CEng', 'CTha', 'CNum', 'CSym', 'SlipID']

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
        data_extractingArea = extractingArea(data_with_finish_label)
        data_concat_word = data_area_word(data_with_finish_label, data_extractingArea)
        texCount = countingWord(data_concat_word)
        finsih_array = arrayWithCount_Final(data_concat_word, texCount, files)

        if len(finsih_array) > 0:
            for array_2d in finsih_array:
                dataFrame.append(array_2d.tolist())
        else:
            print('Try to convert in array 2D: \n')
            print(len(finsih_array))
            print(finsih_array)

        if len(dataFrame[iterate]) == 17:
            print('count array :',len(dataFrame[iterate]))
        else:
            print('error array not equal 17 :',len(dataFrame[iterate]), files)
    else:
        continue
 
df = pd.DataFrame(dataFrame, columns= featureName)
df.to_csv('data.csv')