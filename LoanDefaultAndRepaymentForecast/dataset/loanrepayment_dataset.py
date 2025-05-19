import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 1000

# Generate synthetic repayment forecasting dataset
business_age = np.random.randint(1, 21, n_samples)
annual_revenue = np.random.randint(50000, 5000000, n_samples)

# Credit score influenced by business age and revenue
credit_score = np.clip(
    (
        business_age * 15
        + np.log1p(annual_revenue) * 10
        + np.random.normal(600, 50, n_samples)
    ).astype(int),
    300,
    850,
)

# Loan amount requested correlated with annual revenue
loan_amount_requested = (
    annual_revenue * np.random.uniform(0.1, 0.5, n_samples)
).astype(int)

# Loan term based on loan amount
loan_term = np.random.choice(
    [12, 24, 36, 48, 60], n_samples, p=[0.2, 0.3, 0.3, 0.1, 0.1]
)

# Monthly repayment calculated with a realistic interest rate (e.g., 5% annual interest)
interest_rate = 0.05
monthly_repayment = (
    loan_amount_requested * (1 + interest_rate * (loan_term / 12)) / loan_term
).astype(int)

# Repayment status logic
repayment_status = [
    1
    if credit_score[i] > 650 and monthly_repayment[i] < 0.25 * (annual_revenue[i] / 12)
    else 0
    for i in range(n_samples)
]

# Round Annual Revenue and Loan Amount Requested to the nearest thousands
annual_revenue = (np.round(annual_revenue / 1000) * 1000).astype(int)
loan_amount_requested = (np.round(loan_amount_requested / 1000) * 1000).astype(int)

data_repayment = {
    "Business Age (years)": business_age,
    "Annual Revenue (RM)": annual_revenue,
    "Credit Score": credit_score,
    "Loan Amount Requested (RM)": loan_amount_requested,
    "Loan Term (months)": loan_term,
    "Monthly Repayment (RM)": monthly_repayment,
    "Repayment Status": repayment_status,  # 0: Late, 1: On-time
}

df_repayment = pd.DataFrame(data_repayment)
df_repayment.to_csv("dataset/loan_repayment_data.csv", index=False)
