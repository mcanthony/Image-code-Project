def getPixel( x,y ):
   r = 58355875*(x+y)*x
   return r%256,g%256,b%256