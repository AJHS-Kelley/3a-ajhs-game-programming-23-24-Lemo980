#Dungeon crawler by Eliot Blanton, v1.5

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1024, 786))
pygame.display.set_caption('Dungeon crawler')
clock = pygame.time.Clock()
game_active = True
startTime = 0
pixelFont = pygame.font.Font('gameProgramming\9_FinalProject\graphics\_fonts\Pixeltype.ttf', 85)
# create a surface to draw the font. use .render() to put font on surface 
titleScreen = pygame.image.load('gameProgramming\9_FinalProject\graphics\TitleBG.png').convert()
titleScreenRect = titleScreen.get_rect(center = (512, 393))

def selectMap():
    # selectLvL():
    mapChosen = False
    Map = ""
    jungleButton = pygame.image.load('gameProgramming\9_FinalProject\graphics\JungleButton.png').convert()
    dungeonButton = pygame.image.load('gameProgramming\9_FinalProject\graphics\DungeonButton.png').convert()
    jButtonRect = jungleButton.get_rect(center = (850, 600))
    dButtonRect = dungeonButton.get_rect(center = (150, 600))
    while mapChosen == False:

        screen.blit(titleScreen, (0,0))
        screen.blit(dungeonButton, dButtonRect)
        screen.blit(jungleButton, jButtonRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if dButtonRect.collidepoint(event.pos):
                    screen.fill((100,0,100), titleScreenRect)
                    Map = "dungeon"
                    mapChosen = True

                elif jButtonRect.collidepoint(event.pos):
                    screen.fill((200,200,50), titleScreenRect)
                    Map = "jungle"
                    mapChosen = True
            pygame.display.update()
    return Map

def selectDiff():
    easyButton = pygame.image.load('gameProgramming\9_FinalProject\graphics\easyButton.png').convert()
    hardButton = pygame.image.load('gameProgramming\9_FinalProject\graphics\hardButton.png').convert()
    easyButtonRect = easyButton.get_rect(center = (890, 600))
    hardButtonRect = hardButton.get_rect(center = (130, 600))
    chooseDiffTxt = pixelFont.render('Choose Your Difficulty', False, (0, 0, 0))
    chooseDiffTxtRect = chooseDiffTxt.get_rect(center = (512, 393))
    difficulty = ""
    difficultyChosen = False
    
    
    while difficultyChosen == False:
        screen.blit(easyButton, easyButtonRect)
        screen.blit(hardButton, hardButtonRect)
        screen.blit(chooseDiffTxt, chooseDiffTxtRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easyButtonRect.collidepoint(event.pos):
                    screen.fill((0,255,0), titleScreenRect)
                    difficulty = "easy"
                    difficultyChosen = True
                    

                elif hardButtonRect.collidepoint(event.pos):
                    screen.fill((255,0,0), titleScreenRect)
                    difficulty = "hard"
                    difficultyChosen = True
                    
                    
            pygame.display.update()
    return (difficulty)

Map = selectMap()
difficulty = selectDiff()

if difficulty == "easy":
    coins = 200
else:
    coins = 100

def shop(coins):
    coinCount = pixelFont.render(str(coins)+" coins left", False, (200, 200, 0))
    coinCountRect = coinCount.get_rect(midleft = (20, 50))
    while True:
        shopBG = pygame.image.load('gameProgramming\9_FinalProject\graphics\shopBG.png').convert()
        screen.blit(shopBG, (0,0))
        screen.blit(coinCount, coinCountRect)
        pygame.display.update()

shop(coins)