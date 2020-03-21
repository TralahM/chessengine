#!env python
# -*- coding: utf-8 -*-
"""
=======================================================================
:AUTHOR:	 Tralah M Brian <briantralah@tralahtek.com>
:TWITTER: 	 @TralahM <https://twitter.com/TralahM>
:GITHUB: 	 <https://github.com/TralahM>
:KAGGLE: 	 <https://kaggle.com/TralahM>
:COPYRIGHT:  (c) 2020  TralahTek LLC.
:LICENSE: 	 MIT , see LICENSE for more details.
:WEBSITE:	<https://www.tralahtek.com>
:CREATED: 	2020-02-22  03:56

:FILENAME:	lookup_tables.py
=======================================================================


    DESCRIPTION OF lookup_tables MODULE:

Bit Masks for Manipulating Bitboard Data Structures
"""

from bitboard import Bitboard

# Location Indexes
A1, A2, A3, A4, A5, A6, A7, A8 = range(0, 64, 8)
B1, B2, B3, B4, B5, B6, B7, B8 = range(1, 64, 8)
C1, C2, C3, C4, C5, C6, C7, C8 = range(2, 64, 8)
D1, D2, D3, D4, D5, D6, D7, D8 = range(3, 64, 8)
E1, E2, E3, E4, E5, E6, E7, E8 = range(4, 64, 8)
F1, F2, F3, F4, F5, F6, F7, F8 = range(5, 64, 8)
G1, G2, G3, G4, G5, G6, G7, G8 = range(6, 64, 8)
H1, H2, H3, H4, H5, H6, H7, H8 = range(7, 64, 8)

# FILES and RANKS
FL_A, FL_B, FL_C, FL_D, FL_E, FL_F, FL_G, FL_H = range(1, 9)
R1, R2, R3, R4, R5, R6, R7, R8 = range(1, 9)


EMPTY_BB = Bitboard()
FULL_BB = ~Bitboard()


def clear_rank(i: int) -> Bitboard:
    return ~Bitboard(f'{sum([2**i for i in range(8*(i-1),i*8)]):064b}')


def mask_rank(i: int) -> Bitboard:
    return Bitboard(f'{sum([2**i for i in range(8*(i-1),i*8)]):064b}')


def clear_file(i: int) -> Bitboard:
    return ~Bitboard(f'{sum([2**i for i in range(i-1,64,8)]):064b}')


def mask_file(i: int) -> Bitboard:
    return Bitboard(f'{sum([2**i for i in range(i-1,64,8)]):064b}')


def mask_diagonal(i: int):
    pass


def mask_antidiagonal(i: int):
    pass


def piece(loc: int) -> Bitboard:
    return Bitboard(f'{2**loc:064b}')


def compute_king_incomplete(king_loc: Bitboard, own_side: Bitboard) -> Bitboard:
    king_clip_file_h = king_loc & clear_file(FL_H)
    king_clip_file_a = king_loc & clear_file(FL_A)
    spot1 = king_clip_file_h << 7
    spot2 = king_loc << 8
    spot3 = king_clip_file_h << 9
    spot4 = king_clip_file_h << 1
    spot5 = king_clip_file_a >> 7
    spot6 = king_loc >> 8
    spot7 = king_clip_file_a >> 9
    spot8 = king_clip_file_a >> 1
    king_moves = spot1 | spot2 | spot3 | spot4 | spot5 | spot6 | spot7 | spot8
    king_valid = king_moves & ~own_side
    return king_valid


def compute_knight(knight_loc: Bitboard, own_side: Bitboard) -> Bitboard:
    spot1clip = spot8clip = clear_file(FL_A) & clear_file(FL_B)
    spot2clip = spot7clip = clear_file(FL_A)
    spot3clip = spot6clip = clear_file(FL_H)
    spot4clip = spot5clip = clear_file(FL_H) & clear_file(FL_G)
    spot1 = (knight_loc & spot1clip) << 6
    spot2 = (knight_loc & spot2clip) << 15
    spot3 = (knight_loc & spot3clip) << 17
    spot4 = (knight_loc & spot4clip) << 10
    spot5 = (knight_loc & spot5clip) >> 6
    spot6 = (knight_loc & spot6clip) >> 15
    spot7 = (knight_loc & spot7clip) >> 17
    spot8 = (knight_loc & spot8clip) >> 10
    knight_valid = spot1 | spot2 | spot3 | spot4 | spot5 | spot6 | spot7 | spot8
    return knight_valid


def compute_white_pawn(wp_loc: Bitboard, all_pieces: Bitboard, all_black_pieces: Bitboard) -> Bitboard:
    wp_one_step = (wp_loc << 8) & all_pieces
    wp_two_steps = ((wp_one_step & mask_rank(R3)) << 8) & all_pieces
    wp_valid_moves = wp_one_step | wp_two_steps
    # check left and right attacks minding overflows and underflows
    wp_left_attack = (wp_loc & clear_file(FL_A)) << 7
    wp_right_attack = (wp_loc & clear_file(FL_H)) << 9
    wp_attacks = wp_left_attack | wp_right_attack
    wp_valid_attacks = wp_attacks & all_black_pieces
    wp_valid = wp_valid_moves | wp_valid_attacks
    return wp_valid


def compute_black_pawn(bp_loc: Bitboard, all_pieces: Bitboard, all_white_pieces: Bitboard) -> Bitboard:
    bp_one_step = (bp_loc << 8) & all_pieces
    bp_two_steps = ((bp_one_step & mask_rank(R3)) << 8) & all_pieces
    bp_valid_moves = bp_one_step | bp_two_steps
    # check left and right attacks minding overflows and underflows
    bp_left_attack = (bp_loc & clear_file(FL_A)) << 7
    bp_right_attack = (bp_loc & clear_file(FL_H)) << 9
    bp_attacks = bp_left_attack | bp_right_attack
    bp_valid_attacks = bp_attacks & all_white_pieces
    bp_valid = bp_valid_moves | bp_valid_attacks
    return bp_valid
