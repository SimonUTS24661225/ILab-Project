import streamlit as st
import base64
from tab import create_tabs
from PIL import Image
import requests
from io import BytesIO

def set_bg_hack_url():
    '''
    A function for the background.
    '''
        
    def set_bg_hack_url():
    '''
    A function for the background.
    '''
    # Load the image from URL
    image_url = "https://images.pexels.com/photos/221012/pexels-photo-221012.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    
    # Resize the image to lower resolution
    new_width = 500  # Adjust as needed
    new_height = 300  # Adjust as needed
    image = image.resize((new_width, new_height))
    
    # Convert the image to data URL
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    img_css = f'data:image/jpeg;base64,{img_str}'
    
    # Set the background image
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("{img_css}");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

    
st.set_page_config(
    page_title="ECOHEALTH WEBPAGE",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

set_bg_hack_url()

custom_css = """
<style>
body {
    background-color: #ffff99;
    color: #333;
}
.sidebar .sidebar-content {
    background-color: #ffffff;
}
.stButton>button {
    background-color: #ffcc00 !important;
}
</style>
"""

st.write("# Welcome to WebPage of EcoHealth! ")

st.sidebar.markdown(custom_css, unsafe_allow_html=True)
st.sidebar.success("Select a Pollutant Below.")
pollutant = st.sidebar.selectbox(
    "Choose a pollutant:",
    ("Methane", "Ammonia")
)

st.sidebar.markdown(custom_css, unsafe_allow_html=True)
st.sidebar.success("Select a cause of air pollution.")
pollutant = st.sidebar.selectbox(
    "Choose a cause:",
    ("Enteric fermentation", "Manure Management", "Agrifood systems waste disposal")
)

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

