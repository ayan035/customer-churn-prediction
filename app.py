import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# Load Model
# --------------------------------------------------

model = joblib.load("gradient_boosting_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📊 Customer Churn Prediction")

st.write(
    "Predict whether a bank customer is likely to churn "
    "using a Gradient Boosting Machine Learning model."
)

st.info(
    "Enter the customer's details below and click "
    "**Predict Churn** to generate the prediction."
)


# --------------------------------------------------
# Customer Information
# --------------------------------------------------

st.subheader("👤 Customer Information")


col1, col2 = st.columns(2)

with col1:

    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=850,
        value=650
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=40
    )

    tenure = st.number_input(
        "Tenure",
        min_value=0,
        max_value=10,
        value=5
    )

    balance = st.number_input(
        "Balance",
        min_value=0.0,
        value=60000.0,
        step=1000.0
    )

    estimated_salary = st.number_input(
        "Estimated Salary",
        min_value=0.0,
        value=50000.0,
        step=1000.0
    )


with col2:

    geography = st.selectbox(
        "Geography",
        ["France", "Germany", "Spain"]
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    num_products = st.number_input(
        "Number of Products",
        min_value=1,
        max_value=4,
        value=2
    )

    has_credit_card = st.selectbox(
        "Has Credit Card?",
        ["Yes", "No"]
    )

    active_member = st.selectbox(
        "Is Active Member?",
        ["Yes", "No"]
    )


# --------------------------------------------------
# Convert categorical values
# --------------------------------------------------

geography_germany = 1 if geography == "Germany" else 0
geography_spain = 1 if geography == "Spain" else 0

gender_male = 1 if gender == "Male" else 0

has_card = 1 if has_credit_card == "Yes" else 0
active = 1 if active_member == "Yes" else 0


# --------------------------------------------------
# Create Model Input
# --------------------------------------------------

input_data = pd.DataFrame([{
    "CreditScore": credit_score,
    "Age": age,
    "Tenure": tenure,
    "Balance": balance,
    "NumOfProducts": num_products,
    "HasCrCard": has_card,
    "IsActiveMember": active,
    "EstimatedSalary": estimated_salary,
    "Geography_Germany": geography_germany,
    "Geography_Spain": geography_spain,
    "Gender_Male": gender_male
}])


# Keep exactly the same feature order used during training
input_data = input_data[feature_columns]


# --------------------------------------------------
# Prediction
# --------------------------------------------------

st.markdown("---")

if st.button("🔍 Predict Customer Churn", use_container_width=True):

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.subheader("📌 Prediction Result")

    if prediction == 1:

        st.error(
            "⚠️ Customer is likely to CHURN"
        )

    else:

        st.success(
            "✅ Customer is likely to STAY"
        )

    st.metric(
        label="Churn Probability",
        value=f"{probability:.2%}"
    )

    if probability >= 0.50:

        st.warning(
            "The model estimates a relatively high probability "
            "of customer churn."
        )

    else:

        st.info(
            "The model estimates a relatively low probability "
            "of customer churn."
        )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Customer Churn Prediction | Machine Learning Project"
)

st.caption(
    "Developed by AYAN AHMAD | B.Tech Student | "
    "Artificial Intelligence & Machine Learning Engineer"
)

st.markdown(
    "[LinkedIn](https://www.linkedin.com/in/ayan-ahmad-4234a8313/) "
    " | "
    "[GitHub](https://github.com/ayan035)"
)