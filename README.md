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

 

