# dari pada melulis perulangan 1 sampai 10 dengan print manual dan memperbanyak struktur code, ad cara simpel menggunakan for 
list_number = [1,2,3,4,5,6,7,8,9,10]

for i in list_number:
    print(i)
    
"""
    akan menampilkan 1 sampai 10
"""
    
    
# adapun contoh lain mengunakan perulangan 
for i in range(10): # hasil akan 0 sampai 9 karena range memulai dari 0
    print(i)

"""
    strukture range(start,stop,step)
"""
for i in range(1,10,2): 
    print(i)
    
    

print("   ")


"""
    sintaks python while 
    
    While termasuk sintaks dalam Python yang bersifat indefinite iteration. Indefinite iteration adalah sebuah proses iterasi yang akan berhenti ketika memenuhi kondisi tertentu.
"""
    
counter = 1
while counter <= 5:
    print(counter)
    counter += 1 # Increment
    
#hati2 jangan membuat loop terus 

"""
    Loop bersarang
    
    Ketika Anda membuat perulangan, sering kali menemukan perulangan dalam perulangan atau disebut sebagai nested loop. 
"""

for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)
    