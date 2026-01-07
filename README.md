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

# 🧠 Feature Engineering – PriceOptima Dynamic Pricing Project

## 📌 Overview
This milestone focuses on **Feature Engineering**, a critical step in the PriceOptima Dynamic Pricing Project.  
The objective of this phase is to transform raw data into **meaningful, structured, and model-ready features** that help capture:

- Demand behavior
- Pricing trends
- Seasonality & time effects
- Inventory conditions
- Competitive influence
- Profitability impact

All required feature engineering tasks have been successfully implemented.

---

## 🎯 Objective
- Enhance raw data with informative features
- Improve model understanding of real-world pricing dynamics
- Prepare a clean, structured dataset for modeling and deployment

---

## 🧩 Feature Engineering Tasks Completed

---

## 1️⃣ Time-Based Features
To capture seasonality and temporal demand patterns, the following features were created:

- Day
- Month
- Year
- Day of Week
- Weekend Indicator
- Season (e.g., Summer / Monsoon / Winter)
- Festival / Holiday Indicator

These features help identify demand fluctuations over time.

---

## 2️⃣ Price-Based Features
To model pricing behavior and changes:

- Lag Price (Previous Day)
- Lag Price (7-Day)
- Price Change Percentage
- Discount Percentage

These features allow the model to understand short-term price movements and discount effects.

---

## 3️⃣ Demand Features (Lag & Rolling)
To capture demand trends and variability:

- Lag Sales (1-Day, 7-Day, 30-Day)
- Rolling Average Sales (7-Day, 30-Day)
- Demand Volatility (Standard Deviation of Sales)

These features help model momentum, seasonality, and uncertainty in demand.

---

## 4️⃣ Price Elasticity Features
To understand customer sensitivity to price changes:

- Price Elasticity Calculation
- Elasticity Classification:
  - High Elasticity
  - Medium Elasticity
  - Low Elasticity

This enables differentiated pricing strategies across products.

---

## 5️⃣ Competitor Features (Where Available)
To incorporate market competition:

- Competitor Price Difference
- Competitor Price Index
- Competitor-Cheaper Indicator

These features allow pricing decisions to respond to competitor behavior.

---

## 6️⃣ Inventory Features
To align pricing with stock conditions:

- Inventory Ratio
- Days Until Stock-Out
- Low-Stock Indicator
- Overstock Indicator

These features ensure inventory-aware pricing decisions.

---

## 7️⃣ Profit Features
To balance revenue and profitability:

- Profit per Unit
- Profit Margin

These features help optimize prices without sacrificing margins.

---

## 8️⃣ Interaction Features
To capture non-linear relationships:

- Weekend × Price
- Season × Discount
- Inventory × Price
- Demand × Discount

Interaction features help the model learn combined effects beyond individual variables.

---

## 9️⃣ Categorical Encoding
Categorical variables were encoded using appropriate techniques based on cardinality:

- Product ID
- Category
- Brand
- Store ID

Encoding ensures compatibility with machine learning models.

---

## 🔟 Final Data Cleaning & Preparation
Before finalizing the dataset:

- Missing values were handled
- Duplicate records were removed
- Outliers were treated
- Numerical features were scaled where required

This ensures data quality and model stability.

---

## ✅ Outcome
- Dataset is fully **model-ready**
- Features capture real-world pricing, demand, inventory, and competition behavior
- Strong foundation for dynamic pricing models
- Improved interpretability and predictive performance.


 

