import requests
import json
import csv

url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
response = requests.get(url)
result=json.loads(response.text)

# 中国总数据domestic data
result1=result['data']['diseaseh5Shelf']['chinaTotal']
with open('do_all.csv',"w",encoding="gbk",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(['无症状感染者人数','境外输入人数','大陆现有确诊人数','全国现有确诊人数','全国累计确诊人数','全国累计死亡人数','全国累计治愈人数'])
    csv_writer.writerow([result1['noInfect'],result1['importedCase'],result1['localConfirm'],result1['nowConfirm'],result1['confirm'],result1['dead'],result1['heal']])
    f.close()

# 中国5.6新增
result2=result['data']['diseaseh5Shelf']['chinaAdd']
with open('do_day.csv',"w",encoding="gbk",newline="") as f2:
    csv_writer=csv.writer(f2)
    csv_writer.writerow(['无症状感染者人数','境外输入人数','大陆现有确诊人数','全国现有确诊人数','全国累计确诊人数','全国累计死亡人数','全国累计治愈人数'])
    csv_writer.writerow([result2['noInfect'],result2['importedCase'],result2['localConfirm'],result2['nowConfirm'],result2['confirm'],result2['dead'],result2['heal']])
    f2.close()
