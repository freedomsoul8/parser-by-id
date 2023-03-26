import random

import pandas as pd
import requests
from excel import *
from config import *

# Create Url for product by vendor code
def url_wb(value):
    url_wildberries = f'https://card.wb.ru/cards/detail?spp=0&regions=80,64,58,83,4,38,33,70,82,69,86,30,40,48,1,22,66,31&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=2,12,7,3,6,13,21&dest=-1113276,-79379,-1104258,-5803327&nm={value}'
    return str(url_wildberries)

def parse(srcfilename,filename,columnname):
    prices = list()
    items = list()
    # Parsing items from file
    try:
        for item in get_column(filename=srcfilename,column_name=columnname):

            response = requests.get(url=url_wb(value=item)).json()
            stock = response["data"]["products"][0]["sizes"][0]["stocks"]

            # Check if product in stock
            if stock == []:
                price = '0'
            else:
                if len(str(response["data"]["products"][0]["salePriceU"])) == 4:
                    price = str(response["data"]["products"][0]["salePriceU"])
                else:
                    price = str(response["data"]["products"][0]["salePriceU"]).replace('00','')

            # Save data in lists
            prices.append(price)
            items.append(item)

            # Create new dataframe with parsed data
            parsed_df = pd.DataFrame({"code":items,"prices":prices})

            # Create excel file with saved data
            writer = pd.ExcelWriter(filename, engine='xlsxwriter')
            parsed_df.to_excel(writer,sheet_name="wb",index=False)
            writer.close()
    except Exception as e:
        print(e)






