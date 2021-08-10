import random
import copy


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


def is_zero_cells(arr):
    """"checks if there is empty cells (0) in the array """
    for row in arr:
        if 0 in row:
            return True
    return False


def move_left(arr):
    """"function to move all elements to the left"""
    origin = copy.deepcopy(arr)
    n = len(arr[0])
    delta = 0
    for row in arr:
        while 0 in row:
            row.remove(0)
        while len(row) < 4:
            row.append(0)
    for i in range(n):
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1] and arr[i][j] != 0:
                arr[i][j] *= 2
                delta += arr[i][j]
                arr[i].pop(j+1)
                arr[i].append(0)
    return arr, delta, not origin == arr


def move_right(arr):
    """"function to move all elements to the right"""
    origin = copy.deepcopy(arr)
    n = len(arr[0])
    delta = 0
    for row in arr:
        while 0 in row:
            row.remove(0)
        while len(row) < 4:
            row.insert(0, 0)
    for i in range(n):
        for j in range(n-1, 0, -1):
            if arr[i][j] == arr[i][j-1] and arr[i][j] != 0:
                arr[i][j] *= 2
                delta += arr[i][j]
                arr[i].pop(j-1)
                arr[i].insert(0, 0)
    return arr, delta, not origin == arr


def move_up(arr):
    """"function to move all elements up"""
    origin = copy.deepcopy(arr)
    n = len(arr[0])
    delta = 0
    for j in range(n):
        column = []
        for i in range(n):
            if arr[i][j] != 0:
                column.append(arr[i][j])
        while len(column) < 4:
            column.append(0)
        for i in range(n - 1):
            if column[i] == column[i+1] and column[i] != 0:
                column[i] *= 2
                delta += column[i]
                column.pop(i+1)
                column.append(0)
        for i in range(n):
            arr[i][j] = column[i]
    return arr, delta, not origin == arr


def move_down(arr):
    """"function to move all elements down"""
    origin = copy.deepcopy(arr)
    n = len(arr[0])
    delta = 0
    for j in range(n):
        column = []
        for i in range(n):
            if arr[i][j] != 0:
                column.append(arr[i][j])
        while len(column) < 4:
            column.insert(0, 0)
        for i in range(n - 1, 0, -1):
            if column[i] == column[i-1] and column[i] != 0:
                column[i] *= 2
                delta += column[i]
                column.pop(i-1)
                column.insert(0, 0)
        for i in range(n):
            arr[i][j] = column[i]
    return arr, delta, not origin == arr


def is_possible_move(arr):
    """"checks if it is possible to make any move"""
    n = len(arr[0])
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[i][j] == arr[i][j+1] or arr[i][j] == arr[i+1][j]:
                return True
    for i in range(1, n):
        for j in range(1, n):
            if arr[i][j] == arr[i-1][j] or arr[i][j] == arr[i][j-1]:
                return True
    return False
