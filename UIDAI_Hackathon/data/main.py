import pandas as pd
import glob

enrol = pd.read_csv("Enrolment_All.csv")
demo = pd.read_csv("Demographic_All.csv")
bio = pd.read_csv("Biometric_All.csv")

for df in [enrol, demo, bio]:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Year'] = df['Date'].dt.year
    
# Now enrol, demo, and bio DataFrames have a 'Year' column extracted from 'Date'
bins = [0, 5, 18, 30, 45, 60, 100]
labels = ['0-5', '6-18', '19-30', '31-45', '46-60', '60+']

for df in [enrol, demo, bio]:
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

enrol_age = enrol.groupby('Age_Group')['Count'].sum().reset_index()
enrol_age

demo_age = demo.groupby('Age_Group')['Count'].sum().reset_index()
demo_age

bio_age = bio.groupby('Age_Group')['Count'].sum().reset_index()
bio_age

final_compare = pd.merge(enrol_age, demo_age, on='Age_Group', how='outer', suffixes=('_Enrol', '_Demo'))
final_compare = pd.merge(final_compare, bio_age, on='Age_Group', how='outer')
final_compare.rename(columns={'Count': 'Biometric_Update'}, inplace=True)

final_compare

demo['Year'] = demo['Date'].dt.year
yearly_updates = demo.groupby('Year')['Count'].sum().reset_index()
yearly_updates
yearly_updates.rename(columns={'Count': 'Demographic_Updates'}, inplace=True)
final_compare = pd.merge(final_compare, yearly_updates, on='Year', how='left')
final_compare
final_compare.to_csv("Final_Comparison.csv", index=False)
print("Final comparison saved successfully")

print(final_compare)


#save final_compare to CSV


