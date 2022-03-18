
# Import QRCode from pyqrcode 
# https://instagram.com/_.mr._.ayush._.patil._
import pyqrcode 
#import random 
import png 
import os
from pyqrcode import QRCode 

  

  
# String which represents the QR code 

s = input('Enter The Website URL : ')

  
# Generate QR code  

url = pyqrcode.create(s) 

  
# Create and save the svg file naming "myqr.svg" 
#os.mkdir('PNG')
#url.svg("PNG/myqr.svg", scale = 8) 

  
# Create and save the png file naming "myqr.png" 
if not os.path.exists('/storage/emulated/0/Python Programming/My Python Programs/Make Qr Code using Python/PNG'):
	os.makedirs('/storage/emulated/0/Python Programming/My Python Programs/Make Qr Code using Python/PNG')
	
#if os.path.exists('/storage/emulated/0/Python Programming/My Python Programs/Make Qr Code using Python/PNG/webqr.png'):
#a = random.randint(1,1000)
a = s[8:18]
url.png(f'/storage/emulated/0/Python Programming/My Python Programs/Make Qr Code using Python/PNG/{a}.png', scale = 6) 
print('Your QR Code is ready')
