import requests
import json
import csv

url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare'
response = requests.get(url)
result=json.loads(response.text)

# 中国每日新增
result1=result['data']['chinaDayAddList']
with open('spider_do_daily_add.csv',"w",encoding="gbk",newline="") as f6:
    csv_writer=csv.writer(f6)
    csv_writer.writerow(['统计时间','输入病例','大陆新增确诊人数','全国新增确诊人数','死亡人数','死亡率','治愈人数','治愈率'])
    for each in result1:
        csv_writer.writerow([each['date'],each['importedCase'],each['localConfirmadd'],each['confirm'],each['dead'],each['deadRate'],each['heal'],each['healRate']])
    f6.close()