import sqlite3

conn = sqlite3.connect('movies')

conn.execute("INSERT INTO Movies (name, actor, actress, director, 'year_of_release') VALUES ('RRR', 'Ram Charan', 'Alia Bhatt', 'Chandramouli', 2022);")
conn.execute("INSERT INTO Movies (name, actor, actress, director, 'year_of_release') VALUES ('Bahubali', 'Prabaas', 'Thamanah', 'chandramouli', 2018);")
conn.execute("INSERT INTO Movies (name, actor, actress, director, 'year_of_release') VALUES ('Soorarai Pootru', 'surya ', 'aparna', 'sudha', 2021);")

c = conn.execute("SELECT * FROM Movies")

for i in c:
    print(i)