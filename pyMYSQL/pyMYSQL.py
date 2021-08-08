import pymysql
#查询
#连接数据库
conn = pymysql.connect(host='localhost',user='root',passwd='root66',db='数据库名',pot='3306',
charset='utf8')
#获取游标
cur = conn.cursor()
cur.execute('数据库查询语句')
#获取数据，fetchone获取一条数据，fetchall获取全部数据
data = cur.fetchall()
for d in data:
 print(d)
#关闭游标
cur.close()
#关闭数据库
conn.close()