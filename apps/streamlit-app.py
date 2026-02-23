import streamlit as st

st.title('My First Streamlit App')

age = st.number_input('Age', min_value=18, max_value=100, value=18)
income = st.number_input('Income', min_value=0, max_value=1000000, value=10000)