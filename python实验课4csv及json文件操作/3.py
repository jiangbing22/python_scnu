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
        json_string = matches.group(1)
        df=pd.read_json(json_string)
        print(df["workoutDetailData"])
    else:
        print(f'Variable {variable_name} not found in the JavaScript code.')

    df.to_csv("test3.csv")