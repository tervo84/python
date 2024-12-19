# ül6
import math
import turtle
nurk = 53
kõrgus = 4.4

rad = math.radians(nurk)
kaugus = kõrgus / math.tan(rad)
c = math.sqrt(math.pow(kaugus,2) + math.pow(kõrgus,2))

print(c)
kordaja =10
turtle.fd(kaugus*kordaja)
turtle.lt(90)
turtle.fd(kõrgus*kordaja)
turtle.rt(360-143)
turtle.fd(c*kordaja)


turtle.done()
#nvldkfnvlk