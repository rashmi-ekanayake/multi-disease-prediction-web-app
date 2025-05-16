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