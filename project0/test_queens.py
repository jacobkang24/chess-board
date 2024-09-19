# test_queens.py
#
# ICS 33 Spring 2024
# Project 0: History of Modern
#
# Unit tests for the QueensState class in "queens.py".
#
# Docstrings are not required in your unit tests, though each test does need to have
# a name that clearly indicates its purpose.  Notice, for example, that the provided
# test method is named "test_queen_count_is_zero_initially" instead of something generic
# like "test_queen_count", since it doesn't entirely test the "queen_count" method,
# but instead focuses on just one aspect of how it behaves.  You'll want to do likewise.

import unittest
from queens import QueensState, Position, DuplicateQueenError, MissingQueenError



class TestQueensState(unittest.TestCase):
    def test_queen_count_is_zero_initially(self):
        state = QueensState(8, 8)
        self.assertEqual(state.queen_count(), 0)

    def test_queen_count_after_adding_queens(self):
        state = QueensState(8, 8)
        self.assertEqual(state.queen_count(), 0)

        chessboard = state.with_queens_added([Position(0, 0), Position(1, 1)])
        self.assertEqual(chessboard.queen_count(), 2)

    def test_return_queen_count_when_queens(self):
        chessboard = QueensState(4, 4)
        chessboard.grid[0][0] = 1
        chessboard.grid[2][2] = 1

        count = chessboard.queen_count()
        self.assertEqual(count, 2)

    def test_return_queen_count_no_queens(self):
        chessboard = QueensState(4, 4)
        count = chessboard.queen_count()
        self.assertEqual(count, 0)

    def test_queens_position_on_chessboard(self):
        chessboard = QueensState(4, 4)
        chessboard.grid[0][0] = 1
        chessboard.grid[2][2] = 1

        positions = chessboard.queens()
        expected_positions = [(0, 0), (2, 2)]
        self.assertEqual(positions, expected_positions)

    def test_has_queens_if_queen_in_and_out_position(self):
        chessboard = QueensState(4, 4)
        chessboard.grid[0][0] = 1
        chessboard.grid[2][2] = 1

        self.assertTrue(chessboard.has_queen(Position(0, 0)))
        self.assertTrue(chessboard.has_queen(Position(2, 2)))
        self.assertFalse(chessboard.has_queen(Position(3, 2)))
        self.assertFalse(chessboard.has_queen(Position(-1, 0)))
        self.assertFalse(chessboard.has_queen(Position(0, -1)))

    def test_if_queen_is_unsafe_and_safe(self):
        chessboard = QueensState(4, 4)
        chessboard.grid[0][0] = 1
        chessboard.grid[2][2] = 1
        self.assertTrue(chessboard.any_queens_unsafe())

        chessboard = QueensState(4, 4)
        chessboard.grid[0][0] = 1
        chessboard.grid[2][1] = 1
        self.assertFalse(chessboard.any_queens_unsafe())

    def test_the_board_if_queens_added(self):
        chessboard = QueensState(4, 4)
        new_chessboard = chessboard.with_queens_added([Position(0, 0), Position(1, 1)])

        self.assertEqual(chessboard.queen_count(), 0)

        self.assertEqual(new_chessboard.queen_count(), 2)
        self.assertTrue(new_chessboard.has_queen(Position(0, 0)))
        self.assertTrue(new_chessboard.has_queen(Position(1, 1)))

        with self.assertRaises(DuplicateQueenError):
            new_chessboard.with_queens_added([Position(0, 0), Position(1, 1)])

        new_chessboard2 = new_chessboard.with_queens_added([Position(3, 2)])
        self.assertTrue(new_chessboard2.has_queen(Position(3, 2)))

    def test_board_if_queens_removed(self):
        chessboard = QueensState(4, 4)
        chessboard.grid[0][0] = 1
        chessboard.grid[1][1] = 1
        chessboard.grid[2][2] = 1

        new_chessboard = chessboard.with_queens_removed([Position(0, 0), Position(1, 1)])
        self.assertEqual(chessboard.queen_count(), 3)

        self.assertEqual(new_chessboard.queen_count(), 1)
        self.assertFalse(new_chessboard.has_queen(Position(0, 0)))
        self.assertFalse(new_chessboard.has_queen(Position(1, 1)))
        self.assertTrue(new_chessboard.has_queen(Position(2, 2)))

        with self.assertRaises(MissingQueenError):
            new_chessboard.with_queens_removed([Position(0, 0), Position(1, 1)])

        with self.assertRaises(MissingQueenError):
            new_chessboard.with_queens_removed([Position(-1, 4)])

if __name__ == '__main__':
    unittest.main()
