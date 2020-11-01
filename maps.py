harita = [
    # 1.dikey
    [-6, 7, -5, 7], [-4, 7, -3, 7], [-2, 7, -1, 7], [6, 7, 7, 7],
    # 1.yatay
    [-2, 7, -2, 6], [0, 7, 0, 6], [1, 7, 1, 6], [3, 7, 3, 6],
    # 2.dikey
    [-7, 6, -6, 6], [-7, 6, -6, 6], [-6, 6, -5, 6], [-5, 6, -4, 6], [-4, 6, -3, 6], [-1, 6, 0, 6], [1, 6, 2, 6],
    [1, 6, 2, 6], [3, 6, 4, 6], [5, 6, 6, 6], [6, 6, 7, 6],
    # 2.yatay
    [-7, 6, -7, 5], [-3, 6, -3, 5], [-2, 6, -2, 5], [-1, 6, -1, 5], [2, 6, 2, 5], [3, 6, 3, 5], [4, 6, 4, 5],
    # 3.dikey
    [-6, 5, -5, 5], [-5, 5, -4, 5], [-3, 5, -2, 5], [0, 5, 1, 5], [5, 5, 6, 5], [6, 5, 7, 5],
    # 3.yatay
    [-6, 5, -6, 4], [-5, 5, -5, 4], [-7, 5, -7, 4], [-7, 5, -7, 4], [-1, 5, -1, 4], [0, 5, 0, 4], [1, 5, 1, 4],
    [2, 5, 2, 4], [3, 5, 3, 4], [4, 5, 4, 4], [5, 5, 5, 4],
    # 4.dikey
    [-7, 4, -6, 4], [-4, 4, -3, 4], [-3, 4, -2, 4], [-2, 4, -1, 4], [0, 4, 1, 4],
    # 4.yatay
    [-5, 4, -5, 3], [-4, 4, -4, 3], [1, 4, 1, 3], [4, 4, 4, 3], [5, 4, 5, 3], [6, 4, 6, 3], [7, 4, 7, 3],
    # 5.dikey
    [-5, 3, -4, 3], [-3, 3, -2, 3], [-1, 3, 0, 3], [1, 3, 2, 3], [2, 3, 3, 3], [5, 3, 6, 3],
    # 5.yatay
    [-7, 3, -7, 2], [-4, 3, -4, 2], [-3, 3, -3, 2], [-2, 3, -2, 2], [0, 3, 0, 2], [2, 3, 2, 2], [3, 3, 3, 2],
    [4, 3, 4, 2]
    # 6.dikey
    # ...
    # 15.yatay
]


def disduvar(turtle2, size):
    turtle2.color("white")
    turtle2.goto((-size / 2) - 4, (size / 2) + 4)
    turtle2.color("black")
    # üst duvar
    turtle2.forward(size / 2 - 25)
    turtle2.color("white")
    turtle2.forward(50)
    turtle2.color("black")
    turtle2.forward(size / 2 - 25)
    # sağ duvar
    turtle2.right(90)
    turtle2.forward(size)
    # alt duvar
    turtle2.right(90)
    turtle2.forward(size / 2 - 25)
    turtle2.color("white")
    turtle2.forward(50)
    turtle2.color("black")
    turtle2.forward(size / 2 - 25)
    # sol duvar
    turtle2.right(90)
    turtle2.forward(size)
    turtle2.right(90)


# Her 50x50 birimlik yer yerx,yery listesinde bir boşluktur.
# Her duvar iki birimin isminin yan yana gelmesiyle oluşur.
#
# Örneğin:
# [x-7,y+7] [x-6,y+7]
# [x-7,y+6] [x-6,y+6]
#
# [x-7,y+7],[x-6,y+7] duvarı dikey ve ikisinin arasındadır.

def icduvar(turtle2, size, harita1):
    # Dikey duvarlar
    for x in range(int(-(size - 1) / 2), int((size - 1) / 2), 1):
        if x == 0:
            turtle2.color("white")
        else:
            turtle2.color("black")
        turtle2.forward(50)
        turtle2.right(90)
        # aşağı in
        turtle2.color("gray")
        turtle2.forward(size * 50)
        # yukarı çık ve yazdır
        turtle2.right(180)
        for y in range(int(-(size - 1) / 2), int((size + 1) / 2), 1):
            if [x, y, x + 1, y] in harita1:
                turtle2.color("black")
            else:
                turtle2.color("lightgreen")
            turtle2.forward(50)
        turtle2.right(90)
    turtle2.color("black")
    turtle2.forward(50)
    # Yatay duvarlar
    turtle2.right(90)
    for y in range(int((size - 1) / 2), int(-(size - 1) / 2), -1):
        turtle2.color("black")
        turtle2.forward(50)
        turtle2.right(90)
        # sağa git
        turtle2.color("gray")
        turtle2.forward(size * 50)
        # yukarı çık ve yazdır
        turtle2.right(180)
        for x in range(int(-(size - 1) / 2), int((size + 1) / 2), 1):
            if [x, y, x, y - 1] in harita1:
                turtle2.color("black")
            else:
                turtle2.color("lightgreen")
            turtle2.forward(50)
        turtle2.right(90)
    turtle2.color("black")
    turtle2.forward(50)
