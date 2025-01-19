import pickle
import streamlit as st

model = pickle.load(open('estimasi_latop.sav', 'rb'))

st.title('Estimasi Harga Laptop')

brand = st.number_input('Input Brand ')
processor = st.number_input('Input processor ')
ram = st.number_input('Input ram ')
storage = st.number_input('Input storage ')
screen = st.number_input('Input screen ')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[brand,processor,ram,storage,screen]]
    )
    st.write('Estimasi Harga Laptop Dalam INR : ', predict)
    st.write('Estimasi Harga Laptop Dalam INR : ', predict*190)