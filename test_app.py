import streamlit as st

st.title("Simple Test Page")
st.write("If you can see this, Streamlit is working correctly!")

ip_info = st.expander("Network Information")
with ip_info:
    import socket
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        localhost_ip = socket.gethostbyname('localhost')
        
        st.write(f"Hostname: {hostname}")
        st.write(f"Local IP: {local_ip}")
        st.write(f"Localhost resolves to: {localhost_ip}")
    except Exception as e:
        st.error(f"Error getting network info: {str(e)}")

st.success("Test completed successfully!")