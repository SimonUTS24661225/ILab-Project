import streamlit as st
import pandas as pd

def create_tabs():
    empty_df = pd.DataFrame()

    # Buttons to select different sections
    button_visualization = st.button("Visualization")
    button_information = st.button("Information")
    button_contents = st.button("Contents")
    button_dataset = st.button("Dataset")

    # Display content based on button clicks
    if button_visualization:
        st.header("Visualisation Tab")
        st.write("Visualisation content goes here.")

    if button_information:
        st.header("Information Tab")
        st.subheader("Table 1")
        st.table(empty_df)
        st.subheader("Table 2")
        st.table(empty_df)

    if button_contents:
        st.header("Contents Tab")
        st.write("Content details go here.")

    if button_dataset:
        st.header("Dataset Tab")
        st.write("Dataset details go here.")
