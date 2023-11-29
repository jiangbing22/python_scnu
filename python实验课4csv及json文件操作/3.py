from bs4 import  BeautifulSoup
import re
import json
import csv
import pandas as pd
with open("Dylan_van_Baarle.html") as html:
    soup=BeautifulSoup(html,'html.parser')
    # 使用诸如find()和find_all()等方法访问元素
    script_tag = soup.find_all('script',{'type':'text/javascript'})
    code=script_tag[2].string
    variable_name = 'publicActivityWrapper'
    pattern = re.compile(rf'\b{variable_name}\s*=\s*({{.*?}});', re.DOTALL)
    matches = pattern.search(code)

    if matches:
        # 获取匹配到的 JSON 字符串
        json_string = matches.group(1)

        # 将 JSON 字符串解析为 Python 字典
        df=pd.read_json(json_string)
        print(f'The value of {variable_name} is:')
        print(df)
    else:
        print(f'Variable {variable_name} not found in the JavaScript code.')
    df.to_csv("test3.csv")

# 将数据写入CSV文件
