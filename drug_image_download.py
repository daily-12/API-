# 의약품 낱알식별 정보(DB) 서비스

from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
#from pandas_datareader import data
from datetime import datetime
import requests, xmltodict, json
import pandas as pd 
import numpy as np 


key = 'mFY7S%2BvZr%2BV5qfNSnOV43jwWv6jLN9C4CG8YWB4eRd4vQ08JBb7d3UbLFNnrlPzeEjZP3UOjbTe2VszpDW92nw%3D%3D'
url = 'http://apis.data.go.kr/1470000/MdcinGrnIdntfcInfoService/getMdcinGrnIdntfcInfoList?ServiceKey={}&pageNo=3'.format(key)

content = requests.get(url).content 
dict = xmltodict.parse(content)


jsoncontent = json.dumps(dict['response']['body']['items']['item'])
jsoncontent = json.loads(jsoncontent)
print(jsoncontent[0]['ITEM_IMAGE'])

dir = 'D:\data\opendata_api\drug_image\\'
def download(url, file_name = None):
    if url == None : 
        url = None
    else : 
        if not file_name: # file_name을 특별히 지정하지 않을 때 실행됨
            file_name = url.split('/')[-1] # ex) 문자열을 '/'로 분리하여 각 단어 중 가장 마지막에 있는 문자열을 추출함
        with open(dir + file_name + '.jpg', 'wb') as file: # 파일을 dir + file_name + '.jpg' 형태로 저장하고자 함.
            response = requests.get(url)
            file.write(response.content) # 파일을 쓰기모드로 읽기 위함

'''
if __name__ == '__main__':
    item_image = jsoncontent[0]['ITEM_IMAGE']
    download(url = item_image, file_name = dir + item_image.split('/')[-1] + '.jpg')
'''


if __name__ == '__main__':
    item_image = jsoncontent[6]['MARK_CODE_FRONT_IMG']
    print(item_image)
    download(url = item_image)

'''
if __name__ == '__main__':
    item_image = jsoncontent[0]['MARK_CODE_BACK_IMG']
    print(item_image)
    download(url = item_image)
'''