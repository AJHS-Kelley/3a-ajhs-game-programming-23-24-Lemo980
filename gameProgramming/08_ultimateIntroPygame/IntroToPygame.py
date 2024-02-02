import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('gameProgramming/08_ultimateIntroPygame/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('gameProgramming/08_ultimateIntroPygame/graphics/Sky.png').convert()
ground_surface = pygame.image.load('gameProgramming/08_ultimateIntroPygame/graphics/ground.png').convert()


score_surf = test_font.render('My game', False, 'Black')
score_rect = score_surf.get_rect(center = (400,50))

snail_surface = pygame.image.load('gameProgramming/08_ultimateIntroPygame/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))


player_surf = pygame.image.load('gameProgramming/08_ultimateIntroPygame/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    pygame.draw.rect(screen, 'Pink', score_rect, 10)
    pygame.draw.rect(screen, 'Pink', score_rect)
    screen.blit(score_surf, score_rect)
    
    snail_rect.x -= 4
    if snail_rect.right < 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    
    player_rect.left += 1
    screen.blit(player_surf, player_rect)

    pygame.display.update()

#    if player_rect.colliderect(snail_rect):
#        print("collision")

#    mouse_pos = pygame.mouse.get_pos()
#    if player_rect.collidepoint(mouse_pos):
#        print(pygame.mouse.get_pressed())

    clock.tick(60)

























































