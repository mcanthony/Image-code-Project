def getPixel( x,y ):
   grey = int(100*sin(x*15))/5.0*(10-y)
   return r%256,g%256,b%256