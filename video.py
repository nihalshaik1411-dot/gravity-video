import streamlit as st

st.title("📹 Video Player from GitHub")

# Replace this URL with the raw GitHub link to your mp4 file
video_url = "https://github.com/nihalshaik1411-dot/gravity-video"

st.markdown("### Playing video from GitHub repo:")
st.video(video_url)
