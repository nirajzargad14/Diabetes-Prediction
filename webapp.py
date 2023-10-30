import numpy as np
import pickle
import streamlit as st

# Load the pre-trained model
loaded_model = pickle.load(open('D:/ML Mini Project/trained_model.sav', 'rb'))

def diabetes_prediction(input_data):
    # ... (no changes needed in this function)
    input_data_as_numpy_array = np.asarray(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape (1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    
    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

def main():
    st.title('Diabetes Prediction')
    st.write("Enter the details of the patient: ")

    with st.form('user_input'):
        col1, col2 = st.columns(2)
        with col1:
            pregnancies = st.text_input('Number of Pregnancies')
            glucose = st.text_input('Glucose Level')
            blood_pressure = st.text_input('Blood Pressure')
            skin_thickness = st.text_input('Skin Thickness')
        with col2:
            insulin = st.text_input('Insulin Level')
            bmi = st.text_input('BMI')
            dpf = st.text_input('Diabetes Pedigree Function')
            age = st.text_input('Age')
        submit_button = st.form_submit_button('Predict Result')

    diagnosis = ''

    # Check if the button was clicked
    if submit_button:
        if not (pregnancies and glucose and blood_pressure and skin_thickness and insulin and bmi and dpf and age):
            st.error("Please fill in all the fields.")
        else:
            diagnosis = diabetes_prediction([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age])
            st.info(f"Prediction: {diagnosis}")

    st.sidebar.write("Mini Project Title: Diabetes Prediction")
    st.sidebar.write("")
    st.sidebar.write("Group Information:")
    st.sidebar.write(" 33178 - Vinayak Vairat")
    st.sidebar.write(" 33179 - Mahesh Wagh")
    st.sidebar.write(" 33181 - Niraj Zargad")

if __name__ == '__main__':
    main()