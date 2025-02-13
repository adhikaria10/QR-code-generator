import qrcode

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
)

data = "https://facebook.com/NKUBYC"
qr.add_data(data)
qr.make(fit = True)

img = qr.make_image(fill = 'black', back_color = 'white')
img.save("generated_qr.png")

print("Your QR code has been generated!!!")