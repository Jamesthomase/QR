import qrcode
import os

# Prompt user to enter the URL
input_URL = input("Enter the URL to generate QR code: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

# Convert into image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img_path = "url_qrcode.png"
img.save(img_path)

# Open the saved image with the default image viewer
os.system(img_path)
