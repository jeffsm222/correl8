import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Correlation Analysis App")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.dataframe(df.head())  # Display the first few rows

    # Select only the numeric columns
    numeric_df = df.select_dtypes(include=[np.number])

    # Calculate the correlation matrix
    corr_matrix = numeric_df.corr()
    # # run df.corr on 
    # # Correlation matrix
    # corr_matrix = df.corr()

    st.subheader("Correlation Matrix")
    st.dataframe(corr_matrix)

    # Heatmap visualization
    st.subheader("Correlation Heatmap")
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    st.pyplot()

    # Pairwise scatter plots
    st.subheader("Pairwise Scatter Plots")
    sns.pairplot(df)
    st.pyplot()

else:
    st.write("Please upload a CSV file.")
