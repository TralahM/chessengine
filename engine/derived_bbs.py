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
:CREATED: 	2020-02-22  23:22

:FILENAME:	derived_bbs.py
=======================================================================


    DESCRIPTION OF derived_bbs MODULE:

Deriving more complex bitboards from our already  defined structures
We will derive white and black pawns,rooks,bishops,queens,kings and knights as
is a the start of a game of chess
"""

import lookup_tables


WhitePawns = lookup_tables.mask_rank(lookup_tables.R2)
WhiteRooks = lookup_tables.piece(
    lookup_tables.A1) | lookup_tables.piece(lookup_tables.H1)
WhiteBishops = lookup_tables.piece(
    lookup_tables.C1) | lookup_tables.piece(lookup_tables.F1)
WhiteKnights = lookup_tables.piece(
    lookup_tables.B1) | lookup_tables.piece(lookup_tables.G1)
WhiteQueens = lookup_tables.piece(lookup_tables.D1)
WhiteKing = lookup_tables.piece(lookup_tables.E1)
BlackPawns = lookup_tables.mask_rank(lookup_tables.R7)
BlackRooks = lookup_tables.piece(
    lookup_tables.A8) | lookup_tables.piece(lookup_tables.H8)
BlackBishops = lookup_tables.piece(
    lookup_tables.C8) | lookup_tables.piece(lookup_tables.F8)
BlackKnights = lookup_tables.piece(
    lookup_tables.B8) | lookup_tables.piece(lookup_tables.G8)
BlackQueens = lookup_tables.piece(lookup_tables.D8)
BlackKing = lookup_tables.piece(lookup_tables.E8)

AllBlackPieces = BlackPawns | BlackRooks | BlackBishops | BlackKnights | BlackQueens | BlackKing
AllWhitePieces = WhitePawns | WhiteRooks | WhiteBishops | WhiteKnights | WhiteQueens | WhiteKing
AllPieces = AllBlackPieces | AllWhitePieces
