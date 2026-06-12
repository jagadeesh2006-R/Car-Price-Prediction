import streamlit as st # type: ignore
import pickle
import pandas as pd # type: ignore

# Load model
model = pickle.load(open('model.pkl','rb'))
st.set_page_config(
    page_title="Car Price Predictor",
    layout="wide"
)
st.title("🚗 Car Price Prediction System")
st.write("Enter car details to predict selling price.")
# Inputs
year = st.number_input("Manufacturing Year", 2000, 2025)

km_driven = st.number_input("Kilometers Driven", min_value=0)

fuel = st.selectbox(
    "Fuel Type",
    ["Diesel", "Electric", "LPG", "Petrol"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Individual", "Trustmark Dealer", "Dealer"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner = st.selectbox(
    "Owner",
    [
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth & Above Owner",
        "Test Drive Car"
    ]
)
from datetime import datetime

current_year = datetime.now().year
car_age = current_year - year

data = pd.DataFrame({
    'km_driven':[km_driven],
    'Car_Age':[car_age],

    'fuel_Diesel':[0],
    'fuel_Electric':[0],
    'fuel_LPG':[0],
    'fuel_Petrol':[0],

    'seller_type_Individual':[0],
    'seller_type_Trustmark Dealer':[0],

    'transmission_Manual':[0],

    'owner_Fourth & Above Owner':[0],
    'owner_Second Owner':[0],
    'owner_Test Drive Car':[0],
    'owner_Third Owner':[0]
})
# Fuel
if fuel == "Diesel":
    data['fuel_Diesel'] = 1
elif fuel == "Electric":
    data['fuel_Electric'] = 1
elif fuel == "LPG":
    data['fuel_LPG'] = 1
elif fuel == "Petrol":
    data['fuel_Petrol'] = 1

# Seller Type
if seller_type == "Individual":
    data['seller_type_Individual'] = 1
elif seller_type == "Trustmark Dealer":
    data['seller_type_Trustmark Dealer'] = 1

# Transmission
if transmission == "Manual":
    data['transmission_Manual'] = 1

# Owner
if owner == "Second Owner":
    data['owner_Second Owner'] = 1
elif owner == "Third Owner":
    data['owner_Third Owner'] = 1
elif owner == "Fourth & Above Owner":
    data['owner_Fourth & Above Owner'] = 1
elif owner == "Test Drive Car":
    data['owner_Test Drive Car'] = 1
prediction = model.predict(data)
st.success(
    f"Predicted Car Price: ₹ {prediction[0]:,.2f}"
)