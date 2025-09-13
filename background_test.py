import streamlit as st
import os

def main():
    # Set the page title and icon
    st.set_page_config(
        page_title="Background Test",
        page_icon="🖼️",
        layout="wide"
    )
    
    # Insert custom CSS with background image
    bg_path = "../NFS/background.png"  # Relative path to the background image
    
    if os.path.exists(bg_path):
        print(f"Found background image at: {bg_path}")
    else:
        print(f"Background image not found at: {bg_path}")
        # Try absolute path
        bg_path = "C:\\Users\\shika\\OneDrive\\Desktop\\Evaluation\\NFS\\background.png"
        if os.path.exists(bg_path):
            print(f"Found background image at: {bg_path}")
        else:
            print(f"Background image not found at: {bg_path}")
            
    # Add CSS for background
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f8f9fa;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Try embedding the image directly if it exists
    try:
        import base64
        with open(bg_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{data}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        print("Successfully embedded background image")
    except Exception as e:
        print(f"Error embedding background image: {e}")
    
    # Page content
    st.title("Background Image Test")
    st.write("This is a test to see if the background image is displayed correctly.")
    
if __name__ == "__main__":
    main()