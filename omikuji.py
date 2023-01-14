import pyxel
import random


pyxel.init(200,200)
pyxel.mouse(True)

TAIKICHU = 1800
HYOUJICHU = 0
mikuji = 0


def update():
    global mikuji
    global HYOUJICHU
    
    if HYOUJICHU > 0:
        HYOUJICHU -= 1
    else:
        mikuji = 0

        if pyxel.btn(pyxel.KEY_SPACE):

            mikuji = random.randint(1,4)
            HYOUJICHU = 300



def draw():
    global HYOUJICHU, TAIKICHU, mikuji
    pyxel.cls(6)



    if mikuji == 0:

        #おみくじ
        pyxel.load("omikuji.pyxres")
        pyxel.blt(70,20,0,32,16,64,16)

        #スペースキー押してね
        pyxel.load("omikuji.pyxres")
        pyxel.blt(20,80,0,0,144,160,16)
        if TAIKICHU > 0:
            TAIKICHU -= 1
        else:
            
            #押してください
            pyxel.load("omikuji.pyxres")
            pyxel.blt(70,120,0,48,0,104,16)

    elif mikuji == 1:
        #大吉
        pyxel.load("omikuji.pyxres")
        pyxel.blt(70,20,0,0,0,32,16)

        #今年はあなたの年
        pyxel.load("omikuji.pyxres")
        pyxel.blt(20,80,0,0,128,128,16)

    elif mikuji == 2:
        #中吉
        pyxel.load("omikuji.pyxres")
        pyxel.blt(70,20,0,0,32,32,16)

        #そこそこ
        pyxel.load("omikuji.pyxres")
        pyxel.blt(60,80,0,0,160,64,16)

    elif mikuji == 3:
        #小吉
        pyxel.load("omikuji.pyxres")
        pyxel.blt(70,20,0,0,16,32,16)

        #びみょう
        pyxel.load("omikuji.pyxres")
        pyxel.blt(60,80,0,0,176,64,16)

    elif mikuji == 4:
        #凶
        pyxel.load("omikuji.pyxres")
        pyxel.blt(80,20,0,0,48,16,16)

        #きをつけて
        pyxel.load("omikuji.pyxres")
        pyxel.blt(60,80,0,0,192,80,16)
pyxel.run(update, draw)
