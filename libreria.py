import math

def suma (a,b):
    pr = a[0]+b [0]
    pc = a[1]+b [1]
    return (pr, pc)

def producto (a,b):
    rp = (a[0]*b[0])-(a[1]*b[1])
    cp= (a[0]*b[1])+(a[1]*b[0])
    return (rp, cp)

def resta (a,b):
    pr = a[0]-b[0]
    pc = a[1]-b[1]
    return (pr, pc)

def division (a,b):
    div = ((b[0] ** 2) + (b[1] ** 2))
    rp = ((a[0]*b[0])+(a[1]*b[1]))/ div
    cp = ((b[0]*a[1])-(a[0]*b[1]))/div
    return (rp, cp)

def modulo (c):
    return ((c[0]**2+ c[1]**2) **0.5)

def conjugado (c):
    return (c[0],-c[1])

def cartesiano_a_polar(c):
    modulo = ((c[0]**2)+(c[1]**2))**(1/2)
    fase = math.atan2(c[1],c[0])
    return (modulo, fase)

def polar_a_cartesiano(c):
    a = c[0]*math.cos(c[1])
    b = c[0]*math.sin(c[1])
    return (a,b)

def fase(c):
    angulo = math.atan2(c[1],c[0])
    return angulo
