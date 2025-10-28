# 💧 Eco Water Potability & Eco Awareness 🌿

An AI-powered web app that predicts whether a water sample is **potable (safe to drink)** or not — using a trained **Random Forest Classifier**.  
Built with **Python + Streamlit**, and trained on the [Water Potability Dataset](https://www.kaggle.com/datasets/adityakadiwal/water-potability).

---

## 🌍 Live App
Deployed via Streamlit Cloud :
👉 [**Click to Open the App**](https://waterpotabilityproject-t36paphdyrp6xm8357tzyn.streamlit.app/Predict)

---

## 🚀 Features
- 🔍 Predict if water is **potable** based on 9 chemical parameters  
- ⚗️ ML model trained with **Random Forest** and **SMOTE balancing**  
- 🌱 Clean, eco-friendly UI built with Streamlit  
- 📊 Includes dataset exploration and model training notebook  

---

## 📊 Dataset
**Source:** [Kaggle - Water Potability Dataset](https://www.kaggle.com/datasets/adityakadiwal/water-potability)

**Features Used**
| Parameter | Description |
|------------|-------------|
| pH | Acidity/alkalinity of water |
| Hardness | Calcium & magnesium salts |
| Solids | Total dissolved solids |
| Chloramines | Amount of disinfectant |
| Sulfate | Sulfate ions concentration |
| Conductivity | Water’s ionic ability |
| Organic Carbon | Carbon content in water |
| Trihalomethanes | By-products from disinfection |
| Turbidity | Cloudiness due to particles |

---

## 🧠 Model Overview
- **Algorithm:** Random Forest Classifier  
- **Data Balancing:** SMOTE  
- **Accuracy:** ~65%  
- **ROC-AUC:** 0.67  



---

## 🧰 Tech Stack
- **Frontend:** Streamlit  
- **ML Framework:** Scikit-learn  
- **Data Handling:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn  

---

## 🧪 How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/barath1203/WaterPotabilityProject.git
cd WaterPotabilityProject

2)Install Dependencies

 pip install -r requirements.txt

3)Run the Streamlit Web App
 streamlit run app.py
