#DÖNGÜLER
#While Döngüsü

# i=0
# while (i<=5):
# print("Kodlama")
# i=i+1

# i=0
# while (i<=20):
# print(i)
# i=i+2
# print("Döngü bitti")

#Sonsuz Döngü
# i=15
# while (i<20):
# print(i)
# i=i-1

#1-30 (30 dâhil) arasındaki tek sayıları while döngüsü ile ekrana yazdırınız.
i = 1
while(i < 30):
    print(i)
i = i+2

#60-30 (30 dâhil değil) arasındaki çift sayıları azalan sırada while döngüsü ile ekrana yazdırınız
i = 60
while (i > 30):
    print(i)
i = i-2

#0-100 (100 dâhil) arasındaki sayılardan 5’e tam bölünenleri while döngüsü ile ekrana yazdırınız.
i = 0
while(i < 100):
    if i % 5 == 0:
        print(i)
i = i+1

#while döngüsünü kullanarak faktöriyel hesabı yapan programı yazın.
i = 1
sonuc = 1
faktoriyel = int(input("Faktöriyeli hesaplanacak sayıyı girin:"))
while (i <= faktoriyel):
    sonuc = i*sonuc
i = i+1
print("Sonuç:", sonuc)

#1 ile 20 arasındaki (20 dâhil) sayıların toplamını bulan programı while döngüsü ile yazınız.
toplam = 0
i = 1
while (i <= 20):
    toplam = toplam+i
i = i+1
print("Toplam:", toplam)

#Girilen iki sayı arasındaki sayıları toplayan programı while döngüsü ile yazınız.
sayi1 = int(input("Başlangıç değerini girin:"))
sayi2 = int(input("Bitiş değerini girin:"))
toplam = 0
i = sayi1
while i <= sayi2:
    toplam = toplam+sayi1
i = i+1
print(toplam)

# Girilen sayı 0 (sıfır) olana kadar girilen tüm sayıları toplayan
# ve ekranda gösteren programı yazınız.
toplam = 0
sayi = 1
while (sayi != 0):
    sayi = int(input("Bir sayı girin:"))
toplam = toplam+sayi
print("Sonuc:", toplam)
