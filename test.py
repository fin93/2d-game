import pygame, sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
TEXT_COLOUR = (68, 68, 68)
font = pygame.font.SysFont('Arial', 50, True)
text = font.render('Hold down space', True, TEXT_COLOUR)
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, number):
        super().__init__()
        self.sprites = []
        for i in range(number):
            x = pygame.image.load(f'Assets/second/second{i}.png').convert()
            x.set_colorkey((255, 255, 255))
            ok_x = pygame.transform.scale(x, (200, 200))
            self.sprites.append(ok_x)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x - 100, pos_y - 200]
    def update(self):
        self.current_sprite += 0.3
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]


moving_sprites = pygame.sprite.Group()
player = Player(400, 300, 9)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        moving_sprites.update()
    screen.fill((124, 124, 124))
    moving_sprites.draw(screen)
    screen.blit(text, (300 - 50, 30))
    pygame.display.flip()
    clock.tick(60)

