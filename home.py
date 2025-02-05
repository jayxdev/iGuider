import streamlit as st

#if "shared" not in st.session_state:
 #  st.session_state["shared"] = True

st.video("intro.mp4")
n1=st.selectbox("Want to choose your Prefered Stream?", ["Select an Option", "Yes", "No"])

st.markdown('<a href="/app" target="_self">Click To Get counseling from iGUIDER Bot</a>', unsafe_allow_html=True)