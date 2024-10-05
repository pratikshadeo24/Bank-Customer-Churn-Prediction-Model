# 🏦 Bank Customer Churn Prediction Model

Welcome to the **Bank Customer Churn Prediction** project! This repository provides a streamlined solution for predicting customer churn using machine learning techniques. By leveraging customer data, the goal is to help banks and financial institutions identify customers at risk of leaving, allowing them to take proactive measures and improve customer retention.


## 🌟 Key Highlights
- **Accurate Predictions**: Achieved 91% accuracy using the XGBoost algorithm.

---

## 📌 Overview

In the banking sector, **customer churn** refers to the rate at which customers stop using a bank's services. Understanding why customers leave and predicting potential churners can lead to timely interventions and prevent financial loss. This project uses data-driven approaches to predict which customers are likely to churn, focusing on key factors like account activity, customer demographics, and interaction with bank products.

### 🧠 Objective
The main objective of this project is to:
- Predict customer churn using machine learning models.
- Provide actionable insights for banks to improve customer retention.

---

## 🔬 Methodology

### **Workflow**:
1. **Data Collection**: Acquired customer churn dataset from Kaggle.
2. **Exploratory Data Analysis (EDA)**: Analyzed data trends, correlations, and outliers using visualizations.
3. **Data Preprocessing**:
   - Handled missing values and data normalization.
   - Addressed class imbalance through resampling techniques.
4. **Feature Engineering**: Created new features based on customer behavior and activities.
5. **Model Development**:
   - Trained multiple models, including Logistic Regression, Decision Trees, Random Forest, and XGBoost.
   - Hyperparameter tuning for optimized performance.
6. **Model Evaluation**:
   - Assessed model performance using key metrics such as Accuracy, F1-score, Precision, and Recall.
   - Chose the best-performing model (XGBoost) for deployment.


### 🔍 **Techniques**:
- **Data Cleaning**: Removed missing or irrelevant data to ensure clean input.
- **Data Normalization**: Scaled numerical features for better model performance.
- **Handling Imbalanced Classes**: Applied SMOTE to deal with the class imbalance between churn and non-churn customers.

---

## 🚀 Technologies Used

### **Languages**:
- Python

### **Frameworks**:
- Streamlit (for deployment)

### **Python Libraries**:
- **Data Handling**: `Pandas`, `NumPy`
- **Visualization**: `Seaborn`, `Matplotlib`
- **Machine Learning**: `Scikit-learn`, `XGBoost`
- **Imbalanced Data Handling**: `Imblearn`

---

## 📊 Results

The XGBoost model was chosen as the final model due to its superior performance. It achieved an accuracy of **91%** and an F1-score of **91%**, making it the best choice for predicting customer churn.

Here’s a summary of the results:
- **Accuracy**: 91%
- **F1-score**: 91%
- **Precision & Recall**: Balanced and satisfactory for both churn and non-churn customers.

