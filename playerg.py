import pygame
from math import hypot
from pygame import *
from world import collider

pygame.init()
player_img = pygame.image.load("Resources/char1.png")
player_img = pygame.transform.scale(player_img,(64,64))
class Weapons(pygame.sprite.Sprite):
    def __init__(self,wp_x,wp_y,wp_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = wp_image
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = wp_x
        self.rect.y = wp_y
        self.visible = True
weapon_sprites = pygame.sprite.Group()
torch = Weapons(200,200,pygame.image.load("Resources/main_character_torch/torch.png"))
weapon_sprites.add(torch)

class Player():
    def __init__(self,x,y,screen):
        self.screen = screen
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.index = 0
        self.counter = 0
        self.direction = 0 # 0 = down // 1 = right // 2 = left // 3 = up
        self.active_weapon = 0 # 0 nothing// 1 torch // 2 .... // 3 is ...
        self.run_right = []
        self.run_left = []
        self.run_up = []
        self.run_down = []
        self.run_right_t = []
        self.run_left_t = []
        self.run_up_t = []
        self.run_down_t = []
        self.walk_cooldown = 5
        for number in range(1,3):
            images_rr = pygame.image.load(f"character/right/tile{number}.png")
            images_rl = pygame.image.load(f"character/left/tile{number}.png")
            images_ru = pygame.image.load(f"character/up/tile{number}.png")
            images_rd = pygame.image.load(f"character/down/tile{number}.png")
            images_rr = pygame.transform.scale(images_rr,[64,64])
            images_rl = pygame.transform.scale(images_rl,[64,64])
            images_rd = pygame.transform.scale(images_rd,[64,64])
            images_ru = pygame.transform.scale(images_ru,[64,64])
            self.run_right.append(images_rr)
            self.run_left.append(images_rl)
            self.run_up.append(images_ru)
            self.run_down.append(images_rd)
        for number in range(1,3):
            images_rr_t = pygame.image.load(f"Resources/main_character_torch/right/{number}.png")
            images_rl_t = pygame.image.load(f"Resources/main_character_torch/left/{number}.png")
            images_rd_t = pygame.image.load(f"Resources/main_character_torch/down/{number}.png")
            images_ru_t = pygame.image.load(f"Resources/main_character_torch/up/{number}.png")
            images_rr_t = pygame.transform.scale(images_rr_t,[64,64])
            images_rl_t = pygame.transform.scale(images_rl_t,[64,64])
            images_rd_t = pygame.transform.scale(images_rd_t,[64,64])
            images_ru_t = pygame.transform.scale(images_ru_t,[64,64])
            self.run_right_t.append(images_rr_t)
            self.run_left_t.append(images_rl_t)
            self.run_up_t.append(images_ru_t)
            self.run_down_t.append(images_rd_t)

    def update(self):   
        self.hitbox = pygame.Rect(self.rect.x + 15,self.rect.y,32,64)
        key = pygame.key.get_pressed()
        if key[K_RIGHT] and key[K_UP] == False and key[K_DOWN] == False:
            self.rect.x += 1
            self.counter += 1
            self.direction = 1
        if key[K_LEFT] and key[K_UP] == False and key[K_DOWN] == False:
            self.rect.x -= 1
            self.counter += 1
            self.direction = 2
        if key[K_UP] and key[K_RIGHT] == False and key[K_LEFT] == False:
            self.rect.y -= 1
            self.counter += 1
            self.direction = 3
        if key[K_DOWN] and key[K_RIGHT] == False and key[K_LEFT] == False:
            self.rect.y += 1
            self.counter += 1
            self.direction = 0
        if key[K_1]:
            self.active_weapon = 0
        if key[K_2] and torch.visible == False:
            self.active_weapon = 1    
        if hypot(self.rect.x - torch.rect.x , self.rect.y - torch.rect.y) < 40:
            if key[K_f]:
                self.active_weapon = 1
                torch.visible = False 
        for collide in collider:
            if self.hitbox.colliderect(collide):
                if self.direction == 0:
                    self.rect.y -= 1
                if self.direction == 1:
                    self.rect.x -= 1
                if self.direction == 2:
                    self.rect.x += 1
                if self.direction == 3:
                    self.rect.y += 1
        if key[K_RIGHT] == False and key[K_LEFT] == False and key[K_DOWN] == False and key[K_UP] == False and key[K_SPACE] == False:
            self.counter = 0
            self.index = 0
            if self.active_weapon == 1:
                if self.direction == 0:
                    self.image = self.run_down_t[self.index]
                if self.direction == 1:
                    self.image = self.run_right_t[self.index]
                if self.direction == 2:
                    self.image = self.run_left_t[self.index]
                if self.direction == 3:
                    self.image = self.run_up_t[self.index]
            elif self.active_weapon == 0:
                if self.direction == 0:
                    self.image = self.run_down[self.index]
                if self.direction == 1:
                    self.image = self.run_right[self.index]
                if self.direction == 2:
                    self.image = self.run_left[self.index]
                if self.direction == 3:
                    self.image = self.run_up[self.index]
        if self.counter > self.walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= 2:
                self.index = 0
            if self.active_weapon == 1:
                if self.direction == 0:
                    self.image = self.run_down_t[self.index]
                if self.direction == 1:
                    self.image = self.run_right_t[self.index]
                if self.direction == 2:
                    self.image = self.run_left_t[self.index]
                if self.direction == 3:
                    self.image = self.run_up_t[self.index]   
            elif self.active_weapon == 0:
                if self.direction == 0:
                    self.image = self.run_down[self.index]
                if self.direction == 1:
                    self.image = self.run_right[self.index]
                if self.direction == 2:
                    self.image = self.run_left[self.index]
                if self.direction == 3:
                    self.image = self.run_up[self.index]
            
class Display_gui:
    def __init__(self,player,screen):
        self.player = player
        self.screen = screen
        self.surface = pygame.surface.Surface((1280,720))
        self.surface.set_colorkey((0,0,0))
        self.fistimage = pygame.image.load("character/gui/fistgui.png")
        self.fistimage = pygame.transform.scale(self.fistimage,(200,200))
        self.torchimage = pygame.image.load("character/gui/torchgui.png")
        self.torchimage = pygame.transform.scale(self.torchimage,(200,200))
    def update(self):
        if self.player.active_weapon == 0:
            self.surface.blit(self.fistimage,(-53,-53))
            self.screen.blit(self.surface,(0,0))
        if self.player.active_weapon == 1:
            self.surface.blit(self.torchimage,(-53,-53))
            self.screen.blit(self.surface,(0,0))