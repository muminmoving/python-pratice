from pymysql import Connection
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='316276',
    autocommit=True
)
cursor = conn.cursor()
conn.select_db()
print(conn.get_server_info())
conn.close()
