# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import os

# loading the saved models

#diabetes_model = pickle.load(open('C:/Users/91900/Downloads/diabetes_model.sav', 'rb'))

#heart_disease_model = pickle.load(open('C:/Users/91900/Downloads/heart_disease_model.sav','rb'))


# File paths
diabetes_model_path = 'C:/Users/91900/Downloads/diabetes_model.sav/'
heart_disease_model_path = 'C:/Users/91900/Downloads/heart_disease_model.sav/'

# Load models
#diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))
#heart_disease_model = pickle.load(open(heart_disease_model_path, 'rb'))
diabetes_model_path = os.environ.get('DIABETES_MODEL_PATH')
heart_disease_model_path = os.environ.get('HEART_DISEASE_MODEL_PATH')

if diabetes_model_path is None or heart_disease_model_path is None:
    st.error("Model paths are not set. Set the environment variables DIABETES_MODEL_PATH and HEART_DISEASE_MODEL_PATH.")
else:
    diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))
    heart_disease_model = pickle.load(open(heart_disease_model_path, 'rb'))

# Check if files exist
#if os.path.exists(diabetes_model_path) and os.path.exists(heart_disease_model_path):
 #   print("Both pickle files exist.")

    # Check read permissions
  #  if os.access(diabetes_model_path, os.R_OK) and os.access(heart_disease_model_path, os.R_OK):
   #     print("Read permissions are granted.")

    #    try:
            # You've already loaded the models above, so no need to load them again here
     #       print("Models loaded successfully.")

      #  except Exception as e:
       #     print("Error loading models:", e)
   # else:
    #    print("Read permissions are not granted for one or both files.")

#else:
 #   print("One or both pickle files do not exist.")




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['activity','heart'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
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
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model_path.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model_path.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    


