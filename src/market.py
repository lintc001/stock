from src.sqlConn import getConn


def listAllmarket():
    '''
    產業類別
    '''
    conn = getConn()
    # 創建游標
    cursor = conn.cursor()
    selectSQL = """
                    SELECT * FROM market
                """
    cursor.execute(selectSQL)
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return results


print(listAllmarket())
