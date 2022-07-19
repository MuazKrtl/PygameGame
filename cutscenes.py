import pygame 
from pygame import *

pygame.init()
clock = pygame.time.Clock()
class CutSceneOne:
    def __init__(self,screen):
        self.animation = []
        self.screen = screen
        self.index = 0
        self.activate = True
        for number in range(1,40):
            images_entry1 = pygame.image.load(f"cuts/1/{number}.png")
            self.animation.append(images_entry1)
    def draw(self):
        clock.tick(5)
        if self.activate == True:
            if self.index < 39:
                pygame.draw.rect(self.screen,(0,0,0),(0,0,1280,768))
                self.screen.blit(self.animation[self.index],(482,367))
                self.index += 1 
            if self.index >= 39:
                self.activate = False

class CutSceneTwo:
    def __init__(self,screen):
        self.animation = []
        self.screen = screen
        self.index = 0
        self.activate = True
        for number in range(1,38):
            images_entry1 = pygame.image.load(f"cuts/2/{number}.png")
            self.animation.append(images_entry1)
    def draw(self):
        clock.tick(5)
        if self.activate == True:
            if self.index < 36:
                pygame.draw.rect(self.screen,(0,0,0),(0,0,1280,768))
                self.screen.blit(self.animation[self.index],(320,367))
                self.index += 1 
            if self.index >= 36:
                self.activate = False
                    
    


                    


        