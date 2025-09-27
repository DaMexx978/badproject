import random

import pygame
import sys
from datetime import datetime


class PARENTS():
    def __init__(self, WINDOWS, Name_Image):
        self.screen = WINDOWS
        self.image = pygame.image.load(Name_Image)
        self.rect = self.image.get_rect()

    def show_drawing(self):
        self.screen.blit(self.image, self.rect)




class THE_LOBERINT(PARENTS):
    def __init__(self, WINDOWS, THE_LOBERINT ):
        super().__init__(WINDOWS, THE_LOBERINT)


class TungTungsahur_BODY(PARENTS):
    def __init__(self, WINDOWS, image):
        super().__init__(WINDOWS, image)
        self.rect.x = 196
        self.rect.y = 130
        self.show = True

class CAPEBARA_EVIL(PARENTS):
    def __init__(self, WINDOWS, image_r, image_l):
        super().__init__(WINDOWS, image_r)
        self.direction_list = ["left", "right","up", "down"]
        self.image_r = pygame.image.load(image_r)
        self.image_l = pygame.image.load(image_l)
        self.direction = random.choice(self.direction_list)
        self.point = 0
        self.new_direction = True
        self.speed = 1

    def Capebara_back_stab(self):
        step_back = self.speed *5
        if self.direction == "left":
            self.rect.centerx += step_back
        elif self.direction == "right":
            self.rect.centerx -= step_back
        elif self.direction == "up":
            self.rect.centery += step_back
        elif self.direction == "down":
            self.rect.centery -= step_back

    def set_random(self):
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(0, 600)
    def CAPEBARA_MOVMENT(self):
        try:
            if self.new_direction == True:
                self.direction = random.choice(self.direction_list)
                if self.direction ==  "left":
                    self.point = random.randint(0, self.rect.centerx)
                elif self.direction ==  "right":
                    self.point = random.randint(self.rect.centerx, 800)
                elif self.direction ==  "up":
                    self.point = random.randint(25, self.rect.centery)
                elif self.direction == "down":
                    self.point = random.randint(self.rect.centery, 600)
                self.new_direction = False
            else:
                if self.direction == "left":
                    self.rect.centerx -= self.speed
                    if self.image != self.image_l:
                        self.image = self.image_l

                    if self.rect.centerx <= self.point:
                        self.new_direction = True

                elif self.direction == "right":
                    self.rect.centerx += self.speed
                    if self.image != self.image_r:
                        self.image = self.image_r

                    if self.rect.centerx >= self.point:
                        self.new_direction = True

                elif self.direction == "up":
                    self.rect.centery -= self.speed
                    if self.rect.centery <= self.point:
                        self.new_direction = True

                elif self.direction == "down":
                    self.rect.centery += self.speed
                    if self.rect.centery >= self.point:
                        self.new_direction = True
        except:
            pass

class Main_Character(PARENTS):
    def __init__(self, WINDOWS, IMG_S, IMG_W_1, IMG_W_2, IMG_W_3, IMG_W_4, IMG_HAPPY_WIN_animation, position_x, position_y):
        super(Main_Character, self).__init__(WINDOWS, IMG_S)
        self.rect.x = position_x
        self.rect.y = position_y
        self.IMG_W_1 = pygame.image.load(IMG_W_1)
        self.IMG_W_2 = pygame.image.load(IMG_W_2)
        self.IMG_W_3 = pygame.image.load(IMG_W_3)
        self.IMG_W_4 = pygame.image.load(IMG_W_4)
        self.IMG_HAPPY_WIN_ANIMATION = pygame.image.load(IMG_HAPPY_WIN_animation)
        self.Movement_up = False
        self.Movement_down = False
        self.Movement_left = False
        self.Movement_right = False
        self.speed = 3
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.TungTungSaur_BODY = False
        self.invinceble = False
        self.step_sound = pygame.mixer.Sound("WALKING SOUNDS.wav")
        self.WALL_HIT_SOUND = pygame.mixer.Sound("WALL HIT.wav")
        self.sec_wall_hit = datetime.now().second
        self.timestepsound = datetime.now()
        self.soundtungtake = pygame.mixer.Sound("TUNG TUNG TAKE.wav")

    def step_back(self):
        step = self.speed
        if datetime.now().second != self.sec_wall_hit:
            self.sec_wall_hit = datetime.now().second
            self.WALL_HIT_SOUND.play()
        if self.Movement_up == True:
            self.y += step
            self.rect.y = self.y
        if self.Movement_down == True:
            self.y -= step
            self.rect.y = self.y
        if self.Movement_left == True:
            self.x += step
            self.rect.x = self.x
        if self.Movement_right == True:
            self.x -= step
            self.rect.x = self.x




    def MOVEMENT(self):
        if self.Movement_up == True:
            if self.rect.top <-20:
                return
            self.y -= self.speed
            self.rect.y = self.y
        if self.Movement_down == True:
            if self.rect.bottom >620:
                return
            self.y += self.speed
            self.rect.y = self.y
        if self.Movement_left == True:
            if self.image != self.IMG_W_2 and self.image != self.IMG_W_1:
                self.image = self.IMG_W_1
            if self.rect.left <-20:
                return
            self.x -= self.speed
            self.rect.x = self.x
        if self.Movement_right == True:
            if self.image != self.IMG_W_4 and self.image != self.IMG_W_3:
                self.image = self.IMG_W_3
            if self.rect.right >820:
                return
            self.x += self.speed
            self.rect.x = self.x
        if self.Movement_up or self.Movement_down or self.Movement_left or self.Movement_right:
            if datetime.now().microsecond > self.timestepsound.microsecond+500000 \
                    or datetime.now().second != self.timestepsound.second:

                self.step_sound.play()
                self.timestepsound = datetime.now()



class PORTALS(PARENTS):
    def __init__(self, WINDOWS, file_name):
        super().__init__(WINDOWS, file_name)
        self.show = True
        self.rect.centerx = 780
        self.rect.centery = 500


class GAME_STATS():
    def __init__(self, WINDOWS):
        self.screen = WINDOWS
        self.Lives = 3
        self.Lvl = 1
        self.font = pygame.font.SysFont(None, 25)
        self.textlvl = self.font.render(f"Lvl {self.Lvl}", True, (153, 247, 164))
        self.rect_textlvl = self.textlvl.get_rect()
        self.rect_textlvl.x = 750
        self.rect_textlvl.y = 11

        self.textLives = self.font.render(f"Lives {self.Lives}", True, (153, 247, 164))
        self.rect_textLives = self.textLives.get_rect()
        self.rect_textLives.x = 735
        self.rect_textLives.y = 50
        self.win_showing()
        self.lose_showing()
        self.minuslifesound = pygame.mixer.Sound("CHARACTER HIT.wav")
        self.soundportalperehod = pygame.mixer.Sound("PORTAL PEREHOD.wav")
    def show_drawing(self):
        self.screen.blit(self.textlvl, self.rect_textlvl)

        self.screen.blit(self.textLives, self.rect_textLives)
    def win_showing(self):
        self.font_for_win = pygame.font.SysFont(None, 90)
        self.text_for_a_win = self.font_for_win.render("YOU WIN", True, (255, 0, 0))
        self.rectwin = self.text_for_a_win.get_rect()
        self.rectwin.centerx = 400
        self.rectwin.centery = 300

    def win_pokazivaet(self):
        self.screen.blit(self.text_for_a_win, self.rectwin)
        self.screen.blit(self.restartgame, self.restartgamerect)

    def lose_showing(self):
        self.font_for_lose = pygame.font.SysFont(None, 90)
        self.font_for_restart = pygame.font.SysFont(None, 50)
        self.text_for_a_lose = self.font_for_lose.render("YOU LOSE", True, (255, 0, 0))
        self.rectlose = self.text_for_a_lose.get_rect()
        self.rectlose.centerx = 400
        self.rectlose.centery = 300
        self.restartgame = self.font_for_restart.render("PRESS R TO RESTART", True, (125, 235, 214))
        self.restartgamerect = self.restartgame.get_rect()
        self.restartgamerect.centerx = 400
        self.restartgamerect.centery = 450



    def lose_pokazivaet(self):
        self.screen.blit(self.text_for_a_lose, self.rectlose)
        self.screen.blit(self.restartgame, self.restartgamerect)







