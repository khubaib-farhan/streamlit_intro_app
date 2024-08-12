import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")
file_upload = st.file_uploader("Choose a CSV file", type="csv")

if file_upload is not None:
    df = pd.read_csv(file_upload)
    
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)
    
    filtered_data = df[df[selected_column] == selected_value]
    st.write(filtered_data)
    
    st.subheader("Data Visualization")
    x_axis = st.selectbox("Select the X-Axis", columns)
    y_axis = st.selectbox("Select the Y-Axis", columns)
    
    if st.button("Generate Visuals"):
        st.line_chart(filtered_data.set_index(x_axis)[y_axis])
else:
    st.write("Waiting on file upload...")