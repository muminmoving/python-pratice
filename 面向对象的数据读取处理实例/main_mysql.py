from file_define import *
from data_define import *
from pymysql import Connection
text_filereader = Text_filereader("C:/Users/moving/Desktop/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年1月销售数据.txt")
json_filereader = Json_filereader("C:/Users/moving/Desktop/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年2月销售数据JSON.txt")
data1: list[Record] = text_filereader.reader()
data2: list[Record] = json_filereader.reader()

data: list[Record] = data1 + data2

# 链接数据库
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='316276',
    autocommit=True
)
cursor = conn.cursor()
conn.select_db("py_mysql")

for record in data:
    sql = (f"insert into orders(order_date,ordre_id,money,province)"
           f"values('{record.date}','{record.order_id}',{record.money},'{record.province}')")
    #cursor.execute(sql)
with open("C:/Users/moving/Desktop/1.txt", "w", encoding="utf8") as i:
    cursor.execute('select * from orders')
    for j in cursor:
        i.write(f"({str(j)}\n")
conn.close()
