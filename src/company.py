import twstock
from urllib.request import urlopen
import urllib
import codecs
import json
import os
import traceback
import csv
import codecs
from sqlConn import getConn

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


["出表日期", 0, "source_time"]


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

            print(fieldNameList)
            if not checkField(fieldNameList, fileUrlKey):
                continue
            conn = getConn()
            # 創建游標
            cursor = conn.cursor()
            # 欄位名稱已讀取過，這邊直接從第2列開始
            companyList = []
            insertCount = 0
            '''
                csvToDbField：{"上市": [["出表日期", 0, "source_time"],
                         ["公司代號", 1, "stock_code"],
                         ],
               
                }

                '''
            csvField = csvToDbField[fileUrlKey]
            insertQuery = """INSERT INTO company ( stock_code, stock_channel, company_name, short_name, market_id, industry_id
                                                , founding_date, ipo_date, source_time ) 
                                VALUES ( %(stock_code)s, %(stock_channel)s, %(company_name)s, %(short_name)s, %(market_id)s
                                , %(industry_id)s, %(founding_date)s, %(ipo_date)s, %(source_time)s
                                ) """

            for row in reader:

                dataDist = {}
                for f in csvField:
                    dataDist[ f[2] ] = row[ f[1] ]
                if fileUrlKey == "上市":
                    dataDist["market_id"] = "sii"
                elif fileUrlKey == "上市":
                    dataDist["market_id"] = "otc"

                companyList.append(dataDist)
                # 使用 executemany 進行批量插入
            cursor.executemany(insertQuery, companyList)
            conn.commit()



    except Exception as e:
        print(f"請求出錯:")
        traceback.print_exc()
    finally:

        if cursor != None:
            cursor.close()
        if conn != None:
            conn.close()


getCompany()
