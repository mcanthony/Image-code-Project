def getPixel( x,y ):
   r = (sin(x*1) + 1) * 128
   return r%256,g%256,b%256