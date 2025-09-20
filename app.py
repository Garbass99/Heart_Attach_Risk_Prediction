import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image

# Load the trained model and scaler
model = joblib.load("Logistics_Model.pkl")
scaler = joblib.load("normlz.pkl")

# Set up the app
st.set_page_config(
    page_title="Heart Attack Risk Prediction",
    page_icon="❤️",
    layout="wide"
)

# Add custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #e63946;
        text-align: center;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #1d3557;
    }
    .prediction-box {
        background-color: #f1faee;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    .risk-high {
        color: #e63946;
        font-weight: bold;
        font-size: 1.5rem;
    }
    .risk-low {
        color: #2a9d8f;
        font-weight: bold;
        font-size: 1.5rem;
    }
    .recommendation-box {
        background-color: #a8dadc;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# App title and description
st.markdown('<h1 class="main-header">Heart Attack Risk Prediction</h1>', unsafe_allow_html=True)
st.write("""
This app predicts the risk of heart attack based on various health parameters.
Please fill in the details below to get your prediction and personalized recommendations.
""")

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    st.markdown('<h3 class="sub-header">Personal Information</h3>', unsafe_allow_html=True)
    age = st.slider("Age", 20, 100, 45)
    sex = st.radio("Sex", options=["Male", "Female"])
    
    st.markdown('<h3 class="sub-header">Health Metrics</h3>', unsafe_allow_html=True)
    cp = st.selectbox("Chest Pain Type", options=["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
    resting_bp = st.slider("Resting Blood Pressure (mm Hg)", 90, 200, 120)
    cholesterol = st.slider("Cholesterol (mg/dl)", 100, 400, 200)
    fasting_bs = st.radio("Fasting Blood Sugar > 120 mg/dl", options=["No", "Yes"])
    restecg = st.selectbox("Resting Electrocardiographic Results", options=["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])

with col2:
    st.markdown('<h3 class="sub-header">Exercise & ECG</h3>', unsafe_allow_html=True)
    max_hr = st.slider("Maximum Heart Rate Achieved", 60, 220, 150)
    exercise_angina = st.radio("Exercise Induced Angina", options=["No", "Yes"])
    oldpeak = st.slider("ST Depression Induced by Exercise", 0.0, 6.0, 1.0, step=0.1)
    st_slope = st.selectbox("Slope of Peak Exercise ST Segment", options=["Upsloping", "Flat", "Downsloping"])
    
    st.markdown('<h3 class="sub-header">Cardiac Details</h3>', unsafe_allow_html=True)
    num_vessels = st.slider("Number of Major Vessels Colored by Fluoroscopy", 0, 3, 0)
    thalassemia = st.selectbox("Thalassemia", options=["Normal", "Fixed Defect", "Reversible Defect"])

# Convert categorical inputs to numerical values
sex_num = 1 if sex == "Male" else 0
fasting_bs_num = 1 if fasting_bs == "Yes" else 0
exercise_angina_num = 1 if exercise_angina == "Yes" else 0

# Map chest pain type to numerical values
if cp == "Typical Angina":
    cp_num = 0
elif cp == "Atypical Angina":
    cp_num = 1
elif cp == "Non-anginal Pain":
    cp_num = 2
else:
    cp_num = 3

# Map resting ECG to numerical values
if restecg == "Normal":
    restecg_num = 0
elif restecg == "ST-T Wave Abnormality":
    restecg_num = 1
else:
    restecg_num = 2

# Map st_slope to numerical values
if st_slope == "Upsloping":
    st_slope_num = 0
elif st_slope == "Flat":
    st_slope_num = 1
else:
    st_slope_num = 2

# Map thalassemia to numerical values
if thalassemia == "Normal":
    thal_num = 1
elif thalassemia == "Fixed Defect":
    thal_num = 2
else:
    thal_num = 3

# Create feature array in the same order as the model expects
# Based on the error, your model expects 12 features, so we need to include all of them
features = np.array([[age, sex_num, cp_num, resting_bp, cholesterol, fasting_bs_num, 
                      restecg_num, max_hr, exercise_angina_num, oldpeak, st_slope_num, 
                      num_vessels, thal_num]])

# Check if we need to remove one feature (if the model was trained on 12 features but we have 13)
# This depends on how your original data was structured
# Typically, the heart dataset has 13 features + 1 target, so if your model expects 12, 
# you might need to remove one feature

# Try with 12 features first (remove the first feature which might be an index)
features_12 = features[:, :]  # Remove the first column (age)

# Scale the features
try:
    scaled_features = scaler.transform(features_12)
except ValueError as e:
    st.error(f"Feature mismatch error: {e}")
    st.info("Trying with all 13 features...")
    # If that doesn't work, try with all 13 features
    try:
        # You might need to retrain your scaler to handle 13 features
        scaled_features = scaler.transform(features)
    except:
        st.error("Could not transform features. Please check your model and scaler.")
        st.stop()

# Prediction button
if st.button("Predict Heart Attack Risk"):
    # Make prediction
    try:
        prediction = model.predict(scaled_features)
        prediction_proba = model.predict_proba(scaled_features)
        
        # Display results
        st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
        st.subheader("Prediction Result")
        
        if prediction[0] == 1:
            st.markdown('<p class="risk-high">High Risk of Heart Attack</p>', unsafe_allow_html=True)
            st.write(f"Probability: {prediction_proba[0][1]*100:.2f}%")
            
            # Recommendations for high risk
            st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
            st.subheader("Recommendations")
            st.write("""
            Based on your assessment, you appear to be at higher risk for heart disease. 
            We strongly recommend:
            
            - **Consult a cardiologist** for a comprehensive evaluation
            - **Adopt a heart-healthy diet** low in saturated fats and sodium
            - **Engage in regular physical activity** as recommended by your doctor
            - **Monitor your blood pressure and cholesterol** regularly
            - **Quit smoking** if you currently smoke
            - **Limit alcohol consumption**
            - **Manage stress** through meditation, yoga, or other relaxation techniques
            - **Maintain a healthy weight**
            
            Please remember that this is a screening tool, not a medical diagnosis. 
            Always consult with healthcare professionals for personalized advice.
            """)
            st.markdown('</div>', unsafe_allow_html=True)
            
        else:
            st.markdown('<p class="risk-low">Low Risk of Heart Attack</p>', unsafe_allow_html=True)
            st.write(f"Probability: {prediction_proba[0][0]*100:.2f}%")
            
            # Recommendations for low risk
            st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
            st.subheader("Recommendations")
            st.write("""
            Your assessment suggests a lower risk for heart disease. To maintain heart health:
            
            - **Continue with regular physical activity** (at least 150 minutes per week)
            - **Eat a balanced diet** rich in fruits, vegetables, and whole grains
            - **Maintain a healthy weight**
            - **Get regular health check-ups**
            - **Avoid smoking** and limit alcohol consumption
            - **Manage stress** effectively
            
            Even with a lower risk profile, maintaining heart-healthy habits is important 
            for long-term cardiovascular health.
            """)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"Prediction error: {e}")
        st.info("This might be due to a mismatch between the model's expected features and the provided features.")

# Add some information about heart health
st.markdown("---")
st.subheader("About Heart Health")
st.write("""
Heart disease is the leading cause of death worldwide. Key risk factors include:
- High blood pressure
- High cholesterol
- Smoking
- Diabetes
- Obesity
- Physical inactivity
- Family history of heart disease
- Age (risk increases with age)
- Stress

Regular check-ups and maintaining a healthy lifestyle can significantly reduce your risk.
""")

# Footer
st.markdown("---")
st.write("""
**Disclaimer**: This tool is for informational purposes only and is not a substitute for 
professional medical advice, diagnosis, or treatment. Always seek the advice of your 
physician or other qualified health provider with any questions you may have regarding 
a medical condition.
""")