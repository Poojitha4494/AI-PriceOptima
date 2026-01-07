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

# 📊 Feature Engineering – PriceOptima Dynamic Pricing Project

## 📌 Overview
This module covers the **Feature Engineering phase** of the **PriceOptima Dynamic Pricing Project**.  
The objective is to convert raw transactional, pricing, demand, inventory, and competitor data into **meaningful, machine-learning-ready features** that help the model understand:

- Demand patterns
- Pricing behavior
- Seasonality & festivals
- Inventory conditions
- Competitor influence
- Profitability impact

---

## 🧩 Feature Engineering Tasks

### 1️⃣ Time-Based Features
Features created to capture temporal patterns and seasonality:
- Day
- Month
- Year
- Day of Week
- Weekend Flag
- Season (Summer / Monsoon / Winter)
- Festival / Holiday Indicator

---

### 2️⃣ Price-Based Features
To analyze pricing behavior and short-term fluctuations:
- Lag Price (Previous Day)
- Lag Price (7-Day)
- Price Change Percentage
- Discount Percentage

---

### 3️⃣ Demand Features (Lag & Rolling)
To model demand trends and stability:
- Lag Sales (1-Day, 7-Day, 30-Day)
- Rolling Average Sales (7-Day, 30-Day)
- Demand Volatility (Standard Deviation of Sales)

---

### 4️⃣ Price Elasticity Features
To understand customer price sensitivity:
- Price Elasticity Calculation
- Elasticity Classification:
  - High Elasticity
  - Medium Elasticity
  - Low Elasticity

---

### 5️⃣ Competitor Features (If Available)
To capture market competition:
- Competitor Price Difference
- Competitor Price Index
- Competitor-Cheaper Indicator

---

### 6️⃣ Inventory Features
To align pricing decisions with stock conditions:
- Inventory Ratio
- Days Until Stock-Out
- Low-Stock Indicator
- Overstock Indicator

---

### 7️⃣ Profit Features
To balance revenue optimization and profitability:
- Profit per Unit
- Profit Margin

---

### 8️⃣ Interaction Features
To capture non-linear relationships:
- Weekend × Price
- Season × Discount
- Inventory × Price
- Demand × Discount

---

### 9️⃣ Categorical Encoding
Categorical attributes were encoded using appropriate techniques:
- Product ID
- Category
- Brand
- Store ID

---

### 🔟 Final Data Cleaning & Preparation
Final preprocessing steps include:
- Handling missing values
- Removing duplicates
- Treating outliers
- Scaling numerical features (where required)

---

## ✅ Outcome
After completing feature engineering:
- Dataset is **fully model-ready**
- Features reflect **real-world pricing and demand behavior**
- Improved model accuracy, stability, and interpretability
- Strong foundation for **dynamic pricing predictions**

