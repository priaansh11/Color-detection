import streamlit as st
import cv2
from Color_rec import detect_color

st.set_page_config(page_title="Color Detection", layout="centered")

st.title("🎨 Color Detection System")
st.markdown("Hold an object in your hand and align that object in that circle to detect the color.")
st.markdown("⚡ To detect the color, please turn ON the camera using the Start button.")

# ---- Sidebar ----
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

# ---- Session State for Camera ----
if "camera_running" not in st.session_state:
    st.session_state.camera_running = False

# ---- Buttons ----
col1, col2 = st.columns(2)

with col1:
    if st.button("Start Camera"):
        st.session_state.camera_running = True

with col2:
    if st.button("Exit Camera"):
        st.session_state.camera_running = False

FRAME_WINDOW = st.image([])
color_placeholder = st.empty()

# ---- Camera Logic ----
if st.session_state.camera_running:
    cap = cv2.VideoCapture(0)

    while st.session_state.camera_running:
        ret, frame = cap.read()
        if not ret:
            st.error("Camera not working")
            break

        processed_frame, color = detect_color(frame)

        processed_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(processed_frame)

        # ---- Show detected color below in BLACK ----
        color_placeholder.markdown(
            f"<h2 style='text-align:center; color:black;'>Detected Color: {color}</h2>",
            unsafe_allow_html=True
        )

    cap.release()