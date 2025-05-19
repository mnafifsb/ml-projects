import joblib

model_default = joblib.load(
    r"C:\Users\afif.baharun\OneDrive - cgcmb\Machine Learning Repository\LoanDefaultAndRepaymentForecast\model\loan_default_model.pkl"
)
print(
    type(model_default)
)  # Should print the type of the model (e.g., sklearn model class)
