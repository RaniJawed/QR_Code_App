# QR Code Encoder & Decoder with Streamlit

This Streamlit app allows users to generate and decode QR codes easily.

## 📌 Features
- ✅ Modern UI with beautiful buttons, input fields, and hover effects
- ✅ Real-time QR Code generation and downloading
- ✅ Automatic QR Code decoding from uploaded images
- ✅ User-friendly Streamlit interface with icons & animations

## 🚀 How to Run the App
### Install Required Libraries
Ensure you have the necessary libraries installed:
```sh
pip install streamlit qrcode opencv-python numpy pillow
```

### Run the Streamlit App
```sh
streamlit run app.py
```

---

## 🛠 Step-by-Step Code Explanation
### 1️⃣ Import Required Libraries
```python
import streamlit as st
import qrcode
import cv2
import numpy as np
import io
from PIL import Image
```
- **streamlit** → For the web-based UI
- **qrcode** → For generating QR codes
- **cv2 (OpenCV)** → For decoding QR codes
- **numpy** → For handling image arrays
- **io** → For handling image file operations
- **PIL (Pillow)** → For image processing

### 2️⃣ Add Custom CSS Styling
```python
st.markdown("""
    <style>
        body { background-color: #f4f4f4; color: #333; }
        .title { text-align: center; font-size: 36px; font-weight: bold; color: #4CAF50; margin-bottom: 20px; }
        .stButton>button { background-color: #4CAF50; color: white; border-radius: 8px; font-size: 18px; padding: 10px 20px; }
        .stButton>button:hover { background-color: #45a049; }
        .stTextInput>div>div>input { border: 2px solid #4CAF50; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)
```
- Improves UI styling with colors and hover effects

### 3️⃣ Function to Generate QR Code
```python
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
```
- Converts input text or URL into a QR code
- Uses **qrcode** module to generate QR codes
- Converts the QR code into an image file for download

### 4️⃣ Function to Decode QR Code
```python
def decode_qr_code(uploaded_file):
    image = Image.open(uploaded_file)
    image = np.array(image)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(image)
    return data if data else "No QR code detected"
```
- Reads an uploaded QR code image
- Uses OpenCV’s **QRCodeDetector** to extract the text

### 5️⃣ Create Streamlit UI
```python
st.markdown("<h1 class='title'>🔳 QR Code Encoder & Decoder</h1>", unsafe_allow_html=True)
```
- Displays a title for the app

### 6️⃣ Add Selection Options
```python
option = st.radio("", ("📌 Generate QR Code", "📎 Decode QR Code"), horizontal=True)
```
- Allows users to switch between **QR Code Generation** and **Decoding**

### 7️⃣ QR Code Generation Section
```python
if option == "📌 Generate QR Code":
    user_input = st.text_input("🔹 Enter text or URL", placeholder="Type here...")
    
    if st.button("🎨 Generate QR Code"):
        if user_input:
            qr_image = generate_qr_code(user_input)
            st.image(qr_image, caption="✅ Generated QR Code", use_container_width=True)
            st.download_button("📥 Download QR Code", qr_image, file_name="qrcode.png")
        else:
            st.warning("⚠️ Please enter some text to generate QR code.")
```
- If the user selects "Generate QR Code":
  - Takes user input (text/URL)
  - Calls `generate_qr_code()` function
  - Displays the generated QR code
  - Adds a **Download** button

### 8️⃣ QR Code Decoding Section
```python
elif option == "📎 Decode QR Code":
    uploaded_file = st.file_uploader("📤 Upload a QR code image", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        decoded_text = decode_qr_code(uploaded_file)
        st.image(uploaded_file, caption="🖼️ Uploaded QR Code", use_container_width=True)
        st.success(f"✅ Decoded Text: {decoded_text}")
```
- If "Decode QR Code" is selected:
  - Asks the user to upload a QR code image
  - Calls `decode_qr_code()` function
  - Displays the uploaded image
  - Shows the decoded text

---

## 🎯 Summary
| Step | Function | Description |
|------|----------|-------------|
| 1️⃣ | Import libraries | Load Streamlit, QR Code, OpenCV, NumPy, and PIL |
| 2️⃣ | Add styling | Customize UI with CSS |
| 3️⃣ | Generate QR code | Convert text/URL into a QR code image |
| 4️⃣ | Decode QR code | Extract text from an uploaded QR code image |
| 5️⃣ | Create UI | Display title |
| 6️⃣ | Select option | User chooses Generate QR or Decode QR |
| 7️⃣ | Generate section | User inputs text → QR code generated & downloaded |
| 8️⃣ | Decode section | User uploads QR → Text extracted & displayed |

🔥 Now you have a fully functional QR Code Encoder & Decoder! 🚀

"# QR_Code_App" 
