#Break ve Continue Deyimleri
# i=1
# while True:
# if (i==5):
# print("Döngüden çıkıldı")
# break
# print(i)
# i=i+1

#Kullanıcıdan 1 ile 5 arasında bir sayı girmesini isteyiniz. Kullanıcı 3 sayısını girdiğinde
# break komutu ile döngüden çıkılarak “3 sayısı girildi ve döngü sona erdi” çıktısı veren
# kodu yazınız.

# while True:
# sayi=input("1-5 arasında bir sayı girin:")
# if sayi=="3":
# break
# print("3 girildi ve döngü sona erdi.")

#Kullanıcıdan 8 karakterlik bir şifre girmesini isteyiniz. Kullanıcı 8’den az ya da
# daha fazla karakter içeren bir şifre girdiğinde “Şifreniz 8 karakter olmalıdır.”
# şeklinde uyarı verdiriniz. Kullanıcı şartlara uygun bir şifre girdiğinde de
# “Şifreniz kaydedildi.” uyarısı verdiriniz.

# while True:
# sifre = input("Şifre girin:")
# if len(sifre) == 8:
# print('Şifreniz Kaydedildi')
# break
# print('Şifreniz 8 karakterli olmalıdır')

#kullanıcıdan 1-10 arası sayı girmesini isteyin.Girilen sayı kadar döngüyü çalıştıran kodu yazın.
# sayi=int(input("1-10 arasında bir sayı girin:"))
# for i in range(1,10):
# if i==sayi:
# break
# print(i)
# print("Döngü sona erdi.")

#14 sayısı bulunduğunda döngüden çıkılan kodu yazın.
# sayilar=[10,11,12,13,14,15,16]
# for aranan in sayilar:
# print(aranan)
# if (aranan==14):
# print("14 sayısı bulundu")
# break

# Elemanları alfabedeki ilk 8 harf olan bir liste oluşturarak “e”
# harfine gelindiğinde döngüden çıkan kodu yazınız.
# alfabe=["a","b","c","d","e","g","h","j"]
# for harf in alfabe:
# print(harf)
# if(harf=='e'):
# print('harf bulundu')
# break

# import random
# while True:
# n=random.randint(1,20)
# print("Rastgele seçilen",n)
# if n%2==0:
# print("Çift sayı seçildi, döngü bitti")
# break

#1 ile 100 arasında rastgele 6 sayı seçerek ekrana yazdırınız.
# import random
# for i in range(1,7):
# print(random.randint(1,100))