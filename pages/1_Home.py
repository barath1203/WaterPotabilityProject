import streamlit as st

# ----------------------------------------
# 🌊 Page Setup
# ----------------------------------------
st.set_page_config(page_title="About | Water Potability", page_icon="💧", layout="centered")

# ----------------------------------------
# 🌈 Custom CSS Styling
# ----------------------------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #e0f7fa 0%, #b3e5fc 100%);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 2.5rem;
        color: #01579b;
        font-weight: 800;
        margin-top: 0.5rem;
        margin-bottom: 1rem;
    }
    .subtitle {
        text-align: center;
        color: #0277bd;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .section {
        background: rgba(255, 255, 255, 0.9);
        padding: 1.8rem;
        border-radius: 18px;
        box-shadow: 0 5px 15px rgba(0, 100, 200, 0.1);
        line-height: 1.6;
    }
    h3 {
        color: #01579b;
        margin-top: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------
# 🌍 Header
# ----------------------------------------
st.markdown('<h1 class="title">💧 About This Project</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Empowering clean water awareness through technology</p>', unsafe_allow_html=True)

# ----------------------------------------
# 💡 Project Overview
# ----------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.write("""
### 🌍 Project Overview  
Access to clean water is a basic human need.  
This project uses **Machine Learning (Random Forest Classifier)** to predict if a given water sample is **potable (safe to drink)** based on its physical and chemical parameters.

The system analyzes real-world data such as **pH, hardness, solids, chloramines, sulfate, and turbidity** to make accurate predictions.  
It aims to support:
- 🧪 **Quick water quality assessment**  
- 💧 **Eco-friendly awareness**  
- 🌿 **Sustainable water management**
""")
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------
# ⚙️ Technology Stack
# ----------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.write("""
### ⚙️ Technology Stack  
- **Python** 🐍 — Core programming language  
- **Streamlit** 🌐 — Interactive web app framework  
- **Scikit-learn** 🤖 — Machine learning modeling (Random Forest)  
- **Pandas & NumPy** 📊 — Data preprocessing and manipulation  
- **Matplotlib & Seaborn** 🎨 — Data visualization  
""")
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------
# 🚀 Future Scope
# ----------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.write("""
### 🚀 Future Scope  
- 🌦️ Integrate with **real-time water sensors** for continuous monitoring  
- 📱 Build a **mobile version** for on-site testing  
- ☁️ Deploy on **cloud platforms** for community access  
- 🔬 Expand dataset to include **biological parameters** and regional trends  
""")
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------
# ✨ Footer
# ----------------------------------------
st.markdown("---")
st.caption("💧 Developed for Water Potability & Eco Awareness Initiative | Powered by Random Forest ML Model")