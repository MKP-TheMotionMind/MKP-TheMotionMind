import streamlit as st
import joblib
import numpy as np

# Load model with cache (critical for mobile)
@st.cache_resource
def load_model():
    return joblib.load("StrideX_AI_fixed.pkl")

model = load_model()

def predict_time(stride_length):
    if stride_length < 1.5 or stride_length > 2.5:
        return "⚠️ Stride length out of range! Please enter between 1.5m-2.5m."
    else:
        prediction = model.predict(np.array([[stride_length]]))[0]
        return f"🏃 Predicted Time: {prediction:.2f} sec"

# --- Mobile-Friendly UI ---
st.title("StrideX AI: Sprint Time Predictor")
st.markdown("Made by Prabhakar Manikantan : The_MotionMind")

# ====== CHANGE STARTS HERE ======
with st.form("prediction_form"):
    # Modified input field - now always starts fresh at 1.0
    stride_length = st.number_input(
        "Enter Stride Length (meters):",
        min_value=1.0,
        max_value=3.0,
        step=0.01,
        value=1.0, # Always reset to 1.0 instead of remembering last input
        key="stride_input"
    )
    
    if st.form_submit_button("Predict"):
        result = predict_time(stride_length)
        st.session_state.last_result = result # Store ONLY the result

# Display result outside form
if "last_result" in st.session_state:
    st.write(st.session_state.last_result)
# ====== CHANGE ENDS HERE ======

# (Keep your existing mobile CSS)
st.markdown("""
<style>
/* Prevent mobile zoom-in on input */
input[type="number"] {
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)




