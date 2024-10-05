from pathlib import Path
import pandas as pd
import numpy as np
import streamlit as st
import predict
import warnings

# Suppress the specific warning about missing ScriptRunContext
warnings.filterwarnings("ignore", message="missing ScriptRunContext")

# Custom CSS for a nicer look
def custom_css():
    st.markdown("""
        <style>
        body {
            background-color: #f2f2f2;
        }
        .stApp {
            background-color: #fff;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #ff6f61;
            font-family: 'Arial', sans-serif;
            font-weight: bold;
            text-align: center;
        }
        h2 {
            color: #0072ff;
            font-family: 'Arial', sans-serif;
            font-weight: bold;
        }
        .stSlider, .stSelectbox, .stRadio {
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        }
        .stButton button {
            background-color: #0072ff;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
        }
        .stButton button:hover {
            background-color: #0056b3;
        }
        </style>
    """, unsafe_allow_html=True)

def get_user_input(df_train):
    st.markdown("### Customer's Personal Information")
    col1, col2 = st.columns(2)  # Create two columns

    with col1:
        geography = st.radio('🌍 Which country does the customer belong to?',
                             df_train['Geography'].unique(), horizontal=True, index=1)
        gender = st.radio('👤 Customer Gender:',
                          df_train['Gender'].unique(), horizontal=True)
        age = st.slider("🎂 Customer Age:", 18, 100, int(df_train['Age'].mean()))

    with col2:
        credit_score = st.slider("💳 Customer Credit Score:",
                                 int(df_train['CreditScore'].min()),
                                 int(df_train['CreditScore'].max()),
                                 int(df_train['CreditScore'].mean()))
        estimated_salary = st.slider("💼 Customer Estimated Salary:",
                                     0, 200000, int(df_train['EstimatedSalary'].mean()))

    st.markdown("### Customer's Relationship with the Bank")
    col1, col2 = st.columns(2)  # Reuse columns for the second section

    with col1:
        tenure = st.selectbox("⏳ Customer's Tenure with Bank:",
                              sorted(df_train['Tenure'].unique()), index=5)
        balance = st.slider("💰 Customer's Bank Account Balance:",
                            float(df_train['Balance'].min()),
                            float(df_train['Balance'].max()),
                            float(df_train['Balance'].mean()))

    with col2:
        num_of_products = st.radio('📦 Number of Bank Products Customer Owns:',
                                   sorted(df_train['NumOfProducts'].unique()), horizontal=True, index=1)
        has_credit_card = st.radio('💳 Does the customer have a credit card?',
                                   ["Yes", 'No'], horizontal=True)
        has_credit_card = 1 if has_credit_card == "Yes" else 0
        is_active = st.radio('🔔 Is the customer active in bank activities?',
                             ["Yes", 'No'], horizontal=True)
        is_active = 1 if is_active == "Yes" else 0

    X = pd.DataFrame({
        'CreditScore': credit_score,
        'Geography': geography,
        'Gender': gender,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        'NumOfProducts': num_of_products,
        'HasCrCard': has_credit_card,
        'IsActiveMember': is_active,
        'EstimatedSalary': estimated_salary
    }, index=[0])
    return X



if __name__ == "__main__":
    # Set up the page config
    st.set_page_config(page_title="🌟 Bank Customer Churn Prediction 🌟", layout="wide")

    # Apply custom CSS styles
    custom_css()

    st.title("🔮 Bank Customer Churn Prediction App")
    st.image(str(Path(__file__).parents[1] / 'img/churn.png'), width=1200)

    st.write("""
        Welcome to the **Bank Customer Churn Prediction App**! Use this tool to analyze whether 
        a customer is likely to leave the bank. Please enter the required information below, and 
        our prediction model will determine if the customer is likely to churn. 🎯
    """)

    # Load the data
    try:
        df_train = pd.read_csv(str(Path(__file__).parents[1] / 'data/churn_data.csv'))
    except FileNotFoundError:
        st.error("Error: Training data not found. Please ensure 'churn_data.csv' exists in the correct location.")
        st.stop()

    # Collect user input
    st.header("📋 Input Fields")
    input_df = get_user_input(df_train)

    st.header("🔍 Prediction Results")
    with st.spinner('Running prediction...'):
        customer_churn = predict.predict(input_df)[0]  # get predictions

    if customer_churn == 0:
        st.subheader("✅ _Customer is **not** likely to churn._")
        st.balloons()
    else:
        st.subheader("⚠️ _Customer **is** likely to churn._")
        st.snow()
