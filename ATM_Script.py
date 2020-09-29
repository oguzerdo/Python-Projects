import time
import sys

class BankaHesabi:
    def __init__(self):
        self.bakiye = 0
        self.ekbakiye = 2000
        
        
    def hesap(self):
        
        while 1:
            try:
                self.name = input("İsim Giriniz : ")
                self.password = input("Sifre Giriniz : ")
                sys.stdout.write("Giriş yapılıyor, lütfen bekleyiniz")
                name = "....\n"  
                for char in name:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.3)
                print("Giriş başarıyla sağlandı.")
                return self.name, self.password
                
            except:
                print("Hatalı Girdi")
                continue

    def bakiye_goster(self):
        print("")
        print("_________________________________________________________________")
        print("")
        print("Bakiyeniz : {}\nEk Bakiyeniz : {}".format(self.bakiye,self.ekbakiye))
        print("")
        print("_________________________________________________________________")
    
    def para_cek(self,miktar):
        self.top_bakiye = self.bakiye + self.ekbakiye
        print("Merhaba Sn {} ".format(self.name))
        if self.bakiye >= miktar: #Çekilmek istenen ücret bakiyede mevcutsa
            print("")
            sys.stdout.write("Bankadan onay bekleniyor")
            name = "....\n"  
            for char in name:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.4)
            print("İşleminiz başarılıyla tamamlandı.Paranızı alabilirsiniz.")
            print("")
            print("Güncel Bakiyeniz:")
            self.bakiye = self.bakiye-miktar
            self.bakiye_goster()
            
        elif self.top_bakiye >= miktar: #Bakiye yetersiz, ek bakiye ile yeterli
            print("Bakiyeniz {} TL yeterli değil, Ek bakiyenizi {} TL kullanmak ister misiniz? (E/H)".format(self.bakiye,self.ekbakiye))
            value = input()
            value = value.lower()
            if value == "e":
                print("")
                sys.stdout.write("Bankadan onay bekleniyor.")
                name = "....\n"  
                for char in name:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.4)
                print("İşleminiz başarılıyla tamamlandı.Paranızı alabilirsiniz.")
                print("")
                print("Güncel Bakiyeniz:")
                self.top_bakiye = self.top_bakiye - miktar
                self.ekbakiye = self.top_bakiye
                self.bakiye = 0
                self.bakiye_goster()
                
            elif value == "h":
                self.bakiye_goster()
                
            else:
                print("Hatalı Giriş")
        else:
            print("")
            print("Yetersiz Bakiye!")
            print("")
            self.bakiye_goster()
            print("")
            print("Çekmek istediğiniz  tutar {} TL".format(miktar))
            print("En fazla {} TL tutarında para çekebilirsiniz !".format(self.top_bakiye))
            
            
            
    def para_yatir(self, miktar):
        self.bakiye = self.bakiye + miktar
        self.top_bakiye = self.bakiye + self.ekbakiye
        print("")
        print("{} TL tutarındaki paranız başarıyla yatırıldı.".format(miktar))
        self.bakiye_goster()
    
    def sifre_degistir(self):
        kontrol = ""
        while True:
            kontrol = input("Şuanki şifreniz:                        ")
            print("")
            if kontrol == self.password:
                key = input("Yeni şifre giriniz:                     ")
                print("")
                key_control = input("Yeni şifrenizi tekrar giriniz:  ")
                print("")
                if key == key_control:
                    self.password = key
                    sys.stdout.write("Şifre değiştiriliyor...")
                    name = "....\n"
                    for char in name:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(.3)
                    print("")
                    print("-------------------------------------------------------------------")
                    print("Şifreniz başarıyla güncellendi, lütfen şifrenizi kimseyle paylaşmayın")
                    break
                else:
                    print("Girdiğiniz şifreler uyuşmadı.")
                    print("")
            else:
                print("Yanlış şifre girdiniz.")
                print("------------------------")

        
    

    def ust_bilgi(self):
                print("")
                print("")
                print("""
                           {}
                      PYBANK'a Hoşgeldiniz Sn. {} 
                      """.format(time.strftime("%c"),self.name))   
        
user = BankaHesabi()
user.hesap()
user.ust_bilgi()
main_menu = True

while True:
    
    if main_menu:
        print("""
          Yapmak istediğiniz işlemi seçiniz.
      
          1. Bakiye Öğrenme
          2. Para Çekme
          3. Para Yatırma
          4. Şifre Değiştirme
          5. Çıkış""")
          
        print("")  
        choice = input("Seciminiz : ") 
        print("")
        
        try:
            choice = int(choice)
        except ValueError:
            print("ERROR")
            continue
        if choice == 1:
            print("")
            print("BAKİYE BİLGİLERİ")
            user.bakiye_goster()
        elif choice == 2:
            print("")
            print("PARA ÇEKME")
            user.bakiye_goster()
            miktar = int(input("Çekmek istediğiniz tutarı giriniz:\t"))
            user.para_cek(miktar)
            user.bakiye_goster
        elif choice == 3:
            print("")
            print("PARA ÇEKME")
            user.bakiye_goster()
            miktar = int(input("Yatırmak istediğiniz tutarı giriniz:\t"))
            user.para_yatir(miktar) 
        elif choice == 4:
            print("")
            print("ŞİFRE İŞLEMLERİ")
            print("")
            user.sifre_degistir()
        elif choice == 5:
            print("Bizi tercih ettiğiniz için teşekkürler iyi günler !")
            break
        else:
            print("Hatalı Giriş Tekrar Deneyin")
            main_menu = True
            
            

        
        
      
              
        








   