# Customer Churn Prediction

A Machine Learning web application that predicts whether a bank customer is likely to churn based on customer demographic, account, and financial information.

## 🚀 Live Demo

[Try the Customer Churn Prediction App](PASTE_YOUR_STREAMLIT_LINK_HERE)

## 📌 Project Overview

Customer churn is an important problem for banks and financial institutions because losing existing customers can negatively affect business revenue.

This project uses Machine Learning to predict whether a customer is likely to leave the bank. The application takes customer information as input and provides:

- Churn prediction
- Churn probability
- Simple interpretation of the prediction

The Machine Learning model used in this project is a **Gradient Boosting Classifier**.

## 🎯 Objective

The main objective of this project is to build a predictive system that can identify customers who are more likely to churn.

This can help businesses:

- Identify potentially dissatisfied customers
- Take preventive retention actions
- Improve customer retention
- Support data-driven decision making

## 📊 Dataset

The project uses the **Churn Modelling Dataset** containing customer information such as:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Credit Card Status
- Active Membership Status
- Estimated Salary

The target variable is:

**Exited**
- `0` → Customer stayed
- `1` → Customer churned

## 🤖 Machine Learning Model

The project uses:

**Gradient Boosting Classifier**

Gradient Boosting is an ensemble Machine Learning algorithm that combines multiple weak decision-tree models sequentially to build a stronger predictive model.

## 🔧 Data Preprocessing

The following preprocessing techniques were used:

- Categorical feature encoding
- One-hot encoding for categorical variables
- Feature selection
- Train-test splitting
- Model training
- Model evaluation

The final model uses **11 input features**.

## 📈 Prediction

The application provides two outputs:

### Customer Prediction

- Customer is likely to STAY
- Customer is likely to CHURN

### Churn Probability

The application also displays the estimated probability of customer churn as a percentage.

Example:

```text
Customer is likely to STAY
Churn Probability: 6.91%
---
 Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- GitHub

📂 Project Structure
customer-churn-prediction/
│
├── Churn_Modelling.csv
├── Customer_Churn_Prediction.ipynb
├── app.py
├── feature_columns.pkl
├── gradient_boosting_model.pkl
├── requirements.txt
└── README.md

💻 Run Locally
Install the required dependencies:
pip install -r requirements.txt

Run the Streamlit application:
streamlit run app.py

The application will open in your browser.

🌐 Deployment
The application is deployed using Streamlit Community Cloud.

🔮 Future Improvements
Possible future improvements include:
- Hyperparameter tuning
- Feature importance visualization
- Model comparison
- Explainable AI integration
- Customer segmentation
- Retention recommendations
- Improved dashboard and analytics

👨‍💻 Author
Ayan Ahmad
B.Tech Student | Artificial Intelligence & Machine Learning Engineer
- GitHub: https://github.com/ayan035
- LinkedIn: https://www.linkedin.com/in/ayan-ahmad-4234a8313/
