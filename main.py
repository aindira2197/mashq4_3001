def musbat_juftlar(royxat):
    natija = []

    for son in royxat:
        if son > 0:
            if son % 2 == 0:
                natija.append(son)

    return natija


sonlar = [-4, 7, 10, -2, 8, 3, 0, 6]
javob = musbat_juftlar(sonlar)

print("Asosiy ro'yxat:", sonlar)
print("Musbat va juft sonlar:", javob)
