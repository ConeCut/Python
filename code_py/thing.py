import turtle
from turtle import *
import math as m
"""
l = [1, 2, 3, 4, 5, 6]

print(len(l))

for num in l:
    if num % 2 != 0:
        print(num)
    
print("Hello")
 
a = 10
a = a + 2
 
print(a)
 
navn = "Cosmin"
alder = "18"
alder = int(alder)
 
print(navn + " " + str(alder))
 
b = 17
c = 5
 
print("Multiplikasjon: ", b*c)
print("Addisjon: ", b+c)
print("Subrahere: ", b-c)
print("Divisjon: ", b/c)
print("Potens: ", b**c)
print("Modulus: ", b%c)
print("Heltallsdivisjon: ", b//c)
print("Kvadratrot: ", m.sqrt(b))
print("Kvadratrot: {:.2f}".format(m.sqrt(b)))
 
tall = "3,14"
tall = tall.replace(",", ".")
tall = float(tall)
print ("Pi: ", tall)

tekst = "Storebokstaver"

print(tekst.upper)
print(tekst.lower)

base = input("What is the base of the triangle: ")
height = input("Tell me the heigh too bruv: ")
a = int(base)
b = int(height)
print((a * b) / 2)


star = "*"
space = " "
nospace = ""
rows = 5
rows2 = 8

for num in range(rows):
    print(space * ((rows2) - num) + star * (num * 2 + 1))
    
for num in range(rows2, 3, -1):
    print(space * ((rows2) - num) + star * (num * 2 + 1))
    
for num in range(rows):
    print(space * ((rows2) - num) + star * (num * 2 + 1))
    
"""    

turtle.title("rainbow spiral")
turtle.speed("fastest")
turtle.pensize(10)
bgcolor("black")
r,g,b=255,0,0

for i in range(255*2):
    colormode(255)
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        b+=3
    elif i<255*4//3:
        g-=3
    elif i<255*5//3:
        r+=3
    else:
        b-=3
    fd(20+i)
    rt(90.5)
    pencolor(r,g,b)

done()
    
        






a = input('Put a number in man:' )
b = input('Now another:' )

if(a > b):
    print('yuh, ',a , 'is bigger')

if(b > a):
    print('yuh, ',b , 'is bigger')
    
elif(a == b):
    print('same number, they are equal')