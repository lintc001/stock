from src.sqlConn import getConn


def listAllIndustry():
    '''
    產業類別
    '''
    conn = getConn()
    # 創建游標
    cursor = conn.cursor()
    selectSQL = """
                    SELECT i.id,i.`name`,i.market_id,m.name AS market_name 
                    FROM industry i
                    LEFT JOIN  market m  ON  m.id=i.market_id
                """
    cursor.execute(selectSQL)
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return results


print(listAllIndustry())
