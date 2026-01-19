import pandas as pd
import glob

path = "row_Data/Biometric_Update/*.csv"
files = glob.glob(path)

df_list = [pd.read_csv(file) for file in files]
bio_all = pd.concat(df_list, ignore_index=True)

bio_all.to_csv("Biometric_All.csv", index=False)

print("Biometric CSVs combined successfully")
# Path to biometric CSV files

df = pd.read_csv("enrolment_2018.csv")
df["date"].head()
df["Year"] = 2018
