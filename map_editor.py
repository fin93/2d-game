import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

map_level_number = 0
map_name = "full_map"
active_edit = '0'
sky_color = (124, 124, 224)
TEXT_COLOUR = (68, 68, 68)
font = pygame.font.SysFont('Arial', 20, True)
screen.fill(sky_color)
text = font.render('active: sky', True, TEXT_COLOUR)
is_on = False
map_to_write = 'map_1'
level_to_display = 'level: 1'
display_which_level = font.render(level_to_display, True, TEXT_COLOUR)

grass_orig = pygame.image.load('Assets/block/grass.jpg')
grass_block = pygame.transform.scale(grass_orig, (50, 50))
dirt_orig = pygame.image.load('Assets/block/dirt_.jpg')
dirt_block = pygame.transform.scale(dirt_orig, (50, 50))

def write_map(filename, current_map):
    f = open(filename + '.txt', 'w')
    for i in range(12):
        for j in range(16):
            f.write(current_map[i][j])
        f.write('\n')
    f.close()

def load_full_map(filename, map_number):
    f = open(filename + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('nn')
    game_map = []
    for line in data:
        game_map.append(list(line))
    game_map = game_map[map_number]
    temp_game_map = ""
    for i in game_map:
        temp_game_map = temp_game_map + str(i)
    actual_data = temp_game_map.split('\n')
    acc_game_map = []
    for lin in actual_data:
        acc_game_map.append(list(lin))
    acc_game_map.remove([])
    return acc_game_map      
            
def load_map(filename):
    f = open(filename + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for line in data:
        game_map.append(list(line))
    return game_map

game_map = load_full_map(f'maps/{map_name}', map_level_number)


def display_game_map(game_map):
    for i in range(12):
        for j in range(16):
            if game_map[i][j] == '0':
                pass
            elif game_map[i][j] == '1':
                screen.blit(dirt_block, (j * 50, i * 50))
            elif game_map[i][j] == '2':
                screen.blit(grass_block, (j * 50, i * 50))

while True:
    screen.fill(sky_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                active_edit = '0'
                text = font.render('active: sky', True, TEXT_COLOUR)
            elif event.key == pygame.K_2:
                active_edit = '1'
                text = font.render('active: dirt', True, TEXT_COLOUR)
            elif event.key == pygame.K_3:
                active_edit = '2'
                text = font.render('active: grass', True, TEXT_COLOUR)
            if event.key == pygame.K_w:
                write_map(f'maps/{map_to_write}', game_map)
                text = font.render('written', True, TEXT_COLOUR)
            if event.key == pygame.K_RIGHT:
                map_level_number += 1
                game_map = load_full_map('maps/full_map', map_level_number)
                level_to_display = f'level: {map_level_number + 1}'
                display_which_level = font.render(level_to_display, True, TEXT_COLOUR)
            elif event.key == pygame.K_LEFT:
                map_level_number -= 1
                game_map = load_full_map('maps/full_map', map_level_number)
                level_to_display = f'level: {map_level_number + 1}'
                display_which_level = font.render(level_to_display, True, TEXT_COLOUR)
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_on = True
        if event.type == pygame.MOUSEBUTTONUP:
            is_on = False

    if is_on:
        mx, my = pygame.mouse.get_pos()[0] // 50, pygame.mouse.get_pos()[1] // 50
        game_map[my][mx] = active_edit

    display_game_map(game_map)
    screen.blit(text, (20, 20))
    screen.blit(display_which_level, (20, 50))
    pygame.display.update()
