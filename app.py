import streamlit as st
import qrcode
import cv2
import numpy as np
import io
from PIL import Image

# Custom Styling
st.markdown("""
    <style>
        body { background-color: #f4f4f4; color: #333; }
        .title { text-align: center; font-size: 36px; font-weight: bold; color: #4CAF50; margin-bottom: 20px; }
        .stButton>button { background-color: #4CAF50; color: white; border-radius: 8px; font-size: 18px; padding: 10px 20px; }
        .stButton>button:hover { background-color: #45a049; }
        .stTextInput>div>div>input { border: 2px solid #4CAF50; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

# Function to generate QR Code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    return img_bytes

# Function to decode QR Code
def decode_qr_code(uploaded_file):
    image = Image.open(uploaded_file)
    image = np.array(image)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(image)
    return data if data else "No QR code detected"

# Streamlit UI
st.markdown("<h1 class='title'>🔳 QR Code Encoder & Decoder</h1>", unsafe_allow_html=True)

# Radio Button for Options
option = st.radio("", ("📌 Generate QR Code", "📎 Decode QR Code"), horizontal=True)

# QR Code Generation
if option == "📌 Generate QR Code":
    user_input = st.text_input("🔹 Enter text or URL", placeholder="Type here...")
    
    if st.button("🎨 Generate QR Code"):
        if user_input:
            qr_image = generate_qr_code(user_input)
            st.image(qr_image, caption="✅ Generated QR Code", use_container_width=True)  # ✅ FIXED PARAMETER
            
            # Download Button
            st.download_button("📥 Download QR Code", qr_image, file_name="qrcode.png")
        else:
            st.warning("⚠️ Please enter some text to generate QR code.")

# QR Code Decoding
elif option == "📎 Decode QR Code":
    uploaded_file = st.file_uploader("📤 Upload a QR code image", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        decoded_text = decode_qr_code(uploaded_file)
        st.image(uploaded_file, caption="🖼️ Uploaded QR Code", use_container_width=True)  # ✅ FIXED PARAMETER
        st.success(f"✅ Decoded Text: {decoded_text}")
