import streamlit as st

# -------------------------------
# 🌊 Page Configuration
# -------------------------------
st.set_page_config(page_title="About Eco Water Potability", page_icon="ℹ️", layout="centered")

# -------------------------------
# 💧 Custom Styling
# -------------------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #d6f5f5 0%, #cce7ff 100%);
    }
    .about-card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 1.8rem;
        border-radius: 20px;
        box-shadow: 0 6px 25px rgba(0,128,128,0.15);
        margin-top: 1.5rem;
        line-height: 1.6;
    }
    h1 {
        color: #025959;
        text-align: center;
        font-weight: 800;
        margin-bottom: 1rem;
    }
    h3 {
        color: #027368;
    }
    a {
        color: #006699;
        text-decoration: none;
        font-weight: 600;
    }
    a:hover {
        color: #0099cc;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# 🧾 About Section
# -------------------------------
st.markdown('<h1>ℹ️ About the Project</h1>', unsafe_allow_html=True)

st.markdown('<div class="about-card">', unsafe_allow_html=True)
st.write("""
### 📊 Dataset  
The project uses the **[Water Potability Dataset](https://www.kaggle.com/datasets/adityakadiwal/water-potability)** from Kaggle.  
It includes key chemical and physical parameters of water such as:
- pH  
- Hardness  
- Solids  
- Chloramines  
- Sulfate  
- Conductivity  
- Organic Carbon  
- Trihalomethanes  
- Turbidity  

These attributes help predict whether the water sample is **potable (safe to drink)**.
""")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# 🧠 Model Section
# -------------------------------
st.markdown('<div class="about-card">', unsafe_allow_html=True)
st.write("""
### 🤖 Machine Learning Model  
We implemented a **Random Forest Classifier**, enhanced with:
- ⚖️ **SMOTE (Synthetic Minority Oversampling)** for balancing the dataset  
- ⚙️ Feature scaling and data cleaning for reliable results  
- 🎯 Hyperparameter tuning for better accuracy  

**Model Performance:**
- Accuracy: ~68%  
- ROC-AUC: 0.70  
- Balanced Precision & Recall  

This ensures fair and accurate predictions even with initially imbalanced data.
""")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# 🌿 Purpose Section
# -------------------------------
st.markdown('<div class="about-card">', unsafe_allow_html=True)
st.write("""
### 🌍 Purpose  
Access to clean water is fundamental to health and sustainability.  
This project leverages **AI for environmental safety**, enabling:
- 🧪 Quick water quality assessments  
- 🌱 Awareness about safe water consumption  
- ♻️ Support for eco-conscious decisions in communities  
""")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# 👨‍💻 Developer Section
# -------------------------------
st.markdown('<div class="about-card">', unsafe_allow_html=True)
st.write("""
### 👨‍💻 Developers  
**Team Members:**
- 🧑‍💻 *Barath*  
- 👨‍💻 *Jaya Surya*  
- 👨‍💻 *Vaira Prakash*  
- 👨‍💻 *Saravana Goutham*  

> Passionate about building AI solutions that promote sustainability and health awareness.  
> Built using **Python, Streamlit, and Random Forest Classifier**.
""")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# 📬 Footer
# -------------------------------
st.markdown("---")
st.caption("© 2025 Eco Water Potability Project | Built with 💧 Streamlit | Clean Water, Healthy Earth 🌍")