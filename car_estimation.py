import pickle
import streamlit as st

model = pickle.load(open('car_estimation.sav', 'rb'))

st.title('Used Car Price Estimation')

year = st.number_input('Year of Car')
mileage = st.number_input('Car Mileage (km)')
tax = st.number_input('Tax of Car')
mpg = st.number_input('Miles per Gallon')
engineSize = st.number_input('Engine Size')

predict = ''

if st.button('Price Estimation'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write('Estimated price of used cars in Ponds: ', predict)
    st.write('Estimated price of used cars in IDR (Million): ', predict*19000)