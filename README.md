# PriceOptima – Dynamic Pricing System
## Milestone 1: KPI Definition • Dataset Preparation • Preprocessing
### 1. Project Overview

PriceOptima is a dynamic pricing system designed to optimize product prices using sales, cost, and inventory data.


### 2. KPI Definitions
#### A. Revenue Lift

Measures: Increase or decrease in revenue after dynamic pricing.

custom_sales["Dynamic Price"] = custom_sales["Price"] * 0.88
custom_sales["New Revenue"] = custom_sales["Dynamic Price"] * custom_sales["Units Sold"]


Why important: Shows pricing impact on revenue.

### B. Profit Margin Improvement

Measures: Change in profit before vs after pricing.

custom_sales["Original Profit"] = custom_sales["Revenue"] - (custom_sales["Cost Price"] * custom_sales["Units Sold"])
custom_sales["New Profit"] = custom_sales["New Revenue"] - (custom_sales["Cost Price"] * custom_sales["Units Sold"])


Why important: Ensures profitability increases.

### C. Inventory Impact

Measures: How pricing affects stock consumption.

Checked in code:

Stock levels validated

No negative inventory

Why important: Helps reduce excess stock faster.

### 3. Dataset Used — Custom Walmart Sales Dataset

This project uses a combined custom dataset with:

Sales Data Columns

Date

Product_ID

Product_Name

Category

Price

Units_Sold

Revenue

Inventory Data Columns

Stock_Level

Restock_Date

Warehouse_ID

Product Master Data

Cost_Price

Dataset loaded using:

custom_sales = pd.read_csv("custom_sales.csv")

### 4. Why This Dataset Was Chosen
 Contains required fields for pricing
 Reflects real-world retail
 Supports revenue & profit KPIs
 Suitable for ML in future
 Combines product + cost + inventory
###  5. Dataset Validation Summary

notebook performs:

 Missing Value Check
custom_sales.isnull().sum()

Duplicate Removal
 Data Type Verification
custom_sales.dtypes

 Logical Validations

Revenue = Price × Units Sold

Units Sold > 0

Price > 0

Stock not negative

 Statistical Summary
custom_sales.describe()

### 6. Preprocessing Performed
 Missing values cleaned
 Duplicates removed
 Numeric fields validated
 Standardized column values
 Date column converted
custom_sales["Date"] = pd.to_datetime(custom_sales["Date"])

 Dynamic Price column added
 New Revenue calculated
 Original & New Profit calculated
 KPI improvement metrics created
### 7. KPI Calculations in Notebook

Dynamic Price

New Revenue

Original Profit

New Profit

Revenue Difference

Profit Difference

### 8. Conclusion
The Custom Walmart Sales Dataset is clean, validated, and ready for dynamic pricing analysis.
All KPIs needed for Milestone 1 are implemented and prepared for future ML modeling.

# PriceOptima – Feature Engineering & Dynamic Pricing

## Project Overview
This notebook implements the **Feature Engineering phase** of the **PriceOptima Dynamic Pricing Project**.  
The objective of this stage is to transform raw customs sales data into a **model-ready dataset** by capturing demand patterns, pricing behavior, seasonality, inventory conditions, competitor influence, and profitability.

The output of this notebook is a fully engineered dataset that can be directly used for **machine learning models** and **dynamic pricing analysis**.

---

## Dataset Description
The dataset contains historical sales and operational data with the following key columns:

- `Date`
- `Product ID`
- `Units Sold`
- `Price`
- `Revenue`
- `Cost Price`
- `Stock Level`
- `Warehouse/Store ID`
- `Competitor Price`
- `Competitor Name`
- (Optional) `Category`

---

## Feature Engineering Steps Performed

### 1. Time-Based Features
Extracted features to capture seasonality and weekly demand patterns:
- Year
- Month
- Day
- Weekday
- Weekend flag
- Season (Winter, Summer, Monsoon, Festive)
- Festival/Holiday indicator

---

### 2. Demand Features (Lag & Rolling)
Created features to understand historical demand trends:
- Lag sales (1-day, 7-day, 30-day)
- Rolling averages (7-day, 30-day)
- Demand volatility (rolling standard deviation)

---

### 3. Price-Based Features
Engineered features to capture pricing behavior:
- Revenue per unit
- Price change percentage
- Lag price (previous day)
- Discount percentage

---

### 4. Price Elasticity
Calculated elasticity to understand how demand reacts to price changes:
- Elasticity value
- Elasticity classification (High / Medium / Low)

---

### 5. Competitor Features
Incorporated competitive pricing signals:
- Competitor price difference
- Competitor index
- Competitor cheaper indicator

---

### 6. Inventory Features
Added operational constraints and stock insights:
- Inventory ratio
- Days until stock-out
- Low stock indicator

---

### 7. Profit Features
Calculated profitability metrics:
- Total profit
- Profit per unit
- Profit margin percentage

---

### 8. Interaction Features
Created interaction terms to capture combined effects:
- Weekend × Price
- Season × Discount
- Inventory × Price

---

### 9. Categorical Encoding
Converted categorical variables into numerical format using one-hot encoding:
- Category (if available)

---

### 10. Dynamic Pricing Scenarios
Simulated multiple pricing strategies to evaluate business impact:

Price multipliers tested:
- 0.85 (−15%)
- 0.99 (−1%)
- 1.05 (+5%)
- 1.10 (+10%)
- 1.15 (+15%)

For each scenario, calculated:
- Predicted Price
- Predicted Revenue
- Revenue Lift (%)
- Predicted Profit
- Predicted Profit Margin (%)

---

### 11. Data Cleaning
Final preprocessing steps:
- Handled missing values
- Replaced infinite values
- Removed duplicates
- Exported clean dataset

---

## Output
- **Console Output:** Displays a preview of the engineered dataset (wrapped format is expected for wide tables).
- **Generated File:**  
  `customs_sales_features_DYNAMIC_FULL.csv`

# 📊 PriceOptima – Milestone 4  
## Baseline Rule-Based Pricing Engine

---

## 📌 Project Overview
This repository contains **Milestone 4** of the **PriceOptima Dynamic Pricing Project**.  
The objective of this milestone is to build a **baseline rule-based pricing engine** that adjusts product prices using **time-based** and **inventory-based** rules and compares the resulting revenue with **static pricing**.

This baseline system acts as a benchmark before implementing machine learning-based pricing models in later milestones.

---

## 🎯 Objective
Develop a pricing engine that:
- Applies **time-based pricing rules**
- Applies **inventory-based pricing rules**
- Generates a new **rule-based price**
- Compares **static vs rule-based revenue**
- Calculates **revenue uplift**

---

## 🧠 Pricing Strategy

### 1️⃣ Time-Based Pricing Rules
The following rules are applied based on time and demand patterns:

- Increase price on **weekends**
- Increase price during **festival / peak seasons**
- Apply a small increase during **month-end**
- Apply discounts during **low-demand months**

These rules simulate real-world seasonal and demand-driven pricing behavior.

---

### 2️⃣ Inventory-Based Pricing Rules
Prices are adjusted based on inventory levels:

- **Low inventory:** Increase price due to scarcity
- **Balanced inventory:** No price change
- **High inventory:** Apply moderate discount
- **Overstock:** Apply clearance pricing

These rules reflect practical retail inventory management strategies.

---

## 🛠️ Implementation Details

### Rule-Based Price Generation
- A new column called **`rule_price`** is created.
- The original price is copied and adjusted **sequentially** using:
  1. Inventory-based rules
  2. Time-based rules

This ensures logical and realistic price adjustments.

---

### Revenue Calculation
Two revenue metrics are calculated:

- **Static Revenue**
Static Revenue = Original Price × Units Sold


- **Rule-Based Revenue**
 Rule-Based Revenue = Rule Price × Units Sold


---

### Revenue Lift Calculation
Revenue uplift is calculated as:



Revenue Lift = Rule-Based Revenue − Static Revenue
Revenue Lift (%) = (Revenue Lift / Static Revenue) × 100

---

## 📈 Results
- Rule-based pricing dynamically adjusts prices based on demand and stock conditions.
- Revenue comparison demonstrates improvement over static pricing.
- The baseline engine provides a strong foundation for advanced pricing models.

# PriceOptima Dynamic Pricing Project  
## Milestone 5 – Advanced Model Development

## Objective
The objective of this milestone is to move from rule-based pricing to machine learning–driven dynamic pricing.  
Machine learning models are trained to predict demand and simulate dynamic prices. The performance of ML-based pricing is evaluated using historical backtesting and revenue lift analysis.

The goal is to demonstrate that ML-based pricing can outperform static or rule-based pricing, not to achieve maximum uplift.

---

## Dataset
- File Name: based_pricing.csv
- Source: Output from previous milestones
- Key Columns:
  - Date
  - Price
  - Units Sold
  - Stock Level
  - Revenue
  - Feature-engineered variables

---

## Data Preparation
- Dataset is sorted by Date
- Missing values are handled using forward fill and backward fill
- All categorical variables are encoded using LabelEncoder
- Dataset is used without dropping any rows

---

## Feature and Target Definition
- Target Variable (y):
  - Units Sold
- Input Features (X):
  - All columns except Units Sold, Revenue, and Date

---

## Train-Test Split
- A time-based split is applied
- 80% of historical data is used for training
- 20% of future data is used for testing
- No random shuffling is performed

---

## Machine Learning Models
Due to environment limitations, external libraries such as XGBoost and LightGBM were not used.

The following scikit-learn models were implemented:
- Gradient Boosting Regressor
- Random Forest Regressor

Both models are trained using default parameters to ensure simplicity and fairness.

---

## Model Evaluation
The models are evaluated using the following metrics:
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)

These metrics are used to measure demand prediction accuracy on the test dataset.

---

## ML-Based Dynamic Pricing Logic
- Demand is predicted using the trained ML model
- Average predicted demand is calculated
- Pricing strategy:
  - If predicted demand is above average, price is increased by 5%
  - If predicted demand is below or equal to average, price is decreased by 5%
- ML-based prices are stored in a new column called ML_Price
- Original prices are not modified

---

## Rule-Based Pricing Baseline
Rule-based pricing logic from Milestone 4 is recreated:
- Low stock level leads to a price increase
- High stock level leads to a price decrease
- Normal stock level keeps the price unchanged

A new column Rule_Based_Price is created for comparison.

---

## Backtesting
Backtesting is performed on the test dataset using three pricing strategies:
- Static Pricing
- Rule-Based Pricing
- ML-Based Pricing

Revenue is calculated using:
Revenue = Price × Units Sold

---

## Revenue Lift Calculation
Revenue lift is calculated using the formula:

Revenue Lift (%) =  
(ML Revenue − Static Revenue) / Static Revenue × 100

A positive revenue lift indicates improved performance of ML-based pricing.

---

## Outputs
- Model evaluation metrics (RMSE and MAE)
- ML-based simulated prices
- Backtesting revenue results
- Revenue comparison table
- Final revenue lift percentage

---

## Final Observations
- Machine learning models successfully learned demand patterns
- ML-based pricing outperformed static and rule-based pricing
- Time-based validation ensured realistic evaluation
- The objective of demonstrating ML-driven pricing effectiveness was achieved

  # AI PriceOptima – Dynamic Pricing Recommendation System

## Project Title
AI PriceOptima: Real-Time Dynamic Pricing Recommendation System

---

## Project Objective
The objective of this project is to build an AI-based pricing recommendation system that suggests an optimal product price based on key business factors such as cost, demand, inventory level, competitor pricing, and weekend impact.  
The system exposes the trained machine learning model through a FastAPI backend and visualizes predictions using a React.js dashboard.

---

## Dataset Description
The dataset used in this project contains historical pricing and sales-related information, including:
- Cost Price
- Competitor Price
- Demand / Conversion Rate
- Inventory Level
- Weekend Indicator
- Target variable: Optimal / Recommended Price

The dataset was preprocessed and used to train multiple models during Milestone 5, from which the best-performing model was selected.

---

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Joblib
- React.js
- HTML / CSS / JavaScript

---

## Model Development Summary
Multiple machine learning models were trained and evaluated during Milestone 5.  
The best-performing model was selected based on evaluation metrics and saved using `joblib` for reuse.  
The trained model predicts an optimal price based on provided input features.

---

## Backend Implementation (FastAPI)

### Step 1: Backend Preparation
- The trained model is loaded using `joblib`.
- A FastAPI application is created.
- An API endpoint `/predict` is exposed.
- The endpoint accepts inputs such as cost, demand, inventory level, competitor price, and weekend indicator.
- The API returns a recommended price as JSON output.

### Step 2: Backend Execution and Stability Check
- The FastAPI application is executed locally using `uvicorn`.
- All required dependencies are listed in `requirements.txt`.
- The API is tested using FastAPI Swagger UI (`/docs`).
- Successful responses with HTTP 200 status confirm stable execution.

### How to Run the Backend
pip install -r requirements.txt
uvicorn main:app --reload

Open Swagger UI:
http://127.0.0.1:8000/docs

###  Dashboard Implementation (React.js)

### Step 3: React Dashboard
A React.js dashboard is created to interact with the FastAPI backend.

The dashboard allows users to enter the following inputs:
- Cost Price  
- Competitor Price  
- Demand  
- Inventory Level  
- Weekend / Weekday indicator  

The dashboard sends user inputs to the FastAPI `/predict` endpoint.  
The predicted price returned by the API is displayed on the UI in real time.


---

### Dashboard Functionality (Short Explanation)
The React dashboard serves as a user interface for the pricing model.  
Users input pricing-related parameters, and the dashboard communicates with the FastAPI backend to retrieve a recommended price.  
This demonstrates real-time model inference and seamless backend–frontend integration.

---

### Deployment / Execution Approach
- Backend is executed locally using **FastAPI** and **Uvicorn**.  
- Frontend is executed locally using the **React development server**.  
- Docker is not used at this stage, as it is optional.  
- The system architecture is designed to support easy deployment in future stages.

---

### Key Outputs & Results
- Successful price prediction returned via the FastAPI API.  
- Swagger UI confirms stable backend execution.  
- React dashboard displays real-time recommended pricing.  
- End-to-end integration between the model, backend, and frontend is achieved.

## Screenshots

### FastAPI Swagger UI
![Swagger](swagger_ui_success.png.png)

### React Dashboard – Price Prediction
![Dashboard](dasboard_ui.png.png)
---

### Conclusion and Future Enhancements
This project successfully demonstrates an AI-driven pricing recommendation system with a scalable backend and an interactive dashboard.

### Future enhancements may include:
- Docker-based deployment  
- Cloud deployment (AWS / Azure)  
- Authentication and role-based access  
- Real-time data ingestion  
- Advanced pricing strategies and monitoring dashboards
