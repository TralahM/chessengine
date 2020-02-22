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

EMPTY_BB = Bitboard()
FULL_BB = ~Bitboard()


def clear_rank(i: int):
    return ~Bitboard(f'{sum([2**i for i in range(8*(i-1),i*8)]):064b}')


def clear_file(i: int):
    return ~Bitboard(f'{sum([2**i for i in range(i-1,64,8)]):064b}')
