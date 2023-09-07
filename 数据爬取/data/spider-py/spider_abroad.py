import requests
import json
import csv

url = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryConfirmAdd,WomWorld,WomAboard'
response = requests.get(url)
result=json.loads(response.text)

# 国外各地区
result1=result['data']['WomAboard']
with open('spider_ab.csv',"w",encoding="gbk",newline="") as f7:
    csv_writer=csv.writer(f7)
    csv_writer.writerow(['统计时间','大陆','国家','新增确诊人数','当前确诊人数','累计确诊人数','死亡人数','治愈人数'])
    for each in result1:
        csv_writer.writerow([each['date'],each['continent'],each['name'],each['confirmAdd'],each['nowConfirm'],each['confirm'],each['dead'],each['heal']])
    f7.close()