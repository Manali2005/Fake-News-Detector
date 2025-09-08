# 📰 Fake News Detector (Machine Learning + Streamlit)

## 📌 Overview
This is a **Fake News Detection Web App** built using **Machine Learning** and **Streamlit**.  
It helps classify whether a news article is **Real ✅** or **Fake ❌**.

## 🚀 Features
- Paste any news article and instantly check authenticity
- Built using Logistic Regression
- Elegant Dark Theme UI with Streamlit
- Uses TF-IDF vectorizer for text preprocessing

## 🛠 Tech Stack
- Python
- Scikit-learn
- Streamlit
- Joblib
- NumPy, Pandas
- Matplotlib

## 📂 Project Structure
news-prediction-project/
├── app.py # Main Streamlit app
├── lr_model.jb # Trained Logistic Regression model
├── vectorizer.jb # TF-IDF vectorizer
├── requirements.txt # Dependencies
└── README.md # Project documentation

How to run:
1.Install requirements:
pip install -r requirements.txt

2.Run the app:
streamlit run app.py

3.Open in browser:
http://localhost:8501
