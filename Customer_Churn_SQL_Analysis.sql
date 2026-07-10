#1.Data Validation
SELECT *
FROM `wa_fn-usec_-telco-customer-churn`;
RENAME TABLE `wa_fn-usec_-telco-customer-churn`
TO customer_churn;
SELECT COUNT(*) AS Total_Customers
FROM `customer_churn`;
select *
FROM customer_churn
WHERE customerID IS NULL
   OR gender IS NULL
   OR TotalCharges IS NULL
   OR TRIM(TotalCharges) = ''
   OR TotalCharges = ' ';
SELECT customerID,
COUNT(*) AS Duplicate_Count
FROM customer_churn
GROUP BY customerID
HAVING COUNT(*) > 1;
SELECT DISTINCT Contract
FROM customer_churn;
SELECT DISTINCT Gender
FROM customer_churn;
SELECT DISTINCT InternetService
FROM customer_churn;
SELECT DISTINCT PaymentMethod
FROM customer_churn;
SELECT DISTINCT Churn
FROM customer_churn;
SELECT DISTINCT Partner
FROM customer_churn;
SELECT DISTINCT Dependents
FROM customer_churn;
SELECT DISTINCT TechSupport
FROM customer_churn;

#2.Data Cleaning-No cleaning required after validation

#3.Exploratory Data Analysis
    #Question: What percentage of customers leave the company?
SELECT
COUNT(*) AS Total_Customers,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2
) AS Churn_Rate
FROM customer_churn;  #churned customers-1869, churn_rate-26.58

      #How many customers stayed versus churned
SELECT
Churn,
COUNT(*) AS Customers
FROM customer_churn
GROUP BY Churn; #stayed_customer-5163

	#Does gender influence churn?
    SELECT
gender,
COUNT(*) AS Customers,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned
FROM customer_churn
GROUP BY gender; #females are highly churneed

	#Which contract type has the highest churn?
SELECT
Contract,
COUNT(*) AS Total_Customers,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2
) AS Churn_Rate
FROM customer_churn
GROUP BY Contract
ORDER BY Churn_Rate DESC; #month to month are highly(42.71%) churned

	#Which internet service has the highest customer churn?
SELECT
InternetService,
COUNT(*) AS Customers,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2
) AS Churn_Rate
FROM customer_churn
GROUP BY InternetService; #fiber optic

	#What is the average monthly bill?
  SELECT
ROUND(AVG(MonthlyCharges),2) AS Average_Monthly_Charges
FROM customer_churn; #64.8
  
		#Do customers who churn pay higher monthly charges?
	SELECT
Churn,
ROUND(AVG(MonthlyCharges),2) AS Avg_Monthly_Charges
FROM customer_churn
GROUP BY Churn; #yes-74.44

	#avg tenure
SELECT
ROUND(AVG(tenure),2) AS Average_Tenure
FROM customer_churn; #32.42

	#Which customer tenure group is the largest?
SELECT
CASE
WHEN tenure BETWEEN 0 AND 12 THEN '0-12 Months'
WHEN tenure BETWEEN 13 AND 24 THEN '13-24 Months'
WHEN tenure BETWEEN 25 AND 48 THEN '25-48 Months'
ELSE '49-72 Months'
END AS Tenure_Group,
COUNT(*) AS Customers
FROM customer_churn
GROUP BY Tenure_Group
ORDER BY Customers DESC;

	#Which tenure segment experiences the most churn?
SELECT
CASE
WHEN tenure BETWEEN 0 AND 12 THEN '0-12 Months'
WHEN tenure BETWEEN 13 AND 24 THEN '13-24 Months'
WHEN tenure BETWEEN 25 AND 48 THEN '25-48 Months'
ELSE '49-72 Months'
END AS Tenure_Group,
COUNT(*) AS Customers,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned
FROM customer_churn
GROUP BY Tenure_Group;

	#Which contract type generates the most revenue?
SELECT
Contract,
ROUND(SUM(TotalCharges),2) AS Revenue
FROM customer_churn
GROUP BY Contract
ORDER BY Revenue DESC; #two-years

	#How much revenue has been lost due to churn?
SELECT
ROUND(SUM(TotalCharges),2) AS Revenue_Lost
FROM customer_churn
WHERE Churn='Yes'; #2862926.9

		#10 highest revenue customer
SELECT
customerID,
TotalCharges
FROM customer_churn
ORDER BY TotalCharges DESC
LIMIT 10;

#Revenue by Internet Service
SELECT
InternetService,
ROUND(SUM(TotalCharges),2) AS Revenue
FROM customer_churn
GROUP BY InternetService; #fiber optic-9923622.95

#Churn by Payment Method
SELECT
PaymentMethod,
COUNT(*) AS Customers,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2
) AS Churn_Rate
FROM customer_churn
GROUP BY PaymentMethod
ORDER BY Churn_Rate DESC; #ELECTRONIC CHECK-45.26

#Tech Support vs Churn
SELECT
TechSupport,
COUNT(*) AS Customers,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2
) AS Churn_Rate
FROM customer_churn
GROUP BY TechSupport;

#Online Security vs Churn
SELECT
OnlineSecurity,
COUNT(*) AS Customers,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2
) AS Churn_Rate
FROM customer_churn
GROUP BY OnlineSecurity;

#Senior Citizens vs Churn
SELECT
SeniorCitizen,
COUNT(*) AS Customers,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2
) AS Churn_Rate
FROM customer_churn
GROUP BY SeniorCitizen;

#Paperless Billing vs Churn
SELECT
PaperlessBilling,
COUNT(*) AS Customers,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2
) AS Churn_Rate
FROM customer_churn
GROUP BY PaperlessBilling;

#Highest Monthly Charges
SELECT
customerID,
MonthlyCharges
FROM customer_churn
ORDER BY MonthlyCharges DESC
LIMIT 10;