import streamlit as st
import joblib
from utils import extract_features
import pandas as pd

# Load the trained model
model_file = "datas/phishing_model_fixed.pkl"
model = joblib.load(model_file)
st.set_page_config(page_title="Phishing Detection System", page_icon="🔐",layout="centered")

# Streamlit App
st.title("🔐 Phishing Detection System")
st.write("Predict if a URL is phishing or legitimate.")

# URL Input
user_url = st.text_input("Enter a URL to check:")


with st.expander("📚 How It Works"):
    st.write("""
    This app uses a Machine Learning model to classify URLs as **Phishing** or **Legitimate**.
    The model extracts features like **URL length**, **number of dots**, **presence of IP address**, 
    and **special characters** to make predictions.
    """)


if st.button("Check URL"):
    if user_url:
        # Extract features
        features = extract_features(user_url)
        features_df = pd.DataFrame([features])

        # Make prediction
        prediction = model.predict(features_df)[0]
        confidence = model.predict_proba(features_df)[0]

        

        st.write("Extracted Features:", features_df.columns)

        # Display the result
        if prediction == 1:
            st.error(f"🚨 This URL is likely **Phishing** with a confidence of {confidence[1]:.2f}")
        else:
            st.success(f"✅ This URL is likely **Legitimate** with a confidence of {confidence[0]:.2f}")
    else:
        st.warning("⚠️ Please enter a URL to check.")





st.markdown("---")
st.caption("Built with ❤️ using Streamlit | https://github.com/nishat09")
