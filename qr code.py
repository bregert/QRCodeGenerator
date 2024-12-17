import pyqrcode
import os, shutil

title = input("Name of QR Code: ")
text = input("What would you like the QR Code to say? ")

file_name_svg = title + ".svg"
file_name_png = title + ".png"

url = pyqrcode.create(text)

url.svg(file_name_svg, scale=10)
url.png(file_name_png, scale=10)

os.mkdir(fr"C:\Users\John\Desktop\{title}")

shutil.move(f"{file_name_png}", fr"C:\Users\John\Desktop\{title}")
shutil.move(f"{file_name_svg}", fr"C:\Users\John\Desktop\{title}")
