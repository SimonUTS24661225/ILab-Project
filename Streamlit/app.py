import streamlit as st
from tab import create_tabs
import base64


def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

background_image_url = 'https://images.unsplash.com/photo-1542281286-9e0a16bb7366'

# Encode the background image to base64
background_image = get_base64_of_bin_file(background_image_url)

# Custom CSS for styling with background image
custom_css = f"""
    <style>
        .reportview-container {{
            background: url('data:image/png;base64,{background_image}');
            background-size: cover;
        }}
        .sidebar .sidebar-content {{
            background-color: rgba(255, 255, 255, 0.9); /* Adjust background opacity */
        }}
        .stButton>button {{
            background-color: #ffcc00 !important;
        }}
    </style>
"""

# Write the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Set page config and initial sidebar state
st.set_page_config(
    page_title="ECOHEALTH WEBPAGE",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Write the title and introduction
st.write("# Welcome to WebPage of EcoHealth! ")

# Sidebar content
st.sidebar.success("Select a Pollutant Below.")
pollutant = st.sidebar.selectbox(
    "Choose a pollutant:",
    ("Methane", "Ammonia")
)

st.sidebar.success("Select a cause of air pollution.")
pollutant = st.sidebar.selectbox(
    "Choose a cause:",
    ("Enteric fermentation", "Manure Management", "Agrifood systems waste disposal")
)

# Introduction
st.markdown("""
    This webpage is built by team EcoHealth.
    This page serves as a comprehensive resource for exploring the profound impact of pollution on global health.
    Through detailed visualizations, information, and curated content, visitors will gain an in-depth understanding of how various pollutants adversely affect the environment and
    consequently, human health. By examining the interconnections between air, water, and soil pollution and the incidence of health conditions worldwide, this platform aims to 
    raise awareness and encourage proactive measures. It's an invaluable tool for educators, policymakers, and individuals alike, offering insights into the significance of 
    environmental preservation and the urgent need for sustainable practices to safeguard our planet and our well-being.
    
    ### Want to learn more?
    Check out [World Health Organization](https://www.who.int)
""")

# Select the tab
selected_tab = st.selectbox(
    "Select a tab:",
    ("Visualisation", "Information", "Dataset", "References")
)

# Call the function to create tabs
create_tabs(selected_tab)
