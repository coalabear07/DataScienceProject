# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:59:11 2025

@author: hp
"""

import numpy as np
#import xgboost
import pickle
import streamlit as st
from datetime import datetime

# Load the trained model and scaler
loaded_model = pickle.load(open("xgboost.sav", "rb"))
loaded_scaler = pickle.load(open("scaler.sav", "rb"))

# Function for fraud detection
def fraud_detection(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    input_data_scaled = loaded_scaler.transform(input_data_reshaped)
    prediction = loaded_model.predict(input_data_scaled)

    if prediction[0] == 0:
        return "This transaction is legit"
    else:
        return "This transaction is fraudulent"

# Main function
def main():
    # Title
    st.title("Fraudulent Transaction Prediction")

    # Input fields
    # Transaction Date Input
    transaction_date_input = st.text_input("Enter the Transaction Date (DD-MM-YYYY):", placeholder="e.g., 25-12-2022")

    # Optional: Birthdate Input for Age Calculation
    birth_date_input = st.text_input("Enter the Birth Date (DD-MM-YYYY, optional):", placeholder="e.g., 15-08-1990")

    # Validate and Process Input
    if transaction_date_input:
        try:
            # Convert transaction date input to datetime
            transaction_date = datetime.strptime(transaction_date_input, "%d-%m-%Y")
            st.success(f"Transaction Date: {transaction_date.strftime('%d-%m-%Y')}")
    
            # Extract Month and Year from Transaction Date
            Month = transaction_date.month
            Year = transaction_date.year
    
            st.write(f"Month of Transaction: {Month}")
            st.write(f"Year of Transaction: {Year}")
        except ValueError:
            st.error("Invalid Transaction Date format. Please use DD-MM-YYYY.")
            
        # Process Age Calculation if Birthdate is Provided
    if birth_date_input:
        try:
            # Convert birthdate input to datetime
            birth_date = datetime.strptime(birth_date_input, "%d-%m-%Y")
            st.success(f"Birth Date: {birth_date.strftime('%d-%m-%Y')}")
    
            # Calculate Age
            age = transaction_date.year - birth_date.year
            if (transaction_date.month, transaction_date.day) < (birth_date.month, birth_date.day):
                age -= 1
    
            st.write(f"Age at the Time of Transaction: {age} years")
        except ValueError:
            st.error("Invalid Birth Date format. Please use DD-MM-YYYY.")
            
    Zip = st.text_input("Zip of User")
    Merchant_lat = st.text_input("Latitude of the Merchant")
    Merchant_long = st.text_input("Longitude of the Merchant")
    Amount = st.text_input("Amount of Transaction")

    # Dropdown for category selection
    categories = [
        "food dining", "gas transport", "grocery net",
        "grocery pos", "health fitness", "home",
        "kids pets", "misc net", "misc pos",
        "personal care", "shopping net", "shopping pos",
        "travel","entertainment"
    ]
    selected_category = st.selectbox("Select the transaction category:", categories)

    if(selected_category == "food dining"):
        input_data = [Amount,Zip,Merchant_lat,Merchant_long,Year,Month,age,1,0,0,0,0,0,0,0,0,0,0,0,0]
    elif(selected_category == "gas transport"):
        input_data = [Amount,Zip,Merchant_lat,Merchant_long,Year,Month,age,0,1,0,0,0,0,0,0,0,0,0,0,0]
    elif(selected_category == "grocery net"):
        input_data = [Amount,Zip,Merchant_lat,Merchant_long,Year,Month,age,0,0,1,0,0,0,0,0,0,0,0,0,0]
    elif(selected_category == "grocery pos"):
        input_data = [Amount,Zip,Merchant_lat,Merchant_long,Year,Month,age,0,0,0,1,0,0,0,0,0,0,0,0,0]
    elif(selected_category == "health fitness"):
        input_data = [Amount,Zip,Merchant_lat,Merchant_long,Year,Month,age,0,0,0,0,1,0,0,0,0,0,0,0,0]
    elif(selected_category == "home"):
        input_data = [Amount,Zip,Merchant_lat,Merchant_long,Year,Month,age,0,0,0,0,0,1,0,0,0,0,0,0,0]
    elif(selected_category == "kids pets"):
        input_data = [Amount,Zip,Merchant_lat,Merchant_long,Year,Month,age,0,0,0,0,0,0,1,0,0,0,0,0,0]
    elif(selected_category == "misc net"):
        input_data = [Amount,Zip,Merchant_lat,Merchant_long,Year,Month,age,0,0,0,0,0,0,0,1,0,0,0,0,0]
    elif(selected_category == "misc pos"):
        input_data = [Amount,Zip,Merchant_lat,Merchant_long,Year,Month,age,0,0,0,0,0,0,0,0,1,0,0,0,0]
    elif(selected_category == "personal care"):
        input_data = [Amount,Zip,Merchant_lat,Merchant_long,Year,Month,age,0,0,0,0,0,0,0,0,0,1,0,0,0]
    elif(selected_category == "shopping net"):
        input_data = [Amount,Zip,Merchant_lat,Merchant_long,Year,Month,age,0,0,0,0,0,0,0,0,0,0,1,0,0]
    elif(selected_category == "shopping pos"):
        input_data = [Amount,Zip,Merchant_lat,Merchant_long,Year,Month,age,0,0,0,0,0,0,0,0,0,0,0,1,0]
    elif(selected_category == "travel"):
        input_data = [Amount,Zip,Merchant_lat,Merchant_long,Year,Month,age,0,0,0,0,0,0,0,0,0,0,0,0,1]
    else:
        input_data = [Amount,Zip,Merchant_lat,Merchant_long,Year,Month,age,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    diagnosis = ''
    
    # Prediction button
    if st.button("Transaction Test Result"):
        diagnosis = fraud_detection(input_data)
    st.success(diagnosis)


