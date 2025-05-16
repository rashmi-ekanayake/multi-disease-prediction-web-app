import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved model

diabetes_model = pickle.load(open('C:/Users/Rashmi Ekanayaka/Desktop/Multiple Disease Prediction System/saved models/Diabates_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/Rashmi Ekanayaka/Desktop/Multiple Disease Prediction System/saved models/Heart_disease_model.sav','rb'))

pakinson_disease_model = pickle.load(open('C:/Users/Rashmi Ekanayaka/Desktop/Multiple Disease Prediction System/saved models/Pakinson_disease_model.sav','rb'))


# side bar navigation

with st.sidebar:
    
    selected = option_menu('Multiple Diseases Prediction System ',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Pakinson Prediction'],
                           
                           icons = ['activity','heart','person'],
                           
                           default_index = 0)

# Diabetes Prediction Page

if (selected =='Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')
    
