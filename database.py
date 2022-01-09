import sqlite3

con = sqlite3.connect('bigbang.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS corpus
               (input, output)''')
con.commit()
con.close()
