import streamlit as st
import numpy as np
import pandas as pd
import joblib

# ========================================
# 💧 Page Configuration & Styling
# ========================================
st.set_page_config(page_title="AI Water Potability Analysis", page_icon="💧", layout="centered")

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #c2e9fb 0%, #a1c4fd 100%);
        font-family: 'Segoe UI', sans-serif;
    }
    .form-container {
        background-color: rgba(255, 255, 255, 0.96);
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 8px 25px rgba(0, 100, 180, 0.15);
        margin-top: 20px;
        transition: 0.3s;
    }
    .form-container:hover {
        box-shadow: 0 10px 30px rgba(0, 120, 200, 0.25);
    }
    .title {
        color: #01579b;
        text-align: center;
        font-weight: 800;
        font-size: 2rem;
        margin-bottom: 1rem;
    }
    .note {
        text-align: center;
        color: #0277bd;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# ========================================
# 🧠 Load Model & Preprocessing
# ========================================
model = joblib.load('rf_model.joblib')
imputer = joblib.load('imputer.joblib')
scaler = joblib.load('scaler.joblib')

# ========================================
# 🧾 Title and Description
# ========================================
st.markdown('<h1 class="title">💧 AI-Based Water Potability Analysis System</h1>', unsafe_allow_html=True)
st.markdown('<p class="note">Enter the water quality parameters below to check if the sample is potable or not.</p>', unsafe_allow_html=True)

st.markdown('<div class="form-container">', unsafe_allow_html=True)

# ========================================
# 🧪 Input Section
# ========================================
col1, col2, col3 = st.columns(3)

with col1:
    ph = st.number_input("pH (Ideal: 6.5–8.5)", 0.0, 14.0, 7.0)
    hardness = st.number_input("Hardness (mg/L)", 0.0, 500.0, 200.0)
    solids = st.number_input("Solids (ppm)", 0.0, 60000.0, 20000.0)

with col2:
    chloramines = st.number_input("Chloramines (mg/L)", 0.0, 15.0, 8.0)
    sulfate = st.number_input("Sulfate (mg/L)", 0.0, 500.0, 300.0)
    conductivity = st.number_input("Conductivity (μS/cm)", 0.0, 1000.0, 400.0)

with col3:
    organic_carbon = st.number_input("Organic Carbon (mg/L)", 0.0, 30.0, 10.0)
    trihalomethanes = st.number_input("Trihalomethanes (μg/L)", 0.0, 120.0, 70.0)
    turbidity = st.number_input("Turbidity (NTU)", 0.0, 10.0, 3.0)

st.markdown('</div>', unsafe_allow_html=True)

# ========================================
# 🔍 Prediction Logic
# ========================================
if st.button("🔍 Predict Potability", use_container_width=True):
    cols = ['ph','Hardness','Solids','Chloramines','Sulfate','Conductivity',
            'Organic_carbon','Trihalomethanes','Turbidity']

    arr = np.array([[ph, hardness, solids, chloramines, sulfate,
                     conductivity, organic_carbon, trihalomethanes, turbidity]])
    
    arr_imp = imputer.transform(arr)
    arr_scaled = scaler.transform(arr_imp)
    proba = model.predict_proba(arr_scaled)[0][1]
    pred = int(proba >= 0.5)

    # ========================================
    # 🎯 Display Result Summary
    # ========================================
    st.markdown("---")
    st.subheader("🔎 Prediction Summary")

    df_input = pd.DataFrame(arr, columns=cols)
    st.write("### Input Parameters")
    st.dataframe(df_input.style.format("{:.2f}"))

    if pred == 1:
        st.success("✅ **Potable (Safe to Drink)** 💧")
        st.progress(float(proba))
        st.markdown(f"**Confidence Level:** {proba*100:.2f}%")
        st.balloons()
        st.markdown("""
        ✅ The sample water meets safe drinking standards.
        - Acceptable range for most chemical parameters.
        - Physicochemical quality within WHO standards.
        """)
    else:
        st.error("🚱 **Not Potable (Unsafe to Drink)** ⚠️")
        st.progress(float(1 - proba))
        st.markdown(f"**Confidence Level:** {(1 - proba)*100:.2f}%")
        st.markdown("""
        ⚠️ The water sample may not be suitable for consumption due to:
        - High solids, hardness, or organic carbon  
        - Abnormal pH or chloramine content  
        - Poor turbidity or conductivity values  
        """)

    # ========================================
    # 🧪 Example Test Case
    # ========================================
    st.markdown("---")
    st.header("🧪 Example Test Case")
    st.markdown("""
    **Example Input:**  
    - pH: 7.2  
    - Hardness: 190 mg/L  
    - Solids: 22000 ppm  
    - Chloramines: 6.8 mg/L  
    - Sulfate: 300 mg/L  
    - Conductivity: 420 μS/cm  
    - Organic Carbon: 9.5 mg/L  
    - Trihalomethanes: 68 μg/L  
    - Turbidity: 3.1 NTU  

    **Expected Result:** ✅ Potable (Safe to Drink)
    """)

# ========================================
# 🌿 Footer
# ========================================
st.markdown("---")
st.caption("💧AI Project on Water Potability & Eco Awareness")
