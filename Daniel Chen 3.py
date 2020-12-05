# TODO
# Add a column that has the sale price in USD = SO multiply and then add column to the DF.

import pandas as pd, os
print(os.getcwd())
s = lambda : print("\n")

file = open("Tidy\\fresh.xlsx", "rb")

df = pd.read_excel(file, sheet_name="Payment", index_col=0)

# Print rows and state whether they have a status of Pending
print(df["Status"] == "Pending")
s()

# Now let's only print those which are Fraudulent and their Location.
fraudulent_only = df.loc[df["Status"] == "Fraudelent", ["Status", "Location"]]
print(fraudulent_only)
# How does it work? 
# For that, we need to look at df["Status"] == "Pending"
s()

pending_only = df["Status"] == "Pending"
print(type(pending_only))
print(df.loc[pending_only,"Status"]) # For some reason, it only reads the Payment IDs that are true, therefore it gets the payment IDs it has to print
s()


# Now, let's apply multiple conditions.

# For example, Fraudelent and Telephone
fraud_only = df["Status"] == "Fraudelent" # This represents a series with True or False for whether the status is Pending
TelephoneOnly = df["Location"] == "Telephone"

fraud_and_telephone = df.loc[(fraud_only) & (TelephoneOnly), "Sales"] # LATER: Make excel file that has if fraudulent then higher than £43000

print(fraud_and_telephone) # Fraud and Telephone only Sales.


