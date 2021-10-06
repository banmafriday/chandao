import pymysql


def insert_db(sql_insert):
    '''插入操作'''
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='123',
                         db='sys')
    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    try:
        cur.execute(sql_insert)
        # 提交
        db.commit()
    except Exception as e:
        print("错误信息：%s" % str(e))
        # 错误回滚
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    sql_insert = "INSERT INTO sys.xiaozu_phonecode(id,phone,type,addtime,code) VALUES(9921990,8,10,70,12)"
    insert_db(sql_insert)
