import pygame
from pygame import *
import playerg
from playerg import *
import playerg_plat
from playerg_plat import *
import playerg_plane
from playerg_plane import *
import world 
from world import pass_to_stage1
from cutscenes import CutSceneOne,CutSceneTwo
from pygame import mixer
from math import hypot

pygame.init()
fps = 60
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 768
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Alpha 1.0")


player = playerg.Player(100,100,screen)
player_platform = playerg_plat.Platformer_Player(100,1400,screen)
player_plane = playerg_plane.Pilot_Player(100,10000,screen)

gamemap = world.World("map/realmap.tmx",player)
gamemap_image = gamemap.make_map()
gamemap_image2 = gamemap.make_map2()
gamemap_rect = gamemap_image.get_rect()
gamemap_rect2 = gamemap_image2.get_rect()

stage1_map = world.World2("map/realgame_stage1.tmx",player_platform)
stage1_map_image = stage1_map.make_map()
stage1_map_rect = stage1_map_image.get_rect()

stage2_map = world.World3("map/stage2_a.tmx",Pilot_Player)
stage2_map_image = stage2_map.make_map()
stage2_map_rect = stage2_map_image.get_rect()

camera = world.Camera(gamemap.width,gamemap.height)
camera_stage1 = world.Camera(stage1_map.width,stage1_map.height)
camera_stage2 = world.Camera(stage2_map.width,stage2_map.height)

gui = playerg.Display_gui(player,screen)

cutscene_12music = mixer.Sound("cuts/1/typewriter.wav")

cutscene_12music.play(1)
cutscene_1 = CutSceneOne(screen)
cutscene_2 = CutSceneTwo(screen)
night_World = True
run = True
class Game_State:
    def __init__(self):
        self.state = "main_game"
    def state_manager(self):
        if self.state == "main_game":
            self.main_game()
        if self.state == "stage_1":
            self.stage_1()
        if self.state == "stage_2":
            self.stage_2()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
        if cutscene_1.activate == True:
            cutscene_1.draw() 
        else:
            if player.rect.colliderect(pass_to_stage1[0]): 
                self.state = "stage_1"
                cutscene_12music.play(1)
            cutscene_12music.stop()
            camera.update(player)
            screen.blit(gamemap_image,camera.apply_rect(gamemap_rect))
            if torch.visible == True:
                screen.blit(torch.image,camera.apply(torch))
            screen.blit(player.image,camera.apply_rect(player.rect))
            world.player_light(player,screen,camera)
            world.torch_light(torch,screen,camera,player)
            screen.blit(gamemap_image2,camera.apply_rect(gamemap_rect2))
            gui.update()
            world.isNight(screen,night_World)
            player.update()
        pygame.display.update()
    def stage_1(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
        if cutscene_2.activate == True:
            cutscene_2.draw() 
        else:
            camera_stage1.update(player_platform)
            screen.blit(stage1_map_image , camera_stage1.apply_rect(stage1_map_rect))
            screen.blit(player_platform.image , camera_stage1.apply_rect(player_platform.rect))
            player_platform.update()
        pygame.display.update()
    def stage_2(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
        camera_stage2.update(player_plane)
        screen.blit(stage2_map_image,camera_stage2.apply_rect(stage2_map_rect))
        screen.blit(player_plane.image,camera_stage2.apply_rect(player_plane.rect))
        player_plane.update()
        pygame.display.update()
        
game_State = Game_State()

while run:
    clock.tick(fps)
    game_State.state_manager()
pygame.quit()