import pandas
import os

# Parameters of all functions are very important.
# For e.g sheet_name, index = false/true, 
# Add all you can find from Eric (Wrangling) folder and add to here.
# Save the below as variables to see if they can be assigned.


s = lambda : print("\n")

print(os.getcwd())

df = pandas.read_excel(r"\\ukdfs.mintecglobal.com\\User\\Redirect\\Hamza.Malik\\Desktop\\My Python\\Tidy - Wrangling - Daniel Chen\\fresh.xlsx", sheet_name = "Payment")

print(df.head())
s()
print(df.columns)
s()
print(df.index)
s()
print(df.values) # Numpy array version of data set
s()
print(type(df))
s()
print(df.shape) # Does not include column header
s()
print(df.info())
"""
type
range of rows (not including column)
column - non-null count - object
dtypes
memory
"""
s()

# Can we save the column names as list, cycle through them? 

import itertools

column_names = df.columns
iter_columns = list(column_names)

cyc = itertools.cycle(iter_columns)

for turn in range(10):
    print(next(cyc))

# Yes we can.


# Getting one column's data only. Series is one column of data. Dataframe is collection of series.
sale_price_symbol = df["Sales"]

s()

print(df["Sale Price"])
sale_price = df["Sale Price"]
s()
print(type(sale_price)) # Like a 1D numpy array

s()
# Getting series for 2 columns 

subset = df[    ["Payment ID", "Sale Price"]   ]
print(subset)
print(type(subset))

s()
# Using .loc method to find row of certain index
# We need rows 5 - 20 (4 - 19)


# First, let's print row 5
print(df.loc[5])
# REMEMBER - 5 means that we count from the first row after the column header - 0 is first price, 5 is 6th price
# Thus, 5 means 6th row of prices and 7th when looking at the actual cell of the excel file (including the header)

# Let's now get rows 5 and 20 (4 and 19)
s()
print(".loc 4,19")
subset_row_wise = df.loc[[4,19]]
print(subset_row_wise)

# Let's now get rows 5 to 20 (4 to 19) # LATER: Try 3 - 7 and 9 - 14
s()
print(".loc 4 - 20 and sales and status only")
subset_row_wise = df.loc[[x for x in range(4,20)]]
print(subset_row_wise[["Sales", "Status"]])

s()
# loc vs iloc

loc__ = df.loc[2] # if index were a column of names then it can be used here
print(loc__)
s()
loci__= df.iloc[2] # this integer based and does not take alphabets, however 2 will get the same location out.
print(loci__)
s()
loc_index_range = df.iloc[3:13]
print(loc_index_range)





# Advanced: 
# Get country from other sheet, Sales and Status from this one - SQL relational databases would make this even harder.