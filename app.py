import streamlit as st
import pickle
import pandas as pd

# -------------------------------
# Page configuration
# -------------------------------
st.set_page_config(
    page_title="Telecom Customer Churn Prediction",
    page_icon="📞",
    layout="centered"
)

# -------------------------------
# Load model and scaler
# -------------------------------
@st.cache_resource
def load_files():
    # Load trained Random Forest model
    with open("models/random_forest_model.pkl", "rb") as file:
        model_random = pickle.load(file)

    # Load label encoder file
    with open("models/label_encoder.pkl", "rb") as f:
        label_encoders = pickle.load(f)

    # Load standard scaler
    with open("models/standard_scaler.pkl", "rb") as f:
        scaler = pickle.load(f)

    return model_random, label_encoders, scaler


model_random, label_encoders, scaler = load_files()

# -------------------------------
# App title
# -------------------------------
st.title("📞 Telecom Customer Churn Prediction")
st.write("Enter customer details below to predict whether the customer is likely to churn or continue.")

# -------------------------------
# User input form
# -------------------------------
with st.form("prediction_form"):

    international_plan = st.selectbox(
        "International Plan",
        ["yes", "no"]
    )

    voice_mail_plan = st.selectbox(
        "Voice Mail Plan",
        ["yes", "no"]
    )

    account_length = st.number_input(
        "Account Length",
        min_value=0,
        value=100,
        step=1
    )

    number_vmail_messages = st.number_input(
        "Number of Voicemail Messages",
        min_value=0.0,
        value=0.0,
        step=1.0
    )

    total_day_minutes = st.number_input(
        "Total Day Minutes",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

    total_day_calls = st.number_input(
        "Total Day Calls",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

    total_eve_minutes = st.number_input(
        "Total Evening Minutes",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

    total_eve_calls = st.number_input(
        "Total Evening Calls",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

    total_night_minutes = st.number_input(
        "Total Night Minutes",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

    total_night_calls = st.number_input(
        "Total Night Calls",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

    total_intl_minutes = st.number_input(
        "Total International Minutes",
        min_value=0.0,
        value=10.0,
        step=1.0
    )

    total_intl_calls = st.number_input(
        "Total International Calls",
        min_value=0.0,
        value=3.0,
        step=1.0
    )

    customer_service_calls = st.number_input(
        "Customer Service Calls",
        min_value=0.0,
        value=1.0,
        step=1.0
    )

    submitted = st.form_submit_button("Predict")


# -------------------------------
# Prediction logic
# -------------------------------
if submitted:

    # Manual encoding
    # yes = 1, no = 0
    international_plan_encoded = 1 if international_plan == "yes" else 0
    voice_mail_plan_encoded = 1 if voice_mail_plan == "yes" else 0

    # Create input dataframe
    input_df = pd.DataFrame({
        "International plan": [international_plan_encoded],
        "Voice mail plan": [voice_mail_plan_encoded],
        "Account length": [account_length],
        "Number vmail messages": [number_vmail_messages],
        "Total day minutes": [total_day_minutes],
        "Total day calls": [total_day_calls],
        "Total eve minutes": [total_eve_minutes],
        "Total eve calls": [total_eve_calls],
        "Total night minutes": [total_night_minutes],
        "Total night calls": [total_night_calls],
        "Total intl minutes": [total_intl_minutes],
        "Total intl calls": [total_intl_calls],
        "Customer service calls": [customer_service_calls]
    })

    # Numerical columns for scaling
    numerical_cols = [
        "Account length",
        "Number vmail messages",
        "Total day minutes",
        "Total day calls",
        "Total eve minutes",
        "Total eve calls",
        "Total night minutes",
        "Total night calls",
        "Total intl minutes",
        "Total intl calls",
        "Customer service calls"
    ]

    # Apply scaling
    input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])

    # Make prediction
    prediction = model_random.predict(input_df)

    # Show result
    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("This customer is likely to churn!")
    else:
        st.success("The customer is likely to continue!")