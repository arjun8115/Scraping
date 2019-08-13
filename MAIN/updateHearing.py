# from Test import DHCaseStatus
#
# temp = DHCaseStatus.funcCaseType('CO.PET.','704','2014')
#
# print(temp)

import psycopg2
def retriveRecord():
    list_ID= []
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="arjun",
                                      host="localhost",
                                      port="5432",
                                      database="scrap_db")
        cursor = connection.cursor()
        #insert_query = """ INSERT INTO caseUpdate (caseId, hearing) VALUES (%s,%s)"""
        #insert_value = ('CRL.A. 535/2016', 'NULL')
        #del_query = """ DELETE FROM caseUpdate WHERE id=5"""
        retrieve_query = """ SELECT * FROM caseUpdate"""
        cursor.execute(retrieve_query)
        list = cursor.fetchall()

        for item in list:
            tempList = []
            tempList.append(item[0])
            tempList.append(item[3])
            list_ID.append(tempList)
        connection.commit()
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

    return list_ID

def updateRecordDHC(id_num):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="arjun",
                                      host="localhost",
                                      port="5432",
                                      database="scrap_db")
        cursor = connection.cursor()

        retrieve_query = """ SELECT caseid FROM caseUpdate WHERE id= %s"""
        cursor.execute(retrieve_query,(id_num, ))
        list = cursor.fetchall()
        caseId = list[0][0]
        court,noyear = caseId.split()
        tnoyear = noyear
        num = noyear[:-5]
        year = tnoyear[-4:]

        from Test import DHCaseStatus
        list = DHCaseStatus.funcCaseType(court,num,year)
        hearing_date = list[0][3]

        update_query = """ UPDATE caseUpdate SET hearing =%s WHERE id= %s"""
        cursor.execute(update_query,(hearing_date,id_num))
        connection.commit()
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

def updateRecordRERA(id_num):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="arjun",
                                      host="localhost",
                                      port="5432",
                                      database="scrap_db")
        cursor = connection.cursor()

        retrieve_query = """ SELECT caseid FROM caseUpdate WHERE id= %s"""
        cursor.execute(retrieve_query,(id_num, ))
        list = cursor.fetchall()
        caseNO = list[0][0]
        #print(caseNO)

        from Test import NCDRCCaseStatus
        hearing  = NCDRCCaseStatus.funcCaseType(caseNO)

        update_query = """ UPDATE caseUpdate SET hearing =%s WHERE id= %s"""
        cursor.execute(update_query, (hearing, id_num))
        connection.commit()



    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()