import unittest
from io import StringIO
import sys

from chess import is_valid_piece, is_valid_position, add_black_pieces, determine_takeable_pieces

class TestChessFunctions(unittest.TestCase):

    def test_is_valid_piece(self):
        self.assertTrue(is_valid_piece("pawn"))
        self.assertTrue(is_valid_piece("rook"))
        self.assertFalse(is_valid_piece("knight"))
        self.assertFalse(is_valid_piece("queen"))

    def test_is_valid_position(self):
        self.assertTrue(is_valid_position("a1"))
        self.assertTrue(is_valid_position("h8"))
        self.assertFalse(is_valid_position("i1"))
        self.assertFalse(is_valid_position("a9"))
        self.assertFalse(is_valid_position("aa"))
        self.assertFalse(is_valid_position("1a"))

    def test_add_black_pieces(self):
        input_data = "rook e5\npawn f6\ndone\n"
        sys.stdin = StringIO(input_data)
        black_pieces = []
        add_black_pieces(black_pieces)
        self.assertEqual(len(black_pieces), 2)
        self.assertIn(('rook', 'e5'), black_pieces)
        self.assertIn(('pawn', 'f6'), black_pieces)

    def test_add_black_pieces_invalid(self):
        input_data = "knight b3\npawn z9\nrook e5\npawn f6\ndone\n"
        sys.stdin = StringIO(input_data)
        black_pieces = []
        add_black_pieces(black_pieces)
        self.assertEqual(len(black_pieces), 2)
        self.assertIn(('rook', 'e5'), black_pieces)
        self.assertIn(('pawn', 'f6'), black_pieces)

    def test_determine_takeable_pieces_rook(self):
        white_type = "rook"
        white_position = "d4"
        black_pieces = [("pawn", "d6"), ("rook", "h4"), ("pawn", "c3"), ("pawn", "e4")]
        can_take = determine_takeable_pieces(white_type, white_position, black_pieces)
        self.assertEqual(len(can_take), 3)
        self.assertIn(("pawn", "d6"), can_take)
        self.assertIn(("rook", "h4"), can_take)
        self.assertIn(("pawn", "e4"), can_take)

    def test_determine_takeable_pieces_pawn(self):
        white_type = "pawn"
        white_position = "e4"
        black_pieces = [("pawn", "d5"), ("rook", "f5"), ("pawn", "e5"), ("pawn", "c4")]
        can_take = determine_takeable_pieces(white_type, white_position, black_pieces)
        self.assertEqual(len(can_take), 2)
        self.assertIn(("pawn", "d5"), can_take)
        self.assertIn(("rook", "f5"), can_take)

    def test_determine_takeable_pieces_no_capture(self):
        white_type = "pawn"
        white_position = "e4"
        black_pieces = [("pawn", "d6"), ("rook", "h4"), ("pawn", "c3")]
        can_take = determine_takeable_pieces(white_type, white_position, black_pieces)
        self.assertEqual(len(can_take), 0)

