import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="dataset"
)

conn = db.cursor()

conn.execute("CREATE TABLE SERVER("
             "id int(6) NOT NULL UNIQUE,"
             "type int(2)"
             "participants int(6) DEFAULT 1,"
             "timeStart datetime NOT NULL,"
             "questionNumber int(2) DEFAULT (0) NOT NULL,"
             ""
             ")")

#how does loadig screen work - does number of guessed right update as the lobby guesses?



"""
conn.execute("CREATE TABLE COMPANIES ("
               "id int(6),"
               "name VARCHAR(20) NOT NULL,"
               "emissions int(20) NOT NULL,"
               "tags VARCHAR(30) NOT NULL,"
               "timesSeen int(7) DEFAULT 0,"
               "timesCorrect int(7) DEFAULT 0)")
"""
"""
conn.execute("CREATE TABLE products ("
               "id int(6),"
               "name VARCHAR(10) NOT NULL,"
               "emissions DOUBLE (9,8) NOT NULL,"
               "tags VARCHAR(30) NOT NULL,"
               "timesSeen int(7) DEFAULT 0,"
               "timesCorrect int(7) DEFAULT 0"
               ")")
"""

