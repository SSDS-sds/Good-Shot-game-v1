#importing libraries
import pgzrun
from random import randint 

WIDTH = 500
HEIGHT = 500
TITLE = "Good Shot"

msg = ""
#creating the character
alien = Actor("alien")

def draw():
    screen.clear()
    screen.fill(color = ("blue"))
    alien.draw()
    screen.draw.text(msg,center = (400,20),fontsize = 30,color = ("#0A210F"))

def place_aln ():
    alien.x = randint(50,450)
    alien.y = randint(50,450)

def on_mouse_down(pos):
    global msg
    if alien.collidepoint(pos):
        msg = "GOOD SHOT!"
        place_aln()
    else:
        msg = "YOU MISSED!!!"

place_aln()


pgzrun.go()