#DÖNGÜLER
#for döngüsü
#in kullanımı

# meyveler=["Karpuz","Çilek","Erik","Kavun"]
# for meyve in meyveler:
# print(meyve)
# for harfler in "BİLİŞİM":
# print(harfler*5)

# #PYTHON harflerini yan yana 10 defa ekrana yazdıran kodu oluşturun.
# for harfler in "PYTHON":
# print(harfler*10)

#10-20 arası sayılardan oluşan sayilar isimli bir liste oluşturarak liste içinde
# 3’e tam bölünen sayıları ekrana yazdırınız.
# sayilar=[10,11,12,13,14,15,16,17,18,19,20]
# for sayi in sayilar:
# if sayi%3==0:
# print(sayi)
#Yukarıdaki listede bulunan çift sayıları ekrana yazdırınız.
# sayilar=[10,11,12,13,14,15,16,17,18,19,20]
# for sayi in sayilar:
# if sayi%2==0:
# print(sayi)

#alan_adi isimli, değeri bilişim olan bir değişken tanımlayarak içinde kaç adet “i”
#harfi olduğunu bulup ekrana yazdırınız.
alan_adi="bilişim"
toplam=0
for aranan in alan_adi:
    if aranan=="i":
         toplam=toplam+1
print("Bu kelimede toplam",toplam,"adet i harfi vardır.")
#DÖNGÜLER
#for döngüsü
#Range kullanımı
#
# for sayilar in range(10):
# print(sayilar)
# print("------------------")
# for sayilar in range(5,10):
# print(sayilar)
# print("------------------")
# for sayilar in range(3,30,5):
# print(sayilar)
# print("------------------")
# for sayilar in range(30,5,-4):
# print(sayilar)
# print("------------------")
# #ÖRNEKLER
# #1-)0-20 arası çift sayıları for döngüsü ile ekrana yazdırınız.
# for sayi in range(0,20,2):
# print(sayi)
# print("------------------")
# #2-)1-30 arası tek sayıları for döngüsü ile ekrana yazdırınız.
# for sayi in range(1,30,2):
# print(sayi)
# print("------------------")
# #3-)3’ten başlayarak 41’e kadar olan sayıları 5’er arttırarak for döngüsü ile ekrana yazdırınız.
# for cift in range(3,41,5):
# print(cift)
# print("------------------")
# #4-)50’den 20’ye kadar olan sayıları 3’er azaltarak for döngüsü ile ekrana yazdırınız.
# for sayilar in range(50,20,-3):
# print(sayilar)
# else:
# print("Döngü bitti")

# #for döngüsü ile 1’den 10’a kadar olan sayıların toplamını bularak ekrana yazdırınız.
# toplam=0
# for sayilar in range(11):
# toplam=toplam+sayilar
# print("Sayıların toplamı:",toplam)
#
# #Girilen iki sayı arasındaki sayıların toplamını bularak ekrana yazdırınız.
# toplam=0
# sayi1=int(input('1. Sayıyı Giriniz: '))
# sayi2=int(input('2. Sayıyı Giriniz: '))
# for i in range(sayi1,sayi2+1):
# toplam+=i #toplam=toplam+i
# print(toplam)
#Girilen sayının faktöriyelini bularak ekrana yazdırınız.
sayi=int(input("Faktöriyelini almak istediğin sayıyı gir:"))
sonuc=1
for faktoriyel in range(sayi):
    sonuc=sonuc*(faktoriyel+1)
print("Faktöriyel:",sonuc)