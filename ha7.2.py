

nimi = ["Jyri Pootsman" ,"MARI Jyrgens", "ans maali", "JUULI"]

# for i in nimi:
#     print(i)
    
for i in range(4):
    print(f"{i+1}. {nimi[i]}")
    
valik = int(input("vali lugu (1-4): "))
print(f"Mängin: {nimi[valik-1]}")