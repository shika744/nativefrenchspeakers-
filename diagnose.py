import socket
import webbrowser
import subprocess
import sys
import os
import platform
import time

def check_port(port):
    """Check if a port is in use"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def get_ip():
    """Get the local IP address"""
    try:
        # Create a socket that connects to an external server
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Doesn't need to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        try:
            s.close()
        except:
            pass
    return IP

def ping_localhost():
    """Ping localhost to check if it's responsive"""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', 'localhost']
    return subprocess.call(command, stdout=subprocess.PIPE) == 0

def main():
    print("=== Native French Speakers - Streamlit Diagnostic Tool ===")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Python Version: {sys.version}")
    
    # Check network configuration
    print("\n=== Network Configuration ===")
    hostname = socket.gethostname()
    local_ip = get_ip()
    print(f"Hostname: {hostname}")
    print(f"Local IP: {local_ip}")
    
    # Check if localhost resolves
    print("\n=== Localhost Check ===")
    try:
        localhost_ip = socket.gethostbyname('localhost')
        print(f"Localhost resolves to: {localhost_ip}")
        if localhost_ip != '127.0.0.1':
            print("WARNING: 'localhost' is not resolving to 127.0.0.1")
            print("Check your hosts file to make sure localhost is properly configured")
    except:
        print("ERROR: Cannot resolve 'localhost'")
        print("Your hosts file might be misconfigured")
    
    # Ping localhost
    print("\nPinging localhost...")
    if ping_localhost():
        print("Localhost is responding to pings")
    else:
        print("WARNING: Localhost is not responding to pings")
    
    # Check common ports
    print("\n=== Port Availability ===")
    for port in [8501, 8502, 8503, 8000, 8080]:
        status = "IN USE" if check_port(port) else "AVAILABLE"
        print(f"Port {port}: {status}")
    
    # Provide access URLs
    print("\n=== Access URLs ===")
    print("Your Streamlit app should be available at:")
    print(f"http://localhost:8501/")
    print(f"http://127.0.0.1:8501/")
    print(f"http://{local_ip}:8501/ (from other devices on your network)")
    
    print("\n=== Troubleshooting Steps ===")
    print("1. Ensure the Streamlit app is actually running")
    print("2. Check if any firewall is blocking the connection")
    print("3. Try using '127.0.0.1' instead of 'localhost'")
    print("4. If port 8501 is in use, try a different port: streamlit run app.py --server.port 8502")
    print("5. Check for any error messages in the terminal where Streamlit is running")
    
    print("\nWould you like to try opening the app in your browser? (y/n)")
    choice = input().lower()
    if choice == 'y':
        urls = [
            "http://localhost:8501/",
            "http://127.0.0.1:8501/"
        ]
        for url in urls:
            print(f"Trying to open {url}...")
            try:
                webbrowser.open(url)
                time.sleep(2)
            except:
                print(f"Failed to open {url}")

if __name__ == "__main__":
    main()