def getPixel( x,y ):
   r = x - sin(x%0.1*20)
   return r%256,g%256,b%256