import sqlite3
conn = sqlite3.connect("factbook.db")

c = conn.cursor()
c.execute("SELECT name, population FROM facts WHERE population IS NOT NULL ORDER BY population ASC LIMIT 10;")

for count, (name, population) in enumerate(c.fetchall()):
    print("{0}. {1}: {2}".format(count + 1, name, str(population)))