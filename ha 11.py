

def viruvinkel(t1, t2):
    if t1[0]==t2[0]:
        return True
    else:
        return False





def pikim_sona(s):
    sona =""
    for i in s:
        if len(sona)<len(i):
            sona  =i
    print("pikim sõna on: "+sona)        
        




sonad = ["viisnurk", "ring", "ruut", "suvaline"]
pikim_sona(sonad)
print(viruvinkel("Mario", "Metshein"))
