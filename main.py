import pygame
import sys
from logics import *

game_field = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
game_field[0][2] = 2
game_field[2][1] = 4

white = (255, 255, 150)
grey = (130, 130, 130)

blocks = len(game_field[0])
size_block = 110
margin = 10
width = blocks * size_block + (blocks + 1) * margin
height = width + size_block
title_rec = pygame.Rect(0, 0, width, size_block)

print(get_empty_cells(game_field))
pretty_print(game_field)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2048")

while is_zero_cells(game_field):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            pygame.draw.rect(screen, white, title_rec)
            for row in range(blocks):
                for col in range(blocks):
                    w = col * size_block + (col + 1) * margin
                    h = row * size_block + (row + 1) * margin + size_block
                    pygame.draw.rect(screen, grey, (w, h, size_block, size_block))
            # input()
            empty_cells = get_empty_cells(game_field)
            random.shuffle(empty_cells)
            num_to_fill = empty_cells.pop()
            x, y = get_index_from_number(len(game_field[0]), num_to_fill)
            game_field = insert_2_or_4(game_field, x, y)
            print(f"Filling cell {num_to_fill}")
            pretty_print(game_field)
    pygame.display.update()

