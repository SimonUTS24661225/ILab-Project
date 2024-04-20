import streamlit as st
import base64
from tab import create_tabs
from PIL import Image
import requests
from io import BytesIO
from st_pages import Page, Section, show_pages, add_page_title, hide_pages


def set_bg_hack_url(brightness=1.0, opacity=1.0, blur=0):
    '''
    A function for the background.
    '''
    # Load the image from URL
    image_url = "https://i.ibb.co/8NGXCj1/background-photo.jpg"
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    
    # Resize the image to lower resolution
    new_width = 500  # Adjust as needed
    new_height = 300  # Adjust as needed
    image = image.resize((new_width, new_height))
    
    # Apply CSS filters to adjust intensity
    css_filters = f"brightness({brightness}) opacity({opacity}) blur({blur}px)"
    
    # Convert the image to data URL
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    buffered.seek(0)  # Set the file pointer to the beginning of the buffer
    img_str = base64.b64encode(buffered.getvalue()).decode()
    img_css = f'data:image/jpeg;base64,{img_str}'
    
    # Set the background image with CSS filters
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("{img_css}");
             background-size: cover;
             filter: {css_filters};
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

# set_bg_hack_url()

show_pages(
    [   
        Page("Streamlit/app.py", "EcoHealth", "💌"),

        # # Methane
        Section("Methane Emission", "🧙‍♂️"),
        Page("Streamlit/Methane/information.py", "Methane Overview", "📚", in_section=True),
        Page("Streamlit/Methane/Causes of Methane.py", "Causes of Methane", "1️⃣", in_section=True),
        Page("Streamlit/Methane/impacts on human.py", "Impact of Methane on Human Health", "1️⃣", in_section=True),
        Page("Streamlit/Methane/Fossil-fuel-production.py", "Fossile Fuel Production", "1️⃣", in_section=True),
        Page("Streamlit/Methane/Livestock-farming.py", "Livestock Farming", "1️⃣", in_section=True),
        Page("Streamlit/Methane/Landfills-and-wastes.py", "Landfills and Wastes", "1️⃣", in_section=True),
        
       

        # Ammonia
        Section("Ammonia Emission", "👨‍🔧"),
        Page("Streamlit/Ammonia/information.py", "Ammonia Overview", "📚", in_section=True),



        
        # Dataset
        Page("Streamlit/Datasets.py", "Datasets", icon="💾", in_section=False),
        # Reference
        Page("Streamlit/Reference.py", "Reference", "📜", in_section=False),
        # FAQ
        Page("Streamlit/FAQ.py", "FAQ", "❔", in_section=False),
        # Contact
        Page("Streamlit/Contact.py", "Contact", icon="📩", in_section=False),   
        # About  
        Page("Streamlit/About.py", "About", icon="🖼️", in_section=False) 
    ]
)

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



hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
