def getPixel( x,y ):
   grey = int(10*sin(x*15))/10.0*(1-y)
   return r%256,g%256,b%256