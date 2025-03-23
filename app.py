import pickle
import streamlit as st
import numpy as np

# Load the pre-trained model
try:
    with open("classifier.pkl", "rb") as pickle_in:
        classifier = pickle.load(pickle_in)
except FileNotFoundError:
    st.error("Error: The model file 'classifier.pkl' was not found.")
    st.stop()

def predict_sales(tv, radio, newspaper):
    """Predict sales based on TV, Radio, and Newspaper advertising budget."""
    try:
        prediction = classifier.predict(np.array([[tv, radio, newspaper]]))
        return prediction[0]
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None

def main():
    st.set_page_config(page_title="Sales Prediction App", layout="centered")
    st.title("📈 Sales Prediction App")

    st.markdown("""
    <div style="background-color:#ff4d4d;padding:10px;border-radius:10px">
    <h2 style="color:white;text-align:center;">Sales Predictor ML App</h2>
    </div>
    """, unsafe_allow_html=True)

    # Input fields with number input
    tv = st.number_input("TV Advertising Budget ($)", min_value=0.0, format="%.2f")
    radio = st.number_input("Radio Advertising Budget ($)", min_value=0.0, format="%.2f")
    newspaper = st.number_input("Newspaper Advertising Budget ($)", min_value=0.0, format="%.2f")

    result = None

    if st.button("🔍 Predict"):
        result = predict_sales(tv, radio, newspaper)
        if result is not None:
            st.success(f"📊 Predicted Sales: **${result:.2f}**")

    if st.button("ℹ️ About"):
        st.info("This app predicts sales based on advertising budgets using a Machine Learning model trained on historical data.")

if __name__ == '__main__':
    main()
