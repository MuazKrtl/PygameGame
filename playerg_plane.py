import pygame
from pygame import *
from pygame.locals import *
from world import collider_stage2

pygame.init()

image_plane = pygame.image.load("vehicles/plane/plane.png")
image_plane = pygame.transform.scale(image_plane,(96,96))
class Pilot_Player:
    def __init__(self,x,y,screen):
        self.screen = screen
        self.image = image_plane
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.tornado_cooldown = 5
        self.index = 0
        self.dy = -0.1
        self.tornado_list = []
        for number in range(1,61):
            image_tornado = pygame.image.load(f"vehicles/plane/tornado/{number}.png")
            image_tornado = pygame.transform.flip(image_tornado,False,True)
            self.tornado_list.append(image_tornado)
    def update(self):
        self.dx = 0
        key1 = pygame.key.get_pressed()
        if key1[K_RIGHT]:
            self.dx += 4
        if key1[K_LEFT]:
            self.dx -= 4
        self.index += 1
        if self.index >= 60:
            self.index = 0
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.screen.blit(self.tornado_list[self.index],(self.rect.x + 800,600))
        self.dy += -0.001