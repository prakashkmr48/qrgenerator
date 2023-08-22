import streamlit as st
import qrcode
from PIL import Image
import io

def main():
    st.title("QR Code Generator")

    url = st.text_input("Enter the URL:")
    if url:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")  # Renamed pil_image to qr_image

        # Convert PIL image to bytes
        img_byte_array = io.BytesIO()
        qr_image.save(img_byte_array, format='PNG')  # Use qr_image instead of pil_image

        # Display the image using st.image
        st.image(img_byte_array, caption="Generated QR Code", use_column_width=True)

if __name__ == "__main__":
    main()
