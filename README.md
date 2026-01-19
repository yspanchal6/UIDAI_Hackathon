# UIDAI Aadhaar Lifecycle Service Demand Analysis

## 🔍 Project Summary
A data analytics project that explores **Aadhaar enrolment and update demand across lifecycle stages, regions, and time**.  
The project demonstrates **Exploratory Data Analysis (EDA), data aggregation, visualization readiness, and policy-oriented insights**—without unnecessary ML complexity.

**Outcome:** Insight-ready datasets and visuals that support **service planning and infrastructure decisions**.

---

## 🎯 Business / Policy Problem
**Integrated Analysis of Aadhaar Enrolment and Update Patterns to Assess Lifecycle-Based Service Demand**

Aadhaar usage evolves from **initial enrolment** to **recurring demographic and biometric updates**.  
Understanding *when*, *where*, and *why* these services are demanded helps optimize **centers, staffing, and outreach**.

---

## 🧠 What I Did (EDA Scope)
- Cleaned and standardized UIDAI-style datasets
- Engineered **lifecycle age groups**
- Aggregated service demand (enrolment vs updates)
- Analyzed **regional concentration** (state & city)
- Identified **time trends** (biometric updates)
- Produced **visualization-ready CSVs**

> Focused on interpretability and decision-making rather than black-box ML.

---

## 📦 Datasets Used
| Dataset | Description |
|---|---|
| `Enrolment_All.csv` | New Aadhaar enrolments |
| `Demographic_All.csv` | Demographic updates (address/phone/name) |
| `Biometric_All.csv` | Biometric updates (fingerprint/iris) |

---

## 📊 Final Output Files (Deliverables)
| File | Purpose |
|---|---|
| `Lifecycle_Service_Demand.csv` | Lifecycle-wise enrolment & update demand |
| `State_Wise_Update_Demand.csv` | State-level update concentration |
| `State_City_Wise_Update_Demand.csv` | City-level service hotspots |
| `Biometric_Update_Trend.csv` | Time-series trend of biometric updates |

These files are **directly usable** for dashboards, charts, and reports.

---

## 📈 Visualizations (Examples)
- **Stacked Bar:** Lifecycle-based service demand
- **Horizontal Bar:** Top states by update load
- **Line Chart:** Year-wise biometric update trend
- **City Drill-down:** Urban demand hotspots

---

## 💡 Key Insights
- Enrolments peak at **early ages (0–5)**; updates dominate **working ages (19–45)**.
- **Biometric updates** are prominent among **youth and seniors**.
- Update demand is **regionally skewed**—few states/cities drive most load.
- Biometric updates show a **consistent upward trend** over time.

---

## 🏛 Recommendations
- Shift capacity from enrolment-heavy to **update-focused centers**.
- Allocate resources **regionally**, not uniformly.
- Plan **biometric camps** for schools and senior citizens.
- Use lifecycle demand for **proactive planning**.

---

## 🛠 Tools
- **Python (Pandas)** – Data cleaning & aggregation
- **Excel / BI tools** – Visualization
- **GitHub** – Version control

---

## 📁 Project Structure

```
UIDAI_Hackathon/
│
|
├── analysis/             # Python analysis (YOU handle)
│   └── uidai_lifecycle_analysis.py
│
│
├── assets/               # Final charts (PNG/JPG)
|   ├── Demand/
|   |   ├── by-age-Group.png
|   |   ├── Top-10-Cities by Aadhaar Update.png
|   |   └── top10-State_Wise_Update_Demand.png
|   |
│   ├── Enrol vs Update by age group.png
│   ├── lifecycle_chart.png
|   ├── Share_of_Aadhaar_Update-Top-10 States.png
│   └── yearly_trend.png
│
│
│
├── dataset/                 # Raw UIDAI datasets (READ ONLY)
|   |
│   ├── analysis_outputs/       # Cleaned & aggregated CSVs
|   |   |
|   |   ├── Biometric_Update_Trend.csv
|   |   ├── Lifecycle_Service_Demand.csv
|   |   ├── State_City_Wise_Update_Demand.csv
|   |   └── State_Wise_Update_Demand.csv
|   |
|   |
│   ├── marge_data/
|   |   |
|   |   ├── Biometric_All.csv
|   |   ├── Biometric_Update.py
|   |   ├── Demographic_All.csv
|   |   ├── Demographic.py
|   |   ├── Enrolment_All.csv
|   |   └── Enrolment.py
|   |   
|   |
│   └── row_data/
|       ├── State_City_Wise_Update_Demand.csv
|       |   ├── api_data_aadhar_biometric_0_500000.csv
|       |   ├── api_data_aadhar_biometric_500000_1000000.csv
|       |   ├── api_data_aadhar_biometric_1500000_1861108.csv
|       |   └── api_data_aadhar_biometric_1500000_1861108.csv
|       |   
|       |
|       ├── Demographic_Update/
|       |   ├── api_data_aadhar_demographic_500000_1000000.csv
|       |   ├── api_data_aadhar_demographic_500000_1000000.csv
|       |   ├── api_data_aadhar_demographic_1000000_1500000.csv
|       |   ├── api_data_aadhar_demographic_1500000_2000000.csv
|       |   └── api_data_aadhar_demographic_2000000_2071700.csv
|       |
|       └── Enrolment/
|           ├── api_data_aadhar_enrolment_0_500000.csv
|           ├── api_data_aadhar_enrolment_1000000_1006029.csv
|           └── api_data_aadhar_enrolment_1000000_1006029.csv
|           
│
│
├── final_pdf/            # Final submission
|   |
│   └── UIDAI_Hackathon_Final_Report.pdf
│
├── requirements.txt              # Python dependencies
├── .gitignore
└── README.md
```
---

## 👤 Role
**Data Analyst & Team Leader**
- Designed EDA methodology
- Built lifecycle datasets
- Coordinated visualization & reporting

---

## 📄 License
Educational / hackathon use only.
