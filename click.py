from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

ms = PyMouse()
kb = PyKeyboard()
s = 1 #s clicks/second
sc = 1/s
b = ms.position()
xb = b[0]
yb = b[1]
c = 0 #count
cs = 50 #set count
while(c<=cs):
    b = ms.position()
    xb = b[0]
    yb = b[1]
    ms.click(xb, yb)
    time.sleep(sc)
    print 'a'
    print xb
    print yb
    c = c +1
