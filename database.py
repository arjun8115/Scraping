import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "arjun",
                                  host = "localhost",
                                  port = "5432",
                                  database = "scrap_db")
    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE caseUpdate
              (ID SERIAL PRIMARY KEY     ,
              caseId           CHARACTER VARYING(255)    NOT NULL,
              hearing        CHARACTER VARYING(255) ,
              courtId  CHARACTER VARYING(255)); '''


    insert_query = """ INSERT INTO caseUpdate (caseId, hearing, courtId) VALUES (%s,%s,%s)"""
    insert_value = ('CO.PET. 704/2014','NULL',1)
    #cursor.execute(create_table_query)
    cursor.execute(insert_query,insert_value)
    connection.commit()
    #print("Table created successfully in PostgreSQL ")

finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")