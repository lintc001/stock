import html
import math

from urllib.request import urlopen
import os
import traceback
import csv
import codecs
from sqlConn import getConn
from datetime import datetime

from src.utils import datetimeUtil

# 取得公司資料的網址
fileUrlDict = {"上市": r"https://mopsfin.twse.com.tw/opendata/t187ap03_L.csv",
               "上櫃": r"https://mopsfin.twse.com.tw/opendata/t187ap03_O.csv"
               }
# 儲存公司資料csv的路徑
source = r"./resource/company"
# aa = {"a": {[["出表日期", 0, "source_time"]]}}
# csv與db的欄位對應
csvToDbField = {"上市": [["出表日期", 0, "source_time"],
                         ["公司代號", 1, "stock_code"],
                         ["公司名稱", 2, "company_name"],
                         ["公司簡稱", 3, "short_name"],

                         ["產業別", 5, "industry_id"],
                         ["成立日期", 14, "founding_date"],
                         ["上市日期", 15, "ipo_date"]
                         ],
                "上櫃": [["出表日期", 0, "source_time"],
                         ["公司代號", 1, "stock_code"],
                         ["公司名稱", 2, "company_name"],
                         ["公司簡稱", 3, "short_name"],

                         ["產業別", 5, "industry_id"],
                         ["成立日期", 14, "founding_date"],
                         ["上市日期", 15, "ipo_date"]
                         ]
                }


def checkFolder():
    """
    確保路徑的目錄正常
    """
    global abspath
    try:
        abspath = os.path.abspath(source)
        print(f"路徑({abspath})")
        if not os.path.exists(source):
            print(f"路徑({abspath})不存在,建立中")
            os.makedirs(source, mode=0o777)
            print(f"路徑({abspath})建立完成")
    except Exception as e:
        print(f"請求出錯:")
        traceback.print_exc()
    return abspath


def saveFile(respList, fileUrlKey):
    """
    儲存資源
    """
    checkFolder()
    with open(source + f"\\{fileUrlKey}.csv", "wb") as f:
        for row in respList:
            f.write(row)


def checkField(csvFieldNames, fileUrlKey):
    """
    檢查取得的資源欄位是否正確
    """
    fieldList = csvToDbField[fileUrlKey]
    for ele in fieldList:
        csvFieldName = csvFieldNames[ele[1]]
        if csvFieldName != ele[0]:
            print(f"{fileUrlKey}的資料中，csv的第({ele[1] + 1})欄應該為{ele[0]}(目前為{csvFieldName})")
            return False
    return True


def toDict(reader):
    datList = []

    for row in reader:
        print(row)


def getCompany():
    """
    取得公司資料
    """
    global cursor, conn
    try:

        companyList = []
        for fileUrlKey in fileUrlDict:
            print(f"開始取得{fileUrlKey}的公司資料：")
            resp = urlopen(fileUrlDict[fileUrlKey])
            if resp.code != 200:
                print(f"請求有問題：response code={resp.code}")
                return None

            respList = resp.readlines()
            # saveFile(respList, fileUrlKey)

            reader = csv.reader(codecs.iterdecode(respList, 'utf-8-sig'))
            fieldNameList = next(reader, [])

            # print(fieldNameList)
            if not checkField(fieldNameList, fileUrlKey):
                continue
            conn = getConn()
            # 創建游標
            cursor = conn.cursor()
            # 欄位名稱已讀取過，這邊直接從第2列開始
            insertCount = 0
            '''
                csvToDbField：{"上市": [["出表日期", 0, "source_time"],
                         ["公司代號", 1, "stock_code"],
                         ],
               
                }

                '''
            csvField = csvToDbField[fileUrlKey]
            insertQuery = """INSERT INTO company ( stock_code, company_name, short_name, market_id, industry_id
                                                , founding_date, ipo_date, source_time ) 
                                        VALUES ( %(stock_code)s, %(company_name)s, %(short_name)s, %(market_id)s, %(industry_id)s
                                                , %(founding_date)s, %(ipo_date)s, %(source_time)s
                                ) """
            print(f"{fileUrlKey}整理資料")
            for row in reader:

                dataDist = {}
                for f in csvField:
                    if f[0] == "出表日期":
                        # print(row[f[1]])
                        tranStr = datetimeUtil.twToAd(row[f[1]])
                        tranStr = datetime.strptime(tranStr + " 00:00:00", "%Y%m%d %H:%M:%S")
                        row[f[1]] = tranStr
                    elif f[0] in ("成立日期", "上市日期"):
                        tranStr = datetime.strptime(row[f[1]] + " 00:00:00", "%Y%m%d %H:%M:%S")
                        row[f[1]] = tranStr

                    if (type(row[f[1]]) is str) and (row[f[1]].find("&#") > -1):
                        row[f[1]] = html.unescape("&#20870;星科技股份有限公司")

                    dataDist[f[2]] = row[f[1]]
                if fileUrlKey == "上市":
                    dataDist["market_id"] = "sii"
                elif fileUrlKey == "上櫃":
                    dataDist["market_id"] = "otc"

                companyList.append(dataDist)
            print(f"{fileUrlKey}整理資料完成")

        print(f"準備新增到資料庫")
        listCount = math.ceil((len(companyList) / 1000))
        for i in range(listCount):
            # 使用 executemany 進行批量插入
            cursor.executemany(insertQuery, companyList[i * 1000:i * 1000 + 1000])
        conn.commit()
        print(f"完成新增")
    except Exception as e:
        conn.rollback()
        print(f"請求出錯:")
        traceback.print_exc()
    finally:

        if cursor != None:
            cursor.close()
        if conn != None:
            conn.close()


def listAllCompanyShort():
    '''
    取得所有公司的簡要資料
    :return:
    '''
    conn = getConn()
    # 創建游標
    cursor = conn.cursor()
    selectSQL = """
                SELECT c.id, c.stock_code,c.company_name,c.short_name,c.market_id
                    , m.name AS market_name ,c.industry_id, i.name AS industry_name
                FROM company c
                LEFT JOIN market m ON c.market_id=m.id
                LEFT JOIN industry i ON c.industry_id=i.id AND m.id=i.market_id
                """
    cursor.execute(selectSQL)
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return results


# getCompany()

# print(listAllCompanyShort())
