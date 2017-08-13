#colo-hex.com
#white(0): fff
#light cinza(1):
#cinza(2):888
#black(3):000
#rosa meio vermelho(4): f88 / f08
#red(5): f00 / 800
#beje(6):f80
#brown(7):880
#yellow(8): ff0 / ff8
#light green (9): 8f8 / 8f0
#green(10): 0f0 / 080
#light blue(11):0ff /8ff / 0f8
# verde meio azul (12): 088 / 88f / 08f
#blue(13): 00f / 008
#rosa meio roxo(14): f0f/f8f
#roxo(15):808 / 80f
#magenta (stronger than 4 and 14):f0f

from PIL import Image

im = Image.open("face.png") #Can be many different formats.
pix = im.load()
print im.size #Get the width and hight of the image for iterating over
print pix[0,0] #Get the RGBA Value of the a pixel of an image
#pix[x,y] = value # Set the RGBA Value of the image (tuple)
#im.save("alive_parrot.png") # Save the modified pixels as png