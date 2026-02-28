import qrcode
from faker import Faker

fake = Faker()

for _ in range(10):
    name = fake.name()
    img = qrcode.make(name)
    img.save(name + ".png")
    print(f"QR code for {name} generated and saved as {name}.png")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('bimmer')
qr.make(fit=True)

img = qr.make_image(fill_color="pink", back_color="black")
type(img)  # qrcode.image.pil.PilImage
img.save("some_file5.png")