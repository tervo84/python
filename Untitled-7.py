

fail = open("konto.txt", encoding="UTF-8")

#vastuvoetud = []

for kirje in fail:
    if float(kirje) > 0:
        print(float(kirje), end="\N")

    #vastuvoetud.append(int(rida))

fail.close()


# fail = open("rebased.txt", encoding="UTF-8")

# vastuvoetud = []

# for rida in fail:
#     #print(rida, end="")

#     vastuvoetud.append(int(rida))

# fail.close()
# #aasta=9
# #print(vastuvoetud[aasta-1])

# aasta = input("lisa aasta 2011-2019:")
# print(vastuvoetud[int(aasta[3])-1])
