# Walmart Sales Forecasting

## Overview
This project aims to forecast weekly sales using historical Walmart store data.  
The goal is to build a machine learning model that captures temporal patterns and improves prediction accuracy.

---

## Data
- Weekly sales data across multiple stores and departments
- Additional features:
  - Temperature, Fuel Price
  - CPI, Unemployment
  - Promotional markdowns
  - Holiday indicators

---

## Key Steps

### 1. Data Preprocessing
- Merged multiple datasets (sales, features, stores)
- Handled missing values in markdown features
- Converted date to datetime format

---

### 2. Feature Engineering
- Lag features: `lag_1`, `lag_2`, `lag_4`
- Rolling features: `rolling_mean_4`
- Log transformation on target variable

---

### 3. Exploratory Data Analysis
- Distribution analysis (highly right-skewed target)
- Correlation heatmap
- Relationship between features and sales

---

### 4. Modeling
- Model: LightGBM Regressor
- Time-based train/validation split
- Evaluation metric: RMSE

---

### 5. Hyperparameter Tuning
- Manual grid search over:
  - num_leaves
  - max_depth
  - min_child_samples
  - subsample
  - colsample_bytree

---

## Results

| Metric | Value |
|------|------|
| RMSE (log scale) | ~0.37 |
| RMSE (real scale) | ~3050 |

- Lag features were the most important predictors
- Department and store-level differences significantly influenced sales
- External factors (CPI, fuel price) had moderate impact

---

## Insights
- Historical sales patterns dominate prediction performance
- Feature engineering has a larger impact than hyperparameter tuning
- The model performs reasonably well given high variance in sales

---

## Future Improvements
- Add longer lag features (lag_8, lag_12, lag_52)
- Include more time-based features (month, seasonality)
- Try more advanced models or ensembling

---

## Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- LightGBM
- Scikit-learn
