import streamlit as st
import pandas as pd

def create_tabs():
    empty_df = pd.DataFrame()

    tab1, tab2, tab3, tab4 = st.tabs(["Visualisation", "Information", "Contents", "Dataset"])

    with tab1:
        st.header("Visualisation Tab")
        st.write("Visualisation content goes here.")

    with tab2:
        st.header("Information Tab")
        st.subheader("Table 1")
        st.table(empty_df)
        st.subheader("Table 2")
        st.table(empty_df)

    with tab3:
        st.header("Contents Tab")
        st.write("Content details go here.")

    with tab4:
        st.header("Dataset Tab")
        st.write("Dataset details go here.")
