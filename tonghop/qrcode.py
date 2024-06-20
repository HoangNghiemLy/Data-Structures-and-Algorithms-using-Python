import qrcode as qr 
img = qr.make("https://www.facebook.com/nghiem.hoang.965580/")
img.save("qr.png")
img.show()

