import pandas as pd 
import numpy as np 
import os


arrayThaLang = ['ฎ','พ','ฑ','ธ','ร', 'ณ', 'น', 'ย', 'ญ', 'บ', 'ฐ', 'ล', 'ฟ', 'ฤ', 'ห',
 'ฆ', 'ก', 'ฏ','ด', 'ฌ','ษ', 'ส','ศ', 'ว', 'ซ', 'ง', 'ผ', 'ป','ฉ', 'อ', 'ฮ' , 'ท', 'ม', 'ฒ','ฬ', 'ฝ', 'ฦ', 'ภ', 'ถ', 'ค', 'ต' ,'จ' , 'ข', 'ช']

arrayEngLang = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
arrayNumLang = ['1','2','3','4','5','6','7','8','9','0']
arraySymLang = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']',';',':','<','>','.','?','/','฿','',' ']
feature_col = []

# print(len(arrayThaLang)) 
# print(len(arrayEngLang)) 
# print(len(arrayNumLang)) 
# print(len(arraySymLang)) 

df = pd.read_csv('./trainingData/TrainingData.csv')

# for i in df:
#     feature_col.append(i)

for i in arrayThaLang:
    feature_col.append(i)

for i in arrayEngLang:
    feature_col.append(i)

for i in arrayNumLang:
    feature_col.append(i)

for i in arraySymLang:
    feature_col.append(i)


# data = df.word
# arrayC = []
# array_THB = ['t', 'h', 'b']

# for i in data:
#     counting = 0
#     i = str(i)
#     for j in i:
#         print(j)


def counting_word(data, arrayThaLang, arrayEngLang, arrayNumLang, arraySymLang):

    countingWord =[]
    data = data.word

    for word in data:
        word = str(word)  
        T0=0
        T1=0
        T2=0
        T3=0
        T4=0
        T5=0
        T6=0
        T7=0
        T8=0
        T9=0
        T10=0
        T11=0
        T12=0
        T13=0
        T14=0
        T15=0
        T16=0
        T17=0
        T18=0
        T19=0
        T20=0
        T21=0
        T22=0
        T23=0
        T24=0
        T25=0
        T26=0
        T27=0
        T28=0
        T29=0
        T30=0
        T31=0
        T32=0
        T33=0
        T34=0
        T35=0
        T36=0
        T37=0
        T38=0
        T39=0
        T40=0
        T41=0
        T42=0
        T43=0

        E0=0
        E1=0
        E2=0
        E3=0
        E4=0
        E5=0
        E6=0
        E7=0
        E8=0
        E9=0
        E10=0
        E11=0
        E12=0
        E13=0
        E14=0
        E15=0
        E16=0
        E17=0
        E18=0
        E19=0
        E20=0
        E21=0
        E22=0
        E23=0
        E24=0
        E25=0

        N0=0
        N1=0
        N2=0
        N3=0
        N4=0
        N5=0
        N6=0
        N7=0
        N8=0
        N9=0

        S0=0
        S1=0
        S2=0
        S3=0
        S4=0
        S5=0
        S6=0
        S7=0
        S8=0
        S9=0
        S10=0
        S11=0
        S12=0
        S13=0
        S14=0
        S15=0
        S16=0
        S17=0
        S18=0
        S19=0
        S20=0
        S21=0
        S22=0
        S23=0
        S24=0
        S25=0
        S26=0
        S27=0

        for elemnt2 in word:
            ### counting Tha element 
            if elemnt2 == arrayThaLang[0]:
                T0 += 1
            elif elemnt2 == arrayThaLang[1]:
                T1 += 1
            elif elemnt2 == arrayThaLang[2]:
                T2 += 1
            elif elemnt2 == arrayThaLang[3]:
                T3 += 1
            elif elemnt2 == arrayThaLang[4]:
                T4 += 1
            elif elemnt2 == arrayThaLang[5]:
                T5 += 1
            elif elemnt2 == arrayThaLang[6]:
                T6 += 1
            elif elemnt2 == arrayThaLang[7]:
                T7 += 1
            elif elemnt2 == arrayThaLang[8]:
                T8 += 1
            elif elemnt2 == arrayThaLang[9]:
                T9 += 1
            elif elemnt2 == arrayThaLang[10]:
                T10 += 1
            elif elemnt2 == arrayThaLang[11]:
                T11 += 1
            elif elemnt2 == arrayThaLang[12]:
                T12 += 1
            elif elemnt2 == arrayThaLang[13]:
                T13 += 1
            elif elemnt2 == arrayThaLang[14]:
                T14 += 1
            elif elemnt2 == arrayThaLang[15]:
                T15 += 1
            elif elemnt2 == arrayThaLang[16]:
                T16 += 1
            elif elemnt2 == arrayThaLang[17]:
                T17 += 1
            elif elemnt2 == arrayThaLang[18]:
                T18 += 1
            elif elemnt2 == arrayThaLang[19]:
                T19 += 1
            elif elemnt2 == arrayThaLang[20]:
                T20 += 1
            elif elemnt2 == arrayThaLang[21]:
                T21 += 1
            elif elemnt2 == arrayThaLang[22]:
                T22 += 1
            elif elemnt2 == arrayThaLang[23]:
                T23 += 1
            elif elemnt2 == arrayThaLang[24]:
                T24 += 1
            elif elemnt2 == arrayThaLang[25]:
                T25 += 1
            elif elemnt2 == arrayThaLang[26]:
                T26 += 1
            elif elemnt2 == arrayThaLang[27]:
                T27 += 1
            elif elemnt2 == arrayThaLang[28]:
                T28 += 1
            elif elemnt2 == arrayThaLang[29]:
                T29 += 1
            elif elemnt2 == arrayThaLang[30]:
                T30 += 1
            elif elemnt2 == arrayThaLang[31]:
                T31 += 1
            elif elemnt2 == arrayThaLang[32]:
                T32 += 1
            elif elemnt2 == arrayThaLang[33]:
                T33 += 1
            elif elemnt2 == arrayThaLang[34]:
                T34 += 1
            elif elemnt2 == arrayThaLang[35]:
                T35 += 1
            elif elemnt2 == arrayThaLang[36]:
                T36 += 1
            elif elemnt2 == arrayThaLang[37]:
                T37 += 1
            elif elemnt2 == arrayThaLang[38]:
                T38 += 1
            elif elemnt2 == arrayThaLang[39]:
                T39 += 1
            elif elemnt2 == arrayThaLang[40]:
                T40 += 1
            elif elemnt2 == arrayThaLang[41]:
                T41 += 1
            elif elemnt2 == arrayThaLang[42]:
                T42 += 1
            elif elemnt2 == arrayThaLang[43]:
                T43 += 1
            
            #### counting element Eng
            elif elemnt2 == arrayEngLang[0]:
                E0 += 1
            elif elemnt2 == arrayEngLang[1]:
                E1 += 1
            elif elemnt2 == arrayEngLang[2]:
                E2 += 1
            elif elemnt2 == arrayEngLang[3]:
                E3 += 1
            elif elemnt2 == arrayEngLang[4]:
                E4 += 1
            elif elemnt2 == arrayEngLang[5]:
                E5 += 1
            elif elemnt2 == arrayEngLang[6]:
                E6 += 1
            elif elemnt2 == arrayEngLang[7]:
                E7 += 1
            elif elemnt2 == arrayEngLang[8]:
                E8 += 1
            elif elemnt2 == arrayEngLang[9]:
                E9 += 1
            elif elemnt2 == arrayEngLang[10]:
                E10 += 1
            elif elemnt2 == arrayEngLang[11]:
                E11 += 1
            elif elemnt2 == arrayEngLang[12]:
                E12 += 1
            elif elemnt2 == arrayEngLang[13]:
                E13 += 1
            elif elemnt2 == arrayEngLang[14]:
                E14 += 1
            elif elemnt2 == arrayEngLang[15]:
                E15 += 1
            elif elemnt2 == arrayEngLang[16]:
                E16 += 1
            elif elemnt2 == arrayEngLang[17]:
                E17 += 1
            elif elemnt2 == arrayEngLang[18]:
                E18 += 1
            elif elemnt2 == arrayEngLang[19]:
                T19 += 1
            elif elemnt2 == arrayEngLang[20]:
                E20 += 1
            elif elemnt2 == arrayEngLang[21]:
                E21 += 1
            elif elemnt2 == arrayEngLang[22]:
                E22 += 1
            elif elemnt2 == arrayEngLang[23]:
                E23 += 1
            elif elemnt2 == arrayEngLang[24]:
                E24 += 1
            elif elemnt2 == arrayEngLang[25]:
                E25 += 1

            ### COUNT NUM ELEMENT 
            elif elemnt2 == arrayNumLang[0]:
                N0 += 1
            elif elemnt2 == arrayNumLang[1]:
                N1 += 1
            elif elemnt2 == arrayNumLang[2]:
                N2 += 1
            elif elemnt2 == arrayNumLang[3]:
                N3 += 1
            elif elemnt2 == arrayNumLang[4]:
                N4 += 1
            elif elemnt2 == arrayNumLang[5]:
                N5 += 1
            elif elemnt2 == arrayNumLang[6]:
                N6 += 1
            elif elemnt2 == arrayNumLang[7]:
                N7 += 1
            elif elemnt2 == arrayNumLang[8]:
                N8 += 1
            elif elemnt2 == arrayNumLang[9]:
                N9 += 1
            ### Counting Symbol

            if elemnt2 == arraySymLang[0]:
                S0 += 1
            elif elemnt2 == arraySymLang[1]:
                S1 += 1
            elif elemnt2 == arraySymLang[2]:
                S2 += 1
            elif elemnt2 == arraySymLang[3]:
                S3 += 1
            elif elemnt2 == arraySymLang[4]:
                S4 += 1
            elif elemnt2 == arraySymLang[5]:
                S5 += 1
            elif elemnt2 == arraySymLang[6]:
                S6 += 1
            elif elemnt2 == arraySymLang[7]:
                S7 += 1
            elif elemnt2 == arraySymLang[8]:
                S8 += 1
            elif elemnt2 == arraySymLang[9]:
                S9 += 1
            elif elemnt2 == arraySymLang[10]:
                S10 += 1
            elif elemnt2 == arraySymLang[11]:
                S11 += 1
            elif elemnt2 == arraySymLang[12]:
                S12 += 1
            elif elemnt2 == arraySymLang[13]:
                S13 += 1
            elif elemnt2 == arraySymLang[14]:
                S14 += 1
            elif elemnt2 == arraySymLang[15]:
                S15 += 1
            elif elemnt2 == arraySymLang[16]:
                S16 += 1
            elif elemnt2 == arraySymLang[17]:
                S17 += 1
            elif elemnt2 == arraySymLang[18]:
                S18 += 1
            elif elemnt2 == arraySymLang[19]:
                S19 += 1
            elif elemnt2 == arraySymLang[20]:
                S20 += 1
            elif elemnt2 == arraySymLang[21]:
                S21 += 1
            elif elemnt2 == arraySymLang[22]:
                S22 += 1
            elif elemnt2 == arraySymLang[23]:
                S23 += 1
            elif elemnt2 == arraySymLang[24]:
                S24 += 1
            elif elemnt2 == arraySymLang[25]:
                S25 += 1
            elif elemnt2 == arraySymLang[26]:
                S26 += 1
            elif elemnt2 == arraySymLang[27]:
                S27 += 1

        countingWord.append([T0, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10,
        T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21,
        T22, T23, T24, T25, T26, T27, T28, T29, T30, T31, T32,
        T33, T34, T35, T36, T37, T38, T39, T40, T41, T42, T43,
        E0, E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11, E12, 
        E13, E14, E15, E16, E17, E18, E19, E20, E21, E22, E23, E24, E25,
        N0, N1, N2, N3, N4, N5, N6, N7, N8, N9,
        S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10,
        S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21,
        S22, S23, S24, S25, S26, S27])
    
    return countingWord
 


testing = counting_word(df, arrayThaLang, arrayEngLang, arrayNumLang, arraySymLang)
df_count = pd.DataFrame(data= testing, columns=feature_col)
dataframe = pd.concat([df, df_count], axis=1)
# print(dataframe)

dataframe.to_csv('data_more_count.csv')