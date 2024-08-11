import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.title(" Dashboard ")

upload_file = st.file_uploader("Choose a CSV file", type="csv")

if upload_file is not None:
    st.write("File uploaded......")
    df = pd.read_csv(upload_file)
    print()
    st.subheader("Data Previev")
    st.write(df.head(10))
    print()
    st.subheader("Data Summary")
    st.write(df.describe())
    print()
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    select_column = st.selectbox("Select Column to filter by", columns)
    unique_value = df[select_column].unique()
    select_value = st.selectbox("Select value", unique_value)
    
    filtered_df = df[df[select_column] == select_value]
    st.write(filtered_df)
    
    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)
    
    if st.button(" Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
    
    else:
        st.write("waiting on file upload......")
