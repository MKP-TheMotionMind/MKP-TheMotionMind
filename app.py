import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load("StrideX_AI_fixed.pkl")

# Define the prediction function with input limiting
def predict_time(stride_length):
    if stride_length < 1.5 or stride_length > 2.5:
        return "⚠️ Stride length out of range! Please enter a value between 1.5m and 2.5m."
    else:
        stride_array = np.array([[stride_length]]) # Convert to 2D array
        prediction = model.predict(stride_array)[0] # Predict sprint time
        return f"🏃 Predicted Sprint Time: {prediction:.2f} sec"

# Streamlit UI
st.title("StrideX AI: Sprint Time Predictor")

st.markdown("Made by Prabhakar Manikantan : The_MotionMind ")

# Get user input
stride_length = st.number_input("Enter Stride Length (meters):", min_value=1.0, max_value=3.0, step=0.01)

# Predict button
if st.button("Predict"):
    result = predict_time(stride_length)
    st.write(result)

