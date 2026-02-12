import streamlit as st
import cv2
import av
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
from Color_rec import detect_color

st.set_page_config(page_title="Color Detection", layout="centered")

st.title("🎨 Color Detection System")
st.markdown("Align the object inside the circle to detect the color.")

st.sidebar.header("🎯 Supported Colors")
st.sidebar.write("""
- Red  
- Orange  
- Yellow  
- Green  
- Light Green  
- Blue  
- Sky Blue  
- Violet  
- White  
""")

class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        processed_frame, _ = detect_color(img)

        return av.VideoFrame.from_ndarray(processed_frame, format="bgr24")

webrtc_streamer(
    key="color-detection",
    video_processor_factory=VideoProcessor,
    media_stream_constraints={"video": True, "audio": False},
)
