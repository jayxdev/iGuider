import streamlit as st

#if "shared" not in st.session_state:
 #  st.session_state["shared"] = True

# URL or file path of your video
video_url = "res/intro.mp4"

# # HTML embed with autoplay attribute
# video_html = f"""
# <video width="700" height="400" autoplay loop controls muted>
#   <source src="{video_url}" type="video/mp4">
#   Your browser does not support the video tag.
# </video>
# """

# # Display the video with autoplay using markdown
# st.markdown(video_html, unsafe_allow_html=True)
st.video(video_url)

n1=st.selectbox("Want to choose your Prefered Stream?", ["Select an Option", "Yes", "No"])

st.markdown('<a href="/App" target="_self" style="text-decoration:none;"><button style="background-color:#4CAF50; color:white; padding:10px 20px; border:none; border-radius:4px; cursor:pointer;">Click To Get counseling from iGUIDER Bot</button></a>', unsafe_allow_html=True)