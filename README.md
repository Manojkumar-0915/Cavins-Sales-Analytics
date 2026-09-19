<div align="center">



\# 📊 Cavins Sales Analytics \& Demand Forecasting



\### 🚀 End-to-End Sales Analytics, Business Intelligence \& Demand Forecasting



<p>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white"/>

<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas\&logoColor=white"/>

<img src="https://img.shields.io/badge/NumPy-Analysis-013243?logo=numpy\&logoColor=white"/>

<img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikit-learn\&logoColor=white"/>

<img src="https://img.shields.io/badge/Statsmodels-Forecasting-4051B5"/>

<img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi\&logoColor=black"/>

<img src="https://img.shields.io/badge/DAX-Business%20Intelligence-00A4EF"/>

<img src="https://img.shields.io/badge/Excel-Dataset-217346?logo=microsoftexcel\&logoColor=white"/>

<img src="https://img.shields.io/badge/Git-GitHub-181717?logo=github\&logoColor=white"/>

</p>



</div>



\---



\## 📌 Project Overview



\*\*Cavins Sales Analytics \& Demand Forecasting\*\* is an end-to-end data analytics project focused on analyzing historical sales demand across products and districts, identifying recurring demand patterns, evaluating forecasting approaches, and presenting insights through an interactive Power BI dashboard.



The project combines \*\*Python-based data cleaning, exploratory analysis, forecasting, model evaluation, and Power BI visualization\*\* into one complete analytics workflow.



\---



\## 🎯 Business Objectives



\- 📦 Analyze product-wise demand

\- 📍 Compare demand across districts

\- 📅 Identify monthly and seasonal demand patterns

\- 📈 Understand historical demand trends

\- 🤖 Evaluate forecasting approaches

\- 🎯 Measure forecast accuracy

\- 📊 Build an interactive Power BI dashboard

\- 💡 Generate business-oriented insights



\---



\## 🔄 Project Workflow



```text

Excel Dataset

&#x20;     ↓

Python / Pandas

&#x20;     ↓

Data Cleaning \& Validation

&#x20;     ↓

Exploratory Data Analysis

&#x20;     ↓

Monthly Demand Aggregation

&#x20;     ↓

Forecasting Models

&#x20;     ↓

Model Evaluation

&#x20;     ↓

Power BI Dashboard

&#x20;     ↓

Business Insights

🛠️ Tech Stack

Category	Technologies

🐍 Programming	Python

📊 Data Analysis	Pandas, NumPy

🤖 Machine Learning	Scikit-learn

📈 Forecasting	Statsmodels

📗 Dataset	Microsoft Excel

📊 Visualization	Power BI

🧮 BI \& Calculations	DAX

🔧 Version Control	Git \& GitHub

📂 Dataset



Dataset: Cavins\_Complete\_Districtwise\_Sales.xlsx



Dataset Summary

Metric	Value

📌 Records	141,450

📦 Products	10

📍 Districts	15

📅 Start Date	2023-01-01

📅 End Date	2025-07-31

❌ Missing Values	0

🔁 Duplicate Rows	0

Dataset Columns

Product

District

order\_date

sold\_qty

Month

Year

🧹 Data Cleaning \& Validation



The dataset was processed using Python and Pandas.



Data Quality Checks

✅ Checked missing values

✅ Checked duplicate records

✅ Converted dates to datetime format

✅ Converted sales quantity to numeric

✅ Removed invalid/non-positive quantities

✅ Sorted records by date, product and district

✅ Validated product and district coverage

Final Dataset

Original Records : 141,450

Cleaned Records  : 141,450



The dataset passed the validation checks without losing records.



📊 Exploratory Data Analysis



The analysis focuses on product demand, district demand and monthly demand patterns.



📦 Product Analysis



The highest total demand products in the dataset include:



🥇 Cavin's Buttermilk

🥈 Cavin's Curd

🥉 Cavin's Lassi

Karthika Seeyakkai Powder

Cavin's Milkshake – Chocolate

📍 District Analysis



Demand was analyzed across all 15 districts.



Top aggregate-demand districts include:



Karur

Dindigul

Erode

Coimbatore

Kanchipuram

📅 Monthly Demand Pattern



The historical series shows a recurring monthly pattern:



February          ↓ Lower Demand

March–May         ↑ Higher Demand

June              → Moderate

July–September    ↓ Lower Demand

October–November  ↑ Higher Demand

December          ↓ Decline

🤖 Demand Forecasting



Three forecasting approaches were evaluated during the project.



1️⃣ Seasonal Naive



Uses the corresponding month from the previous year as the forecast.



2️⃣ Random Forest



A machine-learning experiment using temporal features such as:



Month

Year

Lag 1

Lag 2

Lag 12

Rolling 3-Month Demand

3️⃣ Holt-Winters



An Exponential Smoothing approach incorporating:



Trend

Seasonality

Historical demand

🧪 Evaluation Period



Models were evaluated on the 2025 January–July holdout period.



🏆 Forecasting Results

Model	MAE ↓	RMSE ↓	MAPE ↓

🌱 Seasonal Naive	1,188.00	1,774.10	1.11%

🌲 Random Forest	4,269.31	6,174.43	3.14%

📈 Holt-Winters	1,056.64	1,265.28	0.90%

📌 Result



On the 2025 Jan–Jul holdout period, Holt-Winters produced lower error than the tested Seasonal Naive baseline and Random Forest models.



⚠️ Forecast performance is specific to this dataset and evaluation period.



📊 Power BI Dashboard



The project contains a 3-page interactive Power BI dashboard.



🟦 1. Sales Overview



Includes:



Total Demand

Average Daily Demand

Total Products

Total Districts

Total Records

Monthly Demand Trend

Product Demand

District Demand

Year Filter

🟩 2. Product \& District Analysis



Includes:



Product Demand Ranking

District Demand Ranking

Product × District Matrix

Conditional Formatting

Product Filter

District Filter

🟪 3. Demand Forecasting



Includes:



Actual vs Forecast Demand

Holt-Winters Forecast

MAPE

MAE

RMSE

Forecast Model Comparison

🖼️ Dashboard Preview



🧮 Key DAX Measures

Total Demand

Total Demand =

SUM(cavins\_sales\_cleaned\[sold\_qty])

Average Daily Demand

Average Daily Demand =

AVERAGEX(

&#x20;   VALUES(cavins\_sales\_cleaned\[order\_date]),

&#x20;   \[Total Demand]

)

Total Products

Total Products =

DISTINCTCOUNT(cavins\_sales\_cleaned\[product])

Total Districts

Total Districts =

DISTINCTCOUNT(cavins\_sales\_cleaned\[district])

📁 Project Structure

Cavins-Sales-Analytics/

│

├── 📂 data/

│   ├── 📂 raw/

│   │   └── Cavins\_Complete\_Districtwise\_Sales.xlsx

│   │

│   └── 📂 processed/

│       ├── cavins\_sales\_cleaned.csv

│       ├── product\_performance.csv

│       ├── district\_performance.csv

│       ├── monthly\_sales.csv

│       ├── yearly\_sales.csv

│       ├── product\_district\_performance.csv

│       ├── forecast\_comparison.csv

│       └── forecast\_metrics.csv

│

├── 📂 src/

│   ├── data\_cleaning.py

│   ├── analysis.py

│   └── forecasting.py

│

├── 📂 Power BI/

│   └── Cavins-Sales-Analytics.pbix

│

├── requirements.txt

├── .gitignore

└── README.md

🚀 How to Run

1️⃣ Clone the Repository

git clone https://github.com/Manojkumar-0915/Cavins-Sales-Analytics.git

2️⃣ Navigate to the Project

cd Cavins-Sales-Analytics

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run Data Cleaning

python src/data\_cleaning.py

5️⃣ Run Analysis

python src/analysis.py

6️⃣ Run Forecasting

python src/forecasting.py

7️⃣ Open Power BI

Power BI/Cavins-Sales-Analytics.pbix

💡 Key Insights

📦 Cavin's Buttermilk recorded the highest aggregate demand among the products.

📍 Karur recorded the highest aggregate demand among the districts.

📅 The dataset shows a recurring seasonal demand pattern.

📈 Demand generally increases during March–May and October–November.

🤖 Holt-Winters achieved a 0.90% MAPE on the selected 2025 Jan–Jul holdout period.

⚠️ Project Limitations

The dataset contains sales quantity only; revenue and profit analysis are not available.

2025 data is available only through July 2025.

Forecasting evaluation uses a 2025 Jan–Jul holdout period.

Forecast performance may change with future data.

The structured recurring pattern in the dataset should be considered when interpreting model performance.

🔮 Future Improvements

📡 Automated data ingestion

💰 Revenue and pricing analysis

📦 Inventory and stock-level analysis

🌦️ External demand drivers such as weather

🤖 Additional forecasting models

⚙️ Automated forecasting pipeline

☁️ Cloud deployment

👨‍💻 Author

Manoj Kumar M



🎓 B.E. Computer Science \& Engineering



📊 Data Analyst | Data Analytics | Business Intelligence



🔗 Connect With Me

📱9629633830

📧 manojmottai3@gmail.com





**⭐ If you found this project useful, consider giving it a star!**



Built with 🐍 Python • 📊 Power BI • 📈 Data Analytics





