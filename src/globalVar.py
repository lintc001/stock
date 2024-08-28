from src.company import listAllCompanyShort
from src.industry import listAllIndustry
from src.market import listAllmarket

companyShortList = listAllCompanyShort()
'''所有公司的簡要資料'''

industryList = listAllIndustry()
'''所有的產業類別'''

marketList = listAllmarket()
'''市場類別'''

companyCodeList = [i['stock_code'] for i in companyShortList]