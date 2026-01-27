import sys
import pandas as pd

print("arguments", sys.argv)


df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")
day = int(sys.argv[1]) #argv[0] is the script name that allow to take input from outside.
print(f"Running pipeline for day {day}")