import pandas as pd
import glob
import os
import numpy as np

import matplotlib.pyplot as plt


# Path to enrolment CSV files
path = "01_Datasets/Enrolment/*.csv"

if os.path.exists("Enrolment_All.csv"):
    print("File already existed.")
else:
    # Read all CSV files
    files = glob.glob(path)

    if files:
        # Combine all CSVs
        df_list = [pd.read_csv(file) for file in files]
        enrolment_all = pd.concat(df_list, ignore_index=True)
        enrolment_all.to_csv("Enrolment_All.csv", index=False)
        print("File made successfully.")
    else:
        print("No source files found to create Enrolment_All.csv")


df = pd.read_csv("Enrolment_All.csv")
df.columns = df.columns.str.strip()

# Convert date properly
df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")

#Add Month & Year columns
df["Month"] = df["date"].dt.to_period("M")
df["Year"] = df["date"].dt.year

#Total enrolment

df["Total_Enrolment"] = (
    df["age_0_5"] +
    df["age_5_17"] +
    df["age_18_greater"]
)

# Month-wise analysis
month_data = df.groupby("Month")["Total_Enrolment"].sum()
print(month_data)

#State-wise analysis
state_data = df.groupby("state")["Total_Enrolment"].sum()
print(state_data.sort_values(ascending=False))

#State + Month (Very Powerful)
state_month = df.groupby(["state","Month"])["Total_Enrolment"].sum()
print(state_month)


print(f"Total Enrolment: {df['Total_Enrolment'].sum()}")

# Basic cleaning
df = df.dropna()

print(df.head())
print(df.info())

enrol_summary = df.groupby(['state', 'Year'])['Total_Enrolment'].sum().reset_index()
enrol_summary.to_csv("Enrolment_Summary.csv", index=False)
print("Enrolment summary saved successfully")

print(enrol_summary.head())
print(enrol_summary.describe())

#BASIC VISUALISATION (NOW)

#Bar Chart – Top States (Example: Enrolment)
top_states = enrol_summary.groupby('state')['Total_Enrolment'].sum().sort_values(ascending=False).head(10)

top_states.plot(kind='bar', title='Top 10 States by Aadhaar Enrolment')
plt.show()

#Line Chart – Trend Over Time
trend = enrol_summary.groupby('Year')['Total_Enrolment'].sum()

trend.plot(kind='line', title='Aadhaar Enrolment Trend Over Time')
plt.show()
