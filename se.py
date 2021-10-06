import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123',
                     db='sys')

# 使用 cursor() 方法创建一个游标对象cur
cur = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cur.insert_db("INSERT INTO sys.xiaozu_phonecode(id,phone,type,addtime,code) VALUES(21990,8,10,70,12)")

# 使用 fetchall() 方法获取查询结果
data = cur.fetchall()

print(data)

# 关闭数据库连接
db.close()

