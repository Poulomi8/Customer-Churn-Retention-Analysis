import streamlit as st
import pandas as pd
import joblib

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)
st.markdown("""
<style>

.main{
    background-color:#001730;
}

h1{
    color:#0E4D92;
}

.stButton>button{
    background-color:#0E4D92;
    color:white;
    border-radius:10px;
    height:50px;
    width:100%;
    font-size:18px;
}

.stMetric{
    background-color:#262730;
    padding:15px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)
# -------------------------
# Load Model
# -------------------------
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# -------------------------
# Title
# -------------------------
st.title("📊 Customer Churn Prediction Dashboard")

st.markdown("""
Welcome to the **Customer Churn Prediction Dashboard**.

This application predicts whether a telecom customer is likely to churn based on their demographic information, service usage, billing details, and contract information.

👈 Fill in the customer details in the sidebar and click **Predict Churn**.
""")
st.markdown("## 📈 Dashboard Overview")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric(
        label="🤖 Model",
        value="Logistic Regression"
    )

with kpi2:
    st.metric(
        label="🎯 Accuracy",
        value="80.38%"
    )

with kpi3:
    st.metric(
        label="📈 ROC-AUC",
        value="83.57%"
    )

with kpi4:
    st.metric(
        label="📊 Features",
        value="30"
    )
# -------------------------
# Customer Details
# -------------------------
st.sidebar.title("📋 Customer Details")
st.sidebar.markdown("Please enter the customer's information below.")

st.sidebar.header("Customer Information")

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior = st.sidebar.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.sidebar.selectbox("Partner", ["No", "Yes"])
dependents = st.sidebar.selectbox("Dependents", ["No", "Yes"])

tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)

phone = st.sidebar.selectbox("Phone Service", ["No", "Yes"])
paperless = st.sidebar.selectbox("Paperless Billing", ["No", "Yes"])

monthly = st.sidebar.slider("Monthly Charges", 0.0, 150.0, 70.0)
total = st.sidebar.number_input("Total Charges", value=0.0)

# service
st.sidebar.header("Services")

multiple_lines = st.sidebar.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)

internet = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.sidebar.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)

online_backup = st.sidebar.selectbox(
    "Online Backup",
    ["No", "Yes", "No internet service"]
)

device_protection = st.sidebar.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"]
)

tech_support = st.sidebar.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"]
)

streaming_tv = st.sidebar.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)

streaming_movies = st.sidebar.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"]
)

contract = st.sidebar.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

payment= st.sidebar.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)

# Convert Yes/No values to 0/1
gender = 1 if gender == "Male" else 0
senior = 1 if senior == "Yes" else 0
partner = 1 if partner == "Yes" else 0
dependents = 1 if dependents == "Yes" else 0
phone = 1 if phone == "Yes" else 0
paperless = 1 if paperless == "Yes" else 0

# Create input dictionary
input_data = {
    "gender": gender,
    "SeniorCitizen": senior,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone,
    "PaperlessBilling": paperless,
    "MonthlyCharges": monthly,
    "TotalCharges": total,

    "MultipleLines_No phone service": 1 if multiple_lines == "No phone service" else 0,
    "MultipleLines_Yes": 1 if multiple_lines == "Yes" else 0,

    "InternetService_Fiber optic": 1 if internet == "Fiber optic" else 0,
    "InternetService_No": 1 if internet == "No" else 0,

    "OnlineSecurity_No internet service": 1 if online_security == "No internet service" else 0,
    "OnlineSecurity_Yes": 1 if online_security == "Yes" else 0,

    "OnlineBackup_No internet service": 1 if online_backup == "No internet service" else 0,
    "OnlineBackup_Yes": 1 if online_backup == "Yes" else 0,

    "DeviceProtection_No internet service": 1 if device_protection == "No internet service" else 0,
    "DeviceProtection_Yes": 1 if device_protection == "Yes" else 0,

    "TechSupport_No internet service": 1 if tech_support == "No internet service" else 0,
    "TechSupport_Yes": 1 if tech_support == "Yes" else 0,

    "StreamingTV_No internet service": 1 if streaming_tv == "No internet service" else 0,
    "StreamingTV_Yes": 1 if streaming_tv == "Yes" else 0,

    "StreamingMovies_No internet service": 1 if streaming_movies == "No internet service" else 0,
    "StreamingMovies_Yes": 1 if streaming_movies == "Yes" else 0,

    "Contract_One year": 1 if contract == "One year" else 0,
    "Contract_Two year": 1 if contract == "Two year" else 0,

    "PaymentMethod_Credit card (automatic)": 1 if payment == "Credit card (automatic)" else 0,
    "PaymentMethod_Electronic check": 1 if payment == "Electronic check" else 0,
    "PaymentMethod_Mailed check": 1 if payment == "Mailed check" else 0,
}
# Convert Yes/No values to 0/1
gender = 1 if gender == "Male" else 0
senior = 1 if senior == "Yes" else 0
partner = 1 if partner == "Yes" else 0
dependents = 1 if dependents == "Yes" else 0
phone = 1 if phone == "Yes" else 0
paperless = 1 if paperless == "Yes" else 0

# Create input dictionary
input_data = {
    "gender": gender,
    "SeniorCitizen": senior,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone,
    "PaperlessBilling": paperless,
    "MonthlyCharges": monthly,
    "TotalCharges": total,

    "MultipleLines_No phone service": 1 if multiple_lines == "No phone service" else 0,
    "MultipleLines_Yes": 1 if multiple_lines == "Yes" else 0,

    "InternetService_Fiber optic": 1 if internet == "Fiber optic" else 0,
    "InternetService_No": 1 if internet == "No" else 0,

    "OnlineSecurity_No internet service": 1 if online_security == "No internet service" else 0,
    "OnlineSecurity_Yes": 1 if online_security == "Yes" else 0,

    "OnlineBackup_No internet service": 1 if online_backup == "No internet service" else 0,
    "OnlineBackup_Yes": 1 if online_backup == "Yes" else 0,

    "DeviceProtection_No internet service": 1 if device_protection == "No internet service" else 0,
    "DeviceProtection_Yes": 1 if device_protection == "Yes" else 0,

    "TechSupport_No internet service": 1 if tech_support == "No internet service" else 0,
    "TechSupport_Yes": 1 if tech_support == "Yes" else 0,

    "StreamingTV_No internet service": 1 if streaming_tv == "No internet service" else 0,
    "StreamingTV_Yes": 1 if streaming_tv == "Yes" else 0,

    "StreamingMovies_No internet service": 1 if streaming_movies == "No internet service" else 0,
    "StreamingMovies_Yes": 1 if streaming_movies == "Yes" else 0,

    "Contract_One year": 1 if contract == "One year" else 0,
    "Contract_Two year": 1 if contract == "Two year" else 0,

    "PaymentMethod_Credit card (automatic)": 1 if payment == "Credit card (automatic)" else 0,
    "PaymentMethod_Electronic check": 1 if payment == "Electronic check" else 0,
    "PaymentMethod_Mailed check": 1 if payment == "Mailed check" else 0,
}

# Convert dictionary to DataFrame
input_df = pd.DataFrame([input_data])
input_df = input_df.reindex(columns=feature_columns, fill_value=0)
input_scaled = scaler.transform(input_df)

if st.button("🔮 Predict Churn"):

    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn.")
    else:
        st.success("✅ Customer is likely to stay.")

    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )
    st.progress(float(probability))
    st.write(f"Prediction Confidence: **{probability*100:.2f}%**")


    # Risk Level
    if probability >= 0.70:
        st.error("🔴 Risk Level: HIGH")
    elif probability >= 0.40:
        st.warning("🟡 Risk Level: MEDIUM")
    else:
        st.success("🟢 Risk Level: LOW")

    # Business Recommendation
    st.subheader("💡 Business Recommendation")

    if probability >= 0.70:
        st.write("""
- 📞 Contact the customer immediately.
- 🎁 Offer a loyalty discount.
- 👨‍💼 Assign a retention specialist.
- 📧 Send a personalized offer.
""")
    elif probability >= 0.40:
        st.write("""
- 📧 Send promotional emails.
- 🎉 Recommend suitable plans.
- 💰 Offer a limited-time discount.
""")
    else:
        st.write("""
- 😊 Customer is satisfied.
- ⭐ Continue providing quality service.
- 🎯 Offer premium upgrades.
""")

st.markdown("---")

st.header("📊 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Accuracy", "80.38%")
    st.metric("Precision", "64.76%")

with col2:
    st.metric("Recall", "57.49%")
    st.metric("F1 Score", "60.91%")

with col3:
    st.metric("ROC-AUC", "83.57%")
    st.metric("Model", "Logistic Regression")
   

st.markdown("---")

st.markdown(
"""
<center>

### Developed by **Poulomi Bhowmick**

B.Sc. Data Science | Techno India University

Customer Churn Prediction using Machine Learning & Streamlit

</center>
""",
unsafe_allow_html=True
)