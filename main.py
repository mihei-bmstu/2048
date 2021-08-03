import pygame
import random


def pretty_print(arr):
    """"prints given array arr in pretty way"""
    print("-" * 10)
    for row in arr:
        print(*row)
    print("-" * 10)


def convert_ij_to_number(size, i, j):
    """"converts given cell index i and j to a cell number(starting from 1)"""
    return i * size + j + 1


def get_index_from_number(size, num):
    """"converts given cell number to index """
    num -= 1
    return num // size, num % size


def insert_2_or_4(arr, x, y):
    if random.random() <= 0.75:
        arr[x][y] = 2
    else:
        arr[x][y] = 4
    return arr


def get_empty_cells(arr):
    """"finds all empty cell in the given array arr"""
    empty_cells = []
    n = len(arr[0])
    for i in range(len(arr)):
        for j in range(n):
            if arr[i][j] == 0:
                empty_cells.append(convert_ij_to_number(n, i, j))
    return empty_cells


game_field = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

print(get_empty_cells(game_field))
pretty_print(game_field)
