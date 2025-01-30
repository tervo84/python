
import math
inim = 60
koht = 40

if inim>inim%koht:
    print

print((inim//koht))
print(inim%koht)


busside_arv = math.ceil(inim/koht)
if inim <= koht:
    viimane_inim_arv = inim
else:

    viimane_inim_arv = abs(inim- koht) 

print(f"busside_arv: {busside_arv}")
print(f"viimases bussis on inimes: {viimane_inim_arv}") 


