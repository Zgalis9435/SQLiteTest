import sqlite3

def searchEstudent():
    conn=sqlite3.connect('mydatabase.db')
    cursor=conn.cursor()
    rows=cursor.execute('SELECT * FROM alumnos WHERE NAME="RODRIGO"')

    data=rows.fetchone()

    for row in data:
        print(row)

    cursor.close()
    conn.close()

  
result=searchEstudent()
