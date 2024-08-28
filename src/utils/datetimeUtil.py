def twToAd(twDatetime):
    '''民國時間轉西元'''
    # yyyMMdd
    if len(twDatetime) == 7:
        return str(int(twDatetime[0:3]) + 1911) +  twDatetime[3:]
    else:
        return twDatetime

def AdToTw(adDatetime):
    '''西元時間轉民國'''
    # yyyyMMdd
    if len(adDatetime) == 7:
        return str(int(adDatetime[0:4]) - 1911) + '' + adDatetime[4:]
    else:
        return adDatetime
