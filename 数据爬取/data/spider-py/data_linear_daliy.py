import csv

with open('../data-csv/3.do_daily_add.csv') as f:
    f=csv.DictReader(f)
    # for row in f:
    #     print("'"+row["统计时间"]+"',")

    # for row in f:
    #     print("'"+row["输入病例"]+"',")

    # for row in f:
    #     print("'"+row["大陆新增确诊人数"]+"',")

    # for row in f:
    #     print("'"+row["全国新增确诊人数"]+"',")

    # for row in f:
    #     print("'"+row["死亡人数"]+"',")

    # for row in f:
    #     print("'"+row["死亡率"]+"',")

    # for row in f:
    #     print("'"+row["治愈人数"]+"',")

    for row in f:
        print("'"+row["治愈率"]+"',")