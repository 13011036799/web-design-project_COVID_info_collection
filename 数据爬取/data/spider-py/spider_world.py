import requests
import json
import csv

url = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryConfirmAdd,WomWorld,WomAboard'
response = requests.get(url)
result=json.loads(response.text)

# 全世界情况
result1=result['data']['WomWorld']
with open('do_world.csv',"w",encoding="gbk",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(['时间','当前确诊人数','新增确诊人数','累计确诊人数','累计新增确诊人数','新增死亡人数','累计死亡人数','死亡率','新增治愈人数','累计治愈人数','治愈率'])
    csv_writer.writerow([result1['date'],result1['nowConfirm'],result1['nowConfirmAdd'],result1['confirm'],result1['confirmAdd'],result1['deadAdd'],result1['dead'],result1['deathrate'],result1['healAdd'],result1['heal'],result1['curerate']])
    f.close()