import requests
import json
import csv

url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
response = requests.get(url)
result=json.loads(response.text)

# 中国省情况
# 总情况
result3 = result['data']['diseaseh5Shelf']['areaTree'][0]['children']
with open('do_province.csv',"w",encoding="gbk",newline="") as f3:
    csv_writer=csv.writer(f3)
    csv_writer.writerow(['统计时间','地区','现有确诊人数','累计确诊人数','累计死亡人数','累计治愈人数'])
    for each in result3:
        # print(each['date'],each['name'],each['total']['nowConfirm'],each['total']['confirm'],each['total']['dead'],each['total']['heal'])
        csv_writer.writerow([each['date'],each['name'],each['total']['nowConfirm'],each['total']['confirm'],each['total']['dead'],each['total']['heal']])
    f3.close()

