"""
try:
    kraadid = 30
    if kraadid < 0:
        print("talveriided")
    elif kraadid >=0 and kraadid <= 15:
        print ("Kevad-Sügis")
    else:
        print("Suvi")
except:
    print("Viga sisestuses")
    
"""
import random
import turtle

"""
try:
#     print(random.randint(1,10))
#     print(random.randint(1,10))
    arv1 = random.randint(1,10)
    arv2 = random.randint(1,10)
    vastus = int(input(f"mis on {arv2} * {arv2} vastus?\nSisesta vastus: "))
    korrutis = arv1 * arv2
    print(vastus)
    print(korrutis)
    
    if korrutis == vastus:
        print("õige")
    else:
        print("vale")
        
except:
    print("viga sisestuses")
 """
try:
    valik = random.randint(0,1)
    if arvamus = int(" Vali kull 1 või  kiri 0: "))
       if valik == arvamus:
        print("Arvasid ära")
        turtle.color("green")
        turtle.circle(50)
        else:
            print("Arvasid valesti")
            turtle.color("red")
            turtle.circle(50)
            turtle.done()
        else:
             print("Sellist valikut ju polnud!")
except:
    print("viga sisestuses")