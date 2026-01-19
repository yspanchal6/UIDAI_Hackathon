# ============================================================
# UIDAI HACKATHON – LIFECYCLE BASED DATA ANALYSIS
# Focus:
# - Data Analysis
# - Lifecycle-based Service Demand
# - Output for Visualization & PDF
# ============================================================

import pandas as pd
from pathlib import Path

# ------------------------------------------------------------
# 1. PROJECT ROOT & DATA PATHS
# ------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "dataset" / "marge_data"
OUTPUT_DIR = BASE_DIR / "dataset" / "analysis_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# ------------------------------------------------------------
# 2. LOAD DATA
# ------------------------------------------------------------
enrol = pd.read_csv(DATA_DIR / "Enrolment_All.csv")
demo  = pd.read_csv(DATA_DIR / "Demographic_All.csv")
bio   = pd.read_csv(DATA_DIR / "Biometric_All.csv")

# ------------------------------------------------------------
# 3. CLEAN COLUMN NAMES
# ------------------------------------------------------------
def clean_columns(df):
    df.columns = df.columns.str.strip().str.lower()
    return df

enrol = clean_columns(enrol)
demo  = clean_columns(demo)
bio   = clean_columns(bio)

# ------------------------------------------------------------
# 4. DATE PARSING & YEAR EXTRACTION
# ------------------------------------------------------------
for df in [enrol, demo, bio]:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year'] = df['date'].dt.year

# ------------------------------------------------------------
# 5. NORMALIZE ENROLMENT AGE DATA (WIDE → LONG)
# ------------------------------------------------------------
enrol_long = enrol.melt(
    id_vars=['date', 'year', 'state', 'district', 'pincode'],
    value_vars=['age_0_5', 'age_5_17', 'age_18_greater'],
    var_name='age_group',
    value_name='count'
)

enrol_long['age_group'] = enrol_long['age_group'].replace({
    'age_0_5': '0-5',
    'age_5_17': '6-18',
    'age_18_greater': '18+'
})

# ------------------------------------------------------------
# 6. NORMALIZE DEMOGRAPHIC UPDATE DATA
# ------------------------------------------------------------
demo_long = demo.melt(
    id_vars=['date', 'year', 'state', 'district', 'pincode'],
    value_vars=['demo_age_5_17', 'demo_age_17_'],
    var_name='age_group',
    value_name='count'
)

demo_long['age_group'] = demo_long['age_group'].replace({
    'demo_age_5_17': '6-18',
    'demo_age_17_': '18+'
})

# ------------------------------------------------------------
# 7. NORMALIZE BIOMETRIC UPDATE DATA
# ------------------------------------------------------------
bio_long = bio.melt(
    id_vars=['date', 'year', 'state', 'district', 'pincode'],
    value_vars=['bio_age_5_17', 'bio_age_17_'],
    var_name='age_group',
    value_name='count'
)

bio_long['age_group'] = bio_long['age_group'].replace({
    'bio_age_5_17': '6-18',
    'bio_age_17_': '18+'
})

# ------------------------------------------------------------
# 8. LIFECYCLE-BASED SERVICE DEMAND
# ------------------------------------------------------------
lifecycle_demand = pd.DataFrame({
    "age_group": ["0-5", "5-17", "18+"],

    "new_enrolments": [
        enrol_long.loc[enrol_long["age_group"] == "0-5", "count"].sum(),
        enrol_long.loc[enrol_long["age_group"] == "5-17", "count"].sum(),
        enrol_long.loc[enrol_long["age_group"] == "18+", "count"].sum(),
    ],

    "demographic_updates": [
        0,
        # demo_long.loc[demo_long["age_group"] == "0-5", "count"].sum(),
        demo_long.loc[demo_long["age_group"] == "5-17", "count"].sum(),
        demo_long.loc[demo_long["age_group"] == "18+", "count"].sum()
    ],

    "biometric_updates": [
        0,
        # bio_long.loc[bio_long["age_group"] == "0-5", "count"].sum(),
        bio_long.loc[bio_long["age_group"] == "5-17", "count"].sum(),
        bio_long.loc[bio_long["age_group"] == "18+", "count"].sum()
    ]
})

# ------------------------------------------------------------
# 9. STATE-WISE UPDATE DEMAND
# ------------------------------------------------------------
state_update_demand = (
    demo_long.groupby('state')['count']
    .sum()
    .reset_index()
    .rename(columns={'count': 'total_updates'})
    .sort_values(by='total_updates', ascending=False)
)


# ------------------------------------------------------------
# 10. YEAR-WISE BIOMETRIC UPDATE TREND (NEW)
# ------------------------------------------------------------
biometric_update_trend = (
    bio_long.groupby('year')['count']
    .sum()
    .reset_index()
    .rename(columns={'count': 'total_biometric_updates'})
)

# ------------------------------------------------------------
# 11. STATE + CITY (DISTRICT) WISE UPDATE DEMAND
# ------------------------------------------------------------

state_city_update_demand = (
    demo_long
    .groupby(['state', 'district'])['count']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
# ------------------------------------------------------------
# 12. EXPORT OUTPUT FILES
# ------------------------------------------------------------
lifecycle_demand.to_csv(
    OUTPUT_DIR / "Lifecycle_Service_Demand.csv", index=False
)
state_update_demand.to_csv(
    OUTPUT_DIR / "State_Wise_Update_Demand.csv", index=False
)

state_city_update_demand.to_csv(
    OUTPUT_DIR / "State_City_Wise_Update_Demand.csv", index=False
)

biometric_update_trend.to_csv(
    OUTPUT_DIR / "Biometric_Update_Trend.csv", index=False
    )


# ------------------------------------------------------------
# 13. SUMMARY
# ------------------------------------------------------------
print("✅ UIDAI Lifecycle Data Analysis Completed Successfully\n")

print("Lifecycle-Based Service Demand:")
print(lifecycle_demand)

print("\nTop 10 States by Update Demand:")
print(state_update_demand.head(10))

print("\nYear-wise Aadhaar Update Trend:")
print(biometric_update_trend)

print("\nTop 10 State + City (District) by Update Demand:")
print(state_city_update_demand.head(10))