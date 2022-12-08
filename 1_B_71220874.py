print ("SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERLUBANG")
asu = int(input("Masukkan angka :"))
print (" "*(asu-1), "*")
for bola in range ((asu-1),1,-1) :
    print (" "*(bola-1),"**")
print ("**"*asu)