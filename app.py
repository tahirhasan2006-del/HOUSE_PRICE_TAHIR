
import streamlit as st
import joblib
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# Page Configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Load ML Model
model = joblib.load("Random_search.pkl")

# Custom CSS
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #141E30, #243B55);
}

/* Main Title */
.title {
    text-align: center;
    color: white;
    font-size: 40px;
    font-weight: bold;
    padding: 20px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #D6EAF8;
    font-size: 17px;
    margin-bottom: 30px;
}

/* Input Labels */
label {
    color: white !important;
    font-size: 16px !important;
    font-weight: bold !important;
}

/* Input Box */
.stNumberInput input {
    background-color: #F0F3F4;
    color: #17202A;
    border-radius: 10px;
}

/* Predict Button */
.stButton button {
    width: 100%;
    background: linear-gradient(90deg, #00C9A7, #00A8E8);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px;
    font-size: 20px;
    font-weight: bold;
}

.stButton button:hover {
    background: linear-gradient(90deg, #00A8E8, #00C9A7);
    color: white;
    border: none;
}

/* Prediction Result */
.result {
    background: #D5F5E3;
    color: #145A32;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 25px;
    font-weight: bold;
    margin-top: 20px;
}

/* Footer */
.footer {
    text-align: center;
    color: #D6EAF8;
    font-size: 13px;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# Heading
st.markdown(
    '<div class="title">🏠 House Price Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Machine Learning Based House Price Estimation System</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# Input Section
st.subheader("🏡 Enter House Details")

bedroom = st.number_input(
    "Number of Bedrooms",
    min_value=0,
    value=0
)

bathroom = st.number_input(
    "Number of Bathrooms",
    min_value=0,
    value=0
)

living_area = st.number_input(
    "Living Area (Square Feet)",
    min_value=0,
    value=2000
)

condition_of_house = st.number_input(
    "Condition of House",
    min_value=0,
    value=3
)

number_of_school = st.number_input(
    "Number of Schools Nearby",
    min_value=0,
    value=0
)

st.markdown("---")

# Prediction Button
if st.button("🔍 Predict House Price"):

    x = [[
        bedroom,
        bathroom,
        living_area,
        condition_of_house,
        number_of_school
    ]]

    X_array = np.array(x)

    price = int(model.predict(X_array)[0])

    # Display Result
    st.markdown(
        f'<div class="result">🏠 Predicted House Price<br><br>₹ {price:,}</div>',
        unsafe_allow_html=True
    )

else:
    st.info("Please enter the house details and click the Predict button.")

# Footer
st.markdown("""
<div class="footer">
    House Price Prediction System | Powered by Machine Learning
</div>
""", unsafe_allow_html=True)
