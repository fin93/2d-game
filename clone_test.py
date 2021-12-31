import pygame, sys, math
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.image.load('Assets/player/player.png').convert()
player.set_colorkey((255, 255, 255))

jump_height = -1
g = 10
player_y_vel = 0
player_x = WIDTH // 2
player_y = 50

BG_COLOUR = (124, 124, 124)
screen.fill(BG_COLOUR)

clock = pygame.time.Clock()

def jump(vel):
    vel = math.sqrt(jump_height * -2 * g)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    
    screen.blit(player, (0, 0))
    pygame.display.update()
    clock.tick(60)
