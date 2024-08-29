import math
import random
import time
from datetime import datetime, timedelta

# import twstock

from src.globalVar import companyCodeList, companyShortList, companyChannelList

print(companyCodeList)
countCode = math.ceil(len(companyCodeList) / 100)
print(countCode)
# twstock.realtime.get('1701')
# print('1701' in twstock.codes.keys())
#
# for i in range(countCode):
#     companyCodeSubLst = companyCodeList[(i * 100): (i * 100 + 100)]
#     print("companyCodeSubLst", companyCodeSubLst)
#     stock = twstock.realtime.get(companyCodeSubLst)
#     print("-" * 50)
#     print(stock)
#     with open(r"./resource/realtime.txt", "a") as f:
#         f.write(str(stock))
#     time.sleep(random.randint(1, 20))
import yfinance as yf
import mplfinance as mpf

# 下載台灣 2330 (台積電) 的股票數據
source = r"./resource/price"
yf.set_tz_cache_location(source)

targetTime = datetime.strptime("2024/08/29 13:20:00", "%Y/%m/%d %H:%M:%S")

nowtime = datetime.now()
print(nowtime)

print(" ".join(companyChannelList[0:1]))
df = yf.download(" ".join(companyChannelList[0:1]) , period="1d", interval="1m", start=targetTime)
print(df)
df.to_csv(source+"/priceDownload2.csv")


ddf = yf.Ticker(" ".join(companyChannelList[0:1]))
x = ddf.history(period="1d", interval="1m", start=targetTime)
x.to_csv(source+"/priceDownload_history.csv")
# 檢查數據是否成功下載
# if df.empty:
#     print("股票數據下載失敗或沒有數據。")
# else:
#     # 繪製 K 線圖
#     mpf.plot(df, type='candle', style='charles', title='2330', volume=True)
