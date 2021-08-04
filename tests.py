import unittest
from logics import *


class Test2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(convert_ij_to_number(4, 1, 1), 6)

    def test_2(self):
        self.assertEqual(convert_ij_to_number(4, 3, 3), 16)

    def test_3(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        arr = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_cells(arr), a)

    def test_4(self):
        a = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        arr = [
            [2, 2, 2, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_cells(arr), a)

    def test_5(self):
        a = []
        arr = [
            [2, 2, 2, 4],
            [2, 2, 2, 4],
            [2, 2, 2, 4],
            [2, 2, 2, 4],
        ]
        self.assertEqual(get_empty_cells(arr), a)

    def test_6(self):
        self.assertEqual(get_index_from_number(4, 1), (0, 0))

    def test_7(self):
        self.assertEqual(get_index_from_number(4, 16), (3, 3))

    def test_8(self):
        self.assertEqual(get_index_from_number(4, 6), (1, 1))

    def test_9(self):
        arr = [
            [2, 2, 2, 4],
            [2, 2, 2, 4],
            [2, 2, 2, 4],
            [2, 2, 2, 4],
        ]
        self.assertEqual(is_zero_cells(arr), False)

    def test_10(self):
        arr = [
            [0, 2, 2, 4],
            [0, 2, 2, 4],
            [2, 2, 0, 4],
            [2, 2, 2, 4],
        ]
        self.assertEqual(is_zero_cells(arr), True)

    def test_11(self):
        arr = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(is_zero_cells(arr), True)

    def test_12(self):
        arr = [
            [2, 2, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        rez = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(move_left(arr), (rez, 12))

    def test_13(self):
        arr = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4],
        ]
        rez = [
            [2, 8, 2, 0],
            [4, 2, 0, 0],
            [0, 0, 0, 0],
            [16, 8, 0, 0],
        ]
        self.assertEqual(move_left(arr), (rez, 32))

    def test_14(self):
        arr = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0],
        ]
        rez = [
            [4, 8, 4, 2],
            [8, 0, 0, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(move_up(arr), (rez, 24))

    def test_15(self):
        arr = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0],
        ]
        rez = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 0, 2],
            [8, 8, 4, 4],
        ]
        self.assertEqual(move_down(arr), (rez, 24))

    def test_16(self):
        arr = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0],
        ]
        self.assertEqual(is_possible_move(arr), True)

    def test_17(self):
        arr = [
            [2, 4, 8, 2],
            [8, 2, 4, 8],
            [4, 8, 2, 4],
            [8, 4, 2, 8],
        ]
        self.assertEqual(is_possible_move(arr), True)

    def test_18(self):
        arr = [
            [2, 4, 8, 2],
            [8, 2, 4, 8],
            [4, 8, 2, 4],
            [8, 4, 16, 8],
        ]
        self.assertEqual(is_possible_move(arr), False)

if __name__ == "main":
    unittest.main()
