# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 21:21:49 2022

@author: CSausi
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 

#from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Geography_Germany, Geography_Spain, Gender_Male):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Geography_Germany, Geography_Spain, Gender_Male]])
    print(prediction)
    return prediction



def main():
    st.title("Churn Model")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Churn ML App </h2>
    </div>
    """
    '', '', '', '', '', '','', '', '', '', ''
    st.markdown(html_temp,unsafe_allow_html=True)
    CreditScore = st.text_input("CreditScore","Type Here")
    Age = st.text_input("Age","Type Here")
    Tenure = st.text_input("Tenure","Type Here")
    Balance = st.text_input("Balance","Type Here") 
    NumOfProducts = st.text_input("NumOfProducts","Type Here") 
    HasCrCard = st.text_input("HasCrCard","Type Here") 
    IsActiveMember = st.text_input("IsActiveMember","Type Here") 
    EstimatedSalary = st.text_input("EstimatedSalary","Type Here")
    Geography_Germany = st.text_input("Geography_Germany","Type Here")
    Geography_Spain = st.text_input("Geography_Spain","Type Here")
    Gender_Male = st.text_input("Gender_Male","Type Here")  
    
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Geography_Germany, Geography_Spain, Gender_Male)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()