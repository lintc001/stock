from dbutils.pooled_db import PooledDB

# from DBUtils.PooledDB import PooledDB
import pymysql

# 設置連接池
pool = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=2,
    maxcached=5,
    blocking=True,
    host='localhost',      # MySQL 伺服器地址
    user='stock',  # 使用者名稱
    password='1234',  # 密碼
    database='stock',  # 資料庫名稱
)


def getConn():
    # 使用連接池
    return pool.connection()