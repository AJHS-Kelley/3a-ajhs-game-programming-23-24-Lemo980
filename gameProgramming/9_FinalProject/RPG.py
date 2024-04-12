#Dungeon crawler by Eliot Blanton, v0.0

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1024, 786))
pygame.display.set_caption('Dungeon crawler')
clock = pygame.time.Clock()
game_active = True
startTime = 0
pixelFont = pygame.font.Font('gameProgramming/9_FinalProject/graphics/fonts/Pixeltype.ttf', 50)
titleScreen = pygame.image.load('gameProgramming\9_FinalProject\graphics\TitleBG.png').convert()

jungleButton = pygame.image.load('gameProgramming\9_FinalProject\graphics\JungleButton.png').convert()
dungeonButton = pygame.image.load('gameProgramming\9_FinalProject\graphics\DungeonButton.png').convert()
jButtonRect = jungleButton.get_rect()
dButtonRect = dungeonButton.get_rect()

while game_active:
    screen.blit(titleScreen, (0,0))
    screen.blit(dungeonButton, (50, 600))
    screen.blit(jungleButton, (800, 600))
    pygame.display.update()



