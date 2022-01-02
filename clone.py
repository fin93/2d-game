import pygame, sys, math, os
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

_player = pygame.image.load('Assets/player/player.png').convert()
_player.set_colorkey((255, 255, 255))
player = pygame.transform.scale(_player, (_player.get_width() * 3, _player.get_height() * 3))
grass_orig = pygame.image.load('Assets/block/grass.jpg')
grass_block = pygame.transform.scale(grass_orig, (50, 50))
dirt_orig = pygame.image.load('Assets/block/dirt_.jpg')
dirt_block = pygame.transform.scale(dirt_orig, (50, 50))

map_name = 'full_map'
map_level_number = 0
jump_height = -1
g = 10
player_x = 0
player_y = 0
y_vel = 0
player_x_vel = 0

print(player.get_width(), player.get_height())
player_rect = pygame.Rect(player_x, player_y, player.get_width(), player.get_height())
test_rect = pygame.Rect(100, 100, 50, 50)
BG_COLOUR = (124, 124, 124)
screen.fill(BG_COLOUR)

clock = pygame.time.Clock()

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

game_map = load_full_map(f'maps/{map_name}', map_level_number)

def display_game_map(game_map):
    block_rects = []
    for i in range(12):
        for j in range(16):
            if game_map[i][j] == '1':
                screen.blit(dirt_block, (j * 50, i * 50))
            if game_map[i][j] == '2':
                screen.blit(grass_block, (j * 50, i * 50))
                block_rects.append(pygame.Rect(j * 50, i * 50, 50, 50))
            if game_map[i][j] != '0':
                pass
    return block_rects
    
f = display_game_map(game_map)

def collides(p_rect, block_list):
    hit_list = []
    for block in block_list:
        if p_rect.colliderect(block):
            hit_list.append(block)
    return hit_list

def where(player, block_list, direction, up_down):
    collisions = {'top':False,'bottom':False,'right':False,'left':False}
    player.x += direction
    block_hit_list = collides(player, block_list)
    block_hit_list = collides(player, block_list)
    if len(block_hit_list) != 0:
        for block in block_hit_list:
            if direction > 0:
                player.right = block.left
                collisions['right'] = True
            elif direction < 0:
                player.left = block.right
                collisions['left'] = True
    player.y += up_down
    block_hit_list = collides(player, block_list)
    if len(block_hit_list) != 0:
        for block in block_list:
            if up_down > 0:
                player.bottom = block.top
                collisions['bottom'] = True
            elif up_down < 0:
                player.top = block.bottom
                collisions['top'] = True
    
    return player, collisions


def jump(vel):
    vel = -1 * math.sqrt(jump_height * -2 * g)
    return vel

while True:
    screen.fill(BG_COLOUR)
    blocks = display_game_map(game_map)
    if player_x > WIDTH:
        map_level_number += 1
        game_map = load_full_map(f'maps/{map_name}', map_level_number)
        f = display_game_map(game_map)
        player_x = 0
    if player_x < 0:
        map_level_number -= 1
        game_map = load_full_map(f'maps/{map_name}', map_level_number)
        f = display_game_map(game_map)
        player_x = 599
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_vel = jump(y_vel)
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x_vel = -2 
    elif keys[pygame.K_RIGHT]:
        player_x_vel = 2
    else:
        player_x_vel = 0
    if y_vel > 17:
        y_vel = 17
    player_rect, collisions = where(player_rect, f, player_x_vel, y_vel)
    
    if not collisions['bottom']:
        y_vel += 0.2
        player_y += y_vel
    
    player_x += player_x_vel
    player_rect.x, player_rect.y = player_x, player_y
    
    screen.blit(player, (player_x, player_y))
    pygame.display.update()
    clock.tick(60)
