import base64
import streamlit as st
import os

def set_background_from_file(file_path):
    """
    Function to set page background to an image file
    """
    if not os.path.exists(file_path):
        print(f"Error: File does not exist at {file_path}")
        return False
        
    try:
        with open(file_path, "rb") as f:
            img_data = f.read()
            img_base64 = base64.b64encode(img_data).decode()
            
            page_bg_img = f"""
            <style>
            [data-testid="stAppViewContainer"], [data-testid="stSidebarContent"] {{
                background-image: url("data:image/png;base64,{img_base64}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-position: center;
            }}
            
            [data-testid="stHeader"] {{
                background-color: rgba(0, 0, 0, 0);
            }}
            
            .block-container {{
                background-color: rgba(255, 255, 255, 0.85);
                padding: 20px;
                border-radius: 10px;
            }}
            </style>
            """
            
            st.markdown(page_bg_img, unsafe_allow_html=True)
            return True
            
    except Exception as e:
        print(f"Error setting background: {e}")
        return False