# 🌾 Seasonal Agriculture Performance Analysis

> **VOIS AICTE Batch 1 (2026–2027) — Major Project: Data Analytics**

A data analytics project that investigates how agricultural performance — yield, profitability, resource usage and risk — varies across India's **Kharif, Rabi, and Zaid** growing seasons, using statistical testing and visualization to uncover actionable, evidence-based insights.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Dataset](#-dataset)
- [Key Analytical Questions](#-key-analytical-questions)
- [Project Workflow](#-project-workflow)
- [Tech Stack](#-tech-stack)
- [Installation & Usage](#-installation--usage)
- [Key Findings](#-key-findings)
- [Recommendations](#-recommendations)
- [Limitations](#-limitations)
- [Future Scope](#-future-scope)
- [Project Structure](#-project-structure)
- [Author](#-author)

---

## 🔍 Overview

Agricultural output doesn't behave uniformly across the year — it is shaped by rainfall, temperature, soil conditions, irrigation strategy, and input costs, all of which shift with the season. This project moves beyond a generic exploratory analysis of the dataset and instead **frames a focused, real-world problem**: understanding *how and why* agricultural performance differs across seasons, and what that means for planning and resource allocation.

The complete analysis — from raw data extraction to final recommendations — is documented in a single, well-structured Jupyter Notebook (`Vois.ipynb`).

## 🎯 Problem Statement

Agricultural activities are influenced by seasonal variations in environmental conditions, farming practices, resource availability, and market conditions — yet raw agricultural data does not, on its own, reveal how performance changes across seasons. This project analyzes the given dataset to identify meaningful **patterns, trends, relationships, and variations** in agricultural performance across seasons, supporting evidence-based agricultural planning.

## 📊 Dataset

The source data is provided as a **PDF** (`Vois_input_1.pdf` / referenced in-notebook as `vois input 3.pdf`) and is programmatically extracted into a structured DataFrame using `pdfplumber`.

Each record (one row per farm) includes:

| Category | Fields |
|---|---|
| **Identifiers** | `Farm_ID`, `Season`, `Crop` |
| **Environmental** | `Rainfall_mm`, `Avg_Temperature`, `Humidity_pct`, `Sunlight_Hours`, `Soil_pH`, `Soil_Moisture_pct` |
| **Farming Inputs** | `Farm_Area_Hectares`, `Nitrogen_kg_ha`, `Phosphorus_kg_ha`, `Potassium_kg_ha`, `Fertilizer_kg_ha`, `Pesticide_Litre_ha`, `Seed_Quality_Score`, `Irrigation_Method` |
| **Resource Usage** | `Water_Used_m3`, `Water_Efficiency` |
| **Outcomes** | `Yield_Tonnes_Ha`, `Production_Tonnes`, `Disease_Pest_Risk_pct` |
| **Economics** | `Market_Price_INR`, `Total_Cost_INR`, `Revenue_INR`, `Profit_INR` |

> Raw column headers extracted from the PDF are malformed/truncated (a common PDF-table-extraction artifact). The notebook includes a dedicated **cleaning and standardization step** that maps these to consistent, analysis-ready column names before any analysis begins.

## ❓ Key Analytical Questions

The notebook is driven by a set of self-defined research questions rather than an unfocused exploration:

1. Does `Yield_Tonnes_Ha` differ significantly across seasons, and for which crops is the effect largest?
2. How do `Rainfall_mm`, `Avg_Temperature`, and `Soil_Moisture_pct` vary by season, and how do they correlate with yield?
3. Which irrigation method is most water-efficient (`Water_Efficiency`) per season?
4. How does `Profit_INR` and profit margin vary by season and crop?
5. Do fertilizer/pesticide usage intensities differ by season, and do they correlate with yield or disease risk?
6. Which states/crops show a consistent seasonal advantage vs. high seasonal volatility?
7. Is `Disease_Pest_Risk_pct` associated with season, humidity, or irrigation method?
8. Are there outlier farms (unusually high/low profit or yield), and what characterizes them?

## 🧭 Project Workflow

The notebook follows a structured, end-to-end analytics pipeline:

1. **Introduction & Problem Framing** — context and guiding questions
2. **Data Extraction** — parsing tabular data out of the source PDF with `pdfplumber`
3. **Data Cleaning & Preparation** — duplicate checks, missing-value audit, column standardization, type coercion
4. **Univariate Analysis** — distribution of yield/profit, category frequency counts (season, irrigation method)
5. **Seasonal Comparison (Core Analysis)** — boxplots + **one-way ANOVA** to test for statistically significant seasonal differences in yield
6. **Cross-Dimensional & Relationship Analysis** — Crop × Season yield heatmap, full numerical correlation heatmap
7. **Relationship & Driver Analysis** — rainfall-vs-yield regression plots by season, linear regression on environmental drivers
8. **Anomaly / Unusual Pattern Detection** — rule-based flagging of "high cost, low yield" inefficient farms
9. **Key Findings & Recommendations**
10. **Outlier Detection** — Z-score based statistical outlier identification on yield & profit
11. **Conclusion & Future Scope**

## 🛠 Tech Stack

| Purpose | Library |
|---|---|
| Data manipulation | `pandas`, `numpy` |
| PDF data extraction | `pdfplumber` |
| Visualization | `matplotlib`, `seaborn` |
| Statistical testing | `scipy.stats`, `statsmodels` (ANOVA, Tukey HSD) |
| Modeling | `scikit-learn` (Linear Regression) |

## 🚀 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/<your-username>/seasonal-agriculture-performance-analysis.git
cd seasonal-agriculture-performance-analysis

# (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install pandas numpy matplotlib seaborn scipy statsmodels scikit-learn pdfplumber jupyter
```

**Run the notebook:**

```bash
jupyter notebook Vois.ipynb
```

> ⚠️ Update the `pdf_path` variable in the data-extraction cell to point to your local copy of the input PDF (e.g. `Vois_input_1.pdf`) before running.

## 📈 Key Findings

- **Seasonal Productivity:** Kharif yields are significantly higher than Zaid, largely due to rainfall dependency.
- **Profitability Drivers:** Fertilizer intensity shows a positive correlation with yield, but diminishing returns appear in high-input zones.
- **Irrigation Efficiency:** Sprinkler and Drip irrigation consistently show higher water efficiency during Rabi season compared to flood irrigation.
- **Risk Management:** Farms with high humidity in the Kharif season show a marked increase in disease/pest risk.

## ✅ Recommendations

- Transition towards Drip/Sprinkler irrigation systems in Zaid/Rabi seasons to optimize limited water resources.
- Implement early pest-detection protocols for high-humidity crops during the Kharif season.
- Adjust fertilizer application rates based on soil moisture levels to prevent runoff and maximize efficiency.

## ⚠️ Limitations

- The analysis assumes local rainfall data is representative of farm-level conditions.
- Market prices are treated as static per record, though they fluctuate daily in practice.

## 🔮 Future Scope

- Integration of satellite imagery for real-time soil moisture monitoring.
- Predictive modeling for market-price forecasting to optimize crop selection, particularly for the Zaid season.

## 📁 Project Structure

```
├── Vois.ipynb              # Main analysis notebook (end-to-end pipeline)
├── Vois_input_1.pdf         # Source dataset (agricultural records, PDF table format)
└── README.md                 # Project documentation
```

## 👤 Author

Prepared as part of the **VOIS AICTE Batch 1 (2026–2027)** Data Analytics major project.

---

⭐ If you found this project useful or interesting, consider starring the repo!
