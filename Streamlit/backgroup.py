import streamlit as st
import base64
from tab import create_tabs
from PIL import Image
import requests
from io import BytesIO

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
