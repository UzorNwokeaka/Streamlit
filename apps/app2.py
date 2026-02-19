import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(
    page_title="Data Explorer App",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Explorer Demo App")

st.write("This is a second Streamlit app example.")

# Generate sample data
np.random.seed(42)
data = pd.DataFrame({
    "Age": np.random.randint(18, 70, 100),
    "Salary": np.random.randint(20000, 120000, 100),
    "Experience (Years)": np.random.randint(1, 30, 100)
})

st.subheader("Sample Dataset")
st.dataframe(data)

st.subheader("Interactive Controls")

age_filter = st.slider("Select Minimum Age", 18, 70, 25)
filtered_data = data[data["Age"] >= age_filter]

st.write(f"Showing records where Age ≥ {age_filter}")
st.dataframe(filtered_data)

st.subheader("Salary Distribution")
st.bar_chart(filtered_data["Salary"])

st.success("App2 is running successfully 🚀")
