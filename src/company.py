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

fileUrlDict = {"上市": r"https://mopsfin.twse.com.tw/opendata/t187ap03_L.csv",
               "上櫃": r"https://mopsfin.twse.com.tw/opendata/t187ap03_O.csv"
               }

source = r"./resource/company"

fileToDbField = {"上市": {"出表日期": 0,  # source_time
                          "公司代號": 1,  # stock_code
                          "產業別": 5,  # industry_short_name
                          "成立日期": 14,  # founding_date
                          "上市日期": 15,  # ipo_date

                          },
                 "上櫃": {"出表日期": 0,  # source_time
                          "公司代號": 1,  # stock_code
                          "產業別": 5,  # industry_short_name
                          "成立日期": 14,  # founding_date
                          "上市日期": 15,  # ipo_date

                          }

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


def checkField(fieldsName, fileUrlKey):
    """
    檢查取得的資源欄位是否正確
    """
    fieldMap = fileToDbField[fileUrlKey]
    for key in fieldMap:
        if fieldsName[fieldMap[key]] != key:
            print(f"{fileUrlKey}的資料中，{key}與原本位置({fieldMap[key]})不符(檔案資料為{fieldsName[fieldMap[key]]})")
            break
    return False


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
            tmpList = []
            insertCount = 0
            csvField = fileToDbField[fileUrlKey]
            insert_query = "INSERT INTO company (stock_code, stock_channel, company_name) VALUES (%s, %s, %s)"
            for row in reader:
                insertCount += 1
                tmpDict = {}
                tmpDict["source_time"] = row[0]
                tmpDict["stock_code"] = row[1]
                tmpDict["industry_short_name"] = row[5]
                tmpDict["founding_date"] = row[14]
                tmpDict["ipo_date"] = row[15]
                tmpList.index(tmpDict)
                # if len(tmpList)==1000:
                    # cursor.

# cursor.execute(insert_query, (data['name'], data['date_of_birth'], data['profession']))

    except Exception as e:
        print(f"請求出錯:")
        traceback.print_exc()
    finally:
        cursor.close()
        conn.close()

getCompany()
