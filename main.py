#1
m = ("olma", "banan", "anor", "shaftoli", "uzum")

text = m[0]
natija = 0

for i, s in enumerate(m):
    if len(s) > len(text):
        eng_uzun = s
        indeks = i

print("Eng uzun string:", text)
print("Indeksi:", natija)

#2
t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')

natija = ()

for i in range(len(t1)):
    natija += (t1[i], t2[i])

print(natija)

#3
A = {1, 2, 3, 4, 5}
B = {3, 4, 6}
C = {4, 5, 7}

natija = A - (B | C)

print(natija)
