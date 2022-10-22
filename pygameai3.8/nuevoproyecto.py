import pygame, sys
from pygame.locals import *
import pygame_ai as pai
import random
import time
import numpy
import menu

pygame.mixer.pre_init(44100, 16, 1, 512)
pygame.init()

NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)
SSBCOLOR = (236, 250, 252)
VERDE = (34, 177, 76)
ancho = 700
alto = 350
vec = pygame.math.Vector2
ACC = 0.3
FRIC = -0.10
FPS = 60
clock = pygame.time.Clock()
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("combate dragon ball")
pygame.mixer.music.load("musica/Dragon-Ball-Super-Ultimate-Battle-by-Akira-Kushida-sub.-español-『AMV』-_BUENTEMA.APP_.wav")
pygame.mixer.music.play()
Grav = True

headingfont = pygame.font.SysFont("Verdana", 10, True, True)
regularfont = pygame.font.SysFont('Corbel', 25)
smallerfont = pygame.font.SysFont('Corbel', 16)
text = regularfont.render('LOAD', True, ROJO)

kaioken_l = [pygame.image.load("gokukaioken/kaiokenizk8.png"),
             pygame.image.load("gokukaioken/kaiokenizk1.png"),
             pygame.image.load("gokukaioken/kaiokenizk1.png"),
             pygame.image.load("gokukaioken/kaiokenizk1.png"),
             pygame.image.load("gokukaioken/kaiokenizk3.png"),
             pygame.image.load("gokukaioken/kaiokenizk3.png"),
             pygame.image.load("gokukaioken/kaiokenizk3.png"),
             pygame.image.load("gokukaioken/kaiokenizk4.png"),
             pygame.image.load("gokukaioken/kaiokenizk4.png"),
             pygame.image.load("gokukaioken/kaiokenizk4.png"),
             pygame.image.load("gokukaioken/kaiokenizk5.png"),
             pygame.image.load("gokukaioken/kaiokenizk5.png"),
             pygame.image.load("gokukaioken/kaiokenizk5.png"),
             pygame.image.load("gokukaioken/kaiokenizk6.png"),
             pygame.image.load("gokukaioken/kaiokenizk7.png"),
             pygame.image.load("gokukaioken/kaiokenizk8.png"),
             pygame.image.load("gokukaioken/kaiokenizk6.png"),
             pygame.image.load("gokukaioken/kaiokenizk7.png"),
             pygame.image.load("gokukaioken/kaiokenizk8.png"),
             pygame.image.load("gokukaioken/kaiokenizk6.png"),
             pygame.image.load("gokukaioken/kaiokenizk7.png"),
             pygame.image.load("gokukaioken/kaiokenizk8.png"),
             pygame.image.load("gokukaioken/kaiokenizk6.png"),
             pygame.image.load("gokukaioken/kaiokenizk7.png"),
             pygame.image.load("gokukaioken/kaiokenizk8.png"),
             pygame.image.load("gokukaioken/kaiokenizk6.png"),
             pygame.image.load("gokukaioken/kaiokenizk7.png"),
             pygame.image.load("gokukaioken/kaiokenizk8.png"),
             pygame.image.load("gokukaioken/kaiokenizk6.png"),
             pygame.image.load("gokukaioken/kaiokenizk7.png"),
             pygame.image.load("gokukaioken/kaiokenizk8.png"),
             pygame.image.load("gokukaioken/kaiokenizk6.png"),
             pygame.image.load("gokukaioken/kaiokenizk7.png"),
             pygame.image.load("gokukaioken/kaiokenizk8.png"),
             pygame.image.load("gokukaioken/kaiokenizk6.png"),
             pygame.image.load("gokukaioken/kaiokenizk7.png"),
             pygame.image.load("gokukaioken/kaiokenizk8.png"),
             pygame.image.load("gokukaioken/kaiokenizk6.png"),
             pygame.image.load("gokukaioken/kaiokenizk7.png"),
             pygame.image.load("gokukaioken/kaiokenizk8.png"),
             pygame.image.load("gokukaioken/kaiokenizk6.png"),
             pygame.image.load("gokukaioken/kaiokenizk7.png"),
             pygame.image.load("gokukaioken/kaiokenizk8.png"),
             pygame.image.load("gokukaioken/kaiokenizk6.png"),
             pygame.image.load("gokukaioken/kaiokenizk7.png"),
             pygame.image.load("gokukaioken/kaiokenizk8.png")]

kaioken_r = [pygame.image.load("gokukaioken/kaioken8.png"),
             pygame.image.load("gokukaioken/kaioken1.png"),
             pygame.image.load("gokukaioken/kaioken1.png"),
             pygame.image.load("gokukaioken/kaioken1.png"),
             pygame.image.load("gokukaioken/kaioken3.png"),
             pygame.image.load("gokukaioken/kaioken3.png"),
             pygame.image.load("gokukaioken/kaioken3.png"),
             pygame.image.load("gokukaioken/kaioken4.png"),
             pygame.image.load("gokukaioken/kaioken4.png"),
             pygame.image.load("gokukaioken/kaioken4.png"),
             pygame.image.load("gokukaioken/kaioken5.png"),
             pygame.image.load("gokukaioken/kaioken5.png"),
             pygame.image.load("gokukaioken/kaioken5.png"),
             pygame.image.load("gokukaioken/kaioken6.png"),
             pygame.image.load("gokukaioken/kaioken7.png"),
             pygame.image.load("gokukaioken/kaioken8.png"),
             pygame.image.load("gokukaioken/kaioken6.png"),
             pygame.image.load("gokukaioken/kaioken7.png"),
             pygame.image.load("gokukaioken/kaioken8.png"),
             pygame.image.load("gokukaioken/kaioken6.png"),
             pygame.image.load("gokukaioken/kaioken7.png"),
             pygame.image.load("gokukaioken/kaioken8.png"),
             pygame.image.load("gokukaioken/kaioken6.png"),
             pygame.image.load("gokukaioken/kaioken7.png"),
             pygame.image.load("gokukaioken/kaioken8.png"),
             pygame.image.load("gokukaioken/kaioken6.png"),
             pygame.image.load("gokukaioken/kaioken7.png"),
             pygame.image.load("gokukaioken/kaioken8.png"),
             pygame.image.load("gokukaioken/kaioken6.png"),
             pygame.image.load("gokukaioken/kaioken7.png"),
             pygame.image.load("gokukaioken/kaioken8.png"),
             pygame.image.load("gokukaioken/kaioken6.png"),
             pygame.image.load("gokukaioken/kaioken7.png"),
             pygame.image.load("gokukaioken/kaioken8.png"),
             pygame.image.load("gokukaioken/kaioken6.png"),
             pygame.image.load("gokukaioken/kaioken7.png"),
             pygame.image.load("gokukaioken/kaioken8.png"),
             pygame.image.load("gokukaioken/kaioken6.png"),
             pygame.image.load("gokukaioken/kaioken7.png"),
             pygame.image.load("gokukaioken/kaioken8.png"),
             pygame.image.load("gokukaioken/kaioken6.png"),
             pygame.image.load("gokukaioken/kaioken7.png"),
             pygame.image.load("gokukaioken/kaioken8.png"),
             pygame.image.load("gokukaioken/kaioken6.png"),
             pygame.image.load("gokukaioken/kaioken7.png"),
             pygame.image.load("gokukaioken/kaioken8.png")]

jiren_run_r = [pygame.image.load("jiren andando/jiren2.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren2.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren2.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren2.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren3.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren3.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren3.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren3.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren4.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren4.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren4.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren4.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren5.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren5.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren5.png").convert_alpha(),
               pygame.image.load("jiren andando/jiren5.png").convert_alpha()]

jiren_run_l = [pygame.image.load("jiren andando/jirenizk2.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk2.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk2.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk2.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk3.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk3.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk3.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk3.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk4.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk4.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk4.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk4.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk5.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk5.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk5.png").convert_alpha(),
               pygame.image.load("jiren andando/jirenizk5.png").convert_alpha()]
# imagenes correr derecha jugador
correr_der = [pygame.image.load("movimientosGoku/gokuder1.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder1.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder1.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder1.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder2.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder2.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder2.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder2.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder3.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder3.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder3.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder3.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder4.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder4.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder4.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder4.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder5.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder5.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder5.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder5.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder6.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder6.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder6.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder6.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder7.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder7.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder7.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuder7.png").convert_alpha()]

# imagenes correr izquierda jugador
correr_izq = [pygame.image.load("movimientosGoku/gokuizk1.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuizk1.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuizk1.png").convert_alpha(),
              pygame.image.load("movimientosGoku/gokuizk1.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk2.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk2.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk2.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk2.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk3.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk3.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk3.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk3.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk4.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk4.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk4.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk4.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk5.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk5.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk5.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk5.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk6.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk6.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk6.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk6.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk7.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk7.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk7.png").convert(),
              pygame.image.load("movimientosGoku/gokuizk7.png").convert()]
# imagenes atake derecha jugador
atake_der = [pygame.image.load("gokuatakes/puñoder4.png").convert(),
             pygame.image.load("gokuatakes/puñoder4.png").convert(),
             pygame.image.load("gokuatakes/puñoder4.png").convert(),
             pygame.image.load("gokuatakes/puñoder4.png").convert(),
             pygame.image.load("gokuatakes/puñoder5.png").convert(),
             pygame.image.load("gokuatakes/puñoder5.png").convert(),
             pygame.image.load("gokuatakes/puñoder5.png").convert(),
             pygame.image.load("gokuatakes/puñoder5.png").convert(),
             pygame.image.load("gokuatakes/puñoder6.png").convert(),
             pygame.image.load("gokuatakes/puñoder6.png").convert(),
             pygame.image.load("gokuatakes/puñoder6.png").convert(),
             pygame.image.load("gokuatakes/puñoder6.png").convert(),
             pygame.image.load("gokuatakes/puñoder7.png").convert(),
             pygame.image.load("gokuatakes/puñoder7.png").convert(),
             pygame.image.load("gokuatakes/puñoder7.png").convert(),
             pygame.image.load("gokuatakes/puñoder7.png").convert(),
             pygame.image.load("gokuatakes/puñoder8.png").convert(),
             pygame.image.load("gokuatakes/puñoder8.png").convert(),
             pygame.image.load("gokuatakes/puñoder8.png").convert(),
             pygame.image.load("gokuatakes/puñoder8.png").convert(),
             pygame.image.load("gokuatakes/puñoder9.png").convert(),
             pygame.image.load("gokuatakes/puñoder9.png").convert(),
             pygame.image.load("gokuatakes/puñoder9.png").convert(),
             pygame.image.load("gokuatakes/puñoder9.png").convert(),
             pygame.image.load("gokuatakes/puñoder10.png").convert(),
             pygame.image.load("gokuatakes/puñoder10.png").convert(),
             pygame.image.load("gokuatakes/puñoder10.png").convert(),
             pygame.image.load("gokuatakes/puñoder10.png").convert(),
             pygame.image.load("gokuatakes/puñoder11.png").convert(),
             pygame.image.load("gokuatakes/puñoder11.png").convert(),
             pygame.image.load("gokuatakes/puñoder11.png").convert(),
             pygame.image.load("gokuatakes/puñoder11.png").convert()]

# imagenes atake izquierda jugador
atake_izq = [pygame.image.load("gokuatakes/puñoizk4.png").convert(),
             pygame.image.load("gokuatakes/puñoizk4.png").convert(),
             pygame.image.load("gokuatakes/puñoizk4.png").convert(),
             pygame.image.load("gokuatakes/puñoizk4.png").convert(),
             pygame.image.load("gokuatakes/puñoizk5.png").convert(),
             pygame.image.load("gokuatakes/puñoizk5.png").convert(),
             pygame.image.load("gokuatakes/puñoizk5.png").convert(),
             pygame.image.load("gokuatakes/puñoizk5.png").convert(),
             pygame.image.load("gokuatakes/puñoizk6.png").convert(),
             pygame.image.load("gokuatakes/puñoizk6.png").convert(),
             pygame.image.load("gokuatakes/puñoizk6.png").convert(),
             pygame.image.load("gokuatakes/puñoizk6.png").convert(),
             pygame.image.load("gokuatakes/puñoizk7.png").convert(),
             pygame.image.load("gokuatakes/puñoizk7.png").convert(),
             pygame.image.load("gokuatakes/puñoizk7.png").convert(),
             pygame.image.load("gokuatakes/puñoizk7.png").convert(),
             pygame.image.load("gokuatakes/puñoizk8.png").convert(),
             pygame.image.load("gokuatakes/puñoizk8.png").convert(),
             pygame.image.load("gokuatakes/puñoizk8.png").convert(),
             pygame.image.load("gokuatakes/puñoizk8.png").convert(),
             pygame.image.load("gokuatakes/puñoizk9.png").convert(),
             pygame.image.load("gokuatakes/puñoizk9.png").convert(),
             pygame.image.load("gokuatakes/puñoizk9.png").convert(),
             pygame.image.load("gokuatakes/puñoizk9.png").convert(),
             pygame.image.load("gokuatakes/puñoizk10.png").convert(),
             pygame.image.load("gokuatakes/puñoizk10.png").convert(),
             pygame.image.load("gokuatakes/puñoizk10.png").convert(),
             pygame.image.load("gokuatakes/puñoizk10.png").convert(),
             pygame.image.load("gokuatakes/puñoizk11.png").convert(),
             pygame.image.load("gokuatakes/puñoizk11.png").convert(),
             pygame.image.load("gokuatakes/puñoizk11.png").convert(),
             pygame.image.load("gokuatakes/puñoizk11.png").convert()]


# Attack animation for the RIGHT
attack_kame_R = [pygame.image.load("movimientosGoku/gokuder1.png").convert(),
                 pygame.image.load("gokuatakes/kameder1.png").convert(),
                 pygame.image.load("gokuatakes/kameder1.png").convert(),
                 pygame.image.load("gokuatakes/kameder1.png").convert(),
                 pygame.image.load("gokuatakes/kameder1.png").convert(),
                 pygame.image.load("gokuatakes/kameder2.png").convert(),
                 pygame.image.load("gokuatakes/kameder2.png").convert(),
                 pygame.image.load("gokuatakes/kameder2.png").convert(),
                 pygame.image.load("gokuatakes/kameder2.png").convert(),
                 pygame.image.load("gokuatakes/kameder3.png").convert(),
                 pygame.image.load("gokuatakes/kameder3.png").convert(),
                 pygame.image.load("gokuatakes/kameder3.png").convert(),
                 pygame.image.load("gokuatakes/kameder3.png").convert(),
                 pygame.image.load("gokuatakes/kameder4.png").convert(),
                 pygame.image.load("gokuatakes/kameder4.png").convert(),
                 pygame.image.load("gokuatakes/kameder4.png").convert(),
                 pygame.image.load("gokuatakes/kameder4.png").convert(),
                 pygame.image.load("gokuatakes/kameder4.png").convert(),
                 pygame.image.load("gokuatakes/kameder4.png").convert(),
                 pygame.image.load("gokuatakes/kameder4.png").convert(),
                 pygame.image.load("gokuatakes/kameder4.png").convert(),
                 pygame.image.load("gokuatakes/kameder4.png").convert(),
                 pygame.image.load("gokuatakes/kameder4.png").convert(),
                 pygame.image.load("gokuatakes/kameder4.png").convert(),
                 pygame.image.load("gokuatakes/kameder4.png").convert(),
                 pygame.image.load("gokuatakes/kameder5.png").convert(),
                 pygame.image.load("gokuatakes/kameder5.png").convert(),
                 pygame.image.load("gokuatakes/kameder5.png").convert(),
                 pygame.image.load("gokuatakes/kameder5.png").convert(),
                 pygame.image.load("gokuatakes/kameder6.png").convert(),
                 pygame.image.load("gokuatakes/kameder6.png").convert(),
                 pygame.image.load("gokuatakes/kameder6.png").convert(),
                 pygame.image.load("gokuatakes/kameder6.png").convert()]

# Attack animation for the LEFT
attack_kame_L = [pygame.image.load("movimientosGoku/gokuizk1.png").convert(),
                 pygame.image.load("gokuatakes/kameizk1.png").convert(),
                 pygame.image.load("gokuatakes/kameizk1.png").convert(),
                 pygame.image.load("gokuatakes/kameizk1.png").convert(),
                 pygame.image.load("gokuatakes/kameizk1.png").convert(),
                 pygame.image.load("gokuatakes/kameizk2.png").convert(),
                 pygame.image.load("gokuatakes/kameizk2.png").convert(),
                 pygame.image.load("gokuatakes/kameizk2.png").convert(),
                 pygame.image.load("gokuatakes/kameizk2.png").convert(),
                 pygame.image.load("gokuatakes/kameizk3.png").convert(),
                 pygame.image.load("gokuatakes/kameizk3.png").convert(),
                 pygame.image.load("gokuatakes/kameizk3.png").convert(),
                 pygame.image.load("gokuatakes/kameizk3.png").convert(),
                 pygame.image.load("gokuatakes/kameizk4.png").convert(),
                 pygame.image.load("gokuatakes/kameizk4.png").convert(),
                 pygame.image.load("gokuatakes/kameizk4.png").convert(),
                 pygame.image.load("gokuatakes/kameizk4.png").convert(),
                 pygame.image.load("gokuatakes/kameizk4.png").convert(),
                 pygame.image.load("gokuatakes/kameizk4.png").convert(),
                 pygame.image.load("gokuatakes/kameizk4.png").convert(),
                 pygame.image.load("gokuatakes/kameizk4.png").convert(),
                 pygame.image.load("gokuatakes/kameizk4.png").convert(),
                 pygame.image.load("gokuatakes/kameizk4.png").convert(),
                 pygame.image.load("gokuatakes/kameizk4.png").convert(),
                 pygame.image.load("gokuatakes/kameizk4.png").convert(),
                 pygame.image.load("gokuatakes/kameizk5.png").convert(),
                 pygame.image.load("gokuatakes/kameizk5.png").convert(),
                 pygame.image.load("gokuatakes/kameizk5.png").convert(),
                 pygame.image.load("gokuatakes/kameizk5.png").convert(),
                 pygame.image.load("gokuatakes/kameizk6.png").convert(),
                 pygame.image.load("gokuatakes/kameizk6.png").convert(),
                 pygame.image.load("gokuatakes/kameizk6.png").convert(),
                 pygame.image.load("gokuatakes/kameizk6.png").convert()]

patada_der = [pygame.image.load("gokuatakes/patadader1.png"),
              pygame.image.load("gokuatakes/patadader1.png"),
              pygame.image.load("gokuatakes/patadader1.png"),
              pygame.image.load("gokuatakes/patadader1.png"),
              pygame.image.load("gokuatakes/patadader2.png"),
              pygame.image.load("gokuatakes/patadader2.png"),
              pygame.image.load("gokuatakes/patadader2.png"),
              pygame.image.load("gokuatakes/patadader2.png"),
              pygame.image.load("gokuatakes/patadader3.png"),
              pygame.image.load("gokuatakes/patadader3.png"),
              pygame.image.load("gokuatakes/patadader3.png"),
              pygame.image.load("gokuatakes/patadader3.png"),
              pygame.image.load("gokuatakes/patadader4.png"),
              pygame.image.load("gokuatakes/patadader4.png"),
              pygame.image.load("gokuatakes/patadader4.png"),
              pygame.image.load("gokuatakes/patadader4.png"),
              pygame.image.load("gokuatakes/patadader5.png"),
              pygame.image.load("gokuatakes/patadader5.png"),
              pygame.image.load("gokuatakes/patadader5.png"),
              pygame.image.load("gokuatakes/patadader5.png"),
              pygame.image.load("gokuatakes/patadader8.png"),
              pygame.image.load("gokuatakes/patadader8.png"),
              pygame.image.load("gokuatakes/patadader8.png"),
              pygame.image.load("gokuatakes/patadader8.png"),
              pygame.image.load("gokuatakes/patadader9.png"),
              pygame.image.load("gokuatakes/patadader9.png"),
              pygame.image.load("gokuatakes/patadader9.png"),
              pygame.image.load("gokuatakes/patadader9.png"), ]

patada_izq = [pygame.image.load("gokuatakes/patadaizk1.png"),
              pygame.image.load("gokuatakes/patadaizk1.png"),
              pygame.image.load("gokuatakes/patadaizk1.png"),
              pygame.image.load("gokuatakes/patadaizk1.png"),
              pygame.image.load("gokuatakes/patadaizk2.png"),
              pygame.image.load("gokuatakes/patadaizk2.png"),
              pygame.image.load("gokuatakes/patadaizk2.png"),
              pygame.image.load("gokuatakes/patadaizk2.png"),
              pygame.image.load("gokuatakes/patadaizk3.png"),
              pygame.image.load("gokuatakes/patadaizk3.png"),
              pygame.image.load("gokuatakes/patadaizk3.png"),
              pygame.image.load("gokuatakes/patadaizk3.png"),
              pygame.image.load("gokuatakes/patadaizk4.png"),
              pygame.image.load("gokuatakes/patadaizk4.png"),
              pygame.image.load("gokuatakes/patadaizk4.png"),
              pygame.image.load("gokuatakes/patadaizk4.png"),
              pygame.image.load("gokuatakes/patadaizk5.png"),
              pygame.image.load("gokuatakes/patadaizk5.png"),
              pygame.image.load("gokuatakes/patadaizk5.png"),
              pygame.image.load("gokuatakes/patadaizk5.png"),
              pygame.image.load("gokuatakes/patadaizk8.png"),
              pygame.image.load("gokuatakes/patadaizk8.png"),
              pygame.image.load("gokuatakes/patadaizk8.png"),
              pygame.image.load("gokuatakes/patadaizk8.png"),
              pygame.image.load("gokuatakes/patadaizk9.png"),
              pygame.image.load("gokuatakes/patadaizk9.png"),
              pygame.image.load("gokuatakes/patadaizk9.png"),
              pygame.image.load("gokuatakes/patadaizk9.png"), ]

bola_kame_r = [pygame.image.load("prueba gif/kameder1.png"),
               pygame.image.load("prueba gif/kameder1.png"),
               pygame.image.load("prueba gif/kameder1.png"),
               pygame.image.load("prueba gif/kameder2.png"),
               pygame.image.load("prueba gif/kameder2.png"),
               pygame.image.load("prueba gif/kameder2.png"),
               pygame.image.load("prueba gif/kameder3.png"),
               pygame.image.load("prueba gif/kameder3.png"),
               pygame.image.load("prueba gif/kameder3.png"),
               pygame.image.load("prueba gif/kameder4.png"),
               pygame.image.load("prueba gif/kameder4.png"),
               pygame.image.load("prueba gif/kameder4.png"),
               pygame.image.load("prueba gif/kameder5.png"),
               pygame.image.load("prueba gif/kameder5.png"),
               pygame.image.load("prueba gif/kameder5.png"),
               pygame.image.load("prueba gif/kameder6.png"),
               pygame.image.load("prueba gif/kameder6.png"),
               pygame.image.load("prueba gif/kameder6.png"),
               pygame.image.load("prueba gif/kameder7.png"),
               pygame.image.load("prueba gif/kameder8.png"),
               pygame.image.load("prueba gif/kameder9.png"),
               pygame.image.load("prueba gif/kameder7.png"),
               pygame.image.load("prueba gif/kameder8.png"),
               pygame.image.load("prueba gif/kameder9.png"),
               pygame.image.load("prueba gif/kameder7.png"),
               pygame.image.load("prueba gif/kameder8.png"),
               pygame.image.load("prueba gif/kameder9.png"),
               pygame.image.load("prueba gif/kameder7.png"),
               pygame.image.load("prueba gif/kameder8.png"),
               pygame.image.load("prueba gif/kameder9.png"),
               pygame.image.load("prueba gif/kameder7.png"),
               pygame.image.load("prueba gif/kameder8.png"),
               pygame.image.load("prueba gif/kameder9.png"),
               pygame.image.load("prueba gif/kameder7.png"),
               pygame.image.load("prueba gif/kameder8.png"),
               pygame.image.load("prueba gif/kameder9.png"),
               pygame.image.load("prueba gif/kameder7.png"),
               pygame.image.load("prueba gif/kameder8.png"),
               pygame.image.load("prueba gif/kameder9.png"),
               pygame.image.load("prueba gif/kameder7.png"),
               pygame.image.load("prueba gif/kameder8.png")]

bola_kame_l = [pygame.image.load("prueba gif/kameizk1.png"),
               pygame.image.load("prueba gif/kameizk1.png"),
               pygame.image.load("prueba gif/kameizk1.png"),
               pygame.image.load("prueba gif/kameizk2.png"),
               pygame.image.load("prueba gif/kameizk2.png"),
               pygame.image.load("prueba gif/kameizk2.png"),
               pygame.image.load("prueba gif/kameizk3.png"),
               pygame.image.load("prueba gif/kameizk3.png"),
               pygame.image.load("prueba gif/kameizk3.png"),
               pygame.image.load("prueba gif/kameizk4.png"),
               pygame.image.load("prueba gif/kameizk4.png"),
               pygame.image.load("prueba gif/kameizk4.png"),
               pygame.image.load("prueba gif/kameizk5.png"),
               pygame.image.load("prueba gif/kameizk5.png"),
               pygame.image.load("prueba gif/kameizk5.png"),
               pygame.image.load("prueba gif/kameizk6.png"),
               pygame.image.load("prueba gif/kameizk6.png"),
               pygame.image.load("prueba gif/kameizk6.png"),
               pygame.image.load("prueba gif/kameizk7.png"),
               pygame.image.load("prueba gif/kameizk8.png"),
               pygame.image.load("prueba gif/kameizk9.png"),
               pygame.image.load("prueba gif/kameizk7.png"),
               pygame.image.load("prueba gif/kameizk8.png"),
               pygame.image.load("prueba gif/kameizk9.png"),
               pygame.image.load("prueba gif/kameizk7.png"),
               pygame.image.load("prueba gif/kameizk8.png"),
               pygame.image.load("prueba gif/kameizk9.png"),
               pygame.image.load("prueba gif/kameizk7.png"),
               pygame.image.load("prueba gif/kameizk8.png"),
               pygame.image.load("prueba gif/kameizk9.png"),
               pygame.image.load("prueba gif/kameizk7.png"),
               pygame.image.load("prueba gif/kameizk8.png"),
               pygame.image.load("prueba gif/kameizk9.png"),
               pygame.image.load("prueba gif/kameizk7.png"),
               pygame.image.load("prueba gif/kameizk8.png"),
               pygame.image.load("prueba gif/kameizk9.png"),
               pygame.image.load("prueba gif/kameizk7.png"),
               pygame.image.load("prueba gif/kameizk8.png"),
               pygame.image.load("prueba gif/kameizk9.png"),
               pygame.image.load("prueba gif/kameizk7.png"),
               pygame.image.load("prueba gif/kameizk8.png")]

jiren_puño = [pygame.image.load("jiren andando/jirenpuño1.png"),
              pygame.image.load("jiren andando/jirenpuño1.png"),
              pygame.image.load("jiren andando/jirenpuño1.png"),
              pygame.image.load("jiren andando/jirenpuño2.png"),
              pygame.image.load("jiren andando/jirenpuño2.png"),
              pygame.image.load("jiren andando/jirenpuño2.png"),
              pygame.image.load("jiren andando/jirenpuño3.png"),
              pygame.image.load("jiren andando/jirenpuño3.png"),
              pygame.image.load("jiren andando/jirenpuño3.png")]
jiren_patada = [pygame.image.load("jiren andando/jirenpat1.png"),
                pygame.image.load("jiren andando/jirenpat1.png"),
                pygame.image.load("jiren andando/jirenpat1.png"),
                pygame.image.load("jiren andando/jirenpat2.png"),
                pygame.image.load("jiren andando/jirenpat2.png"),
                pygame.image.load("jiren andando/jirenpat2.png"),
                pygame.image.load("jiren andando/jirenpat3.png"),
                pygame.image.load("jiren andando/jirenpat3.png"),
                pygame.image.load("jiren andando/jirenpat3.png"),
                pygame.image.load("jiren andando/jirenpat4.png"),
                pygame.image.load("jiren andando/jirenpat4.png"),
                pygame.image.load("jiren andando/jirenpat4.png"),
                pygame.image.load("jiren andando/jirenpat5.png"),
                pygame.image.load("jiren andando/jirenpat5.png"),
                pygame.image.load("jiren andando/jirenpat5.png"),
                pygame.image.load("jiren andando/jirenpat6.png"),
                pygame.image.load("jiren andando/jirenpat6.png"),
                pygame.image.load("jiren andando/jirenpat6.png")]
boom = [pygame.image.load("explosiones/0.png"),
        pygame.image.load("explosiones/0.png"),
        pygame.image.load("explosiones/1.png"),
        pygame.image.load("explosiones/1.png"),
        pygame.image.load("explosiones/2.png"),
        pygame.image.load("explosiones/2.png"),
        pygame.image.load("explosiones/3.png"),
        pygame.image.load("explosiones/3.png"),
        pygame.image.load("explosiones/4.png"),
        pygame.image.load("explosiones/4.png"),
        pygame.image.load("explosiones/5.png"),
        pygame.image.load("explosiones/5.png"),
        pygame.image.load("explosiones/6.png"),
        pygame.image.load("explosiones/6.png"),
        pygame.image.load("explosiones/7.png"),
        pygame.image.load("explosiones/7.png"),
        pygame.image.load("explosiones/8.png"),
        pygame.image.load("explosiones/8.png"),
        pygame.image.load("explosiones/9.png"),
        pygame.image.load("explosiones/9.png"),
        pygame.image.load("explosiones/10.png"),
        pygame.image.load("explosiones/10.png"),
        pygame.image.load("explosiones/11.png"),
        pygame.image.load("explosiones/11.png"),
        pygame.image.load("explosiones/12.png"),
        pygame.image.load("explosiones/12.png"),
        pygame.image.load("explosiones/13.png"),
        pygame.image.load("explosiones/13.png")]

carga_r = [pygame.image.load("movimientosGoku/gokuder1.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 45.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 45.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 45.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 45.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 46.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 46.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 46.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 46.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 47.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 48.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 47.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 48.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 47.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 48.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 47.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 48.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 47.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 48.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 47.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi 48.png").convert()]

carga_l = [pygame.image.load("movimientosGoku/gokuizk1.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 45.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 45.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 45.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 45.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 46.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 46.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 46.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 46.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 47.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 48.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 47.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 48.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 47.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 48.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 47.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 48.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 47.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 48.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 47.png").convert(),
           pygame.image.load("gokuparado/Goku Whis Gi izk 48.png").convert()]

genkidama = [pygame.image.load("bolagenki/genki1.png"),
             pygame.image.load("bolagenki/genki1.png"),
             pygame.image.load("bolagenki/genki2.png"),
             pygame.image.load("bolagenki/genki3.png"),
             pygame.image.load("bolagenki/genki2.png"),
             pygame.image.load("bolagenki/genki3.png"),
             pygame.image.load("bolagenki/genki2.png"),
             pygame.image.load("bolagenki/genki3.png"),
             pygame.image.load("bolagenki/genki2.png"),
             pygame.image.load("bolagenki/genki3.png"),
             pygame.image.load("bolagenki/genki2.png"),
             pygame.image.load("bolagenki/genki3.png")]

attack_genki_r = [pygame.image.load("bolagenki/gokugenki5.png"),
                  pygame.image.load("bolagenki/gokugenki1.png"),
                  pygame.image.load("bolagenki/gokugenki1.png"),
                  pygame.image.load("bolagenki/gokugenki2.png"),
                  pygame.image.load("bolagenki/gokugenki2.png"),
                  pygame.image.load("bolagenki/gokugenki3.png"),
                  pygame.image.load("bolagenki/gokugenki3.png"),
                  pygame.image.load("bolagenki/gokugenki4.png"),
                  pygame.image.load("bolagenki/gokugenki4.png"),
                  pygame.image.load("bolagenki/gokugenki5.png"),
                  pygame.image.load("bolagenki/gokugenki5.png")]

attack_genki_l = [pygame.image.load("bolagenki/gokugenkiizk5.png"),
                  pygame.image.load("bolagenki/gokugenkiizk1.png"),
                  pygame.image.load("bolagenki/gokugenkiizk1.png"),
                  pygame.image.load("bolagenki/gokugenkiizk2.png"),
                  pygame.image.load("bolagenki/gokugenkiizk2.png"),
                  pygame.image.load("bolagenki/gokugenkiizk3.png"),
                  pygame.image.load("bolagenki/gokugenkiizk3.png"),
                  pygame.image.load("bolagenki/gokugenkiizk4.png"),
                  pygame.image.load("bolagenki/gokugenkiizk4.png"),
                  pygame.image.load("bolagenki/gokugenkiizk5.png"),
                  pygame.image.load("bolagenki/gokugenkiizk5.png")]

puño_kaioken_r = [pygame.image.load("gokukaioken/puñokaioken1.png"),
                  pygame.image.load("gokukaioken/puñokaioken1.png"),
                  pygame.image.load("gokukaioken/puñokaioken2.png"),
                  pygame.image.load("gokukaioken/puñokaioken2.png"),
                  pygame.image.load("gokukaioken/puñokaioken3.png"),
                  pygame.image.load("gokukaioken/puñokaioken3.png"),
                  pygame.image.load("gokukaioken/puñokaioken1.png"),
                  pygame.image.load("gokukaioken/puñokaioken1.png"),
                  pygame.image.load("gokukaioken/puñokaioken2.png"),
                  pygame.image.load("gokukaioken/puñokaioken2.png"),
                  pygame.image.load("gokukaioken/puñokaioken3.png"),
                  pygame.image.load("gokukaioken/puñokaioken3.png"),
                  pygame.image.load("gokukaioken/puñokaioken1.png"),
                  pygame.image.load("gokukaioken/puñokaioken1.png"),
                  pygame.image.load("gokukaioken/puñokaioken2.png"),
                  pygame.image.load("gokukaioken/puñokaioken2.png"),
                  pygame.image.load("gokukaioken/puñokaioken3.png"),
                  pygame.image.load("gokukaioken/puñokaioken3.png")]

puño_kaioken_l = [pygame.image.load("gokukaioken/puñokaiokenizk1.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk1.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk2.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk2.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk3.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk3.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk1.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk1.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk2.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk2.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk3.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk3.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk1.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk1.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk2.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk2.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk3.png"),
                  pygame.image.load("gokukaioken/puñokaiokenizk3.png")]

patada_kaioken_r = [pygame.image.load("gokukaioken/patadakaioken1.png"),
                    pygame.image.load("gokukaioken/patadakaioken1.png"),
                    pygame.image.load("gokukaioken/patadakaioken1.png"),
                    pygame.image.load("gokukaioken/patadakaioken2.png"),
                    pygame.image.load("gokukaioken/patadakaioken2.png"),
                    pygame.image.load("gokukaioken/patadakaioken2.png"),
                    pygame.image.load("gokukaioken/patadakaioken2.png"),
                    pygame.image.load("gokukaioken/patadakaioken3.png"),
                    pygame.image.load("gokukaioken/patadakaioken3.png"),
                    pygame.image.load("gokukaioken/patadakaioken3.png"),
                    pygame.image.load("gokukaioken/patadakaioken4.png"),
                    pygame.image.load("gokukaioken/patadakaioken4.png"),
                    pygame.image.load("gokukaioken/patadakaioken4.png"),
                    pygame.image.load("gokukaioken/patadakaioken4.png"),
                    pygame.image.load("gokukaioken/patadakaioken5.png"),
                    pygame.image.load("gokukaioken/patadakaioken5.png"),
                    pygame.image.load("gokukaioken/patadakaioken5.png")]

patada_kaioken_l = [pygame.image.load("gokukaioken/patadakaiokenizk1.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk1.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk1.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk2.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk2.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk2.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk2.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk3.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk3.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk3.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk4.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk4.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk4.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk4.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk5.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk5.png"),
                    pygame.image.load("gokukaioken/patadakaiokenizk5.png")]

kame_kaioken_r = [pygame.image.load("gokukaioken/kamekaioken1.png"),
                  pygame.image.load("gokukaioken/kamekaioken1.png"),
                  pygame.image.load("gokukaioken/kamekaioken1.png"),
                  pygame.image.load("gokukaioken/kamekaioken2.png"),
                  pygame.image.load("gokukaioken/kamekaioken2.png"),
                  pygame.image.load("gokukaioken/kamekaioken2.png"),
                  pygame.image.load("gokukaioken/kamekaioken3.png"),
                  pygame.image.load("gokukaioken/kamekaioken3.png"),
                  pygame.image.load("gokukaioken/kamekaioken3.png"),
                  pygame.image.load("gokukaioken/kamekaioken4.png"),
                  pygame.image.load("gokukaioken/kamekaioken4.png"),
                  pygame.image.load("gokukaioken/kamekaioken4.png"),
                  pygame.image.load("gokukaioken/kamekaioken4.png"),
                  pygame.image.load("gokukaioken/kamekaioken4.png"),
                  pygame.image.load("gokukaioken/kamekaioken5.png"),
                  pygame.image.load("gokukaioken/kamekaioken5.png"),
                  pygame.image.load("gokukaioken/kamekaioken5.png"),
                  pygame.image.load("gokukaioken/kamekaioken6.png"),
                  pygame.image.load("gokukaioken/kamekaioken6.png"),
                  pygame.image.load("gokukaioken/kamekaioken6.png")]

kame_kaioken_l = [pygame.image.load("gokukaioken/kamekaiokenizk1.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk1.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk1.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk2.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk2.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk2.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk3.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk3.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk3.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk4.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk4.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk4.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk4.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk4.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk5.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk5.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk5.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk6.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk6.png"),
                  pygame.image.load("gokukaioken/kamekaiokenizk6.png")]

kaioken_energia_r = [pygame.image.load("gokukaioken/gokucargakaioken1.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken2.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken3.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken1.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken2.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken3.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken1.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken2.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken3.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken1.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken2.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken3.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken1.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken2.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken3.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken1.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken2.png"),
                     pygame.image.load("gokukaioken/gokucargakaioken3.png")]

kaioken_energia_l = [pygame.image.load("gokukaioken/gokucargakaiokenizk1.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk2.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk3.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk1.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk2.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk3.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk1.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk2.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk3.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk1.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk2.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk3.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk1.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk2.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk3.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk1.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk2.png"),
                     pygame.image.load("gokukaioken/gokucargakaiokenizk3.png")]

sayajin1_r = [pygame.image.load("gokussf1/gokussf1parado.png"),
              pygame.image.load("gokussf1/gokussf1.png"),
              pygame.image.load("gokussf1/gokussf1.png"),
              pygame.image.load("gokussf1/gokussf2.png"),
              pygame.image.load("gokussf1/gokussf2.png"),
              pygame.image.load("gokussf1/gokussf2.png"),
              pygame.image.load("gokussf1/gokussf3.png"),
              pygame.image.load("gokussf1/gokussf3.png"),
              pygame.image.load("gokussf1/gokussf3.png"),
              pygame.image.load("gokussf1/gokussf1.png"),
              pygame.image.load("gokussf1/gokussf1.png"),
              pygame.image.load("gokussf1/gokussf1.png"),
              pygame.image.load("gokussf1/gokussf2.png"),
              pygame.image.load("gokussf1/gokussf2.png"),
              pygame.image.load("gokussf1/gokussf2.png"),
              pygame.image.load("gokussf1/gokussf3.png"),
              pygame.image.load("gokussf1/gokussf3.png"),
              pygame.image.load("gokussf1/gokussf3.png")]

sayajin1_l = [pygame.image.load("gokussf1/gokussf1paradoizk.png"),
              pygame.image.load("gokussf1/gokussf1izk.png"),
              pygame.image.load("gokussf1/gokussf1izk.png"),
              pygame.image.load("gokussf1/gokussf2izk.png"),
              pygame.image.load("gokussf1/gokussf2izk.png"),
              pygame.image.load("gokussf1/gokussf2izk.png"),
              pygame.image.load("gokussf1/gokussf3izk.png"),
              pygame.image.load("gokussf1/gokussf3izk.png"),
              pygame.image.load("gokussf1/gokussf3izk.png"),
              pygame.image.load("gokussf1/gokussf1izk.png"),
              pygame.image.load("gokussf1/gokussf1izk.png"),
              pygame.image.load("gokussf1/gokussf1izk.png"),
              pygame.image.load("gokussf1/gokussf2izk.png"),
              pygame.image.load("gokussf1/gokussf2izk.png"),
              pygame.image.load("gokussf1/gokussf2izk.png"),
              pygame.image.load("gokussf1/gokussf3izk.png"),
              pygame.image.load("gokussf1/gokussf3izk.png"),
              pygame.image.load("gokussf1/gokussf3izk.png")]

sayajin1_puño_r = [pygame.image.load("gokussf1/puño1.png"),
                   pygame.image.load("gokussf1/puño1.png"),
                   pygame.image.load("gokussf1/puño1.png"),
                   pygame.image.load("gokussf1/puño2.png"),
                   pygame.image.load("gokussf1/puño2.png"),
                   pygame.image.load("gokussf1/puño2.png"),
                   pygame.image.load("gokussf1/puño1.png"),
                   pygame.image.load("gokussf1/puño1.png"),
                   pygame.image.load("gokussf1/puño1.png"),
                   pygame.image.load("gokussf1/puño2.png"),
                   pygame.image.load("gokussf1/puño2.png"),
                   pygame.image.load("gokussf1/puño2.png"),
                   pygame.image.load("gokussf1/puño1.png"),
                   pygame.image.load("gokussf1/puño1.png"),
                   pygame.image.load("gokussf1/puño1.png"),
                   pygame.image.load("gokussf1/puño2.png"),
                   pygame.image.load("gokussf1/puño2.png"),
                   pygame.image.load("gokussf1/puño2.png"),
                   pygame.image.load("gokussf1/puño1.png"),
                   pygame.image.load("gokussf1/puño1.png"),
                   pygame.image.load("gokussf1/puño1.png"),
                   pygame.image.load("gokussf1/puño2.png"),
                   pygame.image.load("gokussf1/puño2.png"),
                   pygame.image.load("gokussf1/puño2.png"),
                   pygame.image.load("gokussf1/puño1.png"),
                   pygame.image.load("gokussf1/puño2.png")]

sayajin1_puño_l = [pygame.image.load("gokussf1/puñoizk1.png"),
                   pygame.image.load("gokussf1/puñoizk1.png"),
                   pygame.image.load("gokussf1/puñoizk1.png"),
                   pygame.image.load("gokussf1/puñoizk2.png"),
                   pygame.image.load("gokussf1/puñoizk2.png"),
                   pygame.image.load("gokussf1/puñoizk2.png"),
                   pygame.image.load("gokussf1/puñoizk1.png"),
                   pygame.image.load("gokussf1/puñoizk1.png"),
                   pygame.image.load("gokussf1/puñoizk1.png"),
                   pygame.image.load("gokussf1/puñoizk2.png"),
                   pygame.image.load("gokussf1/puñoizk2.png"),
                   pygame.image.load("gokussf1/puñoizk2.png"),
                   pygame.image.load("gokussf1/puñoizk1.png"),
                   pygame.image.load("gokussf1/puñoizk1.png"),
                   pygame.image.load("gokussf1/puñoizk1.png"),
                   pygame.image.load("gokussf1/puñoizk2.png"),
                   pygame.image.load("gokussf1/puñoizk2.png"),
                   pygame.image.load("gokussf1/puñoizk2.png"),
                   pygame.image.load("gokussf1/puñoizk1.png"),
                   pygame.image.load("gokussf1/puñoizk1.png"),
                   pygame.image.load("gokussf1/puñoizk1.png"),
                   pygame.image.load("gokussf1/puñoizk2.png"),
                   pygame.image.load("gokussf1/puñoizk2.png"),
                   pygame.image.load("gokussf1/puñoizk2.png"),
                   pygame.image.load("gokussf1/puñoizk1.png"),
                   pygame.image.load("gokussf1/puñoizk2.png")]

sayajin1_patada_r = [pygame.image.load("gokussf1/patada1.png"),
                     pygame.image.load("gokussf1/patada1.png"),
                     pygame.image.load("gokussf1/patada1.png"),
                     pygame.image.load("gokussf1/patada1.png"),
                     pygame.image.load("gokussf1/patada2.png"),
                     pygame.image.load("gokussf1/patada2.png"),
                     pygame.image.load("gokussf1/patada2.png"),
                     pygame.image.load("gokussf1/patada2.png"),
                     pygame.image.load("gokussf1/patada3.png"),
                     pygame.image.load("gokussf1/patada3.png"),
                     pygame.image.load("gokussf1/patada3.png"),
                     pygame.image.load("gokussf1/patada3.png"),
                     pygame.image.load("gokussf1/patada4.png"),
                     pygame.image.load("gokussf1/patada4.png"),
                     pygame.image.load("gokussf1/patada4.png"),
                     pygame.image.load("gokussf1/patada4.png"),
                     pygame.image.load("gokussf1/patada5.png"),
                     pygame.image.load("gokussf1/patada5.png"),
                     pygame.image.load("gokussf1/patada5.png"),
                     pygame.image.load("gokussf1/patada5.png")]

sayajin1_patada_l = [pygame.image.load("gokussf1/patadaizk1.png"),
                     pygame.image.load("gokussf1/patadaizk1.png"),
                     pygame.image.load("gokussf1/patadaizk1.png"),
                     pygame.image.load("gokussf1/patadaizk1.png"),
                     pygame.image.load("gokussf1/patadaizk2.png"),
                     pygame.image.load("gokussf1/patadaizk2.png"),
                     pygame.image.load("gokussf1/patadaizk2.png"),
                     pygame.image.load("gokussf1/patadaizk2.png"),
                     pygame.image.load("gokussf1/patadaizk3.png"),
                     pygame.image.load("gokussf1/patadaizk3.png"),
                     pygame.image.load("gokussf1/patadaizk3.png"),
                     pygame.image.load("gokussf1/patadaizk3.png"),
                     pygame.image.load("gokussf1/patadaizk4.png"),
                     pygame.image.load("gokussf1/patadaizk4.png"),
                     pygame.image.load("gokussf1/patadaizk4.png"),
                     pygame.image.load("gokussf1/patadaizk4.png"),
                     pygame.image.load("gokussf1/patadaizk5.png"),
                     pygame.image.load("gokussf1/patadaizk5.png"),
                     pygame.image.load("gokussf1/patadaizk5.png"),
                     pygame.image.load("gokussf1/patadaizk5.png")]

sayajin1_kame = [pygame.image.load("gokussf1/kame1.png"),
                 pygame.image.load("gokussf1/kame1.png"),
                 pygame.image.load("gokussf1/kame1.png"),
                 pygame.image.load("gokussf1/kame2.png"),
                 pygame.image.load("gokussf1/kame2.png"),
                 pygame.image.load("gokussf1/kame2.png"),
                 pygame.image.load("gokussf1/kame3.png"),
                 pygame.image.load("gokussf1/kame3.png"),
                 pygame.image.load("gokussf1/kame3.png"),
                 pygame.image.load("gokussf1/kame4.png"),
                 pygame.image.load("gokussf1/kame4.png"),
                 pygame.image.load("gokussf1/kame4.png"),
                 pygame.image.load("gokussf1/kame5.png"),
                 pygame.image.load("gokussf1/kame5.png"),
                 pygame.image.load("gokussf1/kame5.png"),
                 pygame.image.load("gokussf1/kame5.png"),
                 pygame.image.load("gokussf1/kame5.png"),
                 pygame.image.load("gokussf1/kame5.png"),
                 pygame.image.load("gokussf1/kame5.png"),
                 pygame.image.load("gokussf1/kame5.png"),
                 pygame.image.load("gokussf1/kame6.png"),
                 pygame.image.load("gokussf1/kame6.png"),
                 pygame.image.load("gokussf1/kame6.png"),
                 pygame.image.load("gokussf1/kame7.png"),
                 pygame.image.load("gokussf1/kame7.png"),
                 pygame.image.load("gokussf1/kame7.png")]

sayajin1_carga_energia_r = [pygame.image.load("gokussf1/carga1.png"),
                            pygame.image.load("gokussf1/carga2.png"),
                            pygame.image.load("gokussf1/carga3.png"),
                            pygame.image.load("gokussf1/carga1.png"),
                            pygame.image.load("gokussf1/carga2.png"),
                            pygame.image.load("gokussf1/carga3.png"),
                            pygame.image.load("gokussf1/carga1.png"),
                            pygame.image.load("gokussf1/carga2.png"),
                            pygame.image.load("gokussf1/carga3.png"),
                            pygame.image.load("gokussf1/carga1.png"),
                            pygame.image.load("gokussf1/carga2.png"),
                            pygame.image.load("gokussf1/carga3.png")]

sayajin1_carga_energia_l = [pygame.image.load("gokussf1/cargaizk1.png"),
                            pygame.image.load("gokussf1/cargaizk2.png"),
                            pygame.image.load("gokussf1/cargaizk3.png"),
                            pygame.image.load("gokussf1/cargaizk1.png"),
                            pygame.image.load("gokussf1/cargaizk2.png"),
                            pygame.image.load("gokussf1/cargaizk3.png"),
                            pygame.image.load("gokussf1/cargaizk1.png"),
                            pygame.image.load("gokussf1/cargaizk2.png"),
                            pygame.image.load("gokussf1/cargaizk3.png"),
                            pygame.image.load("gokussf1/cargaizk1.png"),
                            pygame.image.load("gokussf1/cargaizk2.png"),
                            pygame.image.load("gokussf1/cargaizk3.png")]

sayajin_r = [pygame.image.load("gokuss/ss5.png"),
             pygame.image.load("gokuss/ss1.png"),
             pygame.image.load("gokuss/ss1.png"),
             pygame.image.load("gokuss/ss2.png"),
             pygame.image.load("gokuss/ss2.png"),
             pygame.image.load("gokuss/ss2.png"),
             pygame.image.load("gokuss/ss3.png"),
             pygame.image.load("gokuss/ss3.png"),
             pygame.image.load("gokuss/ss3.png"),
             pygame.image.load("gokuss/ss4.png"),
             pygame.image.load("gokuss/ss4.png"),
             pygame.image.load("gokuss/ss4.png"),
             pygame.image.load("gokuss/ss5.png"),
             pygame.image.load("gokuss/ss5.png"),
             pygame.image.load("gokuss/ss5.png"),
             pygame.image.load("gokuss/ss4.png"),
             pygame.image.load("gokuss/ss4.png"),
             pygame.image.load("gokuss/ss4.png"),
             pygame.image.load("gokuss/ss5.png"),
             pygame.image.load("gokuss/ss5.png"),
             pygame.image.load("gokuss/ss5.png"),
             pygame.image.load("gokuss/ss4.png"),
             pygame.image.load("gokuss/ss4.png"),
             pygame.image.load("gokuss/ss4.png"),
             pygame.image.load("gokuss/ss5.png"),
             pygame.image.load("gokuss/ss5.png"),
             pygame.image.load("gokuss/ss5.png")]

sayajin_l = [pygame.image.load("gokuss/ssizk5.png"),
             pygame.image.load("gokuss/ssizk1.png"),
             pygame.image.load("gokuss/ssizk1.png"),
             pygame.image.load("gokuss/ssizk2.png"),
             pygame.image.load("gokuss/ssizk2.png"),
             pygame.image.load("gokuss/ssizk2.png"),
             pygame.image.load("gokuss/ssizk3.png"),
             pygame.image.load("gokuss/ssizk3.png"),
             pygame.image.load("gokuss/ssizk3.png"),
             pygame.image.load("gokuss/ssizk4.png"),
             pygame.image.load("gokuss/ssizk4.png"),
             pygame.image.load("gokuss/ssizk4.png"),
             pygame.image.load("gokuss/ssizk5.png"),
             pygame.image.load("gokuss/ssizk5.png"),
             pygame.image.load("gokuss/ssizk5.png"),
             pygame.image.load("gokuss/ssizk4.png"),
             pygame.image.load("gokuss/ssizk4.png"),
             pygame.image.load("gokuss/ssizk4.png"),
             pygame.image.load("gokuss/ssizk5.png"),
             pygame.image.load("gokuss/ssizk5.png"),
             pygame.image.load("gokuss/ssizk5.png"),
             pygame.image.load("gokuss/ssizk4.png"),
             pygame.image.load("gokuss/ssizk4.png"),
             pygame.image.load("gokuss/ssizk4.png"),
             pygame.image.load("gokuss/ssizk5.png"),
             pygame.image.load("gokuss/ssizk5.png"),
             pygame.image.load("gokuss/ssizk5.png")]

sayajin_puño_r = [pygame.image.load("gokuss/puño1.png"),
                  pygame.image.load("gokuss/puño1.png"),
                  pygame.image.load("gokuss/puño1.png"),
                  pygame.image.load("gokuss/puño2.png"),
                  pygame.image.load("gokuss/puño2.png"),
                  pygame.image.load("gokuss/puño2.png"),
                  pygame.image.load("gokuss/puño3.png"),
                  pygame.image.load("gokuss/puño3.png"),
                  pygame.image.load("gokuss/puño3.png"),
                  pygame.image.load("gokuss/puño4.png"),
                  pygame.image.load("gokuss/puño4.png"),
                  pygame.image.load("gokuss/puño4.png"),
                  pygame.image.load("gokuss/puño5.png"),
                  pygame.image.load("gokuss/puño5.png"),
                  pygame.image.load("gokuss/puño5.png"),
                  pygame.image.load("gokuss/puño6.png"),
                  pygame.image.load("gokuss/puño6.png"),
                  pygame.image.load("gokuss/puño6.png")]

sayajin_puño_l = [pygame.image.load("gokuss/puñoizk1.png"),
                  pygame.image.load("gokuss/puñoizk1.png"),
                  pygame.image.load("gokuss/puñoizk1.png"),
                  pygame.image.load("gokuss/puñoizk2.png"),
                  pygame.image.load("gokuss/puñoizk2.png"),
                  pygame.image.load("gokuss/puñoizk2.png"),
                  pygame.image.load("gokuss/puñoizk3.png"),
                  pygame.image.load("gokuss/puñoizk3.png"),
                  pygame.image.load("gokuss/puñoizk3.png"),
                  pygame.image.load("gokuss/puñoizk4.png"),
                  pygame.image.load("gokuss/puñoizk4.png"),
                  pygame.image.load("gokuss/puñoizk4.png"),
                  pygame.image.load("gokuss/puñoizk5.png"),
                  pygame.image.load("gokuss/puñoizk5.png"),
                  pygame.image.load("gokuss/puñoizk5.png"),
                  pygame.image.load("gokuss/puñoizk6.png"),
                  pygame.image.load("gokuss/puñoizk6.png"),
                  pygame.image.load("gokuss/puñoizk6.png")]

sayajin_patada_r = [pygame.image.load("gokuss/patada1.png"),
                    pygame.image.load("gokuss/patada1.png"),
                    pygame.image.load("gokuss/patada1.png"),
                    pygame.image.load("gokuss/patada2.png"),
                    pygame.image.load("gokuss/patada2.png"),
                    pygame.image.load("gokuss/patada2.png"),
                    pygame.image.load("gokuss/patada3.png"),
                    pygame.image.load("gokuss/patada3.png"),
                    pygame.image.load("gokuss/patada3.png"),
                    pygame.image.load("gokuss/patada4.png"),
                    pygame.image.load("gokuss/patada4.png"),
                    pygame.image.load("gokuss/patada4.png"),
                    pygame.image.load("gokuss/patada5.png"),
                    pygame.image.load("gokuss/patada5.png"),
                    pygame.image.load("gokuss/patada5.png")]

sayajin_patada_l = [pygame.image.load("gokuss/patadaizk1.png"),
                    pygame.image.load("gokuss/patadaizk1.png"),
                    pygame.image.load("gokuss/patadaizk1.png"),
                    pygame.image.load("gokuss/patadaizk2.png"),
                    pygame.image.load("gokuss/patadaizk2.png"),
                    pygame.image.load("gokuss/patadaizk2.png"),
                    pygame.image.load("gokuss/patadaizk3.png"),
                    pygame.image.load("gokuss/patadaizk3.png"),
                    pygame.image.load("gokuss/patadaizk3.png"),
                    pygame.image.load("gokuss/patadaizk4.png"),
                    pygame.image.load("gokuss/patadaizk4.png"),
                    pygame.image.load("gokuss/patadaizk4.png"),
                    pygame.image.load("gokuss/patadaizk5.png"),
                    pygame.image.load("gokuss/patadaizk5.png"),
                    pygame.image.load("gokuss/patadaizk5.png")]

sayajin_kame = [pygame.image.load("gokuss/kame1.png"),
                pygame.image.load("gokuss/kame1.png"),
                pygame.image.load("gokuss/kame1.png"),
                pygame.image.load("gokuss/kame2.png"),
                pygame.image.load("gokuss/kame2.png"),
                pygame.image.load("gokuss/kame2.png"),
                pygame.image.load("gokuss/kame3.png"),
                pygame.image.load("gokuss/kame3.png"),
                pygame.image.load("gokuss/kame3.png"),
                pygame.image.load("gokuss/kame4.png"),
                pygame.image.load("gokuss/kame4.png"),
                pygame.image.load("gokuss/kame4.png"),
                pygame.image.load("gokuss/kame5.png"),
                pygame.image.load("gokuss/kame5.png"),
                pygame.image.load("gokuss/kame5.png"),
                pygame.image.load("gokuss/kame6.png"),
                pygame.image.load("gokuss/kame6.png"),
                pygame.image.load("gokuss/kame6.png")]

sayajin_carga_energia_r = [pygame.image.load("gokuss/carga1.png"),
                           pygame.image.load("gokuss/carga2.png"),
                           pygame.image.load("gokuss/carga3.png"),
                           pygame.image.load("gokuss/carga1.png"),
                           pygame.image.load("gokuss/carga2.png"),
                           pygame.image.load("gokuss/carga3.png"),
                           pygame.image.load("gokuss/carga1.png"),
                           pygame.image.load("gokuss/carga2.png"),
                           pygame.image.load("gokuss/carga3.png"),
                           pygame.image.load("gokuss/carga1.png"),
                           pygame.image.load("gokuss/carga2.png"),
                           pygame.image.load("gokuss/carga3.png")]

sayajin_carga_energia_l = [pygame.image.load("gokuss/cargaizk1.png"),
                           pygame.image.load("gokuss/cargaizk2.png"),
                           pygame.image.load("gokuss/cargaizk3.png"),
                           pygame.image.load("gokuss/cargaizk1.png"),
                           pygame.image.load("gokuss/cargaizk2.png"),
                           pygame.image.load("gokuss/cargaizk3.png"),
                           pygame.image.load("gokuss/cargaizk1.png"),
                           pygame.image.load("gokuss/cargaizk2.png"),
                           pygame.image.load("gokuss/cargaizk3.png"),
                           pygame.image.load("gokuss/cargaizk1.png"),
                           pygame.image.load("gokuss/cargaizk2.png"),
                           pygame.image.load("gokuss/cargaizk3.png")]

sayajin3_r = [pygame.image.load("gokuss3/fase4.png"),
              pygame.image.load("gokuss3/fase1.png"),
              pygame.image.load("gokuss3/fase1.png"),
              pygame.image.load("gokuss3/fase2.png"),
              pygame.image.load("gokuss3/fase2.png"),
              pygame.image.load("gokuss3/fase2.png"),
              pygame.image.load("gokuss3/fase3.png"),
              pygame.image.load("gokuss3/fase3.png"),
              pygame.image.load("gokuss3/fase3.png"),
              pygame.image.load("gokuss3/fase3.png"),
              pygame.image.load("gokuss3/fase3.png"),
              pygame.image.load("gokuss3/fase3.png"),
              pygame.image.load("gokuss3/fase3.png"),
              pygame.image.load("gokuss3/fase3.png"),
              pygame.image.load("gokuss3/fase3.png"),
              pygame.image.load("gokuss3/fase4.png"),
              pygame.image.load("gokuss3/fase4.png"),
              pygame.image.load("gokuss3/fase4.png")]

sayajin3_l = [pygame.image.load("gokuss3/fase4izk.png"),
              pygame.image.load("gokuss3/fase1izk.png"),
              pygame.image.load("gokuss3/fase1izk.png"),
              pygame.image.load("gokuss3/fase2izk.png"),
              pygame.image.load("gokuss3/fase2izk.png"),
              pygame.image.load("gokuss3/fase2izk.png"),
              pygame.image.load("gokuss3/fase3izk.png"),
              pygame.image.load("gokuss3/fase3izk.png"),
              pygame.image.load("gokuss3/fase3izk.png"),
              pygame.image.load("gokuss3/fase3izk.png"),
              pygame.image.load("gokuss3/fase3izk.png"),
              pygame.image.load("gokuss3/fase3izk.png"),
              pygame.image.load("gokuss3/fase3izk.png"),
              pygame.image.load("gokuss3/fase3izk.png"),
              pygame.image.load("gokuss3/fase3izk.png"),
              pygame.image.load("gokuss3/fase4izk.png"),
              pygame.image.load("gokuss3/fase4izk.png"),
              pygame.image.load("gokuss3/fase4izk.png")]

sayajin3_puño_r = [pygame.image.load("gokuss3/puño1.png"),
                   pygame.image.load("gokuss3/puño1.png"),
                   pygame.image.load("gokuss3/puño1.png"),
                   pygame.image.load("gokuss3/puño2.png"),
                   pygame.image.load("gokuss3/puño2.png"),
                   pygame.image.load("gokuss3/puño2.png"),
                   pygame.image.load("gokuss3/puño3.png"),
                   pygame.image.load("gokuss3/puño3.png"),
                   pygame.image.load("gokuss3/puño3.png"),
                   pygame.image.load("gokuss3/puño4.png"),
                   pygame.image.load("gokuss3/puño4.png"),
                   pygame.image.load("gokuss3/puño4.png"),
                   pygame.image.load("gokuss3/puño5.png"),
                   pygame.image.load("gokuss3/puño5.png"),
                   pygame.image.load("gokuss3/puño5.png"),
                   pygame.image.load("gokuss3/puño6.png"),
                   pygame.image.load("gokuss3/puño6.png"),
                   pygame.image.load("gokuss3/puño6.png")]

sayajin3_puño_l = [pygame.image.load("gokuss3/puñoizk1.png"),
                   pygame.image.load("gokuss3/puñoizk1.png"),
                   pygame.image.load("gokuss3/puñoizk1.png"),
                   pygame.image.load("gokuss3/puñoizk2.png"),
                   pygame.image.load("gokuss3/puñoizk2.png"),
                   pygame.image.load("gokuss3/puñoizk2.png"),
                   pygame.image.load("gokuss3/puñoizk3.png"),
                   pygame.image.load("gokuss3/puñoizk3.png"),
                   pygame.image.load("gokuss3/puñoizk3.png"),
                   pygame.image.load("gokuss3/puñoizk4.png"),
                   pygame.image.load("gokuss3/puñoizk4.png"),
                   pygame.image.load("gokuss3/puñoizk4.png"),
                   pygame.image.load("gokuss3/puñoizk5.png"),
                   pygame.image.load("gokuss3/puñoizk5.png"),
                   pygame.image.load("gokuss3/puñoizk5.png"),
                   pygame.image.load("gokuss3/puñoizk6.png"),
                   pygame.image.load("gokuss3/puñoizk6.png"),
                   pygame.image.load("gokuss3/puñoizk6.png")]

sayajin3_patada_r = [pygame.image.load("gokuss3/patada1.png"),
                     pygame.image.load("gokuss3/patada1.png"),
                     pygame.image.load("gokuss3/patada1.png"),
                     pygame.image.load("gokuss3/patada1.png"),
                     pygame.image.load("gokuss3/patada2.png"),
                     pygame.image.load("gokuss3/patada2.png"),
                     pygame.image.load("gokuss3/patada2.png"),
                     pygame.image.load("gokuss3/patada2.png"),
                     pygame.image.load("gokuss3/patada3.png"),
                     pygame.image.load("gokuss3/patada3.png"),
                     pygame.image.load("gokuss3/patada3.png"),
                     pygame.image.load("gokuss3/patada3.png"),
                     pygame.image.load("gokuss3/patada4.png"),
                     pygame.image.load("gokuss3/patada4.png"),
                     pygame.image.load("gokuss3/patada4.png"),
                     pygame.image.load("gokuss3/patada4.png"),
                     pygame.image.load("gokuss3/patada5.png"),
                     pygame.image.load("gokuss3/patada5.png"),
                     pygame.image.load("gokuss3/patada5.png"),
                     pygame.image.load("gokuss3/patada5.png")]

sayajin3_patada_l = [pygame.image.load("gokuss3/patadaizk1.png"),
                     pygame.image.load("gokuss3/patadaizk1.png"),
                     pygame.image.load("gokuss3/patadaizk1.png"),
                     pygame.image.load("gokuss3/patadaizk1.png"),
                     pygame.image.load("gokuss3/patadaizk2.png"),
                     pygame.image.load("gokuss3/patadaizk2.png"),
                     pygame.image.load("gokuss3/patadaizk2.png"),
                     pygame.image.load("gokuss3/patadaizk2.png"),
                     pygame.image.load("gokuss3/patadaizk3.png"),
                     pygame.image.load("gokuss3/patadaizk3.png"),
                     pygame.image.load("gokuss3/patadaizk3.png"),
                     pygame.image.load("gokuss3/patadaizk3.png"),
                     pygame.image.load("gokuss3/patadaizk4.png"),
                     pygame.image.load("gokuss3/patadaizk4.png"),
                     pygame.image.load("gokuss3/patadaizk4.png"),
                     pygame.image.load("gokuss3/patadaizk4.png"),
                     pygame.image.load("gokuss3/patadaizk5.png"),
                     pygame.image.load("gokuss3/patadaizk5.png"),
                     pygame.image.load("gokuss3/patadaizk5.png"),
                     pygame.image.load("gokuss3/patadaizk5.png")]

sayajin3_kame = [pygame.image.load("gokuss3/kame1.png"),
                 pygame.image.load("gokuss3/kame1.png"),
                 pygame.image.load("gokuss3/kame1.png"),
                 pygame.image.load("gokuss3/kame2.png"),
                 pygame.image.load("gokuss3/kame2.png"),
                 pygame.image.load("gokuss3/kame2.png"),
                 pygame.image.load("gokuss3/kame3.png"),
                 pygame.image.load("gokuss3/kame3.png"),
                 pygame.image.load("gokuss3/kame3.png"),
                 pygame.image.load("gokuss3/kame4.png"),
                 pygame.image.load("gokuss3/kame4.png"),
                 pygame.image.load("gokuss3/kame4.png"),
                 pygame.image.load("gokuss3/kame5.png"),
                 pygame.image.load("gokuss3/kame5.png"),
                 pygame.image.load("gokuss3/kame5.png"),
                 pygame.image.load("gokuss3/kame5.png"),
                 pygame.image.load("gokuss3/kame5.png"),
                 pygame.image.load("gokuss3/kame5.png"),
                 pygame.image.load("gokuss3/kame5.png"),
                 pygame.image.load("gokuss3/kame5.png"),
                 pygame.image.load("gokuss3/kame6.png"),
                 pygame.image.load("gokuss3/kame6.png"),
                 pygame.image.load("gokuss3/kame6.png"),
                 pygame.image.load("gokuss3/kame7.png"),
                 pygame.image.load("gokuss3/kame7.png"),
                 pygame.image.load("gokuss3/kame7.png")]

sayajin3_carga_energia_r = [pygame.image.load("gokuss3/carga1.png"),
                            pygame.image.load("gokuss3/carga2.png"),
                            pygame.image.load("gokuss3/carga3.png"),
                            pygame.image.load("gokuss3/carga1.png"),
                            pygame.image.load("gokuss3/carga2.png"),
                            pygame.image.load("gokuss3/carga3.png"),
                            pygame.image.load("gokuss3/carga1.png"),
                            pygame.image.load("gokuss3/carga2.png"),
                            pygame.image.load("gokuss3/carga3.png"),
                            pygame.image.load("gokuss3/carga1.png"),
                            pygame.image.load("gokuss3/carga2.png"),
                            pygame.image.load("gokuss3/carga3.png")]

sayajin3_carga_energia_l = [pygame.image.load("gokuss3/cargaizk1.png"),
                            pygame.image.load("gokuss3/cargaizk2.png"),
                            pygame.image.load("gokuss3/cargaizk3.png"),
                            pygame.image.load("gokuss3/cargaizk1.png"),
                            pygame.image.load("gokuss3/cargaizk2.png"),
                            pygame.image.load("gokuss3/cargaizk3.png"),
                            pygame.image.load("gokuss3/cargaizk1.png"),
                            pygame.image.load("gokuss3/cargaizk2.png"),
                            pygame.image.load("gokuss3/cargaizk3.png"),
                            pygame.image.load("gokuss3/cargaizk1.png"),
                            pygame.image.load("gokuss3/cargaizk2.png"),
                            pygame.image.load("gokuss3/cargaizk3.png")]

sayajin4_r = [pygame.image.load("ss4/fase4.png"),
              pygame.image.load("ss4/fase1.png"),
              pygame.image.load("ss4/fase1.png"),
              pygame.image.load("ss4/fase2.png"),
              pygame.image.load("ss4/fase2.png"),
              pygame.image.load("ss4/fase2.png"),
              pygame.image.load("ss4/fase3.png"),
              pygame.image.load("ss4/fase3.png"),
              pygame.image.load("ss4/fase3.png"),
              pygame.image.load("ss4/fase3.png"),
              pygame.image.load("ss4/fase3.png"),
              pygame.image.load("ss4/fase3.png"),
              pygame.image.load("ss4/fase3.png"),
              pygame.image.load("ss4/fase3.png"),
              pygame.image.load("ss4/fase3.png"),
              pygame.image.load("ss4/fase4.png"),
              pygame.image.load("ss4/fase4.png"),
              pygame.image.load("ss4/fase4.png")]

sayajin4_l = [pygame.image.load("ss4/faseizk4.png"),
              pygame.image.load("ss4/faseizk1.png"),
              pygame.image.load("ss4/faseizk1.png"),
              pygame.image.load("ss4/faseizk2.png"),
              pygame.image.load("ss4/faseizk2.png"),
              pygame.image.load("ss4/faseizk2.png"),
              pygame.image.load("ss4/faseizk3.png"),
              pygame.image.load("ss4/faseizk3.png"),
              pygame.image.load("ss4/faseizk3.png"),
              pygame.image.load("ss4/faseizk3.png"),
              pygame.image.load("ss4/faseizk3.png"),
              pygame.image.load("ss4/faseizk3.png"),
              pygame.image.load("ss4/faseizk3.png"),
              pygame.image.load("ss4/faseizk3.png"),
              pygame.image.load("ss4/faseizk3.png"),
              pygame.image.load("ss4/faseizk4.png"),
              pygame.image.load("ss4/faseizk4.png"),
              pygame.image.load("ss4/faseizk4.png")]

sayajin4_puño_r = [pygame.image.load("ss4/puño1.png"),
                   pygame.image.load("ss4/puño1.png"),
                   pygame.image.load("ss4/puño1.png"),
                   pygame.image.load("ss4/puño2.png"),
                   pygame.image.load("ss4/puño2.png"),
                   pygame.image.load("ss4/puño2.png"),
                   pygame.image.load("ss4/puño1.png"),
                   pygame.image.load("ss4/puño2.png"),
                   pygame.image.load("ss4/puño1.png"),
                   pygame.image.load("ss4/puño2.png"),
                   pygame.image.load("ss4/puño1.png"),
                   pygame.image.load("ss4/puño2.png"),
                   pygame.image.load("ss4/puño1.png"),
                   pygame.image.load("ss4/puño2.png"),
                   pygame.image.load("ss4/puño1.png"),
                   pygame.image.load("ss4/puño2.png"),
                   pygame.image.load("ss4/puño1.png"),
                   pygame.image.load("ss4/puño2.png")]

sayajin4_puño_l = [pygame.image.load("ss4/puñoizk1.png"),
                   pygame.image.load("ss4/puñoizk1.png"),
                   pygame.image.load("ss4/puñoizk1.png"),
                   pygame.image.load("ss4/puñoizk2.png"),
                   pygame.image.load("ss4/puñoizk2.png"),
                   pygame.image.load("ss4/puñoizk2.png"),
                   pygame.image.load("ss4/puñoizk1.png"),
                   pygame.image.load("ss4/puñoizk2.png"),
                   pygame.image.load("ss4/puñoizk1.png"),
                   pygame.image.load("ss4/puñoizk2.png"),
                   pygame.image.load("ss4/puñoizk1.png"),
                   pygame.image.load("ss4/puñoizk2.png"),
                   pygame.image.load("ss4/puñoizk1.png"),
                   pygame.image.load("ss4/puñoizk2.png"),
                   pygame.image.load("ss4/puñoizk1.png"),
                   pygame.image.load("ss4/puñoizk2.png"),
                   pygame.image.load("ss4/puñoizk1.png"),
                   pygame.image.load("ss4/puñoizk2.png")]

sayajin4_patada_r = [pygame.image.load("ss4/patada1.png"),
                     pygame.image.load("ss4/patada1.png"),
                     pygame.image.load("ss4/patada1.png"),
                     pygame.image.load("ss4/patada1.png"),
                     pygame.image.load("ss4/patada2.png"),
                     pygame.image.load("ss4/patada2.png"),
                     pygame.image.load("ss4/patada2.png"),
                     pygame.image.load("ss4/patada2.png"),
                     pygame.image.load("ss4/patada3.png"),
                     pygame.image.load("ss4/patada3.png"),
                     pygame.image.load("ss4/patada3.png"),
                     pygame.image.load("ss4/patada3.png"),
                     pygame.image.load("ss4/patada1.png"),
                     pygame.image.load("ss4/patada1.png"),
                     pygame.image.load("ss4/patada2.png"),
                     pygame.image.load("ss4/patada2.png"),
                     pygame.image.load("ss4/patada3.png"),
                     pygame.image.load("ss4/patada1.png"),
                     pygame.image.load("ss4/patada2.png"),
                     pygame.image.load("ss4/patada3.png")]

sayajin4_patada_l = [pygame.image.load("ss4/patadaizk1.png"),
                     pygame.image.load("ss4/patadaizk1.png"),
                     pygame.image.load("ss4/patadaizk1.png"),
                     pygame.image.load("ss4/patadaizk1.png"),
                     pygame.image.load("ss4/patadaizk2.png"),
                     pygame.image.load("ss4/patadaizk2.png"),
                     pygame.image.load("ss4/patadaizk2.png"),
                     pygame.image.load("ss4/patadaizk2.png"),
                     pygame.image.load("ss4/patadaizk3.png"),
                     pygame.image.load("ss4/patadaizk3.png"),
                     pygame.image.load("ss4/patadaizk3.png"),
                     pygame.image.load("ss4/patadaizk3.png"),
                     pygame.image.load("ss4/patadaizk1.png"),
                     pygame.image.load("ss4/patadaizk1.png"),
                     pygame.image.load("ss4/patadaizk2.png"),
                     pygame.image.load("ss4/patadaizk2.png"),
                     pygame.image.load("ss4/patadaizk3.png"),
                     pygame.image.load("ss4/patadaizk1.png"),
                     pygame.image.load("ss4/patadaizk2.png"),
                     pygame.image.load("ss4/patadaizk3.png")]

sayajin4_kame = [pygame.image.load("ss4/kame1.png"),
                 pygame.image.load("ss4/kame1.png"),
                 pygame.image.load("ss4/kame1.png"),
                 pygame.image.load("ss4/kame2.png"),
                 pygame.image.load("ss4/kame2.png"),
                 pygame.image.load("ss4/kame2.png"),
                 pygame.image.load("ss4/kame3.png"),
                 pygame.image.load("ss4/kame3.png"),
                 pygame.image.load("ss4/kame3.png"),
                 pygame.image.load("ss4/kame4.png"),
                 pygame.image.load("ss4/kame4.png"),
                 pygame.image.load("ss4/kame4.png"),
                 pygame.image.load("ss4/kame5.png"),
                 pygame.image.load("ss4/kame5.png"),
                 pygame.image.load("ss4/kame5.png"),
                 pygame.image.load("ss4/kame5.png"),
                 pygame.image.load("ss4/kame5.png"),
                 pygame.image.load("ss4/kame5.png"),
                 pygame.image.load("ss4/kame5.png"),
                 pygame.image.load("ss4/kame5.png"),
                 pygame.image.load("ss4/kame6.png"),
                 pygame.image.load("ss4/kame6.png"),
                 pygame.image.load("ss4/kame6.png"),
                 pygame.image.load("ss4/kame7.png"),
                 pygame.image.load("ss4/kame7.png"),
                 pygame.image.load("ss4/kame7.png")]

sayajin4_carga_energia_r = [pygame.image.load("ss4/carga1.png"),
                            pygame.image.load("ss4/carga2.png"),
                            pygame.image.load("ss4/carga3.png"),
                            pygame.image.load("ss4/carga1.png"),
                            pygame.image.load("ss4/carga2.png"),
                            pygame.image.load("ss4/carga3.png"),
                            pygame.image.load("ss4/carga1.png"),
                            pygame.image.load("ss4/carga2.png"),
                            pygame.image.load("ss4/carga3.png"),
                            pygame.image.load("ss4/carga1.png"),
                            pygame.image.load("ss4/carga2.png"),
                            pygame.image.load("ss4/carga3.png")]

sayajin4_carga_energia_l = [pygame.image.load("ss4/cargaizk1.png"),
                            pygame.image.load("ss4/cargaizk2.png"),
                            pygame.image.load("ss4/cargaizk3.png"),
                            pygame.image.load("ss4/cargaizk1.png"),
                            pygame.image.load("ss4/cargaizk2.png"),
                            pygame.image.load("ss4/cargaizk3.png"),
                            pygame.image.load("ss4/cargaizk1.png"),
                            pygame.image.load("ss4/cargaizk2.png"),
                            pygame.image.load("ss4/cargaizk3.png"),
                            pygame.image.load("ss4/cargaizk1.png"),
                            pygame.image.load("ss4/cargaizk2.png"),
                            pygame.image.load("ss4/cargaizk3.png")]

sayajind_r = [pygame.image.load("ssd/fase4.png"),
              pygame.image.load("ssd/fase1.png"),
              pygame.image.load("ssd/fase1.png"),
              pygame.image.load("ssd/fase2.png"),
              pygame.image.load("ssd/fase2.png"),
              pygame.image.load("ssd/fase2.png"),
              pygame.image.load("ssd/fase3.png"),
              pygame.image.load("ssd/fase3.png"),
              pygame.image.load("ssd/fase3.png"),
              pygame.image.load("ssd/fase3.png"),
              pygame.image.load("ssd/fase3.png"),
              pygame.image.load("ssd/fase3.png"),
              pygame.image.load("ssd/fase3.png"),
              pygame.image.load("ssd/fase3.png"),
              pygame.image.load("ssd/fase3.png"),
              pygame.image.load("ssd/fase4.png"),
              pygame.image.load("ssd/fase4.png"),
              pygame.image.load("ssd/fase4.png")]

sayajind_l = [pygame.image.load("ssd/faseizk4.png"),
              pygame.image.load("ssd/faseizk1.png"),
              pygame.image.load("ssd/faseizk1.png"),
              pygame.image.load("ssd/faseizk2.png"),
              pygame.image.load("ssd/faseizk2.png"),
              pygame.image.load("ssd/faseizk2.png"),
              pygame.image.load("ssd/faseizk3.png"),
              pygame.image.load("ssd/faseizk3.png"),
              pygame.image.load("ssd/faseizk3.png"),
              pygame.image.load("ssd/faseizk3.png"),
              pygame.image.load("ssd/faseizk3.png"),
              pygame.image.load("ssd/faseizk3.png"),
              pygame.image.load("ssd/faseizk3.png"),
              pygame.image.load("ssd/faseizk3.png"),
              pygame.image.load("ssd/faseizk3.png"),
              pygame.image.load("ssd/faseizk4.png"),
              pygame.image.load("ssd/faseizk4.png"),
              pygame.image.load("ssd/faseizk4.png")]

sayajind_puño_r = [pygame.image.load("ssd/puño1.png"),
                   pygame.image.load("ssd/puño1.png"),
                   pygame.image.load("ssd/puño1.png"),
                   pygame.image.load("ssd/puño2.png"),
                   pygame.image.load("ssd/puño2.png"),
                   pygame.image.load("ssd/puño2.png"),
                   pygame.image.load("ssd/puño1.png"),
                   pygame.image.load("ssd/puño2.png"),
                   pygame.image.load("ssd/puño1.png"),
                   pygame.image.load("ssd/puño2.png"),
                   pygame.image.load("ssd/puño1.png"),
                   pygame.image.load("ssd/puño2.png"),
                   pygame.image.load("ssd/puño1.png"),
                   pygame.image.load("ssd/puño2.png"),
                   pygame.image.load("ssd/puño1.png"),
                   pygame.image.load("ssd/puño2.png"),
                   pygame.image.load("ssd/puño1.png"),
                   pygame.image.load("ssd/puño2.png")]

sayajind_puño_l = [pygame.image.load("ssd/puñoizk1.png"),
                   pygame.image.load("ssd/puñoizk1.png"),
                   pygame.image.load("ssd/puñoizk1.png"),
                   pygame.image.load("ssd/puñoizk2.png"),
                   pygame.image.load("ssd/puñoizk2.png"),
                   pygame.image.load("ssd/puñoizk2.png"),
                   pygame.image.load("ssd/puñoizk1.png"),
                   pygame.image.load("ssd/puñoizk2.png"),
                   pygame.image.load("ssd/puñoizk1.png"),
                   pygame.image.load("ssd/puñoizk2.png"),
                   pygame.image.load("ssd/puñoizk1.png"),
                   pygame.image.load("ssd/puñoizk2.png"),
                   pygame.image.load("ssd/puñoizk1.png"),
                   pygame.image.load("ssd/puñoizk2.png"),
                   pygame.image.load("ssd/puñoizk1.png"),
                   pygame.image.load("ssd/puñoizk2.png"),
                   pygame.image.load("ssd/puñoizk1.png"),
                   pygame.image.load("ssd/puñoizk2.png")]

sayajind_patada_r = [pygame.image.load("ssd/patada1.png"),
                     pygame.image.load("ssd/patada1.png"),
                     pygame.image.load("ssd/patada1.png"),
                     pygame.image.load("ssd/patada1.png"),
                     pygame.image.load("ssd/patada2.png"),
                     pygame.image.load("ssd/patada2.png"),
                     pygame.image.load("ssd/patada2.png"),
                     pygame.image.load("ssd/patada2.png"),
                     pygame.image.load("ssd/patada3.png"),
                     pygame.image.load("ssd/patada3.png"),
                     pygame.image.load("ssd/patada3.png"),
                     pygame.image.load("ssd/patada3.png"),
                     pygame.image.load("ssd/patada1.png"),
                     pygame.image.load("ssd/patada1.png"),
                     pygame.image.load("ssd/patada2.png"),
                     pygame.image.load("ssd/patada2.png"),
                     pygame.image.load("ssd/patada3.png"),
                     pygame.image.load("ssd/patada1.png"),
                     pygame.image.load("ssd/patada2.png"),
                     pygame.image.load("ssd/patada3.png")]

sayajind_patada_l = [pygame.image.load("ssd/patadaizk1.png"),
                     pygame.image.load("ssd/patadaizk1.png"),
                     pygame.image.load("ssd/patadaizk1.png"),
                     pygame.image.load("ssd/patadaizk1.png"),
                     pygame.image.load("ssd/patadaizk2.png"),
                     pygame.image.load("ssd/patadaizk2.png"),
                     pygame.image.load("ssd/patadaizk2.png"),
                     pygame.image.load("ssd/patadaizk2.png"),
                     pygame.image.load("ssd/patadaizk3.png"),
                     pygame.image.load("ssd/patadaizk3.png"),
                     pygame.image.load("ssd/patadaizk3.png"),
                     pygame.image.load("ssd/patadaizk3.png"),
                     pygame.image.load("ssd/patadaizk1.png"),
                     pygame.image.load("ssd/patadaizk1.png"),
                     pygame.image.load("ssd/patadaizk2.png"),
                     pygame.image.load("ssd/patadaizk2.png"),
                     pygame.image.load("ssd/patadaizk3.png"),
                     pygame.image.load("ssd/patadaizk1.png"),
                     pygame.image.load("ssd/patadaizk2.png"),
                     pygame.image.load("ssd/patadaizk3.png")]

sayajind_kame = [pygame.image.load("ssd/kame1.png"),
                 pygame.image.load("ssd/kame1.png"),
                 pygame.image.load("ssd/kame1.png"),
                 pygame.image.load("ssd/kame2.png"),
                 pygame.image.load("ssd/kame2.png"),
                 pygame.image.load("ssd/kame2.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame3.png"),
                 pygame.image.load("ssd/kame4.png"),
                 pygame.image.load("ssd/kame4.png"),
                 pygame.image.load("ssd/kame4.png"),
                 pygame.image.load("ssd/kame4.png")]

sayajind_carga_energia_r = [pygame.image.load("ssd/carga1.png"),
                            pygame.image.load("ssd/carga2.png"),
                            pygame.image.load("ssd/carga1.png"),
                            pygame.image.load("ssd/carga2.png"),
                            pygame.image.load("ssd/carga1.png"),
                            pygame.image.load("ssd/carga2.png"),
                            pygame.image.load("ssd/carga1.png"),
                            pygame.image.load("ssd/carga2.png"),
                            pygame.image.load("ssd/carga1.png"),
                            pygame.image.load("ssd/carga2.png"),
                            pygame.image.load("ssd/carga1.png"),
                            pygame.image.load("ssd/carga2.png")]

sayajind_carga_energia_l = [pygame.image.load("ssd/cargaizk1.png"),
                            pygame.image.load("ssd/cargaizk2.png"),
                            pygame.image.load("ssd/cargaizk1.png"),
                            pygame.image.load("ssd/cargaizk2.png"),
                            pygame.image.load("ssd/cargaizk1.png"),
                            pygame.image.load("ssd/cargaizk2.png"),
                            pygame.image.load("ssd/cargaizk1.png"),
                            pygame.image.load("ssd/cargaizk2.png"),
                            pygame.image.load("ssd/cargaizk1.png"),
                            pygame.image.load("ssd/cargaizk2.png"),
                            pygame.image.load("ssd/cargaizk1.png"),
                            pygame.image.load("ssd/cargaizk2.png")]

sayajinb_r = [pygame.image.load("ssb/fase4.png"),
              pygame.image.load("ssb/fase1.png"),
              pygame.image.load("ssb/fase1.png"),
              pygame.image.load("ssb/fase2.png"),
              pygame.image.load("ssb/fase2.png"),
              pygame.image.load("ssb/fase2.png"),
              pygame.image.load("ssb/fase3.png"),
              pygame.image.load("ssb/fase3.png"),
              pygame.image.load("ssb/fase3.png"),
              pygame.image.load("ssb/fase3.png"),
              pygame.image.load("ssb/fase3.png"),
              pygame.image.load("ssb/fase3.png"),
              pygame.image.load("ssb/fase3.png"),
              pygame.image.load("ssb/fase3.png"),
              pygame.image.load("ssb/fase3.png"),
              pygame.image.load("ssb/fase4.png"),
              pygame.image.load("ssb/fase4.png"),
              pygame.image.load("ssb/fase4.png")]

sayajinb_l = [pygame.image.load("ssb/faseizk4.png"),
              pygame.image.load("ssb/faseizk1.png"),
              pygame.image.load("ssb/faseizk1.png"),
              pygame.image.load("ssb/faseizk2.png"),
              pygame.image.load("ssb/faseizk2.png"),
              pygame.image.load("ssb/faseizk2.png"),
              pygame.image.load("ssb/faseizk3.png"),
              pygame.image.load("ssb/faseizk3.png"),
              pygame.image.load("ssb/faseizk3.png"),
              pygame.image.load("ssb/faseizk3.png"),
              pygame.image.load("ssb/faseizk3.png"),
              pygame.image.load("ssb/faseizk3.png"),
              pygame.image.load("ssb/faseizk3.png"),
              pygame.image.load("ssb/faseizk3.png"),
              pygame.image.load("ssb/faseizk3.png"),
              pygame.image.load("ssb/faseizk4.png"),
              pygame.image.load("ssb/faseizk4.png"),
              pygame.image.load("ssb/faseizk4.png")]

sayajinb_puño_r = [pygame.image.load("ssb/puño1.png"),
                   pygame.image.load("ssb/puño1.png"),
                   pygame.image.load("ssb/puño1.png"),
                   pygame.image.load("ssb/puño2.png"),
                   pygame.image.load("ssb/puño2.png"),
                   pygame.image.load("ssb/puño2.png"),
                   pygame.image.load("ssb/puño1.png"),
                   pygame.image.load("ssb/puño2.png"),
                   pygame.image.load("ssb/puño1.png"),
                   pygame.image.load("ssb/puño2.png"),
                   pygame.image.load("ssb/puño1.png"),
                   pygame.image.load("ssb/puño2.png"),
                   pygame.image.load("ssb/puño1.png"),
                   pygame.image.load("ssb/puño2.png"),
                   pygame.image.load("ssb/puño1.png"),
                   pygame.image.load("ssb/puño2.png"),
                   pygame.image.load("ssb/puño1.png"),
                   pygame.image.load("ssb/puño2.png")]

sayajinb_puño_l = [pygame.image.load("ssb/puñoizk1.png"),
                   pygame.image.load("ssb/puñoizk1.png"),
                   pygame.image.load("ssb/puñoizk1.png"),
                   pygame.image.load("ssb/puñoizk2.png"),
                   pygame.image.load("ssb/puñoizk2.png"),
                   pygame.image.load("ssb/puñoizk2.png"),
                   pygame.image.load("ssb/puñoizk1.png"),
                   pygame.image.load("ssb/puñoizk2.png"),
                   pygame.image.load("ssb/puñoizk1.png"),
                   pygame.image.load("ssb/puñoizk2.png"),
                   pygame.image.load("ssb/puñoizk1.png"),
                   pygame.image.load("ssb/puñoizk2.png"),
                   pygame.image.load("ssb/puñoizk1.png"),
                   pygame.image.load("ssb/puñoizk2.png"),
                   pygame.image.load("ssb/puñoizk1.png"),
                   pygame.image.load("ssb/puñoizk2.png"),
                   pygame.image.load("ssb/puñoizk1.png"),
                   pygame.image.load("ssb/puñoizk2.png")]

sayajinb_patada_r = [pygame.image.load("ssb/patada1.png"),
                     pygame.image.load("ssb/patada1.png"),
                     pygame.image.load("ssb/patada1.png"),
                     pygame.image.load("ssb/patada1.png"),
                     pygame.image.load("ssb/patada2.png"),
                     pygame.image.load("ssb/patada2.png"),
                     pygame.image.load("ssb/patada2.png"),
                     pygame.image.load("ssb/patada2.png"),
                     pygame.image.load("ssb/patada3.png"),
                     pygame.image.load("ssb/patada3.png"),
                     pygame.image.load("ssb/patada3.png"),
                     pygame.image.load("ssb/patada3.png"),
                     pygame.image.load("ssb/patada1.png"),
                     pygame.image.load("ssb/patada1.png"),
                     pygame.image.load("ssb/patada2.png"),
                     pygame.image.load("ssb/patada2.png"),
                     pygame.image.load("ssb/patada3.png"),
                     pygame.image.load("ssb/patada1.png"),
                     pygame.image.load("ssb/patada2.png"),
                     pygame.image.load("ssb/patada3.png")]

sayajinb_patada_l = [pygame.image.load("ssb/patadaizk1.png"),
                     pygame.image.load("ssb/patadaizk1.png"),
                     pygame.image.load("ssb/patadaizk1.png"),
                     pygame.image.load("ssb/patadaizk1.png"),
                     pygame.image.load("ssb/patadaizk2.png"),
                     pygame.image.load("ssb/patadaizk2.png"),
                     pygame.image.load("ssb/patadaizk2.png"),
                     pygame.image.load("ssb/patadaizk2.png"),
                     pygame.image.load("ssb/patadaizk3.png"),
                     pygame.image.load("ssb/patadaizk3.png"),
                     pygame.image.load("ssb/patadaizk3.png"),
                     pygame.image.load("ssb/patadaizk3.png"),
                     pygame.image.load("ssb/patadaizk1.png"),
                     pygame.image.load("ssb/patadaizk1.png"),
                     pygame.image.load("ssb/patadaizk2.png"),
                     pygame.image.load("ssb/patadaizk2.png"),
                     pygame.image.load("ssb/patadaizk3.png"),
                     pygame.image.load("ssb/patadaizk1.png"),
                     pygame.image.load("ssb/patadaizk2.png"),
                     pygame.image.load("ssb/patadaizk3.png")]

sayajinb_kame = [pygame.image.load("ssb/kame1.png"),
                 pygame.image.load("ssb/kame1.png"),
                 pygame.image.load("ssb/kame1.png"),
                 pygame.image.load("ssb/kame1.png"),
                 pygame.image.load("ssb/kame1.png"),
                 pygame.image.load("ssb/kame1.png"),
                 pygame.image.load("ssb/kame1.png"),
                 pygame.image.load("ssb/kame1.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png"),
                 pygame.image.load("ssb/kame2.png")]

sayajinb_carga_energia_r = [pygame.image.load("ssb/carga1.png"),
                            pygame.image.load("ssb/carga2.png"),
                            pygame.image.load("ssb/carga3.png"),
                            pygame.image.load("ssb/carga1.png"),
                            pygame.image.load("ssb/carga2.png"),
                            pygame.image.load("ssb/carga3.png"),
                            pygame.image.load("ssb/carga1.png"),
                            pygame.image.load("ssb/carga2.png"),
                            pygame.image.load("ssb/carga3.png"),
                            pygame.image.load("ssb/carga1.png"),
                            pygame.image.load("ssb/carga2.png"),
                            pygame.image.load("ssb/carga3.png")]

sayajinb_carga_energia_l = [pygame.image.load("ssb/cargaizk1.png"),
                            pygame.image.load("ssb/cargaizk2.png"),
                            pygame.image.load("ssb/cargaizk3.png"),
                            pygame.image.load("ssb/cargaizk1.png"),
                            pygame.image.load("ssb/cargaizk2.png"),
                            pygame.image.load("ssb/cargaizk3.png"),
                            pygame.image.load("ssb/cargaizk1.png"),
                            pygame.image.load("ssb/cargaizk2.png"),
                            pygame.image.load("ssb/cargaizk3.png"),
                            pygame.image.load("ssb/cargaizk1.png"),
                            pygame.image.load("ssb/cargaizk2.png"),
                            pygame.image.load("ssb/cargaizk3.png")]

sayajinbk_r = [pygame.image.load("ssbk/fase1.png"),
               pygame.image.load("ssbk/fase1.png"),
               pygame.image.load("ssbk/fase1.png"),
               pygame.image.load("ssbk/fase1.png"),
               pygame.image.load("ssbk/fase1.png"),
               pygame.image.load("ssbk/fase1.png"),
               pygame.image.load("ssbk/fase2.png"),
               pygame.image.load("ssbk/fase2.png"),
               pygame.image.load("ssbk/fase2.png"),
               pygame.image.load("ssbk/fase2.png"),
               pygame.image.load("ssbk/fase2.png"),
               pygame.image.load("ssbk/fase2.png"),
               pygame.image.load("ssbk/fase3.png"),
               pygame.image.load("ssbk/fase3.png"),
               pygame.image.load("ssbk/fase3.png"),
               pygame.image.load("ssbk/fase3.png"),
               pygame.image.load("ssbk/fase3.png"),
               pygame.image.load("ssbk/fase3.png"),
               pygame.image.load("ssbk/fase4.png"),
               pygame.image.load("ssbk/fase4.png"),
               pygame.image.load("ssbk/fase4.png"),
               pygame.image.load("ssbk/fase4.png"),
               pygame.image.load("ssbk/fase4.png"),
               pygame.image.load("ssbk/fase4.png"),
               pygame.image.load("ssbk/fase5.png"),
               pygame.image.load("ssbk/fase5.png"),
               pygame.image.load("ssbk/fase5.png"),
               pygame.image.load("ssbk/fase5.png"),
               pygame.image.load("ssbk/fase5.png"),
               pygame.image.load("ssbk/fase5.png"),
               pygame.image.load("ssbk/fase6.png"),
               pygame.image.load("ssbk/fase6.png"),
               pygame.image.load("ssbk/fase6.png"),
               pygame.image.load("ssbk/fase6.png"),
               pygame.image.load("ssbk/fase6.png"),
               pygame.image.load("ssbk/fase6.png"),
               pygame.image.load("ssbk/fase7.png"),
               pygame.image.load("ssbk/fase7.png"),
               pygame.image.load("ssbk/fase7.png"),
               pygame.image.load("ssbk/fase7.png"),
               pygame.image.load("ssbk/fase7.png"),
               pygame.image.load("ssbk/fase7.png"),
               pygame.image.load("ssbk/fase8.png"),
               pygame.image.load("ssbk/fase8.png"),
               pygame.image.load("ssbk/fase8.png"),
               pygame.image.load("ssbk/fase8.png"),
               pygame.image.load("ssbk/fase8.png"),
               pygame.image.load("ssbk/fase8.png"),
               pygame.image.load("ssbk/fase9.png"),
               pygame.image.load("ssbk/fase9.png"),
               pygame.image.load("ssbk/fase9.png"),
               pygame.image.load("ssbk/fase9.png"),
               pygame.image.load("ssbk/fase9.png"),
               pygame.image.load("ssbk/fase9.png")]

sayajinbk_l = [pygame.image.load("ssbk/faseizk1.png"),
               pygame.image.load("ssbk/faseizk1.png"),
               pygame.image.load("ssbk/faseizk1.png"),
               pygame.image.load("ssbk/faseizk1.png"),
               pygame.image.load("ssbk/faseizk1.png"),
               pygame.image.load("ssbk/faseizk1.png"),
               pygame.image.load("ssbk/faseizk2.png"),
               pygame.image.load("ssbk/faseizk2.png"),
               pygame.image.load("ssbk/faseizk2.png"),
               pygame.image.load("ssbk/faseizk2.png"),
               pygame.image.load("ssbk/faseizk2.png"),
               pygame.image.load("ssbk/faseizk2.png"),
               pygame.image.load("ssbk/faseizk3.png"),
               pygame.image.load("ssbk/faseizk3.png"),
               pygame.image.load("ssbk/faseizk3.png"),
               pygame.image.load("ssbk/faseizk3.png"),
               pygame.image.load("ssbk/faseizk3.png"),
               pygame.image.load("ssbk/faseizk3.png"),
               pygame.image.load("ssbk/faseizk4.png"),
               pygame.image.load("ssbk/faseizk4.png"),
               pygame.image.load("ssbk/faseizk4.png"),
               pygame.image.load("ssbk/faseizk4.png"),
               pygame.image.load("ssbk/faseizk4.png"),
               pygame.image.load("ssbk/faseizk4.png"),
               pygame.image.load("ssbk/faseizk5.png"),
               pygame.image.load("ssbk/faseizk5.png"),
               pygame.image.load("ssbk/faseizk5.png"),
               pygame.image.load("ssbk/faseizk5.png"),
               pygame.image.load("ssbk/faseizk5.png"),
               pygame.image.load("ssbk/faseizk5.png"),
               pygame.image.load("ssbk/faseizk6.png"),
               pygame.image.load("ssbk/faseizk6.png"),
               pygame.image.load("ssbk/faseizk6.png"),
               pygame.image.load("ssbk/faseizk6.png"),
               pygame.image.load("ssbk/faseizk6.png"),
               pygame.image.load("ssbk/faseizk6.png"),
               pygame.image.load("ssbk/faseizk7.png"),
               pygame.image.load("ssbk/faseizk7.png"),
               pygame.image.load("ssbk/faseizk7.png"),
               pygame.image.load("ssbk/faseizk7.png"),
               pygame.image.load("ssbk/faseizk7.png"),
               pygame.image.load("ssbk/faseizk7.png"),
               pygame.image.load("ssbk/faseizk8.png"),
               pygame.image.load("ssbk/faseizk8.png"),
               pygame.image.load("ssbk/faseizk8.png"),
               pygame.image.load("ssbk/faseizk8.png"),
               pygame.image.load("ssbk/faseizk8.png"),
               pygame.image.load("ssbk/faseizk8.png"),
               pygame.image.load("ssbk/faseizk9.png"),
               pygame.image.load("ssbk/faseizk9.png"),
               pygame.image.load("ssbk/faseizk9.png"),
               pygame.image.load("ssbk/faseizk9.png"),
               pygame.image.load("ssbk/faseizk9.png"),
               pygame.image.load("ssbk/faseizk9.png")]

sayajinbk_puño_r = [pygame.image.load("ssbk/puño1.png"),
                    pygame.image.load("ssbk/puño1.png"),
                    pygame.image.load("ssbk/puño2.png"),
                    pygame.image.load("ssbk/puño2.png"),
                    pygame.image.load("ssbk/puño3.png"),
                    pygame.image.load("ssbk/puño3.png"),
                    pygame.image.load("ssbk/puño4.png"),
                    pygame.image.load("ssbk/puño4.png"),
                    pygame.image.load("ssbk/puño1.png"),
                    pygame.image.load("ssbk/puño1.png"),
                    pygame.image.load("ssbk/puño2.png"),
                    pygame.image.load("ssbk/puño2.png"),
                    pygame.image.load("ssbk/puño3.png"),
                    pygame.image.load("ssbk/puño3.png"),
                    pygame.image.load("ssbk/puño4.png"),
                    pygame.image.load("ssbk/puño4.png")]

sayajinbk_puño_l = [pygame.image.load("ssbk/puñoizk1.png"),
                    pygame.image.load("ssbk/puñoizk1.png"),
                    pygame.image.load("ssbk/puñoizk2.png"),
                    pygame.image.load("ssbk/puñoizk2.png"),
                    pygame.image.load("ssbk/puñoizk3.png"),
                    pygame.image.load("ssbk/puñoizk3.png"),
                    pygame.image.load("ssbk/puñoizk4.png"),
                    pygame.image.load("ssbk/puñoizk4.png"),
                    pygame.image.load("ssbk/puñoizk1.png"),
                    pygame.image.load("ssbk/puñoizk1.png"),
                    pygame.image.load("ssbk/puñoizk2.png"),
                    pygame.image.load("ssbk/puñoizk2.png"),
                    pygame.image.load("ssbk/puñoizk3.png"),
                    pygame.image.load("ssbk/puñoizk3.png"),
                    pygame.image.load("ssbk/puñoizk4.png"),
                    pygame.image.load("ssbk/puñoizk4.png")]

sayajinbk_patada_r = [pygame.image.load("ssbk/patada1.png"),
                      pygame.image.load("ssbk/patada1.png"),
                      pygame.image.load("ssbk/patada1.png"),
                      pygame.image.load("ssbk/patada1.png"),
                      pygame.image.load("ssbk/patada1.png"),
                      pygame.image.load("ssbk/patada1.png"),
                      pygame.image.load("ssbk/patada2.png"),
                      pygame.image.load("ssbk/patada2.png"),
                      pygame.image.load("ssbk/patada2.png"),
                      pygame.image.load("ssbk/patada2.png"),
                      pygame.image.load("ssbk/patada2.png"),
                      pygame.image.load("ssbk/patada2.png"),
                      pygame.image.load("ssbk/patada3.png"),
                      pygame.image.load("ssbk/patada3.png"),
                      pygame.image.load("ssbk/patada3.png"),
                      pygame.image.load("ssbk/patada3.png"),
                      pygame.image.load("ssbk/patada3.png"),
                      pygame.image.load("ssbk/patada3.png"),
                      pygame.image.load("ssbk/patada4.png"),
                      pygame.image.load("ssbk/patada4.png"),
                      pygame.image.load("ssbk/patada4.png"),
                      pygame.image.load("ssbk/patada4.png"),
                      pygame.image.load("ssbk/patada4.png"),
                      pygame.image.load("ssbk/patada4.png"),
                      pygame.image.load("ssbk/patada5.png"),
                      pygame.image.load("ssbk/patada5.png"),
                      pygame.image.load("ssbk/patada5.png"),
                      pygame.image.load("ssbk/patada5.png"),
                      pygame.image.load("ssbk/patada5.png"),
                      pygame.image.load("ssbk/patada5.png"),
                      pygame.image.load("ssbk/patada6.png"),
                      pygame.image.load("ssbk/patada6.png"),
                      pygame.image.load("ssbk/patada6.png"),
                      pygame.image.load("ssbk/patada6.png"),
                      pygame.image.load("ssbk/patada6.png"),
                      pygame.image.load("ssbk/patada6.png"),
                      pygame.image.load("ssbk/patada7.png"),
                      pygame.image.load("ssbk/patada7.png"),
                      pygame.image.load("ssbk/patada7.png"),
                      pygame.image.load("ssbk/patada7.png"),
                      pygame.image.load("ssbk/patada7.png"),
                      pygame.image.load("ssbk/patada7.png"),
                      pygame.image.load("ssbk/patada8.png"),
                      pygame.image.load("ssbk/patada8.png"),
                      pygame.image.load("ssbk/patada8.png"),
                      pygame.image.load("ssbk/patada8.png"),
                      pygame.image.load("ssbk/patada8.png"),
                      pygame.image.load("ssbk/patada8.png")]

sayajinbk_patada_l = [pygame.image.load("ssbk/patadaizk1.png"),
                      pygame.image.load("ssbk/patadaizk1.png"),
                      pygame.image.load("ssbk/patadaizk1.png"),
                      pygame.image.load("ssbk/patadaizk1.png"),
                      pygame.image.load("ssbk/patadaizk1.png"),
                      pygame.image.load("ssbk/patadaizk1.png"),
                      pygame.image.load("ssbk/patadaizk2.png"),
                      pygame.image.load("ssbk/patadaizk2.png"),
                      pygame.image.load("ssbk/patadaizk2.png"),
                      pygame.image.load("ssbk/patadaizk2.png"),
                      pygame.image.load("ssbk/patadaizk2.png"),
                      pygame.image.load("ssbk/patadaizk2.png"),
                      pygame.image.load("ssbk/patadaizk3.png"),
                      pygame.image.load("ssbk/patadaizk3.png"),
                      pygame.image.load("ssbk/patadaizk3.png"),
                      pygame.image.load("ssbk/patadaizk3.png"),
                      pygame.image.load("ssbk/patadaizk3.png"),
                      pygame.image.load("ssbk/patadaizk3.png"),
                      pygame.image.load("ssbk/patadaizk4.png"),
                      pygame.image.load("ssbk/patadaizk4.png"),
                      pygame.image.load("ssbk/patadaizk4.png"),
                      pygame.image.load("ssbk/patadaizk4.png"),
                      pygame.image.load("ssbk/patadaizk4.png"),
                      pygame.image.load("ssbk/patadaizk4.png"),
                      pygame.image.load("ssbk/patadaizk5.png"),
                      pygame.image.load("ssbk/patadaizk5.png"),
                      pygame.image.load("ssbk/patadaizk5.png"),
                      pygame.image.load("ssbk/patadaizk5.png"),
                      pygame.image.load("ssbk/patadaizk5.png"),
                      pygame.image.load("ssbk/patadaizk5.png"),
                      pygame.image.load("ssbk/patadaizk6.png"),
                      pygame.image.load("ssbk/patadaizk6.png"),
                      pygame.image.load("ssbk/patadaizk6.png"),
                      pygame.image.load("ssbk/patadaizk6.png"),
                      pygame.image.load("ssbk/patadaizk6.png"),
                      pygame.image.load("ssbk/patadaizk6.png"),
                      pygame.image.load("ssbk/patadaizk7.png"),
                      pygame.image.load("ssbk/patadaizk7.png"),
                      pygame.image.load("ssbk/patadaizk7.png"),
                      pygame.image.load("ssbk/patadaizk7.png"),
                      pygame.image.load("ssbk/patadaizk7.png"),
                      pygame.image.load("ssbk/patadaizk7.png"),
                      pygame.image.load("ssbk/patadaizk8.png"),
                      pygame.image.load("ssbk/patadaizk8.png"),
                      pygame.image.load("ssbk/patadaizk8.png"),
                      pygame.image.load("ssbk/patadaizk8.png"),
                      pygame.image.load("ssbk/patadaizk8.png"),
                      pygame.image.load("ssbk/patadaizk8.png")]

sayajinbk_kame = [pygame.image.load("ssbk/kame1.png"),
                  pygame.image.load("ssbk/kame1.png"),
                  pygame.image.load("ssbk/kame1.png"),
                  pygame.image.load("ssbk/kame1.png"),
                  pygame.image.load("ssbk/kame1.png"),
                  pygame.image.load("ssbk/kame2.png"),
                  pygame.image.load("ssbk/kame2.png"),
                  pygame.image.load("ssbk/kame2.png"),
                  pygame.image.load("ssbk/kame2.png"),
                  pygame.image.load("ssbk/kame2.png"),
                  pygame.image.load("ssbk/kame3.png"),
                  pygame.image.load("ssbk/kame3.png"),
                  pygame.image.load("ssbk/kame3.png"),
                  pygame.image.load("ssbk/kame3.png"),
                  pygame.image.load("ssbk/kame3.png"),
                  pygame.image.load("ssbk/kame4.png"),
                  pygame.image.load("ssbk/kame4.png"),
                  pygame.image.load("ssbk/kame4.png"),
                  pygame.image.load("ssbk/kame4.png"),
                  pygame.image.load("ssbk/kame4.png"),
                  pygame.image.load("ssbk/kame4.png"),
                  pygame.image.load("ssbk/kame4.png"),
                  pygame.image.load("ssbk/kame4.png"),
                  pygame.image.load("ssbk/kame4.png"),
                  pygame.image.load("ssbk/kame4.png"),
                  pygame.image.load("ssbk/kame4.png")]

sayajinbk_carga_energia_r = [pygame.image.load("ssbk/carga1.png"),
                             pygame.image.load("ssbk/carga2.png"),
                             pygame.image.load("ssbk/carga1.png"),
                             pygame.image.load("ssbk/carga2.png"),
                             pygame.image.load("ssbk/carga1.png"),
                             pygame.image.load("ssbk/carga2.png"),
                             pygame.image.load("ssbk/carga1.png"),
                             pygame.image.load("ssbk/carga2.png"),
                             pygame.image.load("ssbk/carga1.png"),
                             pygame.image.load("ssbk/carga2.png"),
                             pygame.image.load("ssbk/carga1.png"),
                             pygame.image.load("ssbk/carga2.png")]

sayajinbk_carga_energia_l = [pygame.image.load("ssbk/cargaizk1.png"),
                             pygame.image.load("ssbk/cargaizk2.png"),
                             pygame.image.load("ssbk/cargaizk1.png"),
                             pygame.image.load("ssbk/cargaizk2.png"),
                             pygame.image.load("ssbk/cargaizk1.png"),
                             pygame.image.load("ssbk/cargaizk2.png"),
                             pygame.image.load("ssbk/cargaizk1.png"),
                             pygame.image.load("ssbk/cargaizk2.png"),
                             pygame.image.load("ssbk/cargaizk1.png"),
                             pygame.image.load("ssbk/cargaizk2.png"),
                             pygame.image.load("ssbk/cargaizk1.png"),
                             pygame.image.load("ssbk/cargaizk2.png")]

sayajinu_r = [pygame.image.load("ssu/fase7.png"),
              pygame.image.load("ssu/fase1.png"),
              pygame.image.load("ssu/fase1.png"),
              pygame.image.load("ssu/fase1.png"),
              pygame.image.load("ssu/fase1.png"),
              pygame.image.load("ssu/fase1.png"),
              pygame.image.load("ssu/fase1.png"),
              pygame.image.load("ssu/fase1.png"),
              pygame.image.load("ssu/fase1.png"),
              pygame.image.load("ssu/fase1.png"),
              pygame.image.load("ssu/fase2.png"),
              pygame.image.load("ssu/fase2.png"),
              pygame.image.load("ssu/fase2.png"),
              pygame.image.load("ssu/fase2.png"),
              pygame.image.load("ssu/fase2.png"),
              pygame.image.load("ssu/fase2.png"),
              pygame.image.load("ssu/fase2.png"),
              pygame.image.load("ssu/fase2.png"),
              pygame.image.load("ssu/fase2.png"),
              pygame.image.load("ssu/fase2.png"),
              pygame.image.load("ssu/fase3.png"),
              pygame.image.load("ssu/fase3.png"),
              pygame.image.load("ssu/fase3.png"),
              pygame.image.load("ssu/fase3.png"),
              pygame.image.load("ssu/fase3.png"),
              pygame.image.load("ssu/fase3.png"),
              pygame.image.load("ssu/fase3.png"),
              pygame.image.load("ssu/fase3.png"),
              pygame.image.load("ssu/fase3.png"),
              pygame.image.load("ssu/fase3.png"),
              pygame.image.load("ssu/fase4.png"),
              pygame.image.load("ssu/fase4.png"),
              pygame.image.load("ssu/fase4.png"),
              pygame.image.load("ssu/fase4.png"),
              pygame.image.load("ssu/fase4.png"),
              pygame.image.load("ssu/fase4.png"),
              pygame.image.load("ssu/fase4.png"),
              pygame.image.load("ssu/fase4.png"),
              pygame.image.load("ssu/fase4.png"),
              pygame.image.load("ssu/fase4.png"),
              pygame.image.load("ssu/fase5.png"),
              pygame.image.load("ssu/fase5.png"),
              pygame.image.load("ssu/fase5.png"),
              pygame.image.load("ssu/fase5.png"),
              pygame.image.load("ssu/fase5.png"),
              pygame.image.load("ssu/fase5.png"),
              pygame.image.load("ssu/fase5.png"),
              pygame.image.load("ssu/fase5.png"),
              pygame.image.load("ssu/fase5.png"),
              pygame.image.load("ssu/fase5.png"),
              pygame.image.load("ssu/fase5.png"),
              pygame.image.load("ssu/fase5.png"),
              pygame.image.load("ssu/fase6.png"),
              pygame.image.load("ssu/fase6.png"),
              pygame.image.load("ssu/fase6.png"),
              pygame.image.load("ssu/fase6.png"),
              pygame.image.load("ssu/fase6.png"),
              pygame.image.load("ssu/fase6.png"),
              pygame.image.load("ssu/fase6.png"),
              pygame.image.load("ssu/fase6.png"),
              pygame.image.load("ssu/fase6.png"),
              pygame.image.load("ssu/fase6.png"),
              pygame.image.load("ssu/fase7.png"),
              pygame.image.load("ssu/fase7.png"),
              pygame.image.load("ssu/fase7.png"),
              pygame.image.load("ssu/fase7.png"),
              pygame.image.load("ssu/fase7.png"),
              pygame.image.load("ssu/fase7.png"),
              pygame.image.load("ssu/fase7.png"),
              pygame.image.load("ssu/fase7.png"),
              pygame.image.load("ssu/fase7.png"),
              pygame.image.load("ssu/fase7.png")]

sayajinu_l = [pygame.image.load("ssu/faseizk7.png"),
              pygame.image.load("ssu/faseizk1.png"),
              pygame.image.load("ssu/faseizk1.png"),
              pygame.image.load("ssu/faseizk1.png"),
              pygame.image.load("ssu/faseizk1.png"),
              pygame.image.load("ssu/faseizk1.png"),
              pygame.image.load("ssu/faseizk1.png"),
              pygame.image.load("ssu/faseizk1.png"),
              pygame.image.load("ssu/faseizk1.png"),
              pygame.image.load("ssu/faseizk1.png"),
              pygame.image.load("ssu/faseizk2.png"),
              pygame.image.load("ssu/faseizk2.png"),
              pygame.image.load("ssu/faseizk2.png"),
              pygame.image.load("ssu/faseizk2.png"),
              pygame.image.load("ssu/faseizk2.png"),
              pygame.image.load("ssu/faseizk2.png"),
              pygame.image.load("ssu/faseizk2.png"),
              pygame.image.load("ssu/faseizk2.png"),
              pygame.image.load("ssu/faseizk2.png"),
              pygame.image.load("ssu/faseizk2.png"),
              pygame.image.load("ssu/faseizk3.png"),
              pygame.image.load("ssu/faseizk3.png"),
              pygame.image.load("ssu/faseizk3.png"),
              pygame.image.load("ssu/faseizk3.png"),
              pygame.image.load("ssu/faseizk3.png"),
              pygame.image.load("ssu/faseizk3.png"),
              pygame.image.load("ssu/faseizk3.png"),
              pygame.image.load("ssu/faseizk3.png"),
              pygame.image.load("ssu/faseizk3.png"),
              pygame.image.load("ssu/faseizk3.png"),
              pygame.image.load("ssu/faseizk4.png"),
              pygame.image.load("ssu/faseizk4.png"),
              pygame.image.load("ssu/faseizk4.png"),
              pygame.image.load("ssu/faseizk4.png"),
              pygame.image.load("ssu/faseizk4.png"),
              pygame.image.load("ssu/faseizk4.png"),
              pygame.image.load("ssu/faseizk4.png"),
              pygame.image.load("ssu/faseizk4.png"),
              pygame.image.load("ssu/faseizk4.png"),
              pygame.image.load("ssu/faseizk4.png"),
              pygame.image.load("ssu/faseizk5.png"),
              pygame.image.load("ssu/faseizk5.png"),
              pygame.image.load("ssu/faseizk5.png"),
              pygame.image.load("ssu/faseizk5.png"),
              pygame.image.load("ssu/faseizk5.png"),
              pygame.image.load("ssu/faseizk5.png"),
              pygame.image.load("ssu/faseizk5.png"),
              pygame.image.load("ssu/faseizk5.png"),
              pygame.image.load("ssu/faseizk5.png"),
              pygame.image.load("ssu/faseizk5.png"),
              pygame.image.load("ssu/faseizk5.png"),
              pygame.image.load("ssu/faseizk5.png"),
              pygame.image.load("ssu/faseizk6.png"),
              pygame.image.load("ssu/faseizk6.png"),
              pygame.image.load("ssu/faseizk6.png"),
              pygame.image.load("ssu/faseizk6.png"),
              pygame.image.load("ssu/faseizk6.png"),
              pygame.image.load("ssu/faseizk6.png"),
              pygame.image.load("ssu/faseizk6.png"),
              pygame.image.load("ssu/faseizk6.png"),
              pygame.image.load("ssu/faseizk6.png"),
              pygame.image.load("ssu/faseizk6.png"),
              pygame.image.load("ssu/faseizk7.png"),
              pygame.image.load("ssu/faseizk7.png"),
              pygame.image.load("ssu/faseizk7.png"),
              pygame.image.load("ssu/faseizk7.png"),
              pygame.image.load("ssu/faseizk7.png"),
              pygame.image.load("ssu/faseizk7.png"),
              pygame.image.load("ssu/faseizk7.png"),
              pygame.image.load("ssu/faseizk7.png"),
              pygame.image.load("ssu/faseizk7.png"),
              pygame.image.load("ssu/faseizk7.png")]

sayajinu_puño_r = [pygame.image.load("ssu/puño1.png"),
                   pygame.image.load("ssu/puño2.png"),
                   pygame.image.load("ssu/puño3.png"),
                   pygame.image.load("ssu/puño4.png"),
                   pygame.image.load("ssu/puño2.png"),
                   pygame.image.load("ssu/puño3.png"),
                   pygame.image.load("ssu/puño4.png"),
                   pygame.image.load("ssu/puño2.png"),
                   pygame.image.load("ssu/puño3.png"),
                   pygame.image.load("ssu/puño4.png"),
                   pygame.image.load("ssu/puño2.png"),
                   pygame.image.load("ssu/puño3.png"),
                   pygame.image.load("ssu/puño4.png"),
                   pygame.image.load("ssu/puño2.png"),
                   pygame.image.load("ssu/puño3.png"),
                   pygame.image.load("ssu/puño4.png"),
                   pygame.image.load("ssu/puño2.png"),
                   pygame.image.load("ssu/puño1.png")]

sayajinu_puño_l = [pygame.image.load("ssu/puñoizk1.png"),
                   pygame.image.load("ssu/puñoizk2.png"),
                   pygame.image.load("ssu/puñoizk3.png"),
                   pygame.image.load("ssu/puñoizk4.png"),
                   pygame.image.load("ssu/puñoizk2.png"),
                   pygame.image.load("ssu/puñoizk3.png"),
                   pygame.image.load("ssu/puñoizk4.png"),
                   pygame.image.load("ssu/puñoizk2.png"),
                   pygame.image.load("ssu/puñoizk3.png"),
                   pygame.image.load("ssu/puñoizk4.png"),
                   pygame.image.load("ssu/puñoizk2.png"),
                   pygame.image.load("ssu/puñoizk3.png"),
                   pygame.image.load("ssu/puñoizk4.png"),
                   pygame.image.load("ssu/puñoizk2.png"),
                   pygame.image.load("ssu/puñoizk3.png"),
                   pygame.image.load("ssu/puñoizk4.png"),
                   pygame.image.load("ssu/puñoizk2.png"),
                   pygame.image.load("ssu/puñoizk1.png")]

sayajinu_patada_r = [pygame.image.load("ssu/patada1.png"),
                     pygame.image.load("ssu/patada1.png"),
                     pygame.image.load("ssu/patada1.png"),
                     pygame.image.load("ssu/patada1.png"),
                     pygame.image.load("ssu/patada1.png"),
                     pygame.image.load("ssu/patada1.png"),
                     pygame.image.load("ssu/patada2.png"),
                     pygame.image.load("ssu/patada2.png"),
                     pygame.image.load("ssu/patada2.png"),
                     pygame.image.load("ssu/patada2.png"),
                     pygame.image.load("ssu/patada2.png"),
                     pygame.image.load("ssu/patada2.png"),
                     pygame.image.load("ssu/patada3.png"),
                     pygame.image.load("ssu/patada3.png"),
                     pygame.image.load("ssu/patada3.png"),
                     pygame.image.load("ssu/patada3.png"),
                     pygame.image.load("ssu/patada3.png"),
                     pygame.image.load("ssu/patada3.png"),
                     pygame.image.load("ssu/patada4.png"),
                     pygame.image.load("ssu/patada4.png"),
                     pygame.image.load("ssu/patada4.png"),
                     pygame.image.load("ssu/patada4.png"),
                     pygame.image.load("ssu/patada4.png"),
                     pygame.image.load("ssu/patada4.png"),
                     pygame.image.load("ssu/patada5.png"),
                     pygame.image.load("ssu/patada5.png"),
                     pygame.image.load("ssu/patada5.png"),
                     pygame.image.load("ssu/patada5.png"),
                     pygame.image.load("ssu/patada5.png"),
                     pygame.image.load("ssu/patada5.png"),
                     pygame.image.load("ssu/patada6.png"),
                     pygame.image.load("ssu/patada6.png"),
                     pygame.image.load("ssu/patada6.png"),
                     pygame.image.load("ssu/patada6.png"),
                     pygame.image.load("ssu/patada6.png"),
                     pygame.image.load("ssu/patada6.png"),
                     pygame.image.load("ssu/patada7.png"),
                     pygame.image.load("ssu/patada7.png"),
                     pygame.image.load("ssu/patada7.png"),
                     pygame.image.load("ssu/patada7.png"),
                     pygame.image.load("ssu/patada7.png"),
                     pygame.image.load("ssu/patada7.png"),
                     pygame.image.load("ssu/patada8.png"),
                     pygame.image.load("ssu/patada8.png"),
                     pygame.image.load("ssu/patada8.png"),
                     pygame.image.load("ssu/patada8.png"),
                     pygame.image.load("ssu/patada8.png"),
                     pygame.image.load("ssu/patada8.png"),
                     pygame.image.load("ssu/patada9.png"),
                     pygame.image.load("ssu/patada9.png"),
                     pygame.image.load("ssu/patada9.png"),
                     pygame.image.load("ssu/patada9.png"),
                     pygame.image.load("ssu/patada9.png"),
                     pygame.image.load("ssu/patada9.png"),
                     pygame.image.load("ssu/patada10.png"),
                     pygame.image.load("ssu/patada10.png"),
                     pygame.image.load("ssu/patada10.png"),
                     pygame.image.load("ssu/patada10.png"),
                     pygame.image.load("ssu/patada10.png"),
                     pygame.image.load("ssu/patada10.png")]

sayajinu_patada_l = [pygame.image.load("ssu/patadaizk1.png"),
                     pygame.image.load("ssu/patadaizk1.png"),
                     pygame.image.load("ssu/patadaizk1.png"),
                     pygame.image.load("ssu/patadaizk1.png"),
                     pygame.image.load("ssu/patadaizk1.png"),
                     pygame.image.load("ssu/patadaizk1.png"),
                     pygame.image.load("ssu/patadaizk2.png"),
                     pygame.image.load("ssu/patadaizk2.png"),
                     pygame.image.load("ssu/patadaizk2.png"),
                     pygame.image.load("ssu/patadaizk2.png"),
                     pygame.image.load("ssu/patadaizk2.png"),
                     pygame.image.load("ssu/patadaizk2.png"),
                     pygame.image.load("ssu/patadaizk3.png"),
                     pygame.image.load("ssu/patadaizk3.png"),
                     pygame.image.load("ssu/patadaizk3.png"),
                     pygame.image.load("ssu/patadaizk3.png"),
                     pygame.image.load("ssu/patadaizk3.png"),
                     pygame.image.load("ssu/patadaizk3.png"),
                     pygame.image.load("ssu/patadaizk4.png"),
                     pygame.image.load("ssu/patadaizk4.png"),
                     pygame.image.load("ssu/patadaizk4.png"),
                     pygame.image.load("ssu/patadaizk4.png"),
                     pygame.image.load("ssu/patadaizk4.png"),
                     pygame.image.load("ssu/patadaizk4.png"),
                     pygame.image.load("ssu/patadaizk5.png"),
                     pygame.image.load("ssu/patadaizk5.png"),
                     pygame.image.load("ssu/patadaizk5.png"),
                     pygame.image.load("ssu/patadaizk5.png"),
                     pygame.image.load("ssu/patadaizk5.png"),
                     pygame.image.load("ssu/patadaizk5.png"),
                     pygame.image.load("ssu/patadaizk6.png"),
                     pygame.image.load("ssu/patadaizk6.png"),
                     pygame.image.load("ssu/patadaizk6.png"),
                     pygame.image.load("ssu/patadaizk6.png"),
                     pygame.image.load("ssu/patadaizk6.png"),
                     pygame.image.load("ssu/patadaizk6.png"),
                     pygame.image.load("ssu/patadaizk7.png"),
                     pygame.image.load("ssu/patadaizk7.png"),
                     pygame.image.load("ssu/patadaizk7.png"),
                     pygame.image.load("ssu/patadaizk7.png"),
                     pygame.image.load("ssu/patadaizk7.png"),
                     pygame.image.load("ssu/patadaizk7.png"),
                     pygame.image.load("ssu/patadaizk8.png"),
                     pygame.image.load("ssu/patadaizk8.png"),
                     pygame.image.load("ssu/patadaizk8.png"),
                     pygame.image.load("ssu/patadaizk8.png"),
                     pygame.image.load("ssu/patadaizk8.png"),
                     pygame.image.load("ssu/patadaizk8.png"),
                     pygame.image.load("ssu/patadaizk9.png"),
                     pygame.image.load("ssu/patadaizk9.png"),
                     pygame.image.load("ssu/patadaizk9.png"),
                     pygame.image.load("ssu/patadaizk9.png"),
                     pygame.image.load("ssu/patadaizk9.png"),
                     pygame.image.load("ssu/patadaizk9.png"),
                     pygame.image.load("ssu/patadaizk10.png"),
                     pygame.image.load("ssu/patadaizk10.png"),
                     pygame.image.load("ssu/patadaizk10.png"),
                     pygame.image.load("ssu/patadaizk10.png"),
                     pygame.image.load("ssu/patadaizk10.png"),
                     pygame.image.load("ssu/patadaizk10.png")]

sayajinu_kame = [pygame.image.load("ssu/kame1.png"),
                 pygame.image.load("ssu/kame1.png"),
                 pygame.image.load("ssu/kame1.png"),
                 pygame.image.load("ssu/kame1.png"),
                 pygame.image.load("ssu/kame2.png"),
                 pygame.image.load("ssu/kame2.png"),
                 pygame.image.load("ssu/kame2.png"),
                 pygame.image.load("ssu/kame2.png"),
                 pygame.image.load("ssu/kame3.png"),
                 pygame.image.load("ssu/kame3.png"),
                 pygame.image.load("ssu/kame3.png"),
                 pygame.image.load("ssu/kame3.png"),
                 pygame.image.load("ssu/kame3.png"),
                 pygame.image.load("ssu/kame3.png"),
                 pygame.image.load("ssu/kame3.png"),
                 pygame.image.load("ssu/kame3.png"),
                 pygame.image.load("ssu/kame3.png"),
                 pygame.image.load("ssu/kame3.png"),
                 pygame.image.load("ssu/kame4.png"),
                 pygame.image.load("ssu/kame4.png"),
                 pygame.image.load("ssu/kame4.png"),
                 pygame.image.load("ssu/kame4.png"),
                 pygame.image.load("ssu/kame5.png"),
                 pygame.image.load("ssu/kame5.png"),
                 pygame.image.load("ssu/kame5.png"),
                 pygame.image.load("ssu/kame5.png")]

sayajinu_carga_energia_r = [pygame.image.load("ssu/carga1.png"),
                            pygame.image.load("ssu/carga2.png"),
                            pygame.image.load("ssu/carga1.png"),
                            pygame.image.load("ssu/carga2.png"),
                            pygame.image.load("ssu/carga1.png"),
                            pygame.image.load("ssu/carga2.png"),
                            pygame.image.load("ssu/carga1.png"),
                            pygame.image.load("ssu/carga2.png"),
                            pygame.image.load("ssu/carga1.png"),
                            pygame.image.load("ssu/carga2.png"),
                            pygame.image.load("ssu/carga1.png"),
                            pygame.image.load("ssu/carga2.png")]

sayajinu_carga_energia_l = [pygame.image.load("ssu/cargaizk1.png"),
                            pygame.image.load("ssu/cargaizk2.png"),
                            pygame.image.load("ssu/cargaizk1.png"),
                            pygame.image.load("ssu/cargaizk2.png"),
                            pygame.image.load("ssu/cargaizk1.png"),
                            pygame.image.load("ssu/cargaizk2.png"),
                            pygame.image.load("ssu/cargaizk1.png"),
                            pygame.image.load("ssu/cargaizk2.png"),
                            pygame.image.load("ssu/cargaizk1.png"),
                            pygame.image.load("ssu/cargaizk2.png"),
                            pygame.image.load("ssu/cargaizk1.png"),
                            pygame.image.load("ssu/cargaizk2.png")]

sayajinuc_r = [pygame.image.load("ssuc/fase9.png").convert(),
               pygame.image.load("ssuc/fase1.png").convert(),
               pygame.image.load("ssuc/fase1.png").convert(),
               pygame.image.load("ssuc/fase1.png").convert(),
               pygame.image.load("ssuc/fase1.png").convert(),
               pygame.image.load("ssuc/fase1.png").convert(),
               pygame.image.load("ssuc/fase1.png").convert(),
               pygame.image.load("ssuc/fase1.png").convert(),
               pygame.image.load("ssuc/fase2.png").convert(),
               pygame.image.load("ssuc/fase2.png").convert(),
               pygame.image.load("ssuc/fase2.png").convert(),
               pygame.image.load("ssuc/fase2.png").convert(),
               pygame.image.load("ssuc/fase2.png").convert(),
               pygame.image.load("ssuc/fase2.png").convert(),
               pygame.image.load("ssuc/fase2.png").convert(),
               pygame.image.load("ssuc/fase2.png").convert(),
               pygame.image.load("ssuc/fase3.png").convert(),
               pygame.image.load("ssuc/fase3.png").convert(),
               pygame.image.load("ssuc/fase3.png").convert(),
               pygame.image.load("ssuc/fase3.png").convert(),
               pygame.image.load("ssuc/fase3.png").convert(),
               pygame.image.load("ssuc/fase3.png").convert(),
               pygame.image.load("ssuc/fase3.png").convert(),
               pygame.image.load("ssuc/fase3.png").convert(),
               pygame.image.load("ssuc/fase4.png").convert(),
               pygame.image.load("ssuc/fase4.png").convert(),
               pygame.image.load("ssuc/fase4.png").convert(),
               pygame.image.load("ssuc/fase4.png").convert(),
               pygame.image.load("ssuc/fase4.png").convert(),
               pygame.image.load("ssuc/fase4.png").convert(),
               pygame.image.load("ssuc/fase4.png").convert(),
               pygame.image.load("ssuc/fase4.png").convert(),
               pygame.image.load("ssuc/fase5.png").convert(),
               pygame.image.load("ssuc/fase5.png").convert(),
               pygame.image.load("ssuc/fase5.png").convert(),
               pygame.image.load("ssuc/fase5.png").convert(),
               pygame.image.load("ssuc/fase5.png").convert(),
               pygame.image.load("ssuc/fase5.png").convert(),
               pygame.image.load("ssuc/fase5.png").convert(),
               pygame.image.load("ssuc/fase5.png").convert(),
               pygame.image.load("ssuc/fase6.png").convert(),
               pygame.image.load("ssuc/fase6.png").convert(),
               pygame.image.load("ssuc/fase6.png").convert(),
               pygame.image.load("ssuc/fase6.png").convert(),
               pygame.image.load("ssuc/fase6.png").convert(),
               pygame.image.load("ssuc/fase6.png").convert(),
               pygame.image.load("ssuc/fase6.png").convert(),
               pygame.image.load("ssuc/fase6.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase7.png").convert(),
               pygame.image.load("ssuc/fase9.png").convert(),
               pygame.image.load("ssuc/fase9.png").convert(),
               pygame.image.load("ssuc/fase9.png").convert(),
               pygame.image.load("ssuc/fase9.png").convert(),
               pygame.image.load("ssuc/fase9.png").convert(),
               pygame.image.load("ssuc/fase9.png").convert(),
               pygame.image.load("ssuc/fase9.png").convert(),
               pygame.image.load("ssuc/fase9.png").convert()]

sayajinuc_l = [pygame.image.load("ssuc/faseizk9.png"),
               pygame.image.load("ssuc/faseizk1.png"),
               pygame.image.load("ssuc/faseizk1.png"),
               pygame.image.load("ssuc/faseizk1.png"),
               pygame.image.load("ssuc/faseizk1.png"),
               pygame.image.load("ssuc/faseizk1.png"),
               pygame.image.load("ssuc/faseizk1.png"),
               pygame.image.load("ssuc/faseizk1.png"),
               pygame.image.load("ssuc/faseizk2.png"),
               pygame.image.load("ssuc/faseizk2.png"),
               pygame.image.load("ssuc/faseizk2.png"),
               pygame.image.load("ssuc/faseizk2.png"),
               pygame.image.load("ssuc/faseizk2.png"),
               pygame.image.load("ssuc/faseizk2.png"),
               pygame.image.load("ssuc/faseizk2.png"),
               pygame.image.load("ssuc/faseizk2.png"),
               pygame.image.load("ssuc/faseizk3.png"),
               pygame.image.load("ssuc/faseizk3.png"),
               pygame.image.load("ssuc/faseizk3.png"),
               pygame.image.load("ssuc/faseizk3.png"),
               pygame.image.load("ssuc/faseizk3.png"),
               pygame.image.load("ssuc/faseizk3.png"),
               pygame.image.load("ssuc/faseizk3.png"),
               pygame.image.load("ssuc/faseizk3.png"),
               pygame.image.load("ssuc/faseizk4.png"),
               pygame.image.load("ssuc/faseizk4.png"),
               pygame.image.load("ssuc/faseizk4.png"),
               pygame.image.load("ssuc/faseizk4.png"),
               pygame.image.load("ssuc/faseizk4.png"),
               pygame.image.load("ssuc/faseizk4.png"),
               pygame.image.load("ssuc/faseizk4.png"),
               pygame.image.load("ssuc/faseizk4.png"),
               pygame.image.load("ssuc/faseizk5.png"),
               pygame.image.load("ssuc/faseizk5.png"),
               pygame.image.load("ssuc/faseizk5.png"),
               pygame.image.load("ssuc/faseizk5.png"),
               pygame.image.load("ssuc/faseizk5.png"),
               pygame.image.load("ssuc/faseizk5.png"),
               pygame.image.load("ssuc/faseizk5.png"),
               pygame.image.load("ssuc/faseizk5.png"),
               pygame.image.load("ssuc/faseizk6.png"),
               pygame.image.load("ssuc/faseizk6.png"),
               pygame.image.load("ssuc/faseizk6.png"),
               pygame.image.load("ssuc/faseizk6.png"),
               pygame.image.load("ssuc/faseizk6.png"),
               pygame.image.load("ssuc/faseizk6.png"),
               pygame.image.load("ssuc/faseizk6.png"),
               pygame.image.load("ssuc/faseizk6.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk7.png"),
               pygame.image.load("ssuc/faseizk9.png"),
               pygame.image.load("ssuc/faseizk9.png"),
               pygame.image.load("ssuc/faseizk9.png"),
               pygame.image.load("ssuc/faseizk9.png"),
               pygame.image.load("ssuc/faseizk9.png"),
               pygame.image.load("ssuc/faseizk9.png"),
               pygame.image.load("ssuc/faseizk9.png"),
               pygame.image.load("ssuc/faseizk9.png")]

sayajinuc_puño_r = [pygame.image.load("ssuc/puño1.png"),
                    pygame.image.load("ssuc/puño1.png"),
                    pygame.image.load("ssuc/puño1.png"),
                    pygame.image.load("ssuc/puño1.png"),
                    pygame.image.load("ssuc/puño1.png"),
                    pygame.image.load("ssuc/puño1.png"),
                    pygame.image.load("ssuc/puño1.png"),
                    pygame.image.load("ssuc/puño1.png"),
                    pygame.image.load("ssuc/puño2.png"),
                    pygame.image.load("ssuc/puño2.png"),
                    pygame.image.load("ssuc/puño2.png"),
                    pygame.image.load("ssuc/puño2.png"),
                    pygame.image.load("ssuc/puño2.png"),
                    pygame.image.load("ssuc/puño2.png"),
                    pygame.image.load("ssuc/puño2.png"),
                    pygame.image.load("ssuc/puño2.png"),
                    pygame.image.load("ssuc/puño3.png"),
                    pygame.image.load("ssuc/puño3.png"),
                    pygame.image.load("ssuc/puño3.png"),
                    pygame.image.load("ssuc/puño3.png"),
                    pygame.image.load("ssuc/puño3.png"),
                    pygame.image.load("ssuc/puño3.png"),
                    pygame.image.load("ssuc/puño3.png"),
                    pygame.image.load("ssuc/puño3.png"),
                    pygame.image.load("ssuc/puño4.png"),
                    pygame.image.load("ssuc/puño4.png"),
                    pygame.image.load("ssuc/puño4.png"),
                    pygame.image.load("ssuc/puño4.png"),
                    pygame.image.load("ssuc/puño4.png"),
                    pygame.image.load("ssuc/puño4.png"),
                    pygame.image.load("ssuc/puño4.png"),
                    pygame.image.load("ssuc/puño4.png"),
                    pygame.image.load("ssuc/puño5.png"),
                    pygame.image.load("ssuc/puño5.png"),
                    pygame.image.load("ssuc/puño5.png"),
                    pygame.image.load("ssuc/puño5.png"),
                    pygame.image.load("ssuc/puño5.png"),
                    pygame.image.load("ssuc/puño5.png"),
                    pygame.image.load("ssuc/puño5.png"),
                    pygame.image.load("ssuc/puño5.png"),
                    pygame.image.load("ssuc/puño6.png"),
                    pygame.image.load("ssuc/puño6.png"),
                    pygame.image.load("ssuc/puño6.png"),
                    pygame.image.load("ssuc/puño6.png"),
                    pygame.image.load("ssuc/puño6.png"),
                    pygame.image.load("ssuc/puño6.png"),
                    pygame.image.load("ssuc/puño6.png"),
                    pygame.image.load("ssuc/puño6.png"),
                    pygame.image.load("ssuc/puño7.png"),
                    pygame.image.load("ssuc/puño7.png"),
                    pygame.image.load("ssuc/puño7.png"),
                    pygame.image.load("ssuc/puño7.png"),
                    pygame.image.load("ssuc/puño7.png"),
                    pygame.image.load("ssuc/puño7.png"),
                    pygame.image.load("ssuc/puño7.png"),
                    pygame.image.load("ssuc/puño7.png"),
                    pygame.image.load("ssuc/puño8.png"),
                    pygame.image.load("ssuc/puño8.png"),
                    pygame.image.load("ssuc/puño8.png"),
                    pygame.image.load("ssuc/puño8.png"),
                    pygame.image.load("ssuc/puño8.png"),
                    pygame.image.load("ssuc/puño8.png"),
                    pygame.image.load("ssuc/puño8.png"),
                    pygame.image.load("ssuc/puño8.png"),
                    pygame.image.load("ssuc/puño9.png"),
                    pygame.image.load("ssuc/puño9.png"),
                    pygame.image.load("ssuc/puño9.png"),
                    pygame.image.load("ssuc/puño9.png"),
                    pygame.image.load("ssuc/puño9.png"),
                    pygame.image.load("ssuc/puño9.png"),
                    pygame.image.load("ssuc/puño9.png"),
                    pygame.image.load("ssuc/puño9.png")]

sayajinuc_puño_l = [pygame.image.load("ssuc/puñoizk1.png"),
                    pygame.image.load("ssuc/puñoizk1.png"),
                    pygame.image.load("ssuc/puñoizk1.png"),
                    pygame.image.load("ssuc/puñoizk1.png"),
                    pygame.image.load("ssuc/puñoizk1.png"),
                    pygame.image.load("ssuc/puñoizk1.png"),
                    pygame.image.load("ssuc/puñoizk1.png"),
                    pygame.image.load("ssuc/puñoizk1.png"),
                    pygame.image.load("ssuc/puñoizk2.png"),
                    pygame.image.load("ssuc/puñoizk2.png"),
                    pygame.image.load("ssuc/puñoizk2.png"),
                    pygame.image.load("ssuc/puñoizk2.png"),
                    pygame.image.load("ssuc/puñoizk2.png"),
                    pygame.image.load("ssuc/puñoizk2.png"),
                    pygame.image.load("ssuc/puñoizk2.png"),
                    pygame.image.load("ssuc/puñoizk2.png"),
                    pygame.image.load("ssuc/puñoizk3.png"),
                    pygame.image.load("ssuc/puñoizk3.png"),
                    pygame.image.load("ssuc/puñoizk3.png"),
                    pygame.image.load("ssuc/puñoizk3.png"),
                    pygame.image.load("ssuc/puñoizk3.png"),
                    pygame.image.load("ssuc/puñoizk3.png"),
                    pygame.image.load("ssuc/puñoizk3.png"),
                    pygame.image.load("ssuc/puñoizk3.png"),
                    pygame.image.load("ssuc/puñoizk4.png"),
                    pygame.image.load("ssuc/puñoizk4.png"),
                    pygame.image.load("ssuc/puñoizk4.png"),
                    pygame.image.load("ssuc/puñoizk4.png"),
                    pygame.image.load("ssuc/puñoizk4.png"),
                    pygame.image.load("ssuc/puñoizk4.png"),
                    pygame.image.load("ssuc/puñoizk4.png"),
                    pygame.image.load("ssuc/puñoizk4.png"),
                    pygame.image.load("ssuc/puñoizk5.png"),
                    pygame.image.load("ssuc/puñoizk5.png"),
                    pygame.image.load("ssuc/puñoizk5.png"),
                    pygame.image.load("ssuc/puñoizk5.png"),
                    pygame.image.load("ssuc/puñoizk5.png"),
                    pygame.image.load("ssuc/puñoizk5.png"),
                    pygame.image.load("ssuc/puñoizk5.png"),
                    pygame.image.load("ssuc/puñoizk5.png"),
                    pygame.image.load("ssuc/puñoizk6.png"),
                    pygame.image.load("ssuc/puñoizk6.png"),
                    pygame.image.load("ssuc/puñoizk6.png"),
                    pygame.image.load("ssuc/puñoizk6.png"),
                    pygame.image.load("ssuc/puñoizk6.png"),
                    pygame.image.load("ssuc/puñoizk6.png"),
                    pygame.image.load("ssuc/puñoizk6.png"),
                    pygame.image.load("ssuc/puñoizk6.png"),
                    pygame.image.load("ssuc/puñoizk7.png"),
                    pygame.image.load("ssuc/puñoizk7.png"),
                    pygame.image.load("ssuc/puñoizk7.png"),
                    pygame.image.load("ssuc/puñoizk7.png"),
                    pygame.image.load("ssuc/puñoizk7.png"),
                    pygame.image.load("ssuc/puñoizk7.png"),
                    pygame.image.load("ssuc/puñoizk7.png"),
                    pygame.image.load("ssuc/puñoizk7.png"),
                    pygame.image.load("ssuc/puñoizk8.png"),
                    pygame.image.load("ssuc/puñoizk8.png"),
                    pygame.image.load("ssuc/puñoizk8.png"),
                    pygame.image.load("ssuc/puñoizk8.png"),
                    pygame.image.load("ssuc/puñoizk8.png"),
                    pygame.image.load("ssuc/puñoizk8.png"),
                    pygame.image.load("ssuc/puñoizk8.png"),
                    pygame.image.load("ssuc/puñoizk8.png"),
                    pygame.image.load("ssuc/puñoizk9.png"),
                    pygame.image.load("ssuc/puñoizk9.png"),
                    pygame.image.load("ssuc/puñoizk9.png"),
                    pygame.image.load("ssuc/puñoizk9.png"),
                    pygame.image.load("ssuc/puñoizk9.png"),
                    pygame.image.load("ssuc/puñoizk9.png"),
                    pygame.image.load("ssuc/puñoizk9.png"),
                    pygame.image.load("ssuc/puñoizk9.png")]

sayajinuc_patada_r = [pygame.image.load("ssuc/patada1.png"),
                      pygame.image.load("ssuc/patada1.png"),
                      pygame.image.load("ssuc/patada1.png"),
                      pygame.image.load("ssuc/patada1.png"),
                      pygame.image.load("ssuc/patada1.png"),
                      pygame.image.load("ssuc/patada2.png"),
                      pygame.image.load("ssuc/patada2.png"),
                      pygame.image.load("ssuc/patada2.png"),
                      pygame.image.load("ssuc/patada2.png"),
                      pygame.image.load("ssuc/patada2.png"),
                      pygame.image.load("ssuc/patada3.png"),
                      pygame.image.load("ssuc/patada3.png"),
                      pygame.image.load("ssuc/patada3.png"),
                      pygame.image.load("ssuc/patada3.png"),
                      pygame.image.load("ssuc/patada3.png"),
                      pygame.image.load("ssuc/patada4.png"),
                      pygame.image.load("ssuc/patada4.png"),
                      pygame.image.load("ssuc/patada4.png"),
                      pygame.image.load("ssuc/patada4.png"),
                      pygame.image.load("ssuc/patada4.png"),
                      pygame.image.load("ssuc/patada5.png"),
                      pygame.image.load("ssuc/patada5.png"),
                      pygame.image.load("ssuc/patada5.png"),
                      pygame.image.load("ssuc/patada5.png"),
                      pygame.image.load("ssuc/patada5.png"),
                      pygame.image.load("ssuc/patada6.png"),
                      pygame.image.load("ssuc/patada6.png"),
                      pygame.image.load("ssuc/patada6.png"),
                      pygame.image.load("ssuc/patada6.png"),
                      pygame.image.load("ssuc/patada6.png"),
                      pygame.image.load("ssuc/patada7.png"),
                      pygame.image.load("ssuc/patada7.png"),
                      pygame.image.load("ssuc/patada7.png"),
                      pygame.image.load("ssuc/patada7.png"),
                      pygame.image.load("ssuc/patada7.png"),
                      pygame.image.load("ssuc/patada8.png"),
                      pygame.image.load("ssuc/patada8.png"),
                      pygame.image.load("ssuc/patada8.png"),
                      pygame.image.load("ssuc/patada8.png"),
                      pygame.image.load("ssuc/patada8.png")]

sayajinuc_patada_l = [pygame.image.load("ssuc/patadaizk1.png"),
                      pygame.image.load("ssuc/patadaizk1.png"),
                      pygame.image.load("ssuc/patadaizk1.png"),
                      pygame.image.load("ssuc/patadaizk1.png"),
                      pygame.image.load("ssuc/patadaizk1.png"),
                      pygame.image.load("ssuc/patadaizk2.png"),
                      pygame.image.load("ssuc/patadaizk2.png"),
                      pygame.image.load("ssuc/patadaizk2.png"),
                      pygame.image.load("ssuc/patadaizk2.png"),
                      pygame.image.load("ssuc/patadaizk2.png"),
                      pygame.image.load("ssuc/patadaizk3.png"),
                      pygame.image.load("ssuc/patadaizk3.png"),
                      pygame.image.load("ssuc/patadaizk3.png"),
                      pygame.image.load("ssuc/patadaizk3.png"),
                      pygame.image.load("ssuc/patadaizk3.png"),
                      pygame.image.load("ssuc/patadaizk4.png"),
                      pygame.image.load("ssuc/patadaizk4.png"),
                      pygame.image.load("ssuc/patadaizk4.png"),
                      pygame.image.load("ssuc/patadaizk4.png"),
                      pygame.image.load("ssuc/patadaizk4.png"),
                      pygame.image.load("ssuc/patadaizk5.png"),
                      pygame.image.load("ssuc/patadaizk5.png"),
                      pygame.image.load("ssuc/patadaizk5.png"),
                      pygame.image.load("ssuc/patadaizk5.png"),
                      pygame.image.load("ssuc/patadaizk5.png"),
                      pygame.image.load("ssuc/patadaizk6.png"),
                      pygame.image.load("ssuc/patadaizk6.png"),
                      pygame.image.load("ssuc/patadaizk6.png"),
                      pygame.image.load("ssuc/patadaizk6.png"),
                      pygame.image.load("ssuc/patadaizk6.png"),
                      pygame.image.load("ssuc/patadaizk7.png"),
                      pygame.image.load("ssuc/patadaizk7.png"),
                      pygame.image.load("ssuc/patadaizk7.png"),
                      pygame.image.load("ssuc/patadaizk7.png"),
                      pygame.image.load("ssuc/patadaizk7.png"),
                      pygame.image.load("ssuc/patadaizk8.png"),
                      pygame.image.load("ssuc/patadaizk8.png"),
                      pygame.image.load("ssuc/patadaizk8.png"),
                      pygame.image.load("ssuc/patadaizk8.png"),
                      pygame.image.load("ssuc/patadaizk8.png")]

sayajinuc_kame = [pygame.image.load("ssuc/kame1.png"),
                  pygame.image.load("ssuc/kame1.png"),
                  pygame.image.load("ssuc/kame1.png"),
                  pygame.image.load("ssuc/kame1.png"),
                  pygame.image.load("ssuc/kame1.png"),
                  pygame.image.load("ssuc/kame1.png"),
                  pygame.image.load("ssuc/kame1.png"),
                  pygame.image.load("ssuc/kame1.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png"),
                  pygame.image.load("ssuc/kame2.png")]

sayajinuc_carga_energia_r = [pygame.image.load("ssuc/carga1.png"),
                             pygame.image.load("ssuc/carga2.png"),
                             pygame.image.load("ssuc/carga1.png"),
                             pygame.image.load("ssuc/carga2.png"),
                             pygame.image.load("ssuc/carga1.png"),
                             pygame.image.load("ssuc/carga2.png"),
                             pygame.image.load("ssuc/carga1.png"),
                             pygame.image.load("ssuc/carga2.png"),
                             pygame.image.load("ssuc/carga1.png"),
                             pygame.image.load("ssuc/carga2.png"),
                             pygame.image.load("ssuc/carga1.png"),
                             pygame.image.load("ssuc/carga2.png")]

sayajinuc_carga_energia_l = [pygame.image.load("ssuc/cargaizk1.png"),
                             pygame.image.load("ssuc/cargaizk2.png"),
                             pygame.image.load("ssuc/cargaizk1.png"),
                             pygame.image.load("ssuc/cargaizk2.png"),
                             pygame.image.load("ssuc/cargaizk1.png"),
                             pygame.image.load("ssuc/cargaizk2.png"),
                             pygame.image.load("ssuc/cargaizk1.png"),
                             pygame.image.load("ssuc/cargaizk2.png"),
                             pygame.image.load("ssuc/cargaizk1.png"),
                             pygame.image.load("ssuc/cargaizk2.png"),
                             pygame.image.load("ssuc/cargaizk1.png"),
                             pygame.image.load("ssuc/cargaizk2.png")]


def pause():
    pausa = True
    while pausa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausa = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(5)



class Fotos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("fotos/fotogoku.png")
        self.image.set_colorkey(BLANCO)
        self.imagejiren = pygame.image.load("fotos/fotojiren.jpg")
        self.imagejiren.set_colorkey(BLANCO)
    def render(self):
        ventana.blit(self.image, (0, 0))
        self.image.set_colorkey(BLANCO)
        ventana.blit(self.imagejiren, (640, 0))
        self.imagejiren.set_colorkey(BLANCO)

class BarrasVidaEnergia(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if jugador.vida >= 1:
            pygame.draw.rect(ventana, (255, 0, 0), (ancho - 650, alto - 350, 50, 10))
            pygame.draw.rect(ventana, (0, 128, 0), (ancho - 650, alto - 350, 50 - (3 * (15 - jugador.vida)), 10)) #-3*5 = 15 que son las vidas actuales
            pygame.draw.rect(ventana, (0, 0, 0), (ancho - 650, alto - 340, 50, 10))
            pygame.draw.rect(ventana, (255, 255, 0), (ancho - 650, alto - 340, 50 - (5 * (10 - jugador.energia)), 10))
        if enemy.vidaenemigo >= 1:
            pygame.draw.rect(ventana, (255, 0, 0), (ancho - 120, alto - 350, 50, 10))
            pygame.draw.rect(ventana, (0, 128, 0), (ancho - 120, alto - 350, 50 - (3 * (15 - enemy.vidaenemigo)), 10))
            pygame.draw.rect(ventana, (0, 0, 0), (ancho - 120, alto - 340, 50, 10))
            pygame.draw.rect(ventana, (255, 255, 0), (ancho - 120, alto - 340, 50 - (5 * (10 - enemy.energia)), 10))


class Winer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("winer.png").convert()
        self.image.set_colorkey(BLANCO)

    def render(self):
        ventana.blit(self.image, (150, 20))
        self.image.set_colorkey(BLANCO)


class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("gameover.png").convert()
        self.image.set_colorkey(BLANCO)

    def render(self):
        ventana.blit(self.image, (150, 50))
        self.image.set_colorkey(BLANCO)


class StatusBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 30))
        self.rect = self.surf.get_rect(center=(500, 10))
        self.exp = jugador.experiencia

    def update_draw(self):
        # Create the text to be displayed
        text1 = headingfont.render("NIVEL: " + str(jugador.nivel), True, NEGRO)
        text4 = headingfont.render("EXP: " + str(jugador.experiencia), True, NEGRO)
        # Draw the text to the status bar
        ventana.blit(text1, (0, 60))
        ventana.blit(text4, (0, 338))


class StatusBarEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 30))
        self.rect = self.surf.get_rect(center=(500, 10))
        self.exp = jugador.experiencia

    def update_draw(self):
        # Create the text to be displayed
        text1 = headingfont.render("NIVEL: " + str(enemy.nivel), True, NEGRO)


        # Draw the text to the status bar
        ventana.blit(text1, (640, 60))



class FondoPantalla(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.fondoimagen = pygame.image.load("verdeRoca.jpg")
        self.fondoy = 0
        self.fondox = 0

    def render(self):
        ventana.blit(self.fondoimagen, (self.fondox, self.fondoy))


class SueloPantalla(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sueloimagen = pygame.image.load("Ground.png")
        self.rect = self.sueloimagen.get_rect(center=(350, 350))

    def render(self):
        ventana.blit(self.sueloimagen, (self.rect.x, self.rect.y))


class Explosiones(pygame.sprite.Sprite):
    def __init__(self, centro):
        pygame.sprite.Sprite.__init__(self)
        self.image = boom[enemy.explosion_frame]
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.center = centro

    def update(self):
        if enemy.explosion_frame > 25:
            enemy.explosion_frame = 0
        enemy.explosion_frame += 1
        if enemy.explosion_frame:
            self.kill()


class Genkidama(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.direccion = jugador.direccion
        if self.direccion == "RIGHT":
            self.image = pygame.image.load("bolagenki/genki3.png")

        else:
            self.image = pygame.image.load("bolagenki/genki3.png")

        self.rect = self.image.get_rect(center=jugador.pos)
        self.rect.x = jugador.pos.x - 20
        self.rect.y = jugador.pos.y - 120  # altura del kame

    def ki(self):
        jugador.magic_cooldown = 0

        # Se ejecuta mientras la bola de fuego aún está dentro de la pantalla con margen adicional
        if -10 < self.rect.x < 710:
            if self.direccion == "RIGHT":
                self.image = pygame.image.load("bolagenki/genki3.png")
                self.image.set_colorkey(BLANCO)
                ventana.blit(self.image, self.rect)
            else:
                self.image = pygame.image.load("bolagenki/genki3.png")
                self.image.set_colorkey(BLANCO)
                ventana.blit(self.image, self.rect)

            if self.direccion == "RIGHT":
                self.rect.move_ip(2, 1)
            else:
                self.rect.move_ip(-2, 1)
        else:
            self.kill()
            jugador.magic_cooldown = 1
            jugador.atake3 = False


class FireBall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.direccion = jugador.direccion
        if self.direccion == "RIGHT":
            self.image = pygame.image.load("gokuatakes/kame.png")
            self.image.set_colorkey(BLANCO)
        else:
            self.image = pygame.image.load("gokuatakes/kameizk.png")
            self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect(center=jugador.pos)
        self.rect.x = jugador.pos.x
        self.rect.y = jugador.pos.y - 50

    def fire(self):
        jugador.magic_cooldown = 0
        # Runs while the fireball is still within the screen w/ extra margin
        if -10 < self.rect.x < 710:
            if self.direccion == "RIGHT":
                self.image = pygame.image.load("kames/bolaki.png")
                self.image.set_colorkey(BLANCO)
                ventana.blit(self.image, self.rect)
            else:
                self.image = pygame.image.load("kames/bolakiizk.png")
                self.image.set_colorkey(BLANCO)
                ventana.blit(self.image, self.rect)

            if self.direccion == "RIGHT":
                self.rect.move_ip(6, 0)
            else:
                self.rect.move_ip(-6, 0)
        else:
            self.kill()
            jugador.magic_cooldown = 1
            jugador.atake5 = False


class Kamehameha(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.direccion = jugador.direccion
        if self.direccion == "RIGHT":
            self.image = bola_kame_r[jugador.kame_frame]
        else:
            self.image = bola_kame_l[jugador.kame_frame]

        self.rect = self.image.get_rect(center=jugador.pos)
        self.rect.x = jugador.pos.x + 20
        self.rect.y = jugador.pos.y - 70  # altura del kame

    def ki(self):
        jugador.magic_cooldown = 0
        if jugador.atake3 == False:
            if jugador.direccion == "RIGHT":
                jugador.jugadorimagen = pygame.image.load("gokuatakes/kameder6.png")
                jugador.jugadorimagen.set_colorkey(BLANCO)
                if jugador.kaioken == True:
                    jugador.jugadorimagen = pygame.image.load("gokukaioken/kamekaioken6.png")
                    jugador.jugadorimagen.set_colorkey(BLANCO)
                if jugador.supersayajin == True:
                    jugador.jugadorimagen = pygame.image.load("gokuss/kame6tras.png")
                    jugador.jugadorimagen.set_colorkey(BLANCO)
                if jugador.supersayajin1 == True:
                    jugador.jugadorimagen = pygame.image.load("gokussf1/kame7.png")
                    jugador.jugadorimagen.set_colorkey(BLANCO)
                if jugador.supersayajin3 == True:
                    jugador.jugadorimagen = pygame.image.load("gokuss3/kame7tras.png")
                    jugador.jugadorimagen.set_colorkey(BLANCO)
                if jugador.supersayajin4 == True:
                    jugador.jugadorimagen = pygame.image.load("ss4/kame7.png")
                    jugador.jugadorimagen.set_colorkey(BLANCO)
                if jugador.supersayajind == True:
                    jugador.jugadorimagen = pygame.image.load("ssd/kame4.png")
                    jugador.jugadorimagen.set_colorkey(BLANCO)
                if jugador.supersayajinb == True:
                    jugador.jugadorimagen = pygame.image.load("ssb/kame2tras.png")
                    jugador.jugadorimagen.set_colorkey(SSBCOLOR)
                if jugador.supersayajinbk == True:
                    jugador.jugadorimagen = pygame.image.load("ssbk/kame4.png")
                    jugador.jugadorimagen.set_colorkey(BLANCO)
                if jugador.supersayajinu == True:
                    jugador.jugadorimagen = pygame.image.load("ssu/kame5tras.png")
                    jugador.jugadorimagen.set_colorkey(BLANCO)
                if jugador.supersayajinuc == True:
                    jugador.jugadorimagen = pygame.image.load("ssuc/kame2tras.png")
                    jugador.jugadorimagen.set_colorkey(VERDE)
            else:
                jugador.jugadorimagen = pygame.image.load("gokuatakes/kameizk6.png")
                if jugador.kaioken == True:
                    jugador.jugadorimagen = pygame.image.load("gokukaioken/kamekaiokenizk6.png")
                if jugador.supersayajin1 == True:
                    jugador.jugadorimagen = pygame.image.load("gokussf1/kame7.png")
                jugador.jugadorimagen.set_colorkey(BLANCO)
            if jugador.kame_frame > 39:
                jugador.kame_frame = 0

            if jugador.kame_frame == 39:
                self.kill()
                jugador.magic_cooldown = 1

            # Se ejecuta mientras la bola de fuego aún está dentro de la pantalla con margen adicional
            if -10 < self.rect.x < 710:
                if self.direccion == "RIGHT":
                    self.image = bola_kame_r[jugador.kame_frame]
                    self.image.set_colorkey(BLANCO)
                    ventana.blit(self.image, self.rect)
                else:
                    self.image = bola_kame_l[jugador.kame_frame]
                    self.image.set_colorkey(BLANCO)
                    ventana.blit(self.image, self.rect)
                jugador.kame_frame += 1

                if self.direccion == "RIGHT":
                    self.rect.move_ip(0, 0)
                else:
                    self.rect.move_ip(-0, 0)
            else:
                self.kill()
                jugador.magic_cooldown = 1
                jugador.atake3 = False








class BarraExperiencia(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("barrasexperiencia/barraexperienciavacia.png")
        self.image.set_colorkey(BLANCO)

    def render(self):
        ventana.blit(self.image, (40, 340))
        self.image.set_colorkey(BLANCO)




class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.kaioken = False
        self.supersayajin = False
        self.supersayajin1 = False
        self.supersayajin3 = False
        self.supersayajin4 = False
        self.supersayajind = False
        self.supersayajinb = False
        self.supersayajinbk = False
        self.supersayajinu = False
        self.supersayajinuc = False
        self.jugadorimagen = pygame.image.load("gokuparado/goku1.png")
        self.jugadorimagen.set_colorkey(BLANCO)
        self.rect = self.jugadorimagen.get_rect()
        if self.kaioken == True:
            self.jugadorimagen = pygame.image.load("gokukaioken/kaiokenparado.png")
            self.jugadorimagen.set_colorkey(BLANCO)
            self.rect = self.jugadorimagen.get_rect()
        if self.supersayajin == True:
            self.jugadorimagen = pygame.image.load("gokuss/ss5.png")
            self.jugadorimagen.set_colorkey(BLANCO)
            self.rect = self.jugadorimagen.get_rect()
        if self.supersayajin1 == True:
            self.jugadorimagen = pygame.image.load("gokussf1/gokussf1parado.png")
            self.jugadorimagen.set_colorkey(BLANCO)
            self.rect = self.jugadorimagen.get_rect()
        if self.supersayajin3 == True:
            self.jugadorimagen = pygame.image.load("gokuss3/fase4.png")
            self.jugadorimagen.set_colorkey(BLANCO)
            self.rect = self.jugadorimagen.get_rect()
        if self.supersayajin4 == True:
            self.jugadorimagen = pygame.image.load("ss4/fase4.png")
            self.jugadorimagen.set_colorkey(BLANCO)
            self.rect = self.jugadorimagen.get_rect()
        if self.supersayajind == True:
            self.jugadorimagen = pygame.image.load("ssd/fase4.png")
            self.jugadorimagen.set_colorkey(BLANCO)
            self.rect = self.jugadorimagen.get_rect()
        if self.supersayajinb == True:
            self.jugadorimagen = pygame.image.load("ssb/fase4.png")
            self.jugadorimagen.set_colorkey(SSBCOLOR)
            self.rect = self.jugadorimagen.get_rect()
        if self.supersayajinbk == True:
            self.jugadorimagen = pygame.image.load("ssbk/fase4.png")
            self.jugadorimagen.set_colorkey(SSBCOLOR)
            self.rect = self.jugadorimagen.get_rect()
        if self.supersayajinu == True:
            self.jugadorimagen = pygame.image.load("ssu/fase4.png")
            self.jugadorimagen.set_colorkey(SSBCOLOR)
            self.rect = self.jugadorimagen.get_rect()
        if self.supersayajinuc == True:
            self.jugadorimagen = pygame.image.load("ssuc/fase4.png")
            self.jugadorimagen.set_colorkey(SSBCOLOR)
            self.rect = self.jugadorimagen.get_rect()
        # Position and direction
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direccion = "RIGHT"
        # acciones
        self.salto = False
        self.correr = False
        self.move_frame = 0
        # kaioken
        self.kaioken_carga_energia = False
        self.carga_kaioken = False
        self.atakekaioken = False
        self.atake2kaioken = False
        self.atake3kaioken = False
        self.kaioken_energia_frame = 0
        self.kaioken_frame = 0
        self.puño_kaioken_frame = 0
        self.patada_kaioken_frame = 0
        self.kame_kaioken_frame = 0
        # super sayajin
        self.sayajin_frame = 0
        self.carga_sayajin = False
        self.puño_sayajin_frame = 0
        self.atakesayajin = False
        self.patada_sayajin_frame = 0
        self.atake2sayajin = False
        self.kame_sayajin_frame = 0
        self.atake3sayajin = False
        self.sayajin_energia_frame = 0
        self.sayajin_carga_energia = False
        # super sayajin2
        self.sayajin1_frame = 0
        self.carga_sayajin1 = False
        self.puño_sayajin1_frame = 0
        self.atakesayajin1 = False
        self.patada_sayajin1_frame = 0
        self.atake2sayajin1 = False
        self.kame_sayajin1_frame = 0
        self.atake3sayajin1 = False
        self.sayajin1_energia_frame = 0
        self.sayajin1_carga_energia = False
        # super sayajin3
        self.sayajin3_frame = 0
        self.carga_sayajin3 = False
        self.puño_sayajin3_frame = 0
        self.atakesayajin3 = False
        self.patada_sayajin3_frame = 0
        self.atake2sayajin3 = False
        self.kame_sayajin3_frame = 0
        self.atake3sayajin3 = False
        self.sayajin3_energia_frame = 0
        self.sayajin3_carga_energia = False
        # super sayajin4
        self.sayajin4_frame = 0
        self.carga_sayajin4 = False
        self.puño_sayajin4_frame = 0
        self.atakesayajin4 = False
        self.patada_sayajin4_frame = 0
        self.atake2sayajin4 = False
        self.kame_sayajin4_frame = 0
        self.atake3sayajin4 = False
        self.sayajin4_energia_frame = 0
        self.sayajin4_carga_energia = False
        # super sayajin dios
        self.sayajind_frame = 0
        self.carga_sayajind = False
        self.puño_sayajind_frame = 0
        self.atakesayajind = False
        self.patada_sayajind_frame = 0
        self.atake2sayajind = False
        self.kame_sayajind_frame = 0
        self.atake3sayajind = False
        self.sayajind_energia_frame = 0
        self.sayajind_carga_energia = False
        # super sayajin blue
        self.sayajinb_frame = 0
        self.carga_sayajinb = False
        self.puño_sayajinb_frame = 0
        self.atakesayajinb = False
        self.patada_sayajinb_frame = 0
        self.atake2sayajinb = False
        self.kame_sayajinb_frame = 0
        self.atake3sayajinb = False
        self.sayajinb_energia_frame = 0
        self.sayajinb_carga_energia = False
        # super sayajin blue kaioken
        self.sayajinbk_frame = 0
        self.carga_sayajinbk = False
        self.puño_sayajinbk_frame = 0
        self.atakesayajinbk = False
        self.patada_sayajinbk_frame = 0
        self.atake2sayajinbk = False
        self.kame_sayajinbk_frame = 0
        self.atake3sayajinbk = False
        self.sayajinbk_energia_frame = 0
        self.sayajinbk_carga_energia = False
        # ultra instinto
        self.sayajinu_frame = 0
        self.carga_sayajinu = False
        self.puño_sayajinu_frame = 0
        self.atakesayajinu = False
        self.patada_sayajinu_frame = 0
        self.atake2sayajinu = False
        self.kame_sayajinu_frame = 0
        self.atake3sayajinu = False
        self.sayajinu_energia_frame = 0
        self.sayajinu_carga_energia = False
        # ultra instinto completo
        self.sayajinuc_frame = 0
        self.carga_sayajinuc = False
        self.puño_sayajinuc_frame = 0
        self.atakesayajinuc = False
        self.patada_sayajinuc_frame = 0
        self.atake2sayajinuc = False
        self.kame_sayajinuc_frame = 0
        self.atake3sayajinuc = False
        self.sayajinuc_energia_frame = 0
        self.sayajinuc_carga_energia = False
        # Combat
        self.nivel = 92
        self.inmune = False
        self.special = False
        self.magic_cooldown = 1
        self.atake = False
        self.atake2 = False
        self.atake3 = False
        self.atake4 = False
        self.atake5 = False
        self.atake_kame = False
        self.atake_genki = False
        self.carga_energia = False
        self.energia_frame = 0
        self.atake_frame = 0
        self.atake2_frame = 0
        self.atake3_frame = 0
        self.atake4_frame = 0
        self.atake5_frame = 0
        self.kame_frame = 0
        self.genki_frame = 0

        self.energia = 10
        self.experiencia = 0
        self.cooldown = 0
        self.vida = 15

    def movimiento(self):
        # FUERZA DE GRAVEDAD
        if Grav:
            self.acc = vec(0, 0.5)
        else:
            self.acc = vec(0, 0)
        # Will set running to False if the player has slowed down to a certain extent
        if abs(self.vel.x) > 0.3:
            self.correr = True
        else:
            self.correr = False

        # Returns the current key presses
        pressed_keys = pygame.key.get_pressed()

        # Accelerates the player in the direction of the key press
        if pressed_keys[K_a]:
            self.acc.x = -ACC
        if pressed_keys[K_d]:
            self.acc.x = ACC
        if Grav == False:
            if pressed_keys[K_w]:
                self.acc.y = -ACC
            if pressed_keys[K_s]:
                self.acc.y = ACC
        # Formulas to calculate velocity while accounting for friction
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc  # Updates Position with new values
        # This causes character warping from one point of the screen to the other
        if self.pos.x > ancho:
            self.pos.x = ancho
        if self.pos.x < 0:
            self.pos.x = 0
        self.rect.midbottom = self.pos
        # This causes character warping from one point of the screen to the other
        if self.pos.y > alto:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = alto

    def gravedad(self):
        hits = pygame.sprite.spritecollide(jugador, suelo_grupo, False)
        if self.vel.y > 0:
            if hits:
                lowest = hits[0]
                if self.pos.y < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel.y = 0
                    self.salto = False

    def Jugador_hit(self):
        if self.cooldown == False:
            self.cooldown = True  # Enable the cooldown
            pygame.time.set_timer(hit_cooldown, 1000)  # Resets cooldown in 1 second
            if enemy.vidaenemigo >= 1:  # creamos este if para que cuando muera el enemigo no nos baje la vida sola
                self.vida = self.vida - 1


            if self.vida <= 0:
                self.kill()
                pygame.display.update()

    def update(self):

        # Return to base frame if at end of movement sequence
        if self.move_frame > 27:
            self.move_frame = 0
            return
        # Move the character to the next frame if conditions are met
        if self.salto == False and self.correr == True:
            if self.vel.x > 0:
                self.jugadorimagen = correr_der[self.move_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
                if self.kaioken == True:
                    self.jugadorimagen = pygame.image.load("gokukaioken/kaiokenvolando.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin == True:
                    self.jugadorimagen = pygame.image.load("gokuss/volar.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin1 == True:
                    self.jugadorimagen = pygame.image.load("gokussf1/gokuvolando.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin3 == True:
                    self.jugadorimagen = pygame.image.load("gokuss3/volartras.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin4 == True:
                    self.jugadorimagen = pygame.image.load("ss4/volar.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajind == True:
                    self.jugadorimagen = pygame.image.load("ssd/volar.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinb == True:
                    self.jugadorimagen = pygame.image.load("ssb/volar.png")
                    self.jugadorimagen.set_colorkey(SSBCOLOR)
                if self.supersayajinbk == True:
                    self.jugadorimagen = pygame.image.load("ssbk/volar.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinu == True:
                    self.jugadorimagen = pygame.image.load("ssu/volartras.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinuc == True:
                    self.jugadorimagen = pygame.image.load("ssuc/volartras.png")
                    self.jugadorimagen.set_colorkey(VERDE)
                self.direccion = "RIGHT"

            else:
                self.jugadorimagen = correr_izq[self.move_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
                if self.kaioken == True:
                    self.jugadorimagen = pygame.image.load("gokukaioken/kaiokenvolandoizk.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin == True:
                    self.jugadorimagen = pygame.image.load("gokuss/volarizk.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin1 == True:
                    self.jugadorimagen = pygame.image.load("gokussf1/gokuvolandoizk.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin3 == True:
                    self.jugadorimagen = pygame.image.load("gokuss3/volarizk.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin4 == True:
                    self.jugadorimagen = pygame.image.load("ss4/volarizk.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajind == True:
                    self.jugadorimagen = pygame.image.load("ssd/volarizk.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinb == True:
                    self.jugadorimagen = pygame.image.load("ssb/volarizk.png")
                    self.jugadorimagen.set_colorkey(SSBCOLOR)
                if self.supersayajinbk == True:
                    self.jugadorimagen = pygame.image.load("ssbk/volarizk.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinu == True:
                    self.jugadorimagen = pygame.image.load("ssu/volarizk.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinuc == True:
                    self.jugadorimagen = pygame.image.load("ssuc/volarizk.png")
                    self.jugadorimagen.set_colorkey(VERDE)
                self.direccion = "LEFT"

            self.move_frame += 1
            # Returns to base frame if standing still and incorrect frame is showing
        if abs(self.vel.x) < 0.2 and self.move_frame != 0:
            self.move_frame = 0
            if self.direccion == "RIGHT":
                self.jugadorimagen = correr_der[self.move_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
                if self.kaioken == True:
                    self.jugadorimagen = pygame.image.load("gokukaioken/kaiokenparado.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin == True:
                    self.jugadorimagen = pygame.image.load("gokuss/ss5tras.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin1 == True:
                    self.jugadorimagen = pygame.image.load("gokussf1/gokussf1parado.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin3 == True:
                    self.jugadorimagen = pygame.image.load("gokuss3/fase4tras.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin4 == True:
                    self.jugadorimagen = pygame.image.load("ss4/fase4.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajind == True:
                    self.jugadorimagen = pygame.image.load("ssd/fase4.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinb == True:
                    self.jugadorimagen = pygame.image.load("ssb/fase4.png")
                    self.jugadorimagen.set_colorkey(SSBCOLOR)
                if self.supersayajinbk == True:
                    self.jugadorimagen = pygame.image.load("ssbk/fase9.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinu == True:
                    self.jugadorimagen = pygame.image.load("ssu/fase7tras.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinuc == True:
                    self.jugadorimagen = pygame.image.load("ssuc/fase9tras.png")
                    self.jugadorimagen.set_colorkey(VERDE)
            elif self.direccion == "LEFT":
                self.jugadorimagen = correr_izq[self.move_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
                if self.kaioken == True:
                    self.jugadorimagen = pygame.image.load("gokukaioken/kaiokenparadoizk.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin == True:
                    self.jugadorimagen = pygame.image.load("gokuss/ssizk5.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin1 == True:
                    self.jugadorimagen = pygame.image.load("gokussf1/gokussf1paradoizk.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin3 == True:
                    self.jugadorimagen = pygame.image.load("gokuss3/fase4izk.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin4 == True:
                    self.jugadorimagen = pygame.image.load("ss4/faseizk4.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajind == True:
                    self.jugadorimagen = pygame.image.load("ssd/faseizk4.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinb == True:
                    self.jugadorimagen = pygame.image.load("ssb/faseizk4.png")
                    self.jugadorimagen.set_colorkey(SSBCOLOR)
                if self.supersayajinbk == True:
                    self.jugadorimagen = pygame.image.load("ssbk/faseizk9.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinu == True:
                    self.jugadorimagen = pygame.image.load("ssu/faseizk7.png")
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinuc == True:
                    self.jugadorimagen = pygame.image.load("ssuc/faseizk9.png")
                    self.jugadorimagen.set_colorkey(VERDE)


    def cargasupersayajin(self):
        if self.sayajin_frame > 26:
            self.sayajin_frame = 0
            self.carga_sayajin = False
        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = sayajin_r[self.sayajin_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
        elif self.direccion == "LEFT":
            self.jugadorimagen = sayajin_l[self.sayajin_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            # Update the current attack frame
        self.sayajin_frame += 1

    def cargasupersayajinuc(self):
        if self.sayajinuc_frame > 71:
            self.sayajinuc_frame = 0
            self.carga_sayajinuc = False
        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = sayajinuc_r[self.sayajinuc_frame].convert()
            self.jugadorimagen.set_colorkey(VERDE)
        elif self.direccion == "LEFT":
            self.jugadorimagen = sayajinuc_l[self.sayajinuc_frame].convert()
            self.jugadorimagen.set_colorkey(VERDE)
            # Update the current attack frame
        self.sayajinuc_frame += 1

    def cargasupersayajinu(self):
        if self.sayajinu_frame > 71:
            self.sayajinu_frame = 0
            self.carga_sayajinu = False
        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = sayajinu_r[self.sayajinu_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
        elif self.direccion == "LEFT":
            self.jugadorimagen = sayajinu_l[self.sayajinu_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            # Update the current attack frame
        self.sayajinu_frame += 1

    def cargasupersayajinbk(self):
        if self.sayajinbk_frame > 53:
            self.sayajinbk_frame = 0
            self.carga_sayajinbk = False
        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = sayajinbk_r[self.sayajinbk_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
        elif self.direccion == "LEFT":
            self.jugadorimagen = sayajinbk_l[self.sayajinbk_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            # Update the current attack frame
        self.sayajinbk_frame += 1

    def cargasupersayajind(self):
        if self.sayajind_frame > 17:
            self.sayajind_frame = 0
            self.carga_sayajind = False
        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = sayajind_r[self.sayajind_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
        elif self.direccion == "LEFT":
            self.jugadorimagen = sayajind_l[self.sayajind_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            # Update the current attack frame
        self.sayajind_frame += 1

    def cargasupersayajinb(self):
        if self.sayajinb_frame > 17:
            self.sayajinb_frame = 0
            self.carga_sayajinb = False
        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = sayajinb_r[self.sayajinb_frame].convert()
            self.jugadorimagen.set_colorkey(SSBCOLOR)

        elif self.direccion == "LEFT":
            self.jugadorimagen = sayajinb_l[self.sayajinb_frame].convert()
            self.jugadorimagen.set_colorkey(SSBCOLOR)
            # Update the current attack frame
        self.sayajinb_frame += 1

    def cargasupersayajin4(self):
        if self.sayajin4_frame > 17:
            self.sayajin4_frame = 0
            self.carga_sayajin4 = False
        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = sayajin4_r[self.sayajin4_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            self.pos.y = 280
        elif self.direccion == "LEFT":
            self.jugadorimagen = sayajin4_l[self.sayajin4_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            # Update the current attack frame
        self.sayajin4_frame += 1

    def cargasupersayajin3(self):
        if self.sayajin3_frame > 17:
            self.sayajin3_frame = 0
            self.carga_sayajin3 = False
        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = sayajin3_r[self.sayajin3_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
        elif self.direccion == "LEFT":
            self.jugadorimagen = sayajin3_l[self.sayajin3_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            # Update the current attack frame
        self.sayajin3_frame += 1

    def cargasupersayajin1(self):
        if self.sayajin1_frame > 17:
            self.sayajin1_frame = 0
            self.carga_sayajin1 = False
        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = sayajin1_r[self.sayajin1_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
        elif self.direccion == "LEFT":
            self.jugadorimagen = sayajin1_l[self.sayajin1_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            # Update the current attack frame
        self.sayajin1_frame += 1

    def cargakaioken(self):
        if self.kaioken_frame > 44:
            self.kaioken_frame = 0
            self.carga_kaioken = False
        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = kaioken_r[self.kaioken_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
        elif self.direccion == "LEFT":
            self.jugadorimagen = kaioken_l[self.kaioken_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            # Update the current attack frame
        self.kaioken_frame += 1

    def cargaenergia(self):
        if self.energia_frame > 20:
            self.energia_frame = 0
            self.carga_energia = False
        if self.kaioken_energia_frame > 17:
            self.kaioken_energia_frame = 0
            self.kaioken_carga_energia = False
        if self.sayajin_energia_frame > 11:
            self.sayajin_energia_frame = 0
            self.sayajin_carga_energia = False
        if self.sayajin1_energia_frame > 11:
            self.sayajin1_energia_frame = 0
            self.sayajin1_carga_energia = False
        if self.sayajin3_energia_frame > 11:
            self.sayajin3_energia_frame = 0
            self.sayajin3_carga_energia = False
        if self.sayajin4_energia_frame > 11:
            self.sayajin4_energia_frame = 0
            self.sayajin4_carga_energia = False
            self.pos.y = 260
        if self.sayajind_energia_frame > 11:
            self.sayajind_energia_frame = 0
            self.sayajind_carga_energia = False
        if self.sayajinb_energia_frame > 11:
            self.sayajinb_energia_frame = 0
            self.sayajinb_carga_energia = False
        if self.sayajinbk_energia_frame > 11:
            self.sayajinbk_energia_frame = 0
            self.sayajinbk_carga_energia = False
        if self.sayajinu_energia_frame > 11:
            self.sayajinu_energia_frame = 0
            self.sayajinu_carga_energia = False
        if self.sayajinuc_energia_frame > 11:
            self.sayajinuc_energia_frame = 0
            self.sayajinuc_carga_energia = False
        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = carga_r[self.energia_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            if self.kaioken == True:
                self.jugadorimagen = kaioken_energia_r[self.kaioken_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin == True:
                self.jugadorimagen = sayajin_carga_energia_r[self.sayajin_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin1 == True:
                self.jugadorimagen = sayajin1_carga_energia_r[self.sayajin1_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin3 == True:
                self.jugadorimagen = sayajin3_carga_energia_r[self.sayajin3_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin4 == True:
                self.jugadorimagen = sayajin4_carga_energia_r[self.sayajin4_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
                self.pos.y = 260
            if self.supersayajind == True:
                self.jugadorimagen = sayajind_carga_energia_r[self.sayajind_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinb == True:
                self.jugadorimagen = sayajinb_carga_energia_r[self.sayajinb_energia_frame].convert()
                self.jugadorimagen.set_colorkey(SSBCOLOR)
            if self.supersayajinbk == True:
                self.jugadorimagen = sayajinbk_carga_energia_r[self.sayajinbk_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinu == True:
                self.jugadorimagen = sayajinu_carga_energia_r[self.sayajinu_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinuc == True:
                self.jugadorimagen = sayajinuc_carga_energia_r[self.sayajinuc_energia_frame].convert()
                self.jugadorimagen.set_colorkey(VERDE)

            if self.energia < 10:
                self.energia += 0.01

        elif self.direccion == "LEFT":
            self.jugadorimagen = carga_l[self.energia_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            if self.kaioken == True:
                self.jugadorimagen = kaioken_energia_r[self.kaioken_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin == True:
                self.jugadorimagen = sayajin_carga_energia_r[self.sayajin_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin1 == True:
                self.jugadorimagen = sayajin1_carga_energia_l[self.sayajin1_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin3 == True:
                self.jugadorimagen = sayajin3_carga_energia_l[self.sayajin3_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin4 == True:
                self.jugadorimagen = sayajin4_carga_energia_l[self.sayajin4_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajind == True:
                self.jugadorimagen = sayajind_carga_energia_l[self.sayajind_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinb == True:
                self.jugadorimagen = sayajinb_carga_energia_l[self.sayajinb_energia_frame].convert()
                self.jugadorimagen.set_colorkey(SSBCOLOR)
            if self.supersayajinbk == True:
                self.jugadorimagen = sayajinbk_carga_energia_l[self.sayajinbk_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinu == True:
                self.jugadorimagen = sayajinu_carga_energia_l[self.sayajinu_energia_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinuc == True:
                self.jugadorimagen = sayajinuc_carga_energia_l[self.sayajinuc_energia_frame].convert()
                self.jugadorimagen.set_colorkey(VERDE)
            if self.energia < 10:
                self.energia += 0.01
            # Update the current attack frame
        self.energia_frame += 1
        self.kaioken_energia_frame += 1
        self.sayajin_energia_frame += 1
        self.sayajin1_energia_frame += 1
        self.sayajin3_energia_frame += 1
        self.sayajin4_energia_frame += 1
        self.sayajind_energia_frame += 1
        self.sayajinb_energia_frame += 1
        self.sayajinbk_energia_frame += 1
        self.sayajinu_energia_frame += 1
        self.sayajinuc_energia_frame += 1

    def attack(self):
        # If attack frame has reached end of sequence, return to base frame
        if self.atake_frame > 31:
            self.atake_frame = 0
            self.atake = False
        if self.puño_kaioken_frame > 17:
            self.puño_kaioken_frame = 0
            self.atakekaioken = False
        if self.puño_sayajin_frame > 17:
            self.puño_sayajin_frame = 0
            self.atakesayajin = False
        if self.puño_sayajin1_frame > 25:
            self.puño_sayajin1_frame = 0
            self.atakesayajin1 = False
        if self.puño_sayajin3_frame > 17:
            self.puño_sayajin3_frame = 0
            self.atakesayajin3 = False
        if self.puño_sayajin4_frame > 17:
            self.puño_sayajin4_frame = 0
            self.atakesayajin4 = False
        if self.puño_sayajind_frame > 17:
            self.puño_sayajind_frame = 0
            self.atakesayajind = False
        if self.puño_sayajinb_frame > 17:
            self.puño_sayajinb_frame = 0
            self.atakesayajinb = False
        if self.puño_sayajinbk_frame > 15:
            self.puño_sayajinbk_frame = 0
            self.atakesayajinbk = False
        if self.puño_sayajinu_frame > 17:
            self.puño_sayajinu_frame = 0
            self.atakesayajinu = False
        if self.puño_sayajinuc_frame > 71:
            self.puño_sayajinuc_frame = 0
            self.atakesayajinuc = False

        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = atake_der[self.atake_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            if self.kaioken == True:
                self.jugadorimagen = puño_kaioken_r[self.puño_kaioken_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin == True:
                self.jugadorimagen = sayajin_puño_r[self.puño_sayajin_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin1 == True:
                self.jugadorimagen = sayajin1_puño_r[self.puño_sayajin1_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin3 == True:
                self.jugadorimagen = sayajin3_puño_r[self.puño_sayajin3_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin4 == True:
                self.jugadorimagen = sayajin4_puño_r[self.puño_sayajin4_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajind == True:
                self.jugadorimagen = sayajind_puño_r[self.puño_sayajind_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinb == True:
                self.jugadorimagen = sayajinb_puño_r[self.puño_sayajinb_frame].convert()
                self.jugadorimagen.set_colorkey(SSBCOLOR)
            if self.supersayajinbk == True:
                self.jugadorimagen = sayajinbk_puño_r[self.puño_sayajinbk_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinu == True:
                self.jugadorimagen = sayajinu_puño_r[self.puño_sayajinu_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinuc == True:
                self.jugadorimagen = sayajinuc_puño_r[self.puño_sayajinuc_frame].convert()
                self.jugadorimagen.set_colorkey(VERDE)

        elif self.direccion == "LEFT":
            self.correccion()
            self.jugadorimagen = atake_izq[self.atake_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            if self.kaioken == True:
                self.jugadorimagen = puño_kaioken_l[self.puño_kaioken_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin == True:
                self.jugadorimagen = sayajin_puño_l[self.puño_sayajin_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin1 == True:
                self.jugadorimagen = sayajin1_puño_l[self.puño_sayajin1_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin3 == True:
                self.jugadorimagen = sayajin3_puño_l[self.puño_sayajin3_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin4 == True:
                self.jugadorimagen = sayajin4_puño_l[self.puño_sayajin4_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajind == True:
                self.jugadorimagen = sayajind_puño_l[self.puño_sayajind_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinb == True:
                self.jugadorimagen = sayajinb_puño_l[self.puño_sayajinb_frame].convert()
                self.jugadorimagen.set_colorkey(SSBCOLOR)
            if self.supersayajinbk == True:
                self.jugadorimagen = sayajinbk_puño_l[self.puño_sayajinbk_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinu == True:
                self.jugadorimagen = sayajinu_puño_l[self.puño_sayajinu_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinuc == True:
                self.jugadorimagen = sayajinuc_puño_l[self.puño_sayajinuc_frame].convert()
                self.jugadorimagen.set_colorkey(VERDE)

            # Update the current attack frame
        self.atake_frame += 1
        self.puño_kaioken_frame += 1
        self.puño_sayajin_frame += 1
        self.puño_sayajin1_frame += 1
        self.puño_sayajin3_frame += 1
        self.puño_sayajin4_frame += 1
        self.puño_sayajind_frame += 1
        self.puño_sayajinb_frame += 1
        self.puño_sayajinbk_frame += 1
        self.puño_sayajinu_frame += 1
        self.puño_sayajinuc_frame += 1

    def attack2(self):
        # If attack frame has reached end of sequence, return to base frame
        if self.atake2_frame > 27:
            self.atake2_frame = 0
            self.atake2 = False
        if self.patada_kaioken_frame > 16:
            self.patada_kaioken_frame = 0
            self.atake2kaioken = False
        if self.patada_sayajin_frame > 14:
            self.patada_sayajin_frame = 0
            self.atake2sayajin = False
        if self.patada_sayajin1_frame > 19:
            self.patada_sayajin1_frame = 0
            self.atake2sayajin1 = False
        if self.patada_sayajin3_frame > 14:
            self.patada_sayajin3_frame = 0
            self.atake2sayajin3 = False
        if self.patada_sayajin4_frame > 14:
            self.patada_sayajin4_frame = 0
            self.atake2sayajin4 = False
        if self.patada_sayajind_frame > 14:
            self.patada_sayajind_frame = 0
            self.atake2sayajind = False
        if self.patada_sayajinb_frame > 14:
            self.patada_sayajinb_frame = 0
            self.atake2sayajinb = False
        if self.patada_sayajinbk_frame > 47:
            self.patada_sayajinbk_frame = 0
            self.atake2sayajinbk = False
        if self.patada_sayajinu_frame > 59:
            self.patada_sayajinu_frame = 0
            self.atake2sayajinu = False
        if self.patada_sayajinuc_frame > 39:
            self.patada_sayajinuc_frame = 0
            self.atake2sayajinuc = False

        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = patada_der[self.atake2_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            if self.kaioken == True:
                self.jugadorimagen = patada_kaioken_r[self.patada_kaioken_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin == True:
                self.jugadorimagen = sayajin_patada_r[self.patada_sayajin_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin1 == True:
                self.jugadorimagen = sayajin1_patada_r[self.patada_sayajin1_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin3 == True:
                self.jugadorimagen = sayajin3_patada_r[self.patada_sayajin3_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin4 == True:
                self.jugadorimagen = sayajin4_patada_r[self.patada_sayajin4_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajind == True:
                self.jugadorimagen = sayajind_patada_r[self.patada_sayajind_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinb == True:
                self.jugadorimagen = sayajinb_patada_r[self.patada_sayajinb_frame].convert()
                self.jugadorimagen.set_colorkey(SSBCOLOR)
            if self.supersayajinbk == True:
                self.jugadorimagen = sayajinbk_patada_r[self.patada_sayajinbk_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinu == True:
                self.jugadorimagen = sayajinu_patada_r[self.patada_sayajinu_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinuc == True:
                self.jugadorimagen = sayajinuc_patada_r[self.patada_sayajinuc_frame].convert()
                self.jugadorimagen.set_colorkey(VERDE)

        elif self.direccion == "LEFT":
            self.correccion2()
            self.jugadorimagen = patada_izq[self.atake2_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            if self.kaioken == True:
                self.jugadorimagen = patada_kaioken_l[self.patada_kaioken_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin == True:
                self.jugadorimagen = sayajin_patada_l[self.patada_sayajin_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin1 == True:
                self.jugadorimagen = sayajin1_patada_l[self.patada_sayajin1_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin3 == True:
                self.jugadorimagen = sayajin3_patada_l[self.patada_sayajin3_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin4 == True:
                self.jugadorimagen = sayajin4_patada_l[self.patada_sayajin4_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajind == True:
                self.jugadorimagen = sayajind_patada_l[self.patada_sayajind_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinb == True:
                self.jugadorimagen = sayajinb_patada_l[self.patada_sayajinb_frame].convert()
                self.jugadorimagen.set_colorkey(SSBCOLOR)
            if self.supersayajinbk == True:
                self.jugadorimagen = sayajinbk_patada_l[self.patada_sayajinbk_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinu == True:
                self.jugadorimagen = sayajinu_patada_l[self.patada_sayajinu_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinuc == True:
                self.jugadorimagen = sayajinuc_patada_l[self.patada_sayajinuc_frame].convert()
                self.jugadorimagen.set_colorkey(VERDE)
            # Update the current attack frame
        self.atake2_frame += 1
        self.patada_kaioken_frame += 1
        self.patada_sayajin_frame += 1
        self.patada_sayajin1_frame += 1
        self.patada_sayajin3_frame += 1
        self.patada_sayajin4_frame += 1
        self.patada_sayajind_frame += 1
        self.patada_sayajinb_frame += 1
        self.patada_sayajinbk_frame += 1
        self.patada_sayajinu_frame += 1
        self.patada_sayajinuc_frame += 1

    def attack3(self):
        if enemy.vidaenemigo <= 1:
            # If attack frame has reached end of sequence, return to base frame
            if self.atake3_frame > 32:
                self.atake3_frame = 0
                self.atake3 = False
            if self.kame_kaioken_frame > 16:
                self.kame_kaioken_frame = 0
                self.atake3kaioken = False
            if self.kame_sayajin_frame > 17:
                self.kame_sayajin_frame = 0
                self.atake3sayajin = False
            if self.kame_sayajin1_frame > 25:
                self.kame_sayajin1_frame = 0
                self.atake3sayajin1 = False
            if self.kame_sayajin3_frame > 25:
                self.kame_sayajin3_frame = 0
                self.atake3sayajin3 = False
            if self.kame_sayajin4_frame > 25:
                self.kame_sayajin4_frame = 0
                self.atake3sayajin4 = False
            if self.kame_sayajind_frame > 25:
                self.kame_sayajind_frame = 0
                self.atake3sayajind = False
            if self.kame_sayajinb_frame > 25:
                self.kame_sayajinb_frame = 0
                self.atake3sayajinb = False
            if self.kame_sayajinbk_frame > 25:
                self.kame_sayajinbk_frame = 0
                self.atake3sayajinbk = False
            if self.kame_sayajinu_frame > 25:
                self.kame_sayajinu_frame = 0
                self.atake3sayajinu = False
            if self.kame_sayajinuc_frame > 25:
                self.kame_sayajinuc_frame = 0
                self.atake3sayajinuc = False

            # Check direction for correct animation to display
            if self.direccion == "RIGHT":
                self.jugadorimagen = attack_kame_R[self.atake3_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
                if self.kaioken == True:
                    self.jugadorimagen = kame_kaioken_r[self.kame_kaioken_frame].convert()
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin == True:
                    self.jugadorimagen = sayajin_kame[self.kame_sayajin_frame].convert()
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin1 == True:
                    self.jugadorimagen = sayajin1_kame[self.kame_sayajin1_frame].convert()
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin3 == True:
                    self.jugadorimagen = sayajin3_kame[self.kame_sayajin3_frame].convert()
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajin4 == True:
                    self.jugadorimagen = sayajin4_kame[self.kame_sayajin4_frame].convert()
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajind == True:
                    self.jugadorimagen = sayajind_kame[self.kame_sayajind_frame].convert()
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinb == True:
                    self.jugadorimagen = sayajinb_kame[self.kame_sayajinb_frame].convert()
                    self.jugadorimagen.set_colorkey(SSBCOLOR)
                if self.supersayajinbk == True:
                    self.jugadorimagen = sayajinbk_kame[self.kame_sayajinbk_frame].convert()
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinu == True:
                    self.jugadorimagen = sayajinu_kame[self.kame_sayajinu_frame].convert()
                    self.jugadorimagen.set_colorkey(BLANCO)
                if self.supersayajinuc == True:
                    self.jugadorimagen = sayajinuc_kame[self.kame_sayajinuc_frame].convert()
                    self.jugadorimagen.set_colorkey(VERDE)

            elif self.direccion == "LEFT":
                self.correccion2()
                self.jugadorimagen = attack_kame_L[self.atake3_frame].convert()
                if self.kaioken == True:
                    self.jugadorimagen = sayajin1_kame[self.kame_sayajin1_frame].convert()
                self.jugadorimagen.set_colorkey(BLANCO)
                # Update the current attack frame
            self.atake3_frame += 1
            self.kame_kaioken_frame += 1
            self.kame_sayajin_frame += 1
            self.kame_sayajin1_frame += 1
            self.kame_sayajin3_frame += 1
            self.kame_sayajin4_frame += 1
            self.kame_sayajind_frame += 1
            self.kame_sayajinb_frame += 1
            self.kame_sayajinbk_frame += 1
            self.kame_sayajinu_frame += 1
            self.kame_sayajinuc_frame += 1

    def attack4(self):
        # If attack frame has reached end of sequence, return to base frame
        if self.atake4_frame > 10:
            self.atake4_frame = 0
            self.atake4 = False

        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = attack_genki_r[self.atake4_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
        elif self.direccion == "LEFT":
            self.correccion2()
            self.jugadorimagen = attack_genki_l[self.atake4_frame].convert()
            self.jugadorimagen.set_colorkey(BLANCO)
            # Update the current attack frame
        self.atake4_frame += 1

    def attack5(self):
        # If attack frame has reached end of sequence, return to base frame
        self.atake5 = False
        # Check direction for correct animation to display
        if self.direccion == "RIGHT":
            self.jugadorimagen = pygame.image.load("gokuatakes/gokufire.png")
            self.jugadorimagen.set_colorkey(BLANCO)
            if self.kaioken == True:
                self.jugadorimagen = pygame.image.load("gokukaioken/kaiokenfire.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin == True:
                self.jugadorimagen = pygame.image.load("gokuss/firetras.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin1 == True:
                self.jugadorimagen = pygame.image.load("gokussf1/ssf1fire.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin3 == True:
                self.jugadorimagen = pygame.image.load("gokuss3/firetras.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin4 == True:
                self.jugadorimagen = pygame.image.load("ss4/fire.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajind == True:
                self.jugadorimagen = pygame.image.load("ssd/fire.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinb == True:
                self.jugadorimagen = pygame.image.load("ssb/fire.png")
                self.jugadorimagen.set_colorkey(SSBCOLOR)
            if self.supersayajinbk == True:
                self.jugadorimagen = pygame.image.load("ssbk/fire.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinu == True:
                self.jugadorimagen = pygame.image.load("ssu/firetras.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinuc == True:
                self.jugadorimagen = pygame.image.load("ssuc/firetras.png")
                self.jugadorimagen.set_colorkey(VERDE)

        elif self.direccion == "LEFT":
            self.correccion2()
            self.jugadorimagen = pygame.image.load("gokuatakes/gokufireizk.png")
            self.jugadorimagen.set_colorkey(BLANCO)
            if self.kaioken == True:
                self.jugadorimagen = pygame.image.load("gokukaioken/kaiokenfireizk.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin == True:
                self.jugadorimagen = pygame.image.load("gokuss/fireizk.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin1 == True:
                self.jugadorimagen = pygame.image.load("gokussf1/ssf1fireizk.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin3 == True:
                self.jugadorimagen = pygame.image.load("gokuss3/fireizk.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajin4 == True:
                self.jugadorimagen = pygame.image.load("ss4/fireizk.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajind == True:
                self.jugadorimagen = pygame.image.load("ssd/fireizk.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinb == True:
                self.jugadorimagen = pygame.image.load("ssb/fireizk.png")
                self.jugadorimagen.set_colorkey(SSBCOLOR)
            if self.supersayajinbk == True:
                self.jugadorimagen = pygame.image.load("ssbk/fireizk.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinu == True:
                self.jugadorimagen = pygame.image.load("ssu/fireizk.png")
                self.jugadorimagen.set_colorkey(BLANCO)
            if self.supersayajinuc == True:
                self.jugadorimagen = pygame.image.load("ssuc/fireizk.png")
                self.jugadorimagen.set_colorkey(VERDE)
            # Update the current attack frame

    def correccion(self):
        # Function is used to correct an error
        # with character position on left attack frames
        if self.atake_frame == 1:
            self.pos.x -= 20
        if self.atake_frame == 10:
            self.pos.x += 20

    def correccion2(self):
        # Function is used to correct an error
        # with character position on left attack frames
        if self.atake2_frame == 1:
            self.pos.x -= 20
        if self.atake_frame == 10:
            self.pos.x += 20

    def correccion3(self):
        # Function is used to correct an error
        # with character position on left attack frames
        if self.atake3_frame == 1:
            self.pos.x -= 20
        if self.atake_frame == 10:
            self.pos.x += 20

    def saltar(self):
        self.rect.x += 1
        # Check to see if payer is in contact with the ground
        hits = pygame.sprite.spritecollide(self, suelo_grupo, False)
        self.rect.x -= 1
        # If touching the ground, and not currently jumping, cause the player to jump.
        if hits and not self.salto:
            self.salto = True
            self.vel.y = -12


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("jiren andando/jiren1.png")
        self.rect = self.image.get_rect()
        self.pos = vec((340, 240))
        self.vel = vec(0, 0)
        self.direction = random.randint(0, 1)  # 0 for Right, 1 for Left
        self.vel.x = 2

        # combat
        self.nivel = 10
        self.energia = 10
        self.vidaenemigo = 15
        self.cooldown = False
        self.attack_frame = 0
        self.atake = 0
        self.move_frame = 0
        self.puño_frame = 0
        self.patada_frame = 0
        self.explosion_frame = 0
        self.correr = False

        # Establece la posición inicial del enemigo
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 265
        if self.direction == 1:
            self.pos.x = 700
            self.pos.y = 265




    def move(self):

        # Hace que el enemigo cambie de dirección al llegar al final de la pantalla
        if self.pos.x >= (ancho - 20):
            self.direction = 1
        elif self.pos.x <= 0:
            self.direction = 0
        # Actualiza la posición con nuevos valores
        if self.direction == 0 and self.vidaenemigo > 1:
            self.pos.x += self.vel.x
            self.image = jiren_run_r[self.move_frame]
        if self.direction == 1 and self.vidaenemigo > 1:
            self.pos.x -= self.vel.x
            self.image = jiren_run_l[self.move_frame]
        self.rect.center = self.pos  # Updates rect
        self.move_frame += 1

    def update(self):
        # Regresa al cuadro base si está al final de la secuencia de movimiento
        if self.move_frame > 15:
            self.move_frame = 0
            return

        if self.vidaenemigo == 1:
            self.image = pygame.image.load("jiren andando/jirencansado.png")

        # Checks for collision with the Player
        hits = pygame.sprite.spritecollide(self, Jugadorgrupo, False)
        # Checks for collision with Fireballs
        f_hits = pygame.sprite.spritecollide(self, Fireballs, False)
        k_hits = pygame.sprite.spritecollide(self, Kamehamehas, False)
        g_hits = pygame.sprite.spritecollide(self, Genkidamas, False)
        # Activates upon either of the two expressions being true
        if hits and jugador.atake or hits and jugador.atake2 == True or f_hits or k_hits or g_hits:
            if self.cooldown == False:
                self.cooldown = True
                pygame.time.set_timer(hit_cooldown, 1000)
                self.vidaenemigo = self.vidaenemigo - 1

            if self.vidaenemigo <= 0:
                self.kill()
                self.image.set_colorkey(BLANCO)  # si el enemigo muere se queda esta imagen de barra de vida fija
                pygame.display.update()
        # If collision has occured and player not attacking, call "hit" function
        elif hits and jugador.atake or hits and jugador.atake2 == False:
            jugador.Jugador_hit()
            explosion = Explosiones(enemy.rect.center)
            explosiones.add(explosion)

    def render(self):
        # Displayed the enemy on screen
        ventana.blit(self.image, (self.pos.x, self.pos.y))


# instanciando objetos
jugador = Jugador()
Jugadorgrupo = pygame.sprite.Group()
Jugadorgrupo.add(jugador)
enemy = Enemy()
enemigogrupo = pygame.sprite.Group()
enemigogrupo.add(enemy)
explosiones = pygame.sprite.Group()
fondo = FondoPantalla()
suelo = SueloPantalla()
suelo_grupo = pygame.sprite.Group()
suelo_grupo.add(suelo)
Fireballs = pygame.sprite.Group()
Genkidamas = pygame.sprite.Group()
Kamehamehas = pygame.sprite.Group()
status_bar = StatusBar()
status_bar_enemy = StatusBarEnemy()
barraexperiencia = BarraExperiencia()
gameover = GameOver()
winer = Winer()
fotos = Fotos()

# evento
hit_cooldown = pygame.USEREVENT + 1


while 1:
    menu
    jugador.gravedad()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == hit_cooldown:
            jugador.cooldown = False
            pygame.time.set_timer(hit_cooldown, 0)

        if event.type == hit_cooldown:
            enemy.cooldown = False
            pygame.time.set_timer(hit_cooldown, 0)

        # Event handling for a range of different key presses
        if event.type == KEYDOWN:

            if event.key == pygame.K_m and jugador.magic_cooldown == 1:
                    if enemy.vidaenemigo > 1:
                        if jugador.energia >= 0.5:
                            jugador.energia -= 0.5
                            jugador.atake5 = True
                            fireball = FireBall()
                            Fireballs.add(fireball)

            if event.key == pygame.K_q and jugador.magic_cooldown == 1:
                    if enemy.vidaenemigo <= 1:
                        if jugador.energia >= 0.1:
                            jugador.energia -= 0.1
                            jugador.atake3 = True
                            kamehameha = Kamehameha()
                            Kamehamehas.add(kamehameha)

            if event.key == pygame.K_1 and jugador.magic_cooldown == 1:
                    if enemy.vidaenemigo <= 1:
                        if jugador.energia >= 0.1:
                            jugador.energia -= 0.1
                            jugador.atake4 = True
                            genkidama = Genkidama()
                            Genkidamas.add(genkidama)
            if event.key == pygame.K_SPACE:
                    if Grav:
                        jugador.saltar()
            if event.key == pygame.K_RETURN:
                    if jugador.atake == False:
                        jugador.attack()
                        jugador.atake = True
            if event.key == pygame.K_r:
                    if jugador.atake2 == False:
                        jugador.attack2()
                        jugador.atake2 = True

            if event.key == pygame.K_e:
                    if jugador.carga_energia == False:
                        jugador.cargaenergia()
                        jugador.carga_energia = True
            if event.key == pygame.K_t:
                    if jugador.carga_kaioken == False and jugador.nivel >= 10 and jugador.nivel <= 19:
                        jugador.cargakaioken()
                        jugador.carga_kaioken = True
                        jugador.kaioken = True
                    if jugador.carga_sayajin == False and jugador.nivel >= 20 and jugador.nivel <= 29:
                        jugador.cargasupersayajin()
                        jugador.carga_sayajin = True
                        jugador.supersayajin = True
                    if jugador.carga_sayajin1 == False and jugador.nivel >= 30 and jugador.nivel <= 39:
                        jugador.cargasupersayajin1()
                        jugador.carga_sayajin1 = True
                        jugador.supersayajin1 = True
                    if jugador.carga_sayajin3 == False and jugador.nivel >= 40 and jugador.nivel <= 49:
                        jugador.cargasupersayajin3()
                        jugador.carga_sayajin3 = True
                        jugador.supersayajin3 = True
                    if jugador.carga_sayajin4 == False and jugador.nivel >= 50 and jugador.nivel <= 59:
                        jugador.cargasupersayajin4()
                        jugador.carga_sayajin4 = True
                        jugador.supersayajin4 = True
                    if jugador.carga_sayajind == False and jugador.nivel >= 60 and jugador.nivel <= 69:
                        jugador.cargasupersayajind()
                        jugador.carga_sayajind = True
                        jugador.supersayajind = True
                    if jugador.carga_sayajinb == False and jugador.nivel >= 70 and jugador.nivel <= 79:
                        jugador.cargasupersayajinb()
                        jugador.carga_sayajinb = True
                        jugador.supersayajinb = True
                    if jugador.carga_sayajinbk == False and jugador.nivel >= 80 and jugador.nivel <= 89:
                        jugador.cargasupersayajinbk()
                        jugador.carga_sayajinbk = True
                        jugador.supersayajinbk = True
                    if jugador.carga_sayajinu == False and jugador.nivel >= 90 and jugador.nivel <= 99:
                        jugador.cargasupersayajinu()
                        jugador.carga_sayajinu = True
                        jugador.supersayajinu = True
                    if jugador.carga_sayajinuc == False and jugador.nivel >= 100 and jugador.nivel <= 100:
                        jugador.cargasupersayajinuc()
                        jugador.carga_sayajinuc = True
                        jugador.supersayajinuc = True
            if jugador.vida <= 3 or event.key == K_y:
                    jugador.kaioken = False
                    jugador.supersayajin = False
                    jugador.supersayajin1 = False
                    jugador.supersayajin3 = False
                    jugador.supersayajin4 = False
                    jugador.supersayajind = False
                    jugador.supersayajinb = False
                    jugador.supersayajinbk = False
                    jugador.supersayajinu = False
                    jugador.supersayajinuc = False
            if event.key == pygame.K_0:
                    Grav = False
                    salto = False
                    correr = False
            if event.key == pygame.K_9:
                Grav = True
            elif event.key == pygame.K_p:
                pause()

    # actualiza objetos
    fondo.render()
    suelo.render()
    jugador.update()
    enemy.move()
    enemy.update()
    explosiones.update()

    colision_jugador = pygame.sprite.spritecollide(enemy, Jugadorgrupo, False)
    if colision_jugador:
            explosion = Explosiones(jugador.rect.center)
            explosiones.add(explosion)

    colision = pygame.sprite.spritecollide(jugador, enemigogrupo, False)
    if enemy.direction == 0:
            if colision:
                if enemy.puño_frame > 8:
                    enemy.puño_frame = 0
                explosion = Explosiones(enemy.rect.center)
                explosiones.add(explosion)
                enemy.image = jiren_puño[enemy.puño_frame]
                enemy.image.set_colorkey(BLANCO)
                enemy.puño_frame += 1
    else:
            if colision:
                if enemy.patada_frame > 17:
                    enemy.patada_frame = 0
                explosion = Explosiones(enemy.rect.center)
                explosiones.add(explosion)
                enemy.image = jiren_patada[enemy.patada_frame]
                enemy.image.set_colorkey(BLANCO)
                enemy.patada_frame += 1

    colision_fireballs = pygame.sprite.spritecollide(enemy, Fireballs, False)
    if colision_fireballs:
            enemy.image = pygame.image.load("jiren andando/jirencubriendose.png")
            enemy.image.set_colorkey(BLANCO)
            explosion = Explosiones(enemy.rect.center)
            explosiones.add(explosion)
            if enemy.pos.x <= jugador.pos.x:
                enemy.pos.x -= 3
            else:
                enemy.pos.x += 3

    colision_kame = pygame.sprite.spritecollide(enemy, Kamehamehas, False)
    if colision_kame:
            enemy.image = pygame.image.load("jiren andando/jirencubriendose.png")
            enemy.image.set_colorkey(BLANCO)
            explosion = Explosiones(enemy.rect.center)
            explosiones.add(explosion)
            if enemy.pos.x <= jugador.pos.x:
                enemy.pos.x -= 3
            else:
                enemy.pos.x += 3

    if jugador.atake == True:
        jugador.attack()

    if jugador.atake2 == True:
        jugador.attack2()

    if jugador.atake3 == True:
        jugador.attack3()
    if jugador.atake4 == True:
        jugador.attack4()
    if jugador.atake5 == True:
        jugador.attack5()
    if jugador.carga_energia == True:
        jugador.cargaenergia()
    if jugador.carga_kaioken == True:
        jugador.cargakaioken()
    if jugador.carga_sayajin == True:
        jugador.cargasupersayajin()
    if jugador.carga_sayajin1 == True:
        jugador.cargasupersayajin1()
    if jugador.carga_sayajin3 == True:
        jugador.cargasupersayajin3()
    if jugador.carga_sayajin4 == True:
        jugador.cargasupersayajin4()
    if jugador.carga_sayajind == True:
        jugador.cargasupersayajind()
    if jugador.carga_sayajinb == True:
        jugador.cargasupersayajinb()
    if jugador.carga_sayajinbk == True:
        jugador.cargasupersayajinbk()
    if jugador.carga_sayajinu == True:
        jugador.cargasupersayajinu()
    if jugador.carga_sayajinuc == True:
        jugador.cargasupersayajinuc()
    jugador.movimiento()
    if jugador.vida > 0:
        ventana.blit(jugador.jugadorimagen, jugador.rect)


    ventana.blit(enemy.image, enemy.rect)
    fotos.render()
    explosiones.draw(ventana)
    BarrasVidaEnergia()
    barraexperiencia.render()
    if jugador.vida <= 0:
        gameover.render()
    if enemy.vidaenemigo == 1:

        enemy.pos.x = 500
        enemy.pos.y = 265

    # movimiento muerte enemygo y visualizacion de winer
    if enemy.vidaenemigo <= 0:
        winer.render()
    # Status bar update and render
    status_bar.update_draw()
    status_bar_enemy.update_draw()

    for ball in Fireballs:
        ball.fire()
    for kame in Kamehamehas:
        kame.ki()
    for bola in Genkidamas:
        bola.ki()

    pygame.display.update()
    clock.tick(FPS)
