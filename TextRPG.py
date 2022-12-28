print("TextRPG'ye hoş geldin!")
giris = input("\nYeni karakter oluşturmak için = n, \nEski oyuna devam etmek için = y yaz: ")
if giris == 'n':
    kullanici_adi = input("\nKullanıcı adını seç: ")
    print("\nSınıfler: Savaşçı = 1, Okçu = 2, Büyücü = 3")
    secilen_sinif = input("\nOynamak istediğin sınıfı seç: ")
    if secilen_sinif == '1':
        sınıf = 'savaşçı'
        can = 1750
        hasar = 250
    elif secilen_sinif == '2':
        sınıf = 'okçu'
        can = 1500
        hasar = 300
    elif secilen_sinif == '3':
        sınıf = 'büyücü'
        can = 1250
        hasar = 350
    else:
        print("\nSınıf seçerken bir hata oluştu!")
    altın = 250
    envanter = [""]
    profil = [kullanici_adi, sınıf, can, hasar, altın]
elif giris == 'y':
    def stringToList(string):
        listRes = list(string.split(" "))
        return listRes
    kayitli_oyun = open("TextRPG.txt", "r")
    profil = stringToList(kayitli_oyun.read())
    kayitli_oyun.close()
rehber = "\nRehber = r, Profil = p, Envanter = e, \nMağaza = m, Zindan = z"
print(rehber)
while True: 
    eylem = input("\nNe yapmak istersin: ")
    if eylem == 'r':
        print("\n Rehber = 1, Envanter = 2, Mağaza = 3, Zindan = 4")
    elif eylem == 'p':
        print("\n Kullanıcı Adı:", profil[0], "Sınıf:", profil[1], "Can:", profil[2], "Hasar:", profil[3], "Altın:", profil[4])
    elif eylem == 'e':
        print(envanter)
    kayitli_oyun = open("TextRPG.txt", "w")
    kayitli_oyun.write(str(profil))
    kayitli_oyun.close()