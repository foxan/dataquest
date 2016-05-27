df = pd.read_sql_query(query, conn)import sqlite3
import math
import pandas as pd

conn = sqlite3.connect("factbook.db")
query = "SELECT * FROM facts;"

df = pd.read_sql_query(query, conn)
print("Original: {0}".format(df.shape[0]))
df = df.dropna(axis=0)
print("After dropping NaN rows: {0}".format(df.shape[0]))

def projected_population(df):
    pop = df["population"]
    growth = df["population_growth"]
    year = 2050
    return pop * math.e ** ((growth/100) * (year-2015))

df["population_2050"] = df.apply(projected_population, axis=1)
df = df.sort("population_2050", ascending=False)
pd.options.display.float_format = '{:,.0f}'.format
print(df[["name", "population_2050"]].head(5))