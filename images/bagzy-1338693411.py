def getPixel( x,y ):
   r=255*x*x/1+(y*y+y*y)*cos(x);
   return r%256,g%256,b%256