from PIL import Image 
import pandas as pd 


file1 = 'D:\programing\python\\2021_python\project\\drug_all.csv'

output = pd.read_csv(file1, low_memory = False)

value =  eval(input())
print(type(value))
for i, item_seq in enumerate(output['ITEM_SEQ']):
    if value == item_seq : 
        print('i = {}, item_seq = {}'.format(i, item_seq))
        item_image = output['ITEM_IMAGE'].loc[i]
        print(item_image)
        image_name = item_image.split('/')[-1] + '.jpg'
        image = Image.open('F:\data\drug_image\item_image\\' + image_name)
        image.show()


        
