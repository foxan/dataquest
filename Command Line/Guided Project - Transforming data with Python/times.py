import read
from dateutil import parser

df = read.load_data()

def hour_parser(date):
    parsed_date = parser.parse(date)
    return parsed_date.hour

hour_count = df["submission_time"].apply(hour_parser).value_counts()

print(hour_count)

for hour, count in hour_count.items():
    print("{0}: {1}".format(hour, count), end=", ")