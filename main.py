import random
import sys

import pygame
from Classes import Main_Character, THE_LOBERINT, TungTungsahur_BODY, CAPEBARA_EVIL, PORTALS, GAME_STATS
from datetime import datetime

Start_Time_invinceble = None

def minuse_jizn():
    concretnaya_Capebara(CAPEBARA_DaMexx_77)
    concretnaya_Capebara(CAPEBARA_DaMexx_77_1)
    concretnaya_Capebara(CAPEBARA_DaMexx_77_2)



def concretnaya_Capebara(Capebara):
    global Start_Time_invinceble
    if colision(GLEB_SAHUR, Capebara) and GLEB_SAHUR.invinceble == False:
        Capebara_Stats.Lives -= 1
        Capebara_Stats.textLives = Capebara_Stats.font.render(f"Lives {Capebara_Stats.Lives}", True, (153, 247, 164))
        GLEB_SAHUR.invinceble = True
        Start_Time_invinceble = datetime.now()
    if GLEB_SAHUR.invinceble == True:
        if datetime.now().second - Start_Time_invinceble.second > 3 or datetime.now().min > Start_Time_invinceble.min:
            GLEB_SAHUR.invinceble = False





def PEREHOD_UROVNEI():
    if GLEB_SAHUR.TungTungSaur_BODY == True and colision(GLEB_SAHUR, PORTAL):
        LOBERINT.image = pygame.image.load("LOBERINT_2.png")
        Capebara_Stats.Lvl = 2
        Capebara_Stats.textlvl = Capebara_Stats.font.render(f"Lvl {Capebara_Stats.Lvl}", True, (153, 247, 164))
        GLEB_SAHUR.TungTungSaur_BODY = False
        GLEB_SAHUR.rect.x = 40
        GLEB_SAHUR.rect.y = 2
        GLEB_SAHUR.x = GLEB_SAHUR.rect.x
        GLEB_SAHUR.y = GLEB_SAHUR.rect.y
        TungTungsahur.show = True
        TungTungsahur.rect.x = 30
        TungTungsahur.rect.y = 150
        PORTAL.rect.y = 480
        PORTAL.rect.x = 320


def takebody():
    if GLEB_SAHUR.TungTungSaur_BODY == False:
        if colision(GLEB_SAHUR, TungTungsahur):
            GLEB_SAHUR.TungTungSaur_BODY = True
            TungTungsahur.show = False


def set_random_position(Capebara):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    Capebara.rect.x = x
    Capebara.rect.y = y
    while colision(Capebara, LOBERINT) or colision(Capebara, GLEB_SAHUR)or colision(Capebara, TungTungsahur):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        Capebara.rect.x = x
        Capebara.rect.y = y


def colision(obj_1, obj_2):
    col = pygame.sprite.collide_mask(obj_1, obj_2)
    if col:
        return True
    else:
        return False

def colision_on():
    if colision(LOBERINT, GLEB_SAHUR):
        GLEB_SAHUR.step_back()

pygame.init()
WINDOWS = pygame.display.set_mode((800, 600))
pygame.display.set_caption("HELP GLEB TO ESCAPE")
pygame.display.set_icon(pygame.image.load("TUPAIA_BOSHKA_GLEBA.png"))
GLEB_SAHUR = Main_Character(WINDOWS, "STANDING.png", "WALKING_1.png",
"WALKING_2.png", "WALKING_3.png","WALKING_4.png", "HAPPY-WIN_ANIMATION.png", 0, 500)

LOBERINT = THE_LOBERINT(WINDOWS, "THE_LOBERINT!.png")

TungTungsahur = TungTungsahur_BODY(WINDOWS, "TungTungsahur_BODY.png")

CAPEBARA_DaMexx_77 = CAPEBARA_EVIL(WINDOWS, "CAPEBARA_right.png", "CAPEBARA_left.png")
set_random_position(CAPEBARA_DaMexx_77)
CAPEBARA_DaMexx_77_1 = CAPEBARA_EVIL(WINDOWS, "CAPEBARA_right.png", "CAPEBARA_left.png")
set_random_position(CAPEBARA_DaMexx_77_1)
CAPEBARA_DaMexx_77_2 = CAPEBARA_EVIL(WINDOWS, "CAPEBARA_right.png", "CAPEBARA_left.png")
set_random_position(CAPEBARA_DaMexx_77_2)
PORTAL = PORTALS(WINDOWS, "PORTAL.png")
Capebara_Stats = GAME_STATS(WINDOWS)
while 1 == 1:
    WINDOWS.fill(color= (150,150,150))
    for sobitee in pygame.event.get():
        if sobitee.type == pygame.QUIT:
            sys.exit()
        if sobitee.type == pygame.KEYDOWN:
            if sobitee.key == pygame.K_w:
                GLEB_SAHUR.Movement_up = True
            if sobitee.key == pygame.K_s:
                GLEB_SAHUR.Movement_down = True
            if sobitee.key == pygame.K_a:
                GLEB_SAHUR.Movement_left = True
            if sobitee.key == pygame.K_d:
                GLEB_SAHUR.Movement_right = True

        if sobitee.type == pygame.KEYUP:
            if sobitee.key == pygame.K_w:
                GLEB_SAHUR.Movement_up = False
            if sobitee.key == pygame.K_s:
                GLEB_SAHUR.Movement_down = False
            if sobitee.key == pygame.K_a:
                GLEB_SAHUR.Movement_left = False
            if sobitee.key == pygame.K_d:
                GLEB_SAHUR.Movement_right = False



    GLEB_SAHUR.show_drawing()
    LOBERINT.show_drawing()
    if TungTungsahur.show == True:
        TungTungsahur.show_drawing()
    if PORTAL.show == True:
        PORTAL.show_drawing()
    GLEB_SAHUR.MOVEMENT()
    colision_on()
    takebody()
    PEREHOD_UROVNEI()

    CAPEBARA_DaMexx_77.CAPEBARA_MOVMENT()
    if colision(CAPEBARA_DaMexx_77, LOBERINT) == True:
        CAPEBARA_DaMexx_77.new_direction = True
        CAPEBARA_DaMexx_77.Capebara_back_stab()
    CAPEBARA_DaMexx_77.show_drawing()

    CAPEBARA_DaMexx_77_1.CAPEBARA_MOVMENT()
    if colision(CAPEBARA_DaMexx_77_1, LOBERINT) == True:
        CAPEBARA_DaMexx_77_1.new_direction = True
        CAPEBARA_DaMexx_77_1.Capebara_back_stab()
    CAPEBARA_DaMexx_77_1.show_drawing()

    CAPEBARA_DaMexx_77_2.CAPEBARA_MOVMENT()
    if colision(CAPEBARA_DaMexx_77_2, LOBERINT) == True:
        CAPEBARA_DaMexx_77_2.new_direction = True
        CAPEBARA_DaMexx_77_2.Capebara_back_stab()
    CAPEBARA_DaMexx_77_2.show_drawing()
    Capebara_Stats.show_drawing()

    minuse_jizn()




    pygame.display.flip()
