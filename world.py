import pygame
from pygame import *
import pytmx 
import random
pygame.init()

collider = []
collider_stage1 = []
collider_stage2 = []
pass_to_stage1 = []
class World:
    def __init__(self,filename,player):
        tiledmap = pytmx.load_pygame(filename,pixelalpha = True)
        self.width = tiledmap.width * tiledmap.tilewidth
        self.height = tiledmap.height * tiledmap.tileheight
        self.tmxdata = tiledmap
        self.player = player
        self.color = pygame.Color(0,0,0,0)
    def render(self,surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                if layer.name == "ground":
                    for x,y,gid in layer:
                        tile = ti(gid)
                        if tile:
                            surface.blit(tile,(x*self.tmxdata.tilewidth,y*self.tmxdata.tileheight))
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == 'obstacles':
                    for obj in layer:
                        properties = obj.__dict__
                        x = properties['x']
                        y = properties['y']
                        width = properties["width"]
                        height = properties["height"]
                        new_rect = pygame.Rect(x,y,width,height)
                        collider.append(new_rect)
                if layer.name == 'passdoor':
                    for obj in layer:
                        properties = obj.__dict__
                        x = properties['x']
                        y = properties['y']
                        width = properties["width"]
                        height = properties["height"]
                        new_rect = pygame.Rect(x,y,width,height)
                        pass_to_stage1.append(new_rect)
    def render2(self,surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                if layer.name == "trees":
                    for x,y,gid in layer:
                        tile = ti(gid)
                        if tile:
                            surface.blit(tile,(x*self.tmxdata.tilewidth,y*self.tmxdata.tileheight))
    def make_map(self):
        temp_Surface = pygame.Surface((self.width,self.height))
        self.render(temp_Surface)
        return temp_Surface   
    def make_map2(self):
        temp_Surface2 = pygame.Surface((self.width,self.height))
        temp_Surface2.set_colorkey(self.color)
        self.render2(temp_Surface2)
        return temp_Surface2

class World2:
    def __init__(self,filename,player):
        tiledmap = pytmx.load_pygame(filename,pixelalpha = True)
        self.width = tiledmap.width * tiledmap.tilewidth
        self.height = tiledmap.height * tiledmap.tileheight
        self.tmxdata = tiledmap
        self.player = player
        self.color = pygame.Color(0,0,0,0)
    def render(self,surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x,y,gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile,(x*self.tmxdata.tilewidth,y*self.tmxdata.tileheight))
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == 'obstacles':
                    for obj in layer:
                        properties = obj.__dict__
                        x = properties['x']
                        y = properties['y']
                        width = properties["width"]
                        height = properties["height"]
                        new_rect = pygame.Rect(x,y,width,height)
                        collider_stage1.append(new_rect)
    def make_map(self):
        temp_Surface = pygame.Surface((self.width,self.height))
        self.render(temp_Surface)
        return temp_Surface   

class World3:
    def __init__(self,filename,player):
        tiledmap = pytmx.load_pygame(filename,pixelalpha = True)
        self.width = tiledmap.width * tiledmap.tilewidth
        self.height = tiledmap.height * tiledmap.tileheight
        self.tmxdata = tiledmap
        self.player = player
        self.color = pygame.Color(0,0,0,0)
    def render(self,surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x,y,gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile,(x*self.tmxdata.tilewidth,y*self.tmxdata.tileheight))
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == 'obstacles':
                    for obj in layer:
                        properties = obj.__dict__
                        x = properties['x']
                        y = properties['y']
                        width = properties["width"]
                        height = properties["height"]
                        new_rect = pygame.Rect(x,y,width,height)
                        collider_stage2.append(new_rect)
    def make_map(self):
        temp_Surface = pygame.Surface((self.width,self.height))
        self.render(temp_Surface)
        return temp_Surface 

class Camera:
    def __init__(self,width,height):
        self.camera = pygame.Rect(0,0,width,height)
        self.width = width
        self.height = height
    def apply_rect(self,rect):
        return rect.move(self.camera.topleft)
    def apply(self,entity):
        return entity.rect.move(self.camera.topleft)
    def update(self,target):
        x = -target.rect.centerx + 640 #took target at center 1280 // 2 = 640
        y = -target.rect.centery + 386 #768 // 2
        #limit camera 
        x = min(0,x)
        y = min(0,y)
        x = max(-(self.width - 1280),x)
        y = max(-(self.height - 768),y)
        self.camera = pygame.Rect(x,y,self.width,self.height)

light_size = (200,200)
light_image = pygame.image.load("map/4.png")
light = pygame.transform.scale(light_image,light_size)
light_rect = light.get_rect()

light2_size = (200,200)
light2_image = pygame.image.load("map/sight21.png")
light2 = pygame.transform.scale(light2_image,light2_size)
light2_rect = light2.get_rect()

def isNight(screen,night_World):
    if night_World == True:
        filter = pygame.surface.Surface((1280,768))
        filter.fill((44,55,134))
        screen.blit(filter,(0,0),special_flags=pygame.BLEND_RGBA_SUB)
    else: pass


def player_light(player,screen,camera):
    surf = pygame.surface.Surface((1280,768))
    surf.set_colorkey((0,0,0))
    light_rect.x,light_rect.y = player.rect.x - 80 , player.rect.y - 60 #son ayarlama lazım...
    surf.blit(light,camera.apply_rect(light_rect))
    screen.blit(surf, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

def torch_light(torch,screen,camera,player):
    if torch.visible == True:
        surf = pygame.surface.Surface((1280,768))
        surf.set_colorkey((0,0,0))
        light2_rect.x,light2_rect.y = torch.rect.x -94, torch.rect.y - 90
        surf.blit(light2,camera.apply_rect(light2_rect))
        screen.blit(surf,(0,0),special_flags=pygame.BLEND_RGBA_ADD)
    if torch.visible == False and player.active_weapon == 1:
        surf = pygame.surface.Surface((1280,768))
        surf.set_colorkey((0,0,0))
        light2_size = (500,500)
        light2_rect.x,light2_rect.y = player.rect.x - 84, player.rect.y - 77
        surf.blit(light2,camera.apply_rect(light2_rect))
        screen.blit(surf,(0,0),special_flags=pygame.BLEND_RGBA_ADD)