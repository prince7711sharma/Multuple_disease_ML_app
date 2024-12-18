# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:21:03 2024

@author: CCS
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the save data


diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
kidney_disease_model = pickle.load(open('kidney.pkl', 'rb'))
# sidebar for nacigation
st.sidebar.title('Disease Prediction')
with st.sidebar:st.sidebar.image('data:image/jpeg;base64,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',use_column_width=True)

with st.sidebar:
    
    selected = option_menu('Multiple Disease Pridiction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                           'Kidney disease'],
                           icons = ['activity','heart','person','droplet'],
                           default_index = 0)

with st.sidebar: st.sidebar.image('data:image/jpeg;base64,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',use_column_width=True)
    # diabetes prediction page
st.title('Multiple Disease Prediction')
st.image('data:image/jpeg;base64,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',use_column_width=True)    
    
if(selected == 'Diabetes Prediction'):
    
    #page title
    
    st.title('Diabetes Prediction using ML')
    
    # column for input feilds
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2:
        Insulin = st.text_input('Insulin level')
        
    with col3:
        BMI = st.text_input('BMI level')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for pridiction
    diab_diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if(diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'
            
        else:
            diab_diagnosis = 'The person is Not Diabetic'
            
    st.success(diab_diagnosis)
 
if(selected == 'Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction using ML')
    
    # column for input feilds
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain trypes')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Chilestrol in mg/dl')
        
    with col3:
        fbs = st.text_input('FASTING BLOOD sugar >120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Meart Rate achieved')
    
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('that: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
   
        
    
    # code for pridiction
    heart_diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Heart disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if(heart_prediction[0] == 1):
            heart_diagnosis = 'The person has heart disease'
            
        else:
            heart_diagnosis = 'The person not has heart disease'
            
    st.success(heart_diagnosis)
 
# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        #user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
  
if(selected == 'Kidney disease'):
    
    #page title
    st.title('Cronical Kidney Disease Prediction using ML')
    
    # column for input feilds
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
       age = st.text_input('Age')

    with col2:
       blood_pressure = st.text_input('Blood Pressure')

    with col3:
       specific_gravity = st.text_input('Specific Gravity')

    with col4:
       albumin = st.text_input('Albumin')

    with col5:
       sugar = st.text_input('Sugar')

    with col1:
        red_blood_cells = st.text_input('Red Blood Cell')

    with col2:
       pus_cell = st.text_input('Pus Cell')

    with col3:
       pus_cell_clumps = st.text_input('Pus Cell Clumps')

    with col4:
       bacteria = st.text_input('Bacteria')

    with col5:
       blood_glucose_random = st.text_input('Blood Glucose Random')

    with col1:
       blood_urea = st.text_input('Blood Urea')

    with col2:
       serum_creatinine = st.text_input('Serum Creatinine')

    with col3:
       sodium = st.text_input('Sodium')

    with col4:
       potassium = st.text_input('Potassium')

    with col5:
       haemoglobin = st.text_input('Haemoglobin')

    with col1:
       packed_cell_volume = st.text_input('Packet Cell Volume')

    with col2:
       white_blood_cell_count = st.text_input('White Blood Cell Count')

    with col3:
       red_blood_cell_count = st.text_input('Red Blood Cell Count')

    with col4:
       hypertension = st.text_input('Hypertension')

    with col5:
       diabetes_mellitus = st.text_input('Diabetes Mellitus')

    with col1:
       coronary_artery_disease = st.text_input('Coronary Artery Disease')

    with col2:
       appetite = st.text_input('Appetitte')

    with col3:
       peda_edema = st.text_input('Peda Edema')
    with col4:
       aanemia = st.text_input('Aanemia')
    
    # code for pridiction
    kindey_diagnosis = ''
    
   
    if st.button("Kidney's Test Result"):

       user_input = [age, blood_pressure, specific_gravity, albumin, sugar,
      red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
      blood_glucose_random, blood_urea, serum_creatinine, sodium,
      potassium, haemoglobin, packed_cell_volume,
      white_blood_cell_count, red_blood_cell_count, hypertension,
      diabetes_mellitus, coronary_artery_disease, appetite,
      peda_edema, aanemia]

       user_input = [float(x) for x in user_input]

       prediction = kidney_disease_model.predict([user_input])

       if prediction[0] == 1:
           kindey_diagnosis = "The person has Kidney's disease"
       else:
           kindey_diagnosis = "The person does not have Kidney's disease"
    st.success(kindey_diagnosis)
 

