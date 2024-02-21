import requests
import pandas

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"
}

url = "https://tianqi.2345.com/Pc/GetHistory"

def crawl_data(year,month):
    params = {
        "areaInfo[areaId]": 58321,
        "areaInfo[areaType]": 2,
        "date[year]": year,
        "date[month]": month
    }

    resp = requests.get(url, headers=headers, params=params)
    data = resp.json()["data"]
    df = pandas.read_html(data)[0]
    # print(df.head())
    print(f"成功打印{year},{month}")
    return df

df_list = []
for year in range(2012, 2023):
    for month in range(1, 13):
        df = crawl_data(year, month)
        df_list.append(df)

pandas.concat(df_list).to_excel("tianqi.xlsx", index=False)