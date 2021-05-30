# 의약품 제품 허가 서비스 
# 의약품 제품 허가 상세정보조회

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

key = '본인 key입력'
url = 'http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService1/getMdcinPrductItem?ServiceKey={}'.format(key)

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

ITEM_SEQ = []
ITEM_NAME = []
ENTP_NAME = []
ITEM_PERMIT_DATE = []
CNSGN_MANUF = []
ETC_OTC_CODE = []
CLASS_NO = []
CHART = []
BAR_CODE = []
MATERIAL_NAME = []
EE_DOC_ID = []
UD_DOC_ID = []
NB_DOC_ID = []
INSERT_FILE = []
STORAGE_METHOD = []
VALID_TERM = []
REEXAM_TARGET = []
REEXAM_DATE = []
PACK_UNIT = []
EDI_CODE = []
DOC_TEXT = []
PERMIT_KIND_NAME = []
ENTP_NO = []
MAKE_MATERIAL_FLAG = []
NEWDRUG_CLASS_NAME = []
INDUTY_TYPE = []
CANCEL_DATE = []
CANCEL_NAME = []
CHANGE_DATE = []
NARCOTIC_KIND_CODE = []
GBN_NAME = []
EE_DOC_DATA = []
UD_DOC_DATA = []
NB_DOC_DATA = []
PN_DOC_DATA = []
MAIN_ITEM_INGR = []
INGR_NAME = []



for i in range(int(totalCount)//10): # totalCount가 총 항목 개수인데, 10개씩(Default) 화면에 뿌려주고 있어서 10으로 나눔
    url = 'http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService1/getMdcinPrductItem?ServiceKey={}&pageNo={}'.format(key, i + 1)

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
        CNSGN_MANUF.append(jsoncontent[i]['CNSGN_MANUF'])
        ETC_OTC_CODE.append(jsoncontent[i]['ETC_OTC_CODE'])
        CLASS_NO.append(jsoncontent[i]['CLASS_NO'])
        CHART.append(jsoncontent[i]['CHART'])
        BAR_CODE.append(jsoncontent[i]['BAR_CODE'])
        MATERIAL_NAME.append(jsoncontent[i]['MATERIAL_NAME'])
        EE_DOC_ID.append(jsoncontent[i]['EE_DOC_ID'])
        UD_DOC_ID.append(jsoncontent[i]['UD_DOC_ID'])
        NB_DOC_ID.append(jsoncontent[i]['NB_DOC_ID'])
        INSERT_FILE.append(jsoncontent[i]['INSERT_FILE'])
        STORAGE_METHOD.append(jsoncontent[i]['STORAGE_METHOD'])
        VALID_TERM.append(jsoncontent[i]['VALID_TERM'])
        REEXAM_TARGET.append(jsoncontent[i]['REEXAM_TARGET'])
        REEXAM_DATE.append(jsoncontent[i]['REEXAM_DATE'])
        PACK_UNIT.append(jsoncontent[i]['PACK_UNIT'])
        EDI_CODE.append(jsoncontent[i]['EDI_CODE'])
        DOC_TEXT.append(jsoncontent[i]['DOC_TEXT'])
        PERMIT_KIND_NAME.append(jsoncontent[i]['PERMIT_KIND_NAME'])
        ENTP_NO.append(jsoncontent[i]['ENTP_NO'])
        MAKE_MATERIAL_FLAG.append(jsoncontent[i]['MAKE_MATERIAL_FLAG'])
        NEWDRUG_CLASS_NAME.append(jsoncontent[i]['NEWDRUG_CLASS_NAME'])
        INDUTY_TYPE.append(jsoncontent[i]['INDUTY_TYPE'])
        CANCEL_DATE.append(jsoncontent[i]['CANCEL_DATE'])
        CANCEL_NAME.append(jsoncontent[i]['CANCEL_NAME'])
        CHANGE_DATE.append(jsoncontent[i]['CHANGE_DATE'])
        NARCOTIC_KIND_CODE.append(jsoncontent[i]['NARCOTIC_KIND_CODE'])
        GBN_NAME.append(jsoncontent[i]['GBN_NAME'])
        EE_DOC_DATA.append(jsoncontent[i]['EE_DOC_DATA'])
        UD_DOC_DATA.append(jsoncontent[i]['UD_DOC_DATA'])
        NB_DOC_DATA.append(jsoncontent[i]['NB_DOC_DATA'])
        PN_DOC_DATA.append(jsoncontent[i]['PN_DOC_DATA'])
        MAIN_ITEM_INGR.append(jsoncontent[i]['MAIN_ITEM_INGR'])
        INGR_NAME.append(jsoncontent[i]['INGR_NAME'])

        data = [ITEM_SEQ, ITEM_NAME, ENTP_NAME, ITEM_PERMIT_DATE, CNSGN_MANUF, ETC_OTC_CODE, CLASS_NO, CHART, BAR_CODE, MATERIAL_NAME, EE_DOC_ID, UD_DOC_ID, NB_DOC_ID, INSERT_FILE, STORAGE_METHOD, VALID_TERM, REEXAM_TARGET, REEXAM_DATE, PACK_UNIT, EDI_CODE, DOC_TEXT, PERMIT_KIND_NAME, ENTP_NO, MAKE_MATERIAL_FLAG, NEWDRUG_CLASS_NAME, INDUTY_TYPE, CANCEL_DATE, CANCEL_NAME, CHANGE_DATE, NARCOTIC_KIND_CODE, GBN_NAME, EE_DOC_DATA, UD_DOC_DATA, NB_DOC_DATA, PN_DOC_DATA, MAIN_ITEM_INGR, INGR_NAME]
        data = np.transpose(data)

        df = pd.DataFrame(data, columns = ['ITEM_SEQ', 'ITEM_NAME', 'ENTP_NAME', 'ITEM_PERMIT_DATE', 'CNSGN_MANUF', 'ETC_OTC_CODE', 'CLASS_NO', 'CHART', 'BAR_CODE', 'MATERIAL_NAME', 'EE_DOC_ID', 'UD_DOC_ID', 'NB_DOC_ID', 'INSERT_FILE', 'STORAGE_METHOD', 'VALID_TERM', 'REEXAM_TARGET', 'REEXAM_DATE', 'PACK_UNIT', 'EDI_CODE', 'DOC_TEXT', 'PERMIT_KIND_NAME', 'ENTP_NO', 'MAKE_MATERIAL_FLAG', 'NEWDRUG_CLASS_NAME', 'INDUTY_TYPE', 'CANCEL_DATE', 'CANCEL_NAME', 'CHANGE_DATE', 'NARCOTIC_KIND_CODE', 'GBN_NAME', 'EE_DOC_DATA', 'UD_DOC_DATA', 'NB_DOC_DATA', 'PN_DOC_DATA', 'MAIN_ITEM_INGR', 'INGR_NAME'])
    
#df = pd.DataFrame(ITEM_SEQ , ITEM_NAME , ENTP_SEQ , ENTP_NAME , CHART , ITEM_IMAGE , PRINT_FRONT , PRINT_BACK , DRUG_SHAPE , COLOR_CLASS1 , COLOR_CLASS2 , LINE_FRONT , LINE_BACK , LENG_LONG , LENG_SHORT , THICK , IMG_REGIST_TS , CLASS_NO , CLASS_NAME , ETC_OTC_NAME , ITEM_PERMIT_DATE , FORM_CODE_NAME , MARK_CODE_FRONT_ANAL , MARK_CODE_BACK_ANAL , MARK_CODE_FRONT_IMG , MARK_CODE_BACK_IMG , ITEM_ENG_NAME , CHANGE_DATE , MARK_CODE_FRONT , MARK_CODE_BACK , EDI_CODE)
#print(df)
df.to_csv("D:\programing\python\\2021_python\project\drug_detail.csv", mode='w')

end = time.time() - start
print('save end {}m{}s'.format(end//60, end%60))
#for item_seq, name in  jsoncontent:

