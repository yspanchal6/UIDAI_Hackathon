import pandas as pd
import glob

path = "01_Datasets/Demographic_Update/*.csv"
files = glob.glob(path)

df_list = [pd.read_csv(file) for file in files]
demo_all = pd.concat(df_list, ignore_index=True)

demo_all.to_csv("Demographic_All.csv", index=False)

print("Demographic CSVs combined successfully")
# Path to demographic CSV files
