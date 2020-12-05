import pandas as pd
s = lambda : print("\n")

df = pd.read_csv("Tidy\\CSVs\\pew.csv")
print(df.head())

s()

long_df = pd.melt(df, id_vars="religion") # Change a bunch of columns and turn them into one column - DO NOT TOUCH religion column
print(long_df.head())

print(df)
s()

print(long_df)

# ADVANCED = for stuff like this, make your own dynamic excel file like you EPS mini project

