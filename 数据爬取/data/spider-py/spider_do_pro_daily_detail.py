import requests
import json
import csv

url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
response = requests.get(url)
result=json.loads(response.text)

# 中国地区各省市当天情况
result4=result['data']['statisGradeCityDetail']
with open('do_pro_daily_detail.csv',"w",encoding="gbk",newline="") as f5:
    csv_writer=csv.writer(f5)
    csv_writer.writerow(['统计时间','省份','城市','现有确诊人数','累计确诊人数','累计死亡人数','累计治愈人数'])
    for each in result4:
        csv_writer.writerow([each['date'],each['province'],each['city'],each['nowConfirm'],each['confirm'],each['dead'],each['heal']])
    f5.close()