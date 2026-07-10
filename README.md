📊 Customer Churn Prediction & Retention Analysis
📌 Project Overview

Customer churn is a major challenge for telecom companies because losing existing customers is more expensive than retaining them. The objective of this project is to analyze customer behavior, identify the factors that contribute to churn, and build a machine learning model capable of predicting whether a customer is likely to leave the company. The project also includes an interactive Streamlit web application and a Power BI dashboard to support business decision-making.

🎯 Business Problem

Telecom companies experience significant revenue loss when customers discontinue their services. Understanding the reasons behind customer churn allows businesses to take proactive measures, improve customer satisfaction, and increase customer retention.

This project aims to answer the following questions:

Which customers are most likely to churn?
What factors influence customer churn?
How accurately can churn be predicted using Machine Learning?
What business strategies can reduce customer churn?
🛠 Technologies Used
Python
SQL
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Streamlit
Power BI
Joblib
Git & GitHub
📂 Project Workflow
1️⃣ Data Cleaning
Loaded the telecom customer dataset.
Checked and removed duplicate records.
Verified missing values.
Corrected data types.
Prepared a clean dataset for analysis.
2️⃣ SQL Analysis

Performed SQL queries to analyze customer behavior and identify churn patterns.

Examples of analysis:

Churn by Contract Type
Churn by Payment Method
Churn by Internet Service
Monthly Charges Analysis
Senior Citizen Analysis
Customer Distribution
3️⃣ Exploratory Data Analysis (EDA)

Used Python visualization libraries to understand customer behavior.

Created visualizations such as:

Churn Distribution
Correlation Heatmap
Contract Type Analysis
Monthly Charges Distribution
Tenure Analysis
Internet Service Analysis
Payment Method Analysis
4️⃣ Feature Engineering

Prepared the data for Machine Learning by:

Encoding categorical variables
Scaling numerical features
Creating the final feature matrix
Saving processed data for model training
5️⃣ Machine Learning

Built a Logistic Regression classification model.

Model Development
Train-Test Split
Standard Scaling
Model Training
Prediction
Model Evaluation
6️⃣ Streamlit Application

Developed an interactive web application where users can:

Enter customer details
Predict customer churn
View churn probability
Check customer risk level
Receive business recommendations
View model performance metrics
7️⃣ Power BI Dashboard

Designed an interactive dashboard to visualize:

Churn Rate
Customer Segmentation
Monthly Charges
Contract Analysis
Internet Service Analysis
Key Business KPIs
📈 Model Performance
Metric	Score
Accuracy	80.38%
Precision	64.76%
Recall	57.49%
F1 Score	60.91%
ROC-AUC	83.57%

The Logistic Regression model achieved good predictive performance and can help identify customers who are at risk of churning.

📊 Key Findings

The analysis revealed several important factors associated with customer churn:

Customers with Month-to-Month contracts have the highest churn rate.
Customers using Electronic Check are more likely to churn.
Fiber Optic internet users show higher churn compared to DSL users.
Customers with higher monthly charges tend to churn more frequently.
Customers with shorter tenure are at greater risk of leaving.
Customers without Online Security or Tech Support are more likely to churn.
💼 Business Recommendations

Based on the analysis, the following retention strategies are recommended:

🔴 High-Risk Customers
Contact customers before contract renewal.
Provide personalized retention offers.
Offer loyalty discounts or cashback.
Assign customer support specialists for follow-up.
🟡 Medium-Risk Customers
Recommend more suitable service plans.
Offer limited-time promotional discounts.
Increase customer engagement through email campaigns.
🟢 Low-Risk Customers
Continue providing high-quality service.
Introduce premium plans and upgrades.
Reward long-term customers through loyalty programs.
🚀 Results

Successfully developed a complete end-to-end Customer Churn Prediction system including:

SQL-based business analysis
Python Exploratory Data Analysis
Feature Engineering pipeline
Machine Learning prediction model
Interactive Power BI dashboard
Streamlit web application for real-time churn prediction

The project demonstrates how data analytics and machine learning can support business decisions and help reduce customer churn.

📷 Project Screenshots

(Add your screenshots here)

Streamlit Dashboard
Churn Prediction (High Risk)
Churn Prediction (Low Risk)
Power BI Dashboard
👩‍💻 Author

Poulomi Bhowmick

B.Sc. Data Science
Techno India University

GitHub: https://github.com/Poulomi8
