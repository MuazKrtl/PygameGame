import pygame
from pygame import *
from pygame.locals import *
from world import collider_stage1

pygame.init()


image1 = pygame.image.load("character/right/tile1.png")
image1 = pygame.transform.scale(image1,(64,64))
image2 = pygame.transform.flip(image1,False,True)
class Platformer_Player:
    def __init__(self,x,y,screen):
        self.screen = screen
        self.image = image1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.index = 0
        self.counter = 0
        self.direction = 0 # 1 = right // 2 = left
        self.vel_y = 0
        self.jumped = False
        self.run_right_p = []
        self.run_left_p = []
        self.run_right_p2 = []
        self.run_left_p2 = []
        self.walk_cooldown = 5
        self.gravity = 1 # 1 is normal // 2 is abnormal
        for number in range(1,3):
            images_rrp = pygame.image.load(f"character/right/tile{number}.png")
            images_rlp = pygame.image.load(f"character/left/tile{number}.png")
            images_rrp = pygame.transform.scale(images_rrp,[64,64])
            images_rlp = pygame.transform.scale(images_rlp,[64,64])
            images_rrp2 = pygame.transform.flip(images_rrp,False,True)
            images_rlp2 = pygame.transform.flip(images_rlp,False,True)
            self.run_right_p.append(images_rrp)
            self.run_left_p.append(images_rlp)
            self.run_right_p2.append(images_rrp2)
            self.run_left_p2.append(images_rlp2)
    def update(self):   
        dx = 0
        dy = 0
        key1 = pygame.key.get_pressed()
        if key1[K_g]:
            self.gravity = 2
            self.image = image2
        if key1[K_h]:
            self.gravity = 1
            self.image = image1
        if key1[K_e]:
            if self.gravity == 2:
                self.image = image2
            if self.gravity == 1:
                self.image = image1
        if key1[K_RIGHT]:
            dx += 4
            self.counter += 1
            self.direction = 1
        if key1[K_LEFT]:
            dx -= 4
            self.counter += 1
            self.direction = 2
        if self.gravity == 1:
            if key1[K_UP] and self.jumped == False:
                self.vel_y = -15
                self.jumped = True
            if key1[K_UP] == False and self.jumped == True:
                if self.vel_y == 0:
                    self.jumped = False
        if self.gravity == 2:
            if key1[K_UP] and self.jumped == False:
                self.vel_y = +15
                self.jumped = True
            if key1[K_UP] == False and self.jumped == True:
                if self.vel_y == 0:
                    self.jumped = False

        if key1[K_RIGHT] == False and key1[K_LEFT] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                if self.gravity == 1:
                    self.image = self.run_right_p[self.index]
                if self.gravity == 2:
                    self.image = self.run_right_p2[self.index]
            if self.direction == 2:
                if self.gravity == 1:
                    self.image = self.run_left_p[self.index]
                if self.gravity == 2:
                    self.image = self.run_left_p2[self.index]

        if self.gravity == 1:
            self.vel_y += 0.8
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            if self.rect.bottom > 1536:
	            self.rect.bottom = 1536
	            dy = 0
            
        if self.gravity == 2:
            self.vel_y -= 0.8
            if self.vel_y < -10:
                self.vel_y = -10
            dy += self.vel_y

            if self.rect.top < 0:
	            self.rect.top = 0
	            dy = 0

        for collider in collider_stage1:
            if collider.colliderect(self.rect.x + dx + 25, self.rect.y,15, 64):
                dx = 0
            if collider.colliderect(self.rect.x + 25, self.rect.y + dy,15, 64):
                if self.gravity == 1:
                    if self.vel_y < 0:
                        dy = collider.bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        dy = collider.top - self.rect.bottom
                        self.vel_y = 0
                elif self.gravity == 2:
                    if self.vel_y > 0:
                        dy = collider.top - self.rect.bottom
                        self.vel_y = 0
                    elif self.vel_y <= 0:
                        dy = collider.bottom - self.rect.top
                        self.vel_y = 0

        self.rect.x += dx
        self.rect.y += dy

        if self.counter > self.walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= 2:
                self.index = 0
            if self.direction == 1:
                if self.gravity == 1:
                    self.image = self.run_right_p[self.index]
                if self.gravity == 2:
                    self.image = self.run_right_p2[self.index]
            if self.direction == 2:
                if self.gravity == 1:
                    self.image = self.run_left_p[self.index]
                if self.gravity == 2:
                    self.image = self.run_left_p2[self.index]

