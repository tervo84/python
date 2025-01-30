musa = "edm.txt"

fail = open(musa, encoding="UTF-8")
#näoita kõiki lugusid ja kuva valitud lood 


nr = 1

for pala in fail:
   # if float(kirje) > 0:
        print(str(nr)+" .  "+pala, end="")
        nr+=1
print()
valik = int(input("vali ligu: ")) 
fail = open(musa, encoding="UTF-8")
mangin = 1
for pala in fail:
         
    if valik == mangin:
        print(pala, end="")
        mangin+=1

    #vastuvoetud.append(int(rida))

fail.close()

