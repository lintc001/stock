import math
import random
import time

import twstock

from src.globalVar import companyCodeList

print(companyCodeList)
countCode = math.ceil(len(companyCodeList) / 100)
print(countCode)
twstock.realtime.get('1701')
print('1701' in twstock.codes.keys())
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
