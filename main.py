import pygame
import sys
from logics import *
from database import get_best_result, cur


def draw_intro():
    img2048 = pygame.image.load("2048_logo.png")
    font = pygame.font.SysFont("stxingkai", 70)
    text_welcome = font.render("Welcome!", True, WHITE)
    name = "Введите имя"
    name_not_typed = True
    while name_not_typed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == "Введите имя":
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2:
                        global username
                        username = name
                        name_not_typed = False
        screen.fill(BLACK)
        text_name = font.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        screen.blit(text_welcome, (230, 80))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)


def draw_top_gamers():
    font_top = pygame.font.SysFont("simsun", 30)
    font_gamer = pygame.font.SysFont("simsun", 20)
    text_head = font_top.render("Best: ", True, COLOR_TEXT)
    screen.blit(text_head, (250, 5))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s = f"{index + 1}. {name} - {score}"
        text_gamer = font_gamer.render(s, True, COLOR_TEXT)
        screen.blit(text_gamer, (250, 35 + 25 * index))


def draw_interface(cur_score, cur_delta=0):
    """"draws interface and every cell"""
    pygame.draw.rect(screen, WHITE, title_rec)
    font = pygame.font.SysFont("stxingkai", 70)
    font_score = pygame.font.SysFont("simsun", 48)
    font_delta = pygame.font.SysFont("simsun", 32)
    text_score = font_score.render("Score: ", True, COLOR_TEXT)
    text_score_value = font_score.render(f" {cur_score}", True, COLOR_TEXT)
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_value, (200, 35))
    if cur_delta > 0:
        text_score_delta = font_delta.render(f" +{cur_delta}", True, COLOR_TEXT)
        screen.blit(text_score_delta, (190, 65))
    pretty_print(game_field)
    draw_top_gamers()
    for row in range(blocks):
        for col in range(blocks):
            value = game_field[row][col]
            text = font.render(f"{value}", True, BLACK)
            w = col * size_block + (col + 1) * margin
            h = row * size_block + (row + 1) * margin + size_block
            pygame.draw.rect(screen, COLORS[value], (w, h, size_block, size_block))
            if value != 0:
                font_width, font_height = text.get_size()
                text_x = w + (size_block - font_width) // 2
                text_y = h + (size_block - font_height) // 2
                screen.blit(text, (text_x, text_y))


username = ""
game_field = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
game_field[0][2] = 2
game_field[2][1] = 4

GAMERS_DB = get_best_result()
COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 235, 255),
    32: (255, 235, 128),
    64: (255, 235, 0),
    128: (255, 200, 255),
    256: (255, 200, 128),
    512: (255, 200, 0),
    1024: (255, 150, 255),
    2048: (255, 150, 128),
}
COLOR_TEXT = (255, 127, 0)
WHITE = (255, 255, 255)
GREY = (130, 130, 130)
BLACK = (0, 0, 0)
score = 0

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
draw_intro()
draw_interface(score)
pygame.display.update()

while is_zero_cells(game_field) or is_possible_move(game_field):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            delta = 0
            if event.key == pygame.K_LEFT:
                game_field, delta = move_left(game_field)
            elif event.key == pygame.K_RIGHT:
                game_field, delta = move_right(game_field)
            elif event.key == pygame.K_UP:
                game_field, delta = move_up(game_field)
            elif event.key == pygame.K_DOWN:
                game_field, delta = move_down(game_field)
            score += delta
            empty_cells = get_empty_cells(game_field)
            random.shuffle(empty_cells)
            num_to_fill = empty_cells.pop()
            x, y = get_index_from_number(len(game_field[0]), num_to_fill)
            game_field = insert_2_or_4(game_field, x, y)
            print(f"Filling cell {num_to_fill}")
            draw_interface(score, delta)
            pygame.display.update()
