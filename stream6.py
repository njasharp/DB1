import streamlit as st
import qrcode
from PIL import Image
import io
import os
import tempfile

def create_qr_code(data, fill_color="black", back_color="white"):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img

st.title("Image to QR Code Converter")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Create a temporary directory to store the uploaded image
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Save the uploaded file to the temporary directory
        file_path = os.path.join(tmpdirname, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Display the uploaded image
        image = Image.open(file_path)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Create QR code with the local file path
        qr_code = create_qr_code(file_path)
        
        # Convert QR code to bytes for Streamlit to display
        qr_image = io.BytesIO()
        qr_code.save(qr_image, format="PNG")
        qr_image = qr_image.getvalue()
        
        # Display QR code
        st.image(qr_image, caption="Generated QR Code", use_column_width=True)
        
        # Option to download QR code
        st.download_button(
            label="Download QR Code",
            data=qr_image,
            file_name="qr_code.png",
            mime="image/png"
        )
        
        st.write(f"Scan this QR code to view the image. The local path is: {file_path}")
else:
    st.write("Please upload an image to generate a QR code.")
st.info("built by DW 8-18-24 - v1")
