import sqlite3

conn = sqlite3.connect('workTime.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS works(
   start REAL,
   end REAL,
   work TEXT,
   time REAL);
""")
conn.commit()

s = input('Start= ')
start = float(s)
e = input('End= ')
end = float(e)
work = input(('Work= '))
t1 = s
h1 = int(t1.split('.')[0])
m1 = int(t1.split('.')[1])
t2 = e
h2 = int(t2.split('.')[0])
m2 = int(t2.split('.')[1])
d = (h2*60+m2)-(h1*60+m1)
hd = str(d // 60)
md = str(d % 60)
timeWork = float(hd+'.'+md)
variable = (start, end, work, timeWork)

cur.execute("INSERT INTO works VALUES(?, ?, ?, ?);", variable)
conn.commit()

conn.close()