import streamlit as st
import numpy as np
import joblib

# Streamlit web app UI
st.title("Loan Default Prediction")

# Split inputs into two columns
col1, col2 = st.columns(2)

with col1:
    business_age = st.number_input(
        "Business Age (years)", min_value=1, max_value=50
    )
    annual_revenue = st.number_input(
        "Annual Revenue (RM)", min_value=50000, max_value=5000000
    )
    loan_amount = st.number_input(
        "Loan Amount Requested (RM)", min_value=10000, max_value=1000000000000
    )
    existing_loan = st.selectbox("Existing Loan?", [0, 1])  # 0: No, 1: Yes
    num_employees = st.number_input("No. of Employees", min_value=1, max_value=500)
    

with col2:
    profit_margin = st.number_input("Profit Margin (%)", min_value=1, max_value=100)
    
    industry_risk = st.selectbox(
        "Industry Risk (1 = Low Risk, 2 = Medium Risk, 3 = High Risk)", [1, 2, 3]
    )
    debt_to_income_ratio = st.number_input(
        "Debt-to-Income Ratio (%)", min_value=1, max_value=100, step=1
    )
    loan_tenure = st.number_input(
        "Loan Tenure (months)", min_value=0, max_value=120, step=1
    )
    loan_to_revenue_ratio = st.number_input(
        "Loan-to-Revenue Ratio (%)", min_value=1, max_value=100, step=1
    )
