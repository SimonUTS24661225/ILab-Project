import streamlit as st
import base64
from tab import create_tabs

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://cdn.pixabay.com/photo/2020/06/19/22/33/wormhole-5319067_960_720.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
