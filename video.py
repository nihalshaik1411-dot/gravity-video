import streamlit as st

st.title("📹 Video Player from GitHub")

# Replace this URL with the raw GitHub link to your mp4 file
video_url = "https://gravity-video-mdjkhag628h23cavchhidd.streamlit.app/"

st.markdown("### Playing video from GitHub repo:")
st.video(video_url)

# Optionally allow user to upload their own file
uploaded_file = st.file_uploader("Or upload your own MP4", type=["mp4"])
if uploaded_file is not None:
    st.video(uploaded_file)
