import sqlite3
def db():
    con=sqlite3.connect(database="mac.db")
    cur=con.cursor()


    cur.execute("CREATE TABLE employe (eid INTEGER PRIMARY KEY AUTOINCREMENT,fname text, lname text,contact text,email text, question text,answer text,password text)")
    con.commit()

    con.close()
db()