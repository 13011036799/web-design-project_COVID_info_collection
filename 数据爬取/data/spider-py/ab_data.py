import csv

# with open('../data-csv/4.do_province.csv') as f:
with open('../data-csv/8.ab.csv') as f:
    f=csv.DictReader(f)
    for row in f:
        # print("{"+"地区:'"+row["地区"]+"',"+"现有确诊人数:"+row["现有确诊人数"]+",累计确诊人数:"+row["累计确诊人数"]+",累计死亡人数:"+row["累计死亡人数"]+",累计治愈人数:"+row["累计治愈人数"]+"}"+"")

        # print("{" + "省内地区:'" + row["省内地区"] + "'," + "现有确诊人数:" + row["现有确诊人数"] + ",累计确诊人数:" + row["累计确诊人数"] + ",累计死亡人数:" + row[
        #         "累计死亡人数"] + ",累计治愈人数:" + row["累计治愈人数"] + "}" + "")
        a=0
        if row['大陆']=='北美洲':
            a+=int(row['累计确诊人数'])
        print(a)
