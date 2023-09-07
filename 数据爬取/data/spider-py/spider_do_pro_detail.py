import requests
import json
import csv

url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
response = requests.get(url)
result=json.loads(response.text)

# 中国省情况
result3 = result['data']['diseaseh5Shelf']['areaTree'][0]['children']
# 省内地区情况
with open('do_province_detail.csv',"w",encoding="gbk",newline="") as f4:
    csv_writer=csv.writer(f4)
    csv_writer.writerow(['统计时间','地区','省内地区','现有确诊人数','累计确诊人数','累计死亡人数','累计治愈人数'])
    for each in result3:
        for i in each['children']:
            csv_writer.writerow([i['date'],each['name'],i['name'],i['total']['nowConfirm'],i['total']['confirm'],i['total']['dead'],i['total']['heal']])
    f4.close()