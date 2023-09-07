import csv

with open('../data-csv/4.do_province.csv') as f:
    f=csv.DictReader(f)
    # for row in f:
    #     print("{"+"name:'"+row["地区"]+"省',"+"value:["+row["现有确诊人数"]+","+row["累计确诊人数"]+","+row["累计死亡人数"]+","+row["累计治愈人数"]+"]}"+",")
    #
    # for row in f:
    #     print("{"+"name:'"+row["地区"]+"省',"+"value:"+row["现有确诊人数"]+"}"+",")
    #
    # for row in f:
    #     print("{"+"name:'"+row["地区"]+"省',"+"value:"+row["累计确诊人数"]+"}"+",")
    #
    # for row in f:
    #     print("{"+"name:'"+row["地区"]+"省',"+"value:"+row["累计死亡人数"]+"}"+",")
    # #
    for row in f:
        print("{"+"name:'"+row["地区"]+"省',"+"value:"+row["累计治愈人数"]+"}"+",")

