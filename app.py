import streamlit as st
from PIL import Image

# ------------------------------------------------
# 🌊 Page Configuration
# ------------------------------------------------
st.set_page_config(
    page_title="💧 Water Potability & Eco Awareness",
    page_icon="💧",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------
# 🌍 Home Page Layout
# ------------------------------------------------
def main():
    st.title("💧 Water Potability & Eco Awareness App")

    st.markdown("""
    Welcome to the **Water Potability Prediction System** 🌱  

    This AI-powered app helps you:
    - 🔍 **Predict** if a water sample is safe to drink  
    - 🌿 **Learn** how water quality impacts the environment  
    - 👨‍💻 **Explore** insights about the developer behind this project  

    Use the **sidebar menu** on the left to navigate between:
    👉 *Home*, *Predict Potability*, and *About*
    """)

    # ------------------------------------------------
    # 🌅 Eco-Friendly Banner Image (Local or Online)
    # ------------------------------------------------
    try:
        # ✅ If you have a local image (recommended)
        image = Image.open("static/images/water_potability.webp")  
        st.image(image, use_container_width=True, caption="Clean Water, Healthy Earth 🌍")
    except:
        # 🌐 If local image not found, load online backup
        st.image(
            "https://www.martek-marine.com/wp-content/uploads/2023/06/potable-water-testing-1-jpeg.webp",
            use_container_width=True,
            caption="Clean Water, Healthy Earth 🌍"
        )

    # ------------------------------------------------
    # 💬 Footer Section
    # ------------------------------------------------
    st.markdown("---")
    st.markdown("""
    > 💧 *“Thousands have lived without love, not one without water.”* — W.H. Auden  

    
    """)

# ------------------------------------------------
# 🚀 Run App
# ------------------------------------------------
if __name__ == "__main__":
    main()