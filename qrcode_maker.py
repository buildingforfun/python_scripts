import qrcode
import validators
from pathlib import Path

def qr_maker(url):
    """Generate qr code"""

    if not validators.url(url):
        raise ValueError("Check URL entered")

    qrcode_dir = Path("qrcodes")
    qrcode_dir.mkdir(exist_ok=True)

    filename = "image_{}.jpg".format(hash(url))
    file_path = qrcode_dir / filename

    img = qrcode.make(url)
    img.save(file_path)

    return str(file_path)

url = input("Enter URL: ")
file_path = qr_maker(url)
