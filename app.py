import streamlit as st
import requests

st.set_page_config(
    page_title="Loan Approval System",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 AI Loan Approval System")
st.markdown("### Check your loan eligibility instantly")

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("👤 Personal Details")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=70,
        value=30
    )

    marital_status = st.selectbox(
        "Marital Status",
        ["Single", "Married"]
    )

    dependents = st.number_input(
        "Dependents",
        min_value=0,
        max_value=10,
        value=0
    )

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    employment_status = st.selectbox(
        "Employment Status",
        ["Employed", "Self-Employed", "Unemployed"]
    )

    occupation_type = st.selectbox(
        "Occupation Type",
        ["Engineer", "Doctor", "Teacher", "Business", "Other"]
    )

    residential_status = st.selectbox(
        "Residential Status",
        ["Owned", "Rented"]
    )

with col2:

    st.subheader("💰 Financial Details")

    annual_income = st.number_input(
        "Annual Income",
        min_value=0,
        value=500000
    )

    monthly_expenses = st.number_input(
        "Monthly Expenses",
        min_value=0,
        value=20000
    )

    credit_score = st.slider(
        "Credit Score",
        300,
        900,
        750
    )

    existing_loans = st.number_input(
        "Existing Loans",
        min_value=0,
        value=0
    )

    outstanding_debt = st.number_input(
        "Outstanding Debt",
        min_value=0,
        value=0
    )

    loan_amount_requested = st.number_input(
        "Loan Amount Requested",
        min_value=0,
        value=300000
    )

    loan_term = st.number_input(
        "Loan Term (Months)",
        min_value=1,
        value=60
    )

    loan_purpose = st.selectbox(
        "Loan Purpose",
        [
            "Home",
            "Business",
            "Education",
            "Vehicle",
            "Personal"
        ]
    )

st.divider()

if st.button("🔍 Predict Loan Approval", use_container_width=True):

    payload = {
        "Applicant_ID": 100001,
        "Gender": gender,
        "Age": age,
        "Marital_Status": marital_status,
        "Dependents": dependents,
        "Education": education,
        "Employment_Status": employment_status,
        "Occupation_Type": occupation_type,
        "Residential_Status": residential_status,
        "City_Town": "Bangalore",
        "Annual_Income": annual_income,
        "Monthly_Expenses": monthly_expenses,
        "Credit_Score": credit_score,
        "Existing_Loans": existing_loans,
        "Total_Existing_Loan_Amount": 0,
        "Outstanding_Debt": outstanding_debt,
        "Loan_History": 1,
        "Loan_Amount_Requested": loan_amount_requested,
        "Loan_Term": loan_term,
        "Loan_Purpose": loan_purpose,
        "Interest_Rate": 9.5,
        "Loan_Type": "Personal",
        "Co_Applicant": "No",
        "Bank_Account_History": 5,
        "Transaction_Frequency": 20,
        "Default_Risk": 0.1
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )

    if response.status_code == 200:

        result = response.json()

        probability = result["approval_probability"]

        st.divider()
        st.subheader("📊 Prediction Result")

        if result["prediction"] == 1:
            st.success("✅ Loan Approved")
            st.balloons()
        else:
            st.error("❌ Loan Rejected")

        st.metric(
            "Approval Probability",
            f"{probability}%"
        )

        st.progress(probability / 100)

    else:
        st.error("API Error")
        st.write(response.text)