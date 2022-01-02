import pygame, os, sys
from pygame.locals import *
pygame.init()
main_clock = pygame.time.Clock()
WIDTH, HEIGHT = 400 * 2, 300 * 2
BG_COLOUR = (124, 124, 124)
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
font = pygame.font.SysFont('Arial', 20, True)
block_list = os.listdir('Assets/block')
block_database = {}
for block in block_list:
    img = pygame.image.load(f'Assets/block/{block}')
    block_database[block] = img.copy()

block_map = {}

def Text_to_List(Text, Divider ,is_int=False):
    List = []
    Current = ''
    for char in Text:
        if char != Divider:
            Current += char
        else:
            if is_int == True:
                try:
                    List.append(int(Current))
                except:
                    List.append(Current)
            else:
                List.append(Current)
            Current = ''
    return List
