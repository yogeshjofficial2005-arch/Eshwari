# 🌾 Seasonal Agriculture Performance Analysis

**A data analytics deep-dive into how Kharif, Rabi, and Zaid seasons shape crop yield, profitability, and risk across Indian farms.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=flat-square&logo=pandas&logoColor=white)
![Analysis](https://img.shields.io/badge/Type-Data%20Analytics-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1gErVQxHGK6gqEwsUsbv60IHult9-lDRI?usp=sharing)

---

## 📖 Overview

Agricultural performance is inherently seasonal — success hinges on a complex interplay of **environmental conditions** (rainfall, temperature), **resource management** (irrigation, fertilizer usage), and **market dynamics** (profit, pricing). This project goes beyond generic summary statistics to uncover *how and why* performance varies across the **Kharif**, **Rabi**, and **Zaid** growing seasons.

By integrating environmental, operational, and financial data, the analysis surfaces actionable, season-specific insights rather than one-size-fits-all conclusions.

### 🔑 Headline Findings

| Season | Key Insight |
|--------|-------------|
| 🌧️ **Kharif** | Benefits from higher rainfall, driving stronger yields — but comes with **elevated pest and disease risk** |
| ❄️ **Rabi** | Yields are **highly dependent on irrigation efficiency** rather than rainfall |
| ☀️ **Zaid** | A shorter, resource-intensive window analyzed for volatility and consistency across crops and states |

---

## ❓ Key Analytical Questions

This project was framed around eight core questions:

1. Does `Yield_Tonnes_Ha` differ significantly across seasons — and for which crops is the effect largest?
2. How do `Rainfall_mm`, `Avg_Temperature`, and `Soil_Moisture_pct` vary by season, and how do they correlate with yield?
3. Which **irrigation method** is most water-efficient (`Water_Efficiency`) per season?
4. How does `Profit_INR` and profit margin vary by season and crop?
5. Do fertilizer/pesticide usage intensities differ by season, and do they correlate with yield or disease risk?
6. Which states/crops show **consistent seasonal advantage** vs. **high seasonal volatility**?
7. Is `Disease_Pest_Risk_pct` associated with season, humidity, or irrigation method?
8. Are there **outlier farms** (unusually high/low profit or yield), and what characterizes them?

---

## 🛠️ Project Workflow

The analysis follows a structured, end-to-end data analytics pipeline:

```
┌────────────────────┐     ┌──────────────────────┐     ┌───────────────────┐
│  Data Extraction    │ ──▶ │  Cleaning &           │ ──▶ │  Core / Univariate │
│  & Cleaning         │     │  Preparation          │     │  Analysis          │
└────────────────────┘     └──────────────────────┘     └───────────────────┘
                                                                    │
                                                                    ▼
┌────────────────────┐     ┌──────────────────────┐     ┌───────────────────┐
│  Anomaly Detection  │ ◀── │  Cross-Dimension &    │ ◀── │  Relationship &    │
│  & Analysis         │     │  Relationship Analysis│     │  Driver Analysis   │
└────────────────────┘     └──────────────────────┘     └───────────────────┘
```

---

## 📂 Repository Structure

| File | Description |
|------|-------------|
| 📄 `Project Introduction.txt` | Problem framing, objectives, and the guiding analytical questions |
| 🧹 `Data Extracted & Cleaned.py` | Initial data extraction and cleaning routines |
| 🧼 `DataCleaning & Preperation.py` | Further preprocessing, feature preparation, and data quality checks |
| 📊 `CoreAnalysis.py` | Core statistical summaries and foundational metrics |
| 📈 `UnivariateAnalysis.py` | Distribution analysis of individual variables (yield, rainfall, temperature, etc.) |
| 🔗 `Relationship&DriverAnalysis.py` | Correlation and driver analysis linking environmental/operational factors to yield & profit |
| 🧭 `CrossDimension&RelationshipAnalysis.py` | Multi-dimensional cross-analysis (season × crop × state × irrigation) |
| 🚨 `AnamolyDetection.py` | Detection of outlier farms based on yield and profit metrics |
| 🔍 `AnamolyAnalysis.py` | Deeper investigation into what characterizes the detected anomalies |
| 📘 `README.md` | You're here! |

---

## 📊 Dataset Dimensions

The analysis integrates data across three key dimensions:

- **🌦️ Environmental** — Rainfall, average temperature, soil moisture, humidity
- **⚙️ Operational** — Irrigation method & efficiency, fertilizer/pesticide usage, disease & pest risk
- **💰 Financial** — Profit (INR), profit margin, yield (tonnes/hectare)

Sliced across **season** (Kharif / Rabi / Zaid), **crop**, and **state**.

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scipy
```

### Run Locally
```bash
git clone https://github.com/Yogesh-CyberSapien/Yogesh-Vois-Project.git
cd Yogesh-Vois-Project

# Run the pipeline in order
python "Data Extracted & Cleaned.py"
python "DataCleaning & Preperation.py"
python CoreAnalysis.py
python UnivariateAnalysis.py
python "Relationship&DriverAnalysis.py"
python "CrossDimension&RelationshipAnalysis.py"
python AnamolyDetection.py
python AnamolyAnalysis.py
```

### Or Run in the Cloud
No setup needed — explore the full analysis interactively in Google Colab:

👉 **[Open the Notebook in Colab](https://colab.research.google.com/drive/1gErVQxHGK6gqEwsUsbv60IHult9-lDRI?usp=sharing)**

---

## 🧠 Tech Stack

- **Language:** Python
- **Data Handling:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Environment:** Google Colab / Jupyter

---

## 🎯 Conclusion

Seasonal agricultural performance cannot be explained by a single factor — it's the *interaction* of rainfall, irrigation, pest pressure, and market conditions that determines outcomes. This project demonstrates that:

- **Kharif** success is a rainfall story shadowed by pest risk.
- **Rabi** success is an irrigation-efficiency story.
- Outlier farms and cross-dimensional patterns reveal where targeted interventions (better irrigation tech, pest management, or crop selection) could unlock the greatest gains.

---

## 👤 Author

**Yogesh** — [@Yogesh-CyberSapien](https://github.com/Yogesh-CyberSapien)

*Built as part of a Data Analytics major project.*

---

## 📜 License

This project is available under the [MIT License](LICENSE).

---

<p align="center">⭐ If you found this analysis useful, consider starring the repo!</p>
