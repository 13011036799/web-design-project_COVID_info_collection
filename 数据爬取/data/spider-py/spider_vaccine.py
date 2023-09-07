import requests
import json
import csv

url = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=VaccineTopData'
response = requests.get(url)
result=json.loads(response.text)

# 国内疫苗数据
result1=result['data']['VaccineTopData']['中国']
with open('do_vac.csv',"w",encoding="gbk",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(['中国累计疫苗接种数(剂)','中国较上日新增疫苗接种数(剂)','中国每百人接种数(剂)'])
    csv_writer.writerow([result1['total_vaccinations'],result1['new_vaccinations'],result1['total_vaccinations_per_hundred']])
    f.close()

# 国外疫苗数据
result2=result['data']['VaccineTopData']['全球']
with open('world_vac.csv',"w",encoding="gbk",newline="") as f2:
    csv_writer=csv.writer(f2)
    csv_writer.writerow(['全球累计疫苗接种数(剂)','全球较上日新增疫苗接种数(剂)','全球每百人接种数(剂)'])
    csv_writer.writerow([result2['total_vaccinations'],result2['new_vaccinations'],result2['total_vaccinations_per_hundred']])
    f2.close()