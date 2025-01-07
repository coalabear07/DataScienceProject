# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 22:51:55 2025

@author: hp
"""

import numpy as np
import pickle
import streamlit


loaded_model = pickle.load(open("C:/Users/hp/JPN/randomforest.sav","rb"))
loaded_scaler = pickle.load(open("C:/Users/hp/JPN/scaler.sav","rb"))

# creating function for prediction

def fraud_detection(input_data):
    
    
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    input_data_scaled = loaded_scaler.transform(input_data_reshaped)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0] == 0) :
        return "The transaction is legal"
    else:
        return "The transaction in fraudulent transaction"


def main():
    
    #Title
    st.title('Fraudulent Transaction Prediction')
    
    Amount = st.text_input("Amount of Transaction")
    Merchant_lat = st.text_input("Latitude of the Merchant")
    Merchant_long = st.text_input("Longitude of the Merchant")
    Zip = st.text_input("Zip")
    category_food_dining = st.text_input("category_food_dining")
    category_gas_transport = st.text_input("category_gas_transport")
    category_grocery_net = st.text_input("category_grocery_net")
    category_grocery_pos = st.text_input("category_grocery_pos")
    category_home = st.text_input("category_home")
    category_misc_net = st.text_input("category_misc_net")
    category_misc_pos = st.text_input("category_misc_pos")
    category_personal_care = st.text_input("category_personal_care")
    category_shopping_net = st.text_input("category_shopping_net")
    category_shopping_pos = st.text_input("category_shopping_pos")
    category_travel = st.text_input("category_travel")
    
    #code for predcition
    diagnosis = ''
    
    #craeting a button for prediction
    
    if st.buttton("Transaction Test Result"):
        diagnosis = fraud_detection([Amount,Merchant_lat,Merchant_long,Zip,category_food_dining,
                                     category_gas_transport,category_grocery_net,
                                     category_grocery_pos,category_home,category_misc_net,
                                     category_misc_pos,category_personal_care,category_shopping_net,
                                     category_shopping_pos,category_travel])


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    