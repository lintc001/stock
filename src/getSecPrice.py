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

targetTime = datetime.strptime("2024/08/29 12:30:00", "%Y/%m/%d %H:%M:%S")
print("targetTime:",targetTime)
nowtime = datetime.now()
print(nowtime)
companyChannelStr = " ".join(companyChannelList[0:100])
print(companyChannelStr)
print("使用download")
dtime = datetime.now()
df = yf.download(companyChannelStr , period="1d", interval="1m", start=targetTime, group_by="ticker", threads=True)
print(df)
df.to_csv(source+"/priceDownload2.csv")
print("使用download所需時間=",(datetime.now()-dtime))

print("使用history")
htime = datetime.now()
ddf = yf.Tickers(companyChannelStr)
x = ddf.history(period="1d", interval="1m", start=targetTime, group_by="ticker")
x.to_csv(source+"/priceDownload_history.csv")
print("使用history所需時間=",(datetime.now()-htime))
# 檢查數據是否成功下載
# if df.empty:
#     print("股票數據下載失敗或沒有數據。")
# else:
#     # 繪製 K 線圖
#     mpf.plot(df, type='candle', style='charles', title='2330', volume=True)
