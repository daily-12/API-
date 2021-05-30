# 의약품 제품 허가 서비스
# 의약품 제품 허가 목록조회

from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
#from pandas_datareader import data
from datetime import datetime
import requests, xmltodict, json
import pandas as pd 
import numpy as np 
import time



start = time.time()

key = 'mFY7S%2BvZr%2BV5qfNSnOV43jwWv6jLN9C4CG8YWB4eRd4vQ08JBb7d3UbLFNnrlPzeEjZP3UOjbTe2VszpDW92nw%3D%3D'
url = 'http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService1/getMdcinPrductList?ServiceKey={}'.format(key)

content = requests.get(url).content 
dict = xmltodict.parse(content)


jsoncontent = json.dumps(dict['response']['body']['items']['item'])
jsoncontent = json.loads(jsoncontent)
#pageNo = json.dumps(dict['response']['body']['pageNo'])   #['totalCount'])
#pageNo = pageNo.replace('\"','') # "1"
#totalCount = json.loads(totalCount)
#print(totalCount)  # 1
totalCount = json.dumps(dict['response']['body']['totalCount'])
totalCount = totalCount.replace('\"','') # "1"


#print(type(jsoncontent))
#print(jsoncontent[0]['ITEM_SEQ'])

ITEM_SEQ= [] 
ITEM_NAME= [] 
ENTP_NAME= [] 
ITEM_PERMIT_DATE= [] 
INDUTY = [] 
PRDLST_STDR_CODE = [] 
SPCLTY_PBLC= [] 
PRDUCT_TYPE= [] 
PRDUCT_PRMISN_NO = []
ITEM_INGR_NAME = []
ITEM_INGR_CNT = []
PERMIT_KIND_CODE = []
CANCEL_DATE = []
CANCEL_NAME = []


def download(url, file_name = None, dir=None):
    if url == None : 
        url = None
    else : 
        if not file_name: # file_name을 특별히 지정하지 않을 때 실행됨
            file_name = url.split('/')[-1] # ex) 문자열을 '/'로 분리하여 각 단어 중 가장 마지막에 있는 문자열을 추출함
        with open(dir + file_name + '.jpg', 'wb') as file: # 파일을 dir + file_name + '.jpg' 형태로 저장하고자 함.
            response = requests.get(url)
            file.write(response.content) # 파일을 쓰기모드로 읽기 위함


for i in range(int(totalCount)//10): # totalCount가 총 항목 개수인데, 10개씩(Default) 화면에 뿌려주고 있어서 10으로 나눔
    url = 'http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService1/getMdcinPrductList?ServiceKey={}&pageNo={}'.format(key, i + 1)

    content = requests.get(url).content 
    dict = xmltodict.parse(content)

    jsoncontent = json.dumps(dict['response']['body']['items']['item'])
    jsoncontent = json.loads(jsoncontent)
    if i % 100 == 0 : 
        print(i)

    for i, value in enumerate(jsoncontent):
        """
        print(jsoncontent[i]['ITEM_SEQ'])
        print(jsoncontent[i]['ITEM_NAME'])
        print(jsoncontent[i]['ENTP_SEQ'])
        print(jsoncontent[i]['ENTP_NAME'])
        print(jsoncontent[i]['CHART'])
        print(jsoncontent[i]['ITEM_IMAGE'])
        print(jsoncontent[i]['PRINT_FRONT'])
        print(jsoncontent[i]['PRINT_BACK'])
        print(jsoncontent[i]['DRUG_SHAPE'])
        print(jsoncontent[i]['COLOR_CLASS1'])
        print(jsoncontent[i]['COLOR_CLASS2'])
        print(jsoncontent[i]['LINE_FRONT'])
        print(jsoncontent[i]['LINE_BACK'])
        print(jsoncontent[i]['LENG_LONG'])
        print(jsoncontent[i]['LENG_SHORT'])
        print(jsoncontent[i]['THICK'])
        print(jsoncontent[i]['IMG_REGIST_TS'])
        print(jsoncontent[i]['CLASS_NO'])
        print(jsoncontent[i]['CLASS_NAME'])
        print(jsoncontent[i]['ETC_OTC_NAME'])
        print(jsoncontent[i]['ITEM_PERMIT_DATE'])
        print(jsoncontent[i]['FORM_CODE_NAME'])
        print(jsoncontent[i]['MARK_CODE_FRONT_ANAL'])
        print(jsoncontent[i]['MARK_CODE_BACK_ANAL'])
        print(jsoncontent[i]['MARK_CODE_FRONT_IMG'])
        print(jsoncontent[i]['MARK_CODE_BACK_IMG'])
        print(jsoncontent[i]['ITEM_ENG_NAME'])
        print(jsoncontent[i]['CHANGE_DATE'])
        print(jsoncontent[i]['MARK_CODE_FRONT'])
        print(jsoncontent[i]['MARK_CODE_BACK'])
        print(jsoncontent[i]['EDI_CODE'])
        """

        ITEM_SEQ.append(jsoncontent[i]['ITEM_SEQ'])
        ITEM_NAME.append(jsoncontent[i]['ITEM_NAME'])
        ENTP_NAME.append(jsoncontent[i]['ENTP_NAME'])
        ITEM_PERMIT_DATE.append(jsoncontent[i]['ITEM_PERMIT_DATE'])
        INDUTY.append(jsoncontent[i]['INDUTY'])
        PRDLST_STDR_CODE.append(jsoncontent[i]['PRDLST_STDR_CODE'])
        SPCLTY_PBLC.append(jsoncontent[i]['SPCLTY_PBLC'])
        PRDUCT_TYPE.append(jsoncontent[i]['PRDUCT_TYPE'])
        PRDUCT_PRMISN_NO.append(jsoncontent[i]['PRDUCT_PRMISN_NO'])
        ITEM_INGR_NAME.append(jsoncontent[i]['ITEM_INGR_NAME'])
        ITEM_INGR_CNT.append(jsoncontent[i]['ITEM_INGR_CNT'])
        PERMIT_KIND_CODE.append(jsoncontent[i]['PERMIT_KIND_CODE'])
        CANCEL_DATE.append(jsoncontent[i]['CANCEL_DATE'])
        CANCEL_NAME.append(jsoncontent[i]['CANCEL_NAME'])

        data = [ITEM_SEQ, ITEM_NAME,  ENTP_NAME, ITEM_PERMIT_DATE, INDUTY, PRDLST_STDR_CODE, SPCLTY_PBLC, PRDUCT_TYPE, PRDUCT_PRMISN_NO, ITEM_INGR_NAME, ITEM_INGR_CNT, PERMIT_KIND_CODE, CANCEL_DATE, CANCEL_NAME]
        data = np.transpose(data)

        df = pd.DataFrame(data, columns = ['ITEM_SEQ', 'ITEM_NAME', 'ENTP_NAME', 'ITEM_PERMIT_DATE', 'INDUTY', 'PRDLST_STDR_CODE', 'SPCLTY_PBLC', 'PRDUCT_TYPE', 'PRDUCT_PRMISN_NO', 'ITEM_INGR_NAME', 'ITEM_INGR_CNT', 'PERMIT_KIND_CODE', 'CANCEL_DATE', 'CANCEL_NAME'])
    
#df = pd.DataFrame(ITEM_SEQ , ITEM_NAME , ENTP_SEQ , ENTP_NAME , CHART , ITEM_IMAGE , PRINT_FRONT , PRINT_BACK , DRUG_SHAPE , COLOR_CLASS1 , COLOR_CLASS2 , LINE_FRONT , LINE_BACK , LENG_LONG , LENG_SHORT , THICK , IMG_REGIST_TS , CLASS_NO , CLASS_NAME , ETC_OTC_NAME , ITEM_PERMIT_DATE , FORM_CODE_NAME , MARK_CODE_FRONT_ANAL , MARK_CODE_BACK_ANAL , MARK_CODE_FRONT_IMG , MARK_CODE_BACK_IMG , ITEM_ENG_NAME , CHANGE_DATE , MARK_CODE_FRONT , MARK_CODE_BACK , EDI_CODE)
#print(df)
df.to_csv("D:\programing\python\\2021_python\project\drug_product.csv", mode='w')

end = time.time() - start
print('save end {}m{}s'.format(end//60, end%60))
#for item_seq, name in  jsoncontent:

