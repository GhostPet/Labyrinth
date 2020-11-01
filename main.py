import turtle
import keyboard
import movement
import maps

#   Labirent Oyunu'na Hoş Geldiniz!
#
#     Oyuna başlamak için Enter'a
#              basın...
#
#     Yapımcı: Ali Tiryaki - 2020
#
#     Esc tuşu ile çıkabilirsiniz...
def mainmenu():
    print("\n    Labirent Oyunu'na Hoş Geldiniz!\n\n     Oyuna başlamak için Enter'a\n              basın...\n\n     Yapımcı: Ali Tiryaki - 2020\n\n     Esc tuşu ile çıkabilirsiniz...")
    while True:
        if keyboard.read_key() == "esc":
            return False
        if keyboard.read_key() == "enter":
            return True


if __name__ == '__main__':
    game = mainmenu()  # Ana Menü'yü aç

    # Ekran ayarlama
    ekran = turtle.Screen()
    ekran_birim = 15
    ekran_boyutu = ekran_birim*50
    ekran.setup(ekran_boyutu+11, ekran_boyutu+11)

    # Önce dış sonra iç duvarları ayarlıyoruz.
    print("\n\n\n\n\n\n\n\nHarita yükleniyor... Lütfen biraz bekleyin.\n\n")
    duvarlar = turtle.Turtle()
    duvarlar.speed(3)
    duvarlar.pensize(2)
    maps.disduvar(duvarlar, ekran_boyutu)
    maps.icduvar(duvarlar, ekran_birim, maps.harita)  # Ana harita
    print("\n\n\n\n\n\n\n\nHarita yükleme tamamlandı. Oyuna başlayabilirsiniz.\n\n")

    # Hareket edecek çizgimizi ayarlıyoruz.
    adam = turtle.Turtle()
    adam.speed(0)
    # Onu haritanın orta altına gönderiyoruz.
    adam.color("white")
    adam.right(90)
    adam.forward(ekran_boyutu / 2)
    adam.left(180)
    # Ve harekete başlaması için ayarlıyoruz.
    adam.pensize(5)
    adam.color("red")
    adam.forward(25)
    yerx = 0
    yery = -7
    yon = "up"

    # Ana döngüyü başlat (klavye kontrolü)
    while game:
        if keyboard.read_key() == "up":

            # Kazanıp kazanmadığını kontrol etme
            if yerx == 0 and yery == +7:
                yon = movement.yukari(adam, yon)
                print("\n\n\n\n\n\n\n\nKazandınız!\n\n")
                del ekran
                break

            if -7 <= yery+1 <= +7 and [yerx, yery+1, yerx, yery] not in maps.harita:  # Gidilecek yerde iç/dış duvar var mı?
                yery += 1
                yon = movement.yukari(adam, yon)
            else:
                print("\n\n\n\n\n\n\n\nBir duvar gitmeni engelliyor.\n\n")
        if keyboard.read_key() == "down":
            if -7 <= yery-1 <= +7 and [yerx, yery, yerx, yery-1] not in maps.harita:  # Gidilecek yerde iç/dış duvar var mı?
                yery -= 1
                yon = movement.asagi(adam, yon)
            else:
                print("\n\n\n\n\n\n\n\nBir duvar gitmeni engelliyor.\n\n")
        if keyboard.read_key() == "right":
            if -7 <= yerx+1 <= +7 and [yerx, yery, yerx+1, yery] not in maps.harita:  # Gidilecek yerde iç/dış duvar var mı?
                yerx += 1
                yon = movement.sag(adam, yon)
            else:
                print("\n\n\n\n\n\n\n\nBir duvar gitmeni engelliyor.\n\n")
        if keyboard.read_key() == "left":
            if -7 <= yerx-1 <= +7 and [yerx-1, yery, yerx, yery] not in maps.harita:  # Gidilecek yerde iç/dış duvar var mı?
                yerx -= 1
                yon = movement.sol(adam, yon)
            else:
                print("\n\n\n\n\n\n\n\nBir duvar gitmeni engelliyor.\n\n")
        if keyboard.read_key() == "esc":
            game = False
