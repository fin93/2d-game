import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
global animation_frames
animation_frames = []

def load_ani(path, frame_duration):
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 0
    for frame in frame_duration:
        animation_frame_id = animation_name + str(n)
        img_loc = path + '/' + animation_frame_id + '.png'
        animation_image = pygame.image.load(img_loc).convert()
        animation_image.set_colorkey((255, 255, 255))
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        
        n += 1
    return animation_frame_data

def change_action(action_var, frame, new_value):
    pass

animation_database = {}
animation_database['run'] = load_ani('Assets/second', [3, 3, 3, 3, 3, 3, 3, 3, 3])
animation_database['idle'] = load_ani('Assets/second', [7, 7])

player_action = 'idle'
player_frame = 0
player_flip = False

