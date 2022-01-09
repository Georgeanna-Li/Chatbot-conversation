import sqlite3

con = sqlite3.connect('bigbang.db')
con.text_factory = str
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS corpus
               (input, output)''')

with open('big_bang_test.txt') as f:
    lines = f.readlines()
    # print(lines)
    for line in lines:
        # print(line)
        if "User" in line:
            input = line[(line.index(":")+2):-3]
            output = []
            # print(input)
            continue
        if line == "\r\n":
            output = [one.replace("Esmerelda Quest Bot Says: ", "").replace("\r\n", "") for one in output]
            # output = [one.replace("\r\n", "") for one in output]
            output = ''.join(map(str, output))
            # print(input)
            # print(output)
            # params = (input, output)
            cur.execute("INSERT INTO corpus VALUES (?, ?)", (input, output))
            input = None
            # break
        if input:
            output.append(line)

con.commit()
con.close()
