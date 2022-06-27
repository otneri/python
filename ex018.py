from math import sin,radians,cos,tan

a = (float(input('digite seu angulo')))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('Seu seno é {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(s, c, t))
