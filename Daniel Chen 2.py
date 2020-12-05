import pandas as pd, os

s = lambda : print("\n")
r = lambda x : x-1

print(os.getcwd())
s()

# We have a file that has 2 headers, one is the title and the other is the actual header we want to use.
# Also, we want to use the actual Payment ID as our index - this means we will now use LOC
df = pd.read_excel("Tidy\\complex_header.xlsx", header=[1], sheet_name="Sheet1", index_col=0)
s()

# Printing rows using the Payment ID and LOC
print(df.loc["CT026223":"PT007114"]) # Now, the used is Payment ID
s()

# Get rows 0 - 2 (1 - 3) and their Sale Price
print(df.iloc[0:2]["Sale Price"])
s()

# Get rows 0 - 2 and their Sale Price
print(df.iloc[0:2].loc[:,"Sale Price"])

s()
# Enter description here - Get rows 2 - 4 and 9 - 11

twoToFour = df.iloc[2:4]
nineToEleven = df.iloc[9:11]

print(twoToFour)
s()
print(nineToEleven)
s()
# Now, to combine these 2 ranges. Concatenation.
# Later we will find a way to just print the 2 ranges.

print(pd.concat([twoToFour, nineToEleven]))
s()

# Print all even rows.
print("Evens only")
print(df.iloc[[x for x in range(0, df.values.__len__()) if x % 2 == 0]])

# Head() - Print the 1st five rows of the set - like a demo

# Lets's print rows 3 - 6 , 9 - 11 , 22 - 25 and the "Sales" and "Status" columns but just the first five rows.


some_rows_columns =    pd.concat(
                                    [
                                        df.iloc[2:5], 
                                        df.iloc[8:10], 
                                        df.iloc[21:24]
                                    ]
                                ).loc[:,["Sales", "Status"]]

head_some_rows_columns = some_rows_columns.head()

print(head_some_rows_columns)




# TODO
# Add a column that has the sale price in USD = SO multiply and then add column to the DF.



"""
read_excel FUNCTION ARGUMENTS
(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, 
squeeze=False, dtype=None, engine=None, converters=None, true_values=None, 
false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, 
na_filter=True, verbose=False, parse_dates=False, date_parser=None, thousands=None, 
comment=None, skipfooter=0, convert_float=True, mangle_dupe_cols=True)

enginestr, default None
If io is not a buffer or path, this must be set to identify io. Supported engines: 
“xlrd”, “openpyxl”, “odf”, “pyxlsb”, default “xlrd”. Engine compatibility : - 
“xlrd” supports most old/new Excel file formats. - 
“openpyxl” supports newer Excel file formats. - 
“odf” supports OpenDocument file formats (.odf, .ods, .odt). - 
“pyxlsb” supports Binary Excel files.

"""