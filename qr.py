import pyqrcode
s="www.github.com/blackhatVN"
url = pyqrcode.create(s)
url.svg("myqr.svg",scale=8)