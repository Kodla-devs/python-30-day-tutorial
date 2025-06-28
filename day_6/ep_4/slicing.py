liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(liste[1:4])

print(liste[:4])

print(liste[2:])

print(liste[:])

print(liste[1:5:2])

print(liste[::-1])

liste2 = liste

liste2[0] = 56
print(liste)

liste3 = liste[:]

print(id(liste))
print(id(liste2))
print(id(liste3))

liste4 = liste.copy()

print(id(liste4))


