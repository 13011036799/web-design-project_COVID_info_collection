import csv

# with open('../data-csv/4.do_province.csv') as f:
with open('../data-csv/5.do_province_detail.csv') as f:
    f=csv.DictReader(f)
    for row in f:
        # print("{"+"地区:'"+row["地区"]+"',"+"现有确诊人数:"+row["现有确诊人数"]+",累计确诊人数:"+row["累计确诊人数"]+",累计死亡人数:"+row["累计死亡人数"]+",累计治愈人数:"+row["累计治愈人数"]+"}"+"")

        print("{" + "省内地区:'" + row["省内地区"] + "'," + "现有确诊人数:" + row["现有确诊人数"] + ",累计确诊人数:" + row["累计确诊人数"] + ",累计死亡人数:" + row[
                "累计死亡人数"] + ",累计治愈人数:" + row["累计治愈人数"] + "}" + "")
