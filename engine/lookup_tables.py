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

A1, A2, A3, A4, A5, A6, A7, A8 = range(0, 64, 8)
B1, B2, B3, B4, B5, B6, B7, B8 = range(1, 64, 8)
C1, C2, C3, C4, C5, C6, C7, C8 = range(2, 64, 8)
D1, D2, D3, D4, D5, D6, D7, D8 = range(3, 64, 8)
E1, E2, E3, E4, E5, E6, E7, E8 = range(4, 64, 8)
F1, F2, F3, F4, F5, F6, F7, F8 = range(5, 64, 8)
G1, G2, G3, G4, G5, G6, G7, G8 = range(6, 64, 8)
H1, H2, H3, H4, H5, H6, H7, H8 = range(7, 64, 8)

EMPTY_BB = Bitboard()
FULL_BB = ~Bitboard()


def clear_rank(i: int):
    return ~Bitboard(f'{sum([2**i for i in range(8*(i-1),i*8)]):064b}')


def mask_rank(i: int):
    return Bitboard(f'{sum([2**i for i in range(8*(i-1),i*8)]):064b}')


def clear_file(i: int):
    return ~Bitboard(f'{sum([2**i for i in range(i-1,64,8)]):064b}')


def mask_file(i: int):
    return Bitboard(f'{sum([2**i for i in range(i-1,64,8)]):064b}')


def piece(loc: int):
    return Bitboard(f'{2**loc:064b}')
