import sqlite3
import math
import pandas as pd

conn = sqlite3.connect("factbook.db")
query = "SELECT SUM(area_land) / SUM(area_water) FROM facts;"

result = pd.read_sql_query(query, conn)
print(result)