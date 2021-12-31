import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
BG_COLOUR = (178, 178, 178)
MENU_COLOUR = (120, 120, 120)
MENU_ITEMS_COLOUR = (100, 100, 100)
TEXT_COLOUR = (68, 68, 68)
font = pygame.font.SysFont('Arial', 50, True)
text = font.render('play', True, TEXT_COLOUR)

def load_map(filename):
    f = open(filename + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for line in data:
        game_map.append(list(line))
    return game_map

def change_text(text):
    fon = pygame.font.SysFont('Arial', 50, True)
    return fon.render(text, True, TEXT_COLOUR)

def main_menu():
    screen.fill(MENU_COLOUR)
    running = True
    mx, my = 0, 0
    while running:
        menu_1 = pygame.draw.rect(screen, MENU_ITEMS_COLOUR, (50, 50, 300, 100), 0, 10, 10, 10, 10, 10)
        menu_2 = pygame.draw.rect(screen, MENU_ITEMS_COLOUR, (50, 200, 300, 100), 0, 10, 10, 10, 10, 10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_1.collidepoint(event.pos):
                    main()
                if menu_2.collidepoint(event.pos):
                    quit()
        
        screen.blit(text, (200 - text.get_width() // 2, 67))        
        screen.blit(change_text('quit'), (200 - text.get_width() // 2, 215))
        pygame.display.update()

def main():
    screen.fill(BG_COLOUR)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
        
        pygame.display.update()

main()
