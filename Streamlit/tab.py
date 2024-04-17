import streamlit as st
import pandas as pd

def create_tabs():
    empty_df = pd.DataFrame()

    # Buttons for selecting different sections
    button_visualization = st.button("Visualization")
    button_information = st.button("Information")
    button_contents = st.button("Contents")
    button_dataset = st.button("Dataset")

    # Display content based on button clicks
    if button_visualization:
        st.header("Visualisation")
        st.write("Visualisation content goes here.")

    if button_information:
        st.header("Information")
        st.subheader("Table 1")
        st.table(empty_df)
        st.subheader("Table 2")
        st.table(empty_df)

    if button_contents:
        st.header("Contents")
        st.write("Content details go here.")

    if button_dataset:
        st.header("Dataset")
        st.write("Dataset details go here.")

    # Button to open new web space
    st.markdown("[Open New Web Space](https://www.example.com)")
