from PIL import Image
import streamlit as st
import base64
import os

def add_bg_from_local(image_file):
    """
    Load a local image file and use it as the app's background.
    """
    try:
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/png;base64,{encoded_string});
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            
            /* Make content containers semi-transparent */
            .block-container {{
                background-color: rgba(255, 255, 255, 0.85);
                padding: 2rem;
                border-radius: 10px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        print("Successfully set background image")
        return True
    except Exception as e:
        print(f"Error setting background: {e}")
        return False