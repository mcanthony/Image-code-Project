def getPixel( x,y ):
   r = 1/(tan(x**2)+.0000001)
   return r%256,g%256,b%256