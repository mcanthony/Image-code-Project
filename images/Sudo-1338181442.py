def getPixel( x,y ):
   x = 2*(x-0.5)**2*(0.8+2*y)
   return r%256,g%256,b%256