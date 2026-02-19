# my first streamlit app
import streamlit as st

st.title("Alyticmode ML Web App")
st.write("Fraud Detection Demo Coming Soon 🚀")

number = st.slider("Select a number", 0, 100)
st.write("You selected:", number)
