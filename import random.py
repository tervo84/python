import random
ounad = 14
pp = int(input("mitu pp tahab õunu"))

for i in range(pp):
    suv_oun = random.randint(1,2)
    print(suv_oun)
    ounad -=  suv_oun

print(f"lumivalgekesele jäi {ounad} õuna")    
