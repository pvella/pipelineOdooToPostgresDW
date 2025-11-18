import qrcode

# Data to encode
data = "https://community3008.org.au/event"
filename ="community3008_event2.png"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save it
img.save(filename)
print("QR code saved as " + filename)