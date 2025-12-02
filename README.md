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
