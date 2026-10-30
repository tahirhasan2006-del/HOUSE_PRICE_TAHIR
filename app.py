import streamlit as st
import joblib
import numpy as np
import warnings
warnings.filterwarnings("ignore")

model=joblib.load("Random_search.pkl")#Uploding the Optimized Machine Learning model

st.title(" House Price Prediction ")
st.markdown("---")

bedroom = st.number_input("Enter the number of bedroom",min_value=0,value=0)

bathroom = st.number_input("Enter the number of bathroom",min_value=0,value=0)

living_area =st.number_input("Enter the living area",min_value=0,value=2000)

condition_of_house=st.number_input("Condition of house",min_value=0,value=3)

number_of_school=st.number_input("School min value",min_value=0,value=0)

st.markdown("---")

x=[[bedroom,bathroom,living_area,condition_of_house,number_of_school]]

prediction=st.button("Predict")

if prediction == True:
    X_array=np.array(x)
    price = int(model.predict(X_array)[0])
    st.write(f"House price={price}")

else:
    st.write("Please click on the predict button")
