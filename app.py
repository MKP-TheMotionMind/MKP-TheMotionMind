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

# 1. Use st.form + session_state (key for mobile stability)
with st.form("mobile_friendly_form"):
    stride_length = st.number_input(
        "Enter Stride Length (meters):",
        min_value=1.0,
        max_value=3.0,
        step=0.01,
        value=st.session_state.get("last_input", 1.0), # Remembers last input
        key="mobile_input"
    )
    
    if st.form_submit_button("Predict"):
        st.session_state.last_input = stride_length # Save for next run
        result = predict_time(stride_length)
        st.session_state.last_result = result # Store result

# 2. Display result OUTSIDE form (avoids mobile refresh)
if "last_result" in st.session_state:
    st.write(st.session_state.last_result)

# 3. Mobile-specific optimizations
st.markdown("""
<style>
/* Prevent mobile zoom-in on input */
input[type="number"] {
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)



