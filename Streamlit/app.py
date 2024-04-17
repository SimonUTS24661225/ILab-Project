import streamlit as st
import pandas as pd
# Importing tab function from tab.py
from tab import create_tabs

st.set_page_config(
    page_title="ECOHEALTH WEBPAGE",
    page_icon="👋",
)

st.write("# Welcome to WebPage of EcoHealth! ")

st.sidebar.success("Select a Pollutant Below.")
pollutant = st.sidebar.selectbox(
    "Choose a pollutant:",
    ("Methane", "Ammonia")
)

st.markdown("""
    This webpage is built by team EcoHealth.
    This page serves as a comprehensive resource for exploring the profound impact of pollution on global health.
    Through detailed visualizations, information, and curated content, visitors will gain an in-depth understanding of how various pollutants adversely affect the environment and
    consequently, human health. By examining the interconnections between air, water, and soil pollution and the incidence of health conditions worldwide, this platform aims to 
    raise awareness and encourage proactive measures. It's an invaluable tool for educators, policymakers, and individuals alike, offering insights into the significance of 
    environmental preservation and the urgent need for sustainable practices to safeguard our planet and our well-being.
    
    ### Want to learn more?
    Check out  [World Health Organizaation](https://www.who.int)

""")

# Function call to create tabs
create_tabs()
