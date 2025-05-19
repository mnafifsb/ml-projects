import pandas as pd
import numpy as np
from sklearn.utils import resample

# Seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 10000

# Generate synthetic dataset with logical dependencies
business_age = np.random.randint(1, 16, n_samples)  # Businesses aged 1-15 years
annual_revenue = np.random.uniform(50000, 500000, n_samples).astype(
    int
)  # Revenue between 50k and 500k
existing_loan = np.random.choice(
    [0, 1], n_samples, p=[0.7, 0.3]
)  # 70% have no existing loans
num_employees = np.random.randint(1, 50, n_samples)  # Employees between 1 and 50
profit_margin = np.random.uniform(3, 30, n_samples)  # Profit margin between 3% and 30%

# Ensure logical bounds
profit_margin = np.clip(profit_margin, 3, 30)

# Round annual revenue to the nearest thousands
annual_revenue = np.round(annual_revenue, -3)

# Loan amount requested is proportional to annual revenue, capped at 40%
loan_amount_requested = (
    annual_revenue * np.random.uniform(0.1, 0.4, n_samples)
).astype(int)
loan_amount_requested = np.round(loan_amount_requested, -3).astype(int)

# Round profit margin to 2 decimal places
profit_margin = np.round(profit_margin, 2)

# New feature: Industry Risk (1 = Low Risk, 2 = Medium Risk, 3 = High Risk)
industry_risk = np.random.choice(
    [1, 2, 3], n_samples, p=[0.5, 0.3, 0.2]
)  # 50% low, 30% medium, 20% high risk

# New feature: Debt-to-Income Ratio (DTI)
debt_to_income_ratio = np.random.uniform(
    0.2, 0.8, n_samples
) + existing_loan * np.random.uniform(0.1, 0.3, n_samples)
debt_to_income_ratio = np.round(debt_to_income_ratio, 2)

# New feature: Loan Tenure (in months)
loan_tenure = np.random.randint(
    6, 60, n_samples
)  # Loan tenure between 6 months and 5 years

# Set loan tenure to 0 for rows with zero existing loans
loan_tenure[existing_loan == 0] = 0

# New feature: Loan-to-Revenue Ratio
loan_to_revenue_ratio = loan_amount_requested / annual_revenue

# Adjust default probability formula to balance defaults
default_probability = (
    0.4
    - profit_margin / 100
    + existing_loan * 0.2
    + loan_to_revenue_ratio * 0.3
    + industry_risk * 0.1
    + debt_to_income_ratio * 0.3
    - loan_tenure / 500
)
default_probability = np.clip(
    default_probability, 0, 1
)  # Ensure probabilities are between 0 and 1

loan_default = (np.random.rand(n_samples) < default_probability).astype(int)

# Convert ratios to percentages
debt_to_income_ratio = (debt_to_income_ratio * 100).round(2)
loan_to_revenue_ratio = (loan_to_revenue_ratio * 100).round(2)

# Combine into a DataFrame
data = {
    "BusinessAge": business_age,
    "AnnualRevenue": annual_revenue,
    "ExistingLoan": existing_loan,
    "NoOfEmployees": num_employees,
    "ProfitMargin": profit_margin,
    "LoanAmountRequested": loan_amount_requested,
    "IndustryRisk": industry_risk,
    "DebttoIncomeRatio": debt_to_income_ratio,
    "LoanTenure": loan_tenure,
    "LoanToRevenueRatio": loan_to_revenue_ratio,
    "LoanDefault": loan_default,
}

df_default = pd.DataFrame(data)

# Save to CSV
df_default.to_csv("dataset/loan_default_data.csv", index=False)
