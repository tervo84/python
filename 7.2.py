jtemp =[ "jaanuar" ,-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]
print(f"mõõdetav kuu:{jtemp[0]}")
print(f"viimase mõõtmise tulemus:{jtemp[-1]} kraadi")
print(f"viimase mõõtmise tulemus:{jtemp[-1]} kraadi")

max = 0
min = 100
summa = 0
kokku = 0
kordused = 0
 
for t in range(1,len(jtemp)):               
    print(jtemp[t], end=" ")
    if jtemp[t]>max:
        max = jtemp[t]
    if jtemp[t]>min:
        min = jtemp[t]
    summa+=jtemp[t]
    kokku+=1

    if jtemp[t]== -20:
        kordused+=1

jtemp.pop(5)
jtemp.insert(5,40)
#jtemp.sort()


print()        
print(f"maksimum temp on: {max}")            
print(f"miinimum temp on: {min}")
print(f"keskmine temp on :{summa/kokku:0.2f}")            
print(f"temp -20 esineb :{kordused} korda")
print(jtemp)


        
        

