def getPixel( x,y ):
   r = sqrt(x*y + y*x)
   return r%256,g%256,b%256