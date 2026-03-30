# materi kuliah perulangn di python

a = ["aura", "bogi", "fairus"]

for x in a:
    print(x)

for x in enumerate(a):
    print(x,end="")

print("")
# perulangan dengan range
for i in range(10):
    print(i)
    
    
# loop while
# i = 0
# while i < 10:
#     print(i)
    

print("")
# membuat stape 
for i in range(1,10,2): # mulai, akhir, kelipatan
    print(i, end="")
    
    
print("")
wkwkwk = int(input("masukan nilai anda: "))
for i in range(wkwkwk):
    print(i)
    

angka = int(input("masukan bilangan: (1-10)"))

if angka < 1 or angka > 10:
    print("salah input")
else:
    for i in range(angka):
        print(i)
        
        
angka2 = int(input("masukan bilangan: (1-10)"))


if angka2 < 1:
    print("salah input")
elif angka2 > 10:
    print("salah input")
else:
    for i in range(angka2):
        print(i)
        
print("")
        
