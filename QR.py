import qrcode

# Create a QRCode instance
qr = qrcode.QRCode(
    version=1,  # QR code version (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box/pixel
    border=4,  # Border size (in boxes)
)

# Data you want to encode in the QR code
data = "Hello, World!"

# Add data to the QR code
qr.add_data(data)

# Generate the QR code
qr.make(fit=True)

# Create a PIL Image object from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image to a file
qr_image.save("my_qr_code.png")

# Display the QR code
qr_image.show()
