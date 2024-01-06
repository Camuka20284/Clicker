#pgzero

WIDTH = 600  # Oyunun genişlik boyutu
HEIGHT = 400  # Oyunun yükseklik boyutu

TITLE = "Hayvan Avcısı"  # Oyunun başlığı
FPS = 30  # Oyunun saniyedeki kare hızı (FPS - Frames Per Second)

# Oyun nesneleri (örnek: karakterler, arka plan)
hayvan = Actor("zürafa", (150, 250))  # Oyundaki ana karakter 
arkaplan = Actor("arkaplan")  # Oyunun arka planı
bonus_1 = Actor("bonus1", (450, 80))  # Bonus nesneleri
bonus_2 = Actor("bonus1", (450, 200))
bonus_3 = Actor("bonus1", (450, 320))
oyna = Actor("oyna", (300, 100))  # Ana menüdeki "Oyna" düğmesi
carpi = Actor("çarpı", (580, 20))  # Menü ve mağaza kapatma düğmesi
ok = Actor("ok2", (560, 360))  # Mağaza modunda "OK" düğmesi
ok2 = Actor("ok", (40, 360))  # Mağaza2 modunda "OK" düğmesi
magaza = Actor("mağaza", (300, 200))  # Ana menüdeki "Mağaza" düğmesi
koleksiyon = Actor("koleksiyon", (300, 300))  # Ana menüdeki "Koleksiyon" düğmesi
timsah = Actor("timsah", (120, 200))  # Mağaza modunda satın alınabilir hayvan karakteri
suaygiri = Actor("suaygırı", (300, 200))  # Mağaza modunda satın alınabilir hayvan karakteri
denizayisi = Actor('denizayısı', (480, 200))  # Mağaza modunda satın alınabilir hayvan karakteri
alinan = []  # Koleksiyon modunda toplanan hayvanlar
hayvanlar = []  # Oyunda kullanılabilir hayvan karakterlerinin listesi

# Değişkenler
puan = 0  # Oyundaki puan
tiklama = 1  # Tıklamayla kazanılan puan miktarı
mod = 'menü'  # Oyunun modu (menü, oyun, mağaza, mağaza2, koleksiyon)
ucret_1 = 15  # Bonus 1'in fiyatı
ucret_2 = 200  # Bonus 2'nin fiyatı
ucret_3 = 600  # Bonus 3'ün fiyatı

# draw fonksiyonu, oyundaki görsel öğelerin görüntülenmesi için kullanılır
def draw():
    if mod == 'menü':
        arkaplan.draw()
        oyna.draw()
        screen.draw.text(puan, center=(30, 20), color="black", fontsize=36)
        magaza.draw()
        koleksiyon.draw()
   
    elif mod == 'oyun':    
        arkaplan.draw()
        hayvan.draw()
        screen.draw.text(puan, center=(150, 100), color="black", fontsize=96)
        bonus_1.draw()
        screen.draw.text("Her 2 saniye için 1$", center=(450, 60), color="black", fontsize=20)
        screen.draw.text(ucret_1, center=(450, 90), color="black", fontsize=20)
        bonus_2.draw()
        screen.draw.text("Her 2 saniye için 15$", center=(450, 180), color="black", fontsize=20)
        screen.draw.text(ucret_2, center=(450, 210), color="black", fontsize=20)
        bonus_3.draw()
        screen.draw.text("Her 2 saniye için 50$", center=(450, 300), color="black", fontsize=20)
        screen.draw.text(ucret_3, center=(450, 330), color="black", fontsize=20)
        carpi.draw()
    
    elif mod == "mağaza":
        arkaplan.draw()
        screen.draw.text(puan, center=(30, 20), color="black", fontsize=36)
        carpi.draw()
        timsah.draw()
        screen.draw.text("500$", center=(120, 300), color="black", fontsize=36)
        suaygiri.draw()
        screen.draw.text("2500$", center=(300, 300), color="black", fontsize=36)
        denizayisi.draw()
        screen.draw.text("7000$", center=(485, 300), color="black", fontsize=36)
        
    elif mod == "mağaza2":
        arkaplan.draw()
        screen.draw.text(puan, center=(30, 20), color="black", fontsize=36)
        carpi.draw()
        screen.draw.text("...$", center=(120, 300), color="black", fontsize=36)
        screen.draw.text("...$", center=(300, 300), color="black", fontsize=36)
        screen.draw.text("...$", center=(485, 300), color="black", fontsize=36)
        ok2.draw()

    elif mod == "koleksiyon":
        arkaplan.draw()
        screen.draw.text(puan, center=(30, 20), color="black", fontsize=36)
        carpi.draw()
        screen.draw.text("+2$", center=(120, 300), color="black", fontsize=36)
        screen.draw.text("+3$", center=(300, 300), color="black", fontsize=36)
        screen.draw.text("+4$", center=(480, 300), color="black", fontsize=36)
        for i in range(len(hayvanlar)):
            hayvanlar[i].draw()

# bonus_1_icin, bonus 1'in tetiklendiğinde puanı artırır
def bonus_1_icin():
    global puan
    puan += 1

# bonus_2_icin, bonus 2'nin tetiklendiğinde puanı artırır
def bonus_2_icin():
    global puan
    puan += 15

# bonus_3_icin, bonus 3'ün tetiklendiğinde puanı artırır
def bonus_3_icin():
    global puan
    puan += 50

# on_mouse_down, fare tıklamalarını işler
def on_mouse_down(button, pos):
    global puan
    global mod
    global ucret_1, ucret_2, ucret_3
    global tiklama
    # Oyun Modu
    if button == mouse.LEFT and mod == "oyun":
        # Hayvanın üzerinde tıklama
        if hayvan.collidepoint(pos):
            puan += tiklama
            hayvan.y = 200
            animate(hayvan, tween='bounce_end', duration=0.5, y=250)
          # bonus_1 butonu tıklandığında  
        elif bonus_1.collidepoint(pos):
            bonus_1.y = 85
            animate(bonus_1, tween='bounce_end', duration=0.5, y=80)
            if puan >= ucret_1:
                schedule_interval(bonus_1_icin, 2)
                puan -= ucret_1
                ucret_1 += 25
        # bonus_2 butonu tıklandığında 
        elif bonus_2.collidepoint(pos):
            bonus_2.y = 205
            animate(bonus_2, tween='bounce_end', duration=0.5, y=200)
            if puan >= ucret_2:
                schedule_interval(bonus_2_icin, 2)
                puan -= ucret_2
                ucret_2 += 100
        # bonus_3 butonu tıklandığında
        elif bonus_3.collidepoint(pos):
            bonus_3.y = 325
            animate(bonus_3, tween='bounce_end', duration=0.5, y=320)
            if puan >= ucret_3:
                schedule_interval(bonus_3_icin, 2)
                puan -= ucret_3
                ucret_3 += 250
        elif carpi.collidepoint(pos):
            mod = 'menü'
    
    # Menü Modu
    elif mod == 'menü' and button == mouse.LEFT:
        if oyna.collidepoint(pos):
            mod = 'oyun'
        elif magaza.collidepoint(pos):
            mod = "mağaza"
        elif koleksiyon.collidepoint(pos):
            mod = "koleksiyon"
            
    elif mod == "mağaza" and button == mouse.LEFT:
        if carpi.collidepoint(pos):
            mod = "menü"
        elif timsah.collidepoint(pos):
            if timsah not in alinan and puan >= 500:
                alinan.append(timsah)
                timsah.y = 180
                animate(timsah, tween='bounce_end', duration=0.5, y=200)
                hayvan.image = "timsah"
                tiklama = 2
                puan -= 500
                hayvanlar.append(timsah)
        elif denizayisi.collidepoint(pos):
            if denizayisi not in alinan and puan >= 7000:
                alinan.append(denizayisi)
                denizayisi.y = 180
                animate(denizayisi, tween='bounce_end', duration=0.5, y=200)
                hayvan.image = "denizayısı"
                tiklama = 4
                puan -= 7000
                hayvanlar.append(denizayisi)
        elif suaygiri.collidepoint(pos):
            if suaygiri not in alinan and puan >= 2500:
                alinan.append(suaygiri)
                suaygiri.y = 180
                animate(suaygiri, tween='bounce_end', duration=0.5, y=200)
                hayvan.image = "suaygırı"
                tiklama = 3
                puan -= 2500
                hayvanlar.append(suaygiri)
                
        elif mod == "mağaza2" and button == mouse.LEFT:
            if ok2.collidepoint(pos):
                mod = "mağaza"
            if carpi.collidepoint(pos):
                mod = "menü"
                    
    elif mod == "koleksiyon" and button == mouse.LEFT:
        if carpi.collidepoint(pos):
            mod = "menü"
        elif timsah.collidepoint(pos):
            tiklama = 2
            timsah.y = 180
            animate(timsah, tween='bounce_end', duration=0.5, y=200)
            if timsah in hayvanlar:    
                hayvan.image = "timsah"
        elif suaygiri.collidepoint(pos):
            tiklama = 3
            suaygiri.y = 180
            animate(suaygiri, tween='bounce_end', duration=0.5, y=200)
            if suaygiri in hayvanlar:
                hayvan.image = "suaygırı"
        elif denizayisi.collidepoint(pos):
            tiklama = 4
            denizayisi.y = 180
            animate(denizayisi, tween='bounce_end', duration=0.5, y=200)
            if denizayisi in hayvanlar:
                hayvan.image = "denizayısı"
