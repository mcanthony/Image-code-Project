def getPixel( x,y ):
   r = sin(1*y*x*y)-sin(5*x*y*x)
   return r%256,g%256,b%256