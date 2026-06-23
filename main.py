from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Load trained model
model = joblib.load("loan_approval_model.pkl")


class LoanData(BaseModel):
    Applicant_ID: int
    Gender: str
    Age: int
    Marital_Status: str
    Dependents: int
    Education: str
    Employment_Status: str
    Occupation_Type: str
    Residential_Status: str
    City_Town: str
    Annual_Income: int
    Monthly_Expenses: int
    Credit_Score: int
    Existing_Loans: int
    Total_Existing_Loan_Amount: int
    Outstanding_Debt: int
    Loan_History: int
    Loan_Amount_Requested: int
    Loan_Term: int
    Loan_Purpose: str
    Interest_Rate: float
    Loan_Type: str
    Co_Applicant: str
    Bank_Account_History: int
    Transaction_Frequency: int
    Default_Risk: float


@app.get("/")
def home():
    return {
        "message": "Loan Approval API Running"
    }


@app.post("/predict")
def predict(data: LoanData):

    df = pd.DataFrame([data.dict()])

    df.rename(
        columns={
            "City_Town": "City/Town",
            "Co_Applicant": "Co-Applicant"
        },
        inplace=True
    )

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "approval_probability": round(probability * 100, 2)
    }