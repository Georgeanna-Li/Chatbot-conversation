import sqlite3
con = sqlite3.connect('bigbang.db')
cur = con.cursor()
result = []
for row in cur.execute("SELECT input FROM corpus"):
    print(row)
con.close()
