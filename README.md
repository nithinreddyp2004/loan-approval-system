# 🏦 Loan Approval Prediction System

A Machine Learning web application that predicts whether a loan application will be **Approved** or **Rejected** using a **Random Forest Classifier**. The project includes a **FastAPI REST API**, a **Streamlit frontend**, and **Docker** for containerized deployment.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)

---

## 📌 Overview

This project automates the loan approval process by analyzing applicant information such as income, credit history, education, loan amount, and property area. A trained **Random Forest Classifier** predicts whether a loan application is likely to be approved.

The application follows an end-to-end Machine Learning deployment workflow:

- Data preprocessing
- Model training
- REST API development using FastAPI
- Interactive Streamlit frontend
- Docker-based containerization

---

## 🚀 Features

- ✅ Loan Approval Prediction
- ✅ Random Forest Machine Learning Model
- ✅ FastAPI REST API
- ✅ Interactive Streamlit Web Interface
- ✅ Dockerized Deployment
- ✅ Real-time Predictions
- ✅ Easy to Deploy and Extend

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Machine Learning | Scikit-learn, Pandas, NumPy |
| Backend | FastAPI, Uvicorn |
| Frontend | Streamlit |
| Deployment | Docker |

---

## 📂 Project Structure

```text
loan-approval-system/
│── app.py                     # Streamlit frontend
│── main.py                    # FastAPI backend
│── model_training.ipynb        # Model training notebook
│── loan_approval_model.pkl     # Trained ML model
│── Loan Dataset.csv            # Dataset
│── Dockerfile
│── requirements.txt
│── start.sh
└── README.md
```

---

## 🔄 Project Workflow

1. Load and preprocess the loan applicant dataset.
2. Train a Random Forest Classifier using Scikit-learn.
3. Evaluate the model using test data and cross-validation.
4. Save the trained model using Joblib.
5. Build a FastAPI backend to serve prediction requests.
6. Develop a Streamlit frontend for user interaction.
7. Connect the Streamlit application with the FastAPI API.
8. Containerize the application using Docker for easy deployment.

---

## 📦 Requirements

- Python 3.11+
- FastAPI
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Uvicorn
- Docker

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/nithinreddyp2004/loan-approval-system.git
cd loan-approval-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the FastAPI Backend

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

Swagger API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run the Streamlit Frontend

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

## 🐳 Run with Docker

Build the Docker image:

```bash
docker build -t loan-approval-system .
```

Run the container:

```bash
docker run -p 8000:8000 -p 8501:8501 loan-approval-system
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/predict` | Predict loan approval |

---

## 📊 Model Information

| Item | Details |
|------|----------|
| Algorithm | Random Forest Classifier |
| Test Accuracy | ~85.6% |
| Cross-Validation Accuracy | ~84.9% (5-fold) |
| Problem Type | Binary Classification |

### Input Features

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

### Output

- ✅ Loan Approved
- ❌ Loan Rejected

---

## 🔮 Future Improvements

- Authentication
- Cloud Deployment (AWS/Azure)
- CI/CD Pipeline
- Model Monitoring
- Explainable AI (SHAP/LIME)

---

## 👨‍💻 Author

**Nithin Reddy P**

GitHub: **https://github.com/nithinreddyp2004**

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub!
