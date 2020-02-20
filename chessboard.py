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
:CREATED: 	2020-02-03  23:01

:FILENAME:	chessboard.py
=======================================================================


    DESCRIPTION OF chessboard MODULE:

CHESS BOARD Modelling

 _________________
8|-|-|-|-|-|-|-|-|
7|-|-|-|-|-|-|-|-|
6|-|-|-|-|-|-|-|-|
5|-|-|-|-|-|-|-|-|
4|-|-|-|-|-|-|-|-|
3|-|-|-|-|-|-|-|-|
2|-|-|-|-|-|-|-|-|
1|-|-|-|-|-|-|-|-|
 -----------------
  a b c d e f g h
"""
import numpy as np
COLMAP = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h',
}
FILES = {v: k for k, v in COLMAP.items()}
RANKS = [i for i in range(1, 9)]
MAX = 8
MIN = 1
PIECES = {
    'K': 'King', 'Q': 'Queen', 'R': 'Rook',
    'B': 'Bishop', 'N': 'Knight', ' ': "Pawn",
    # Pawns have no special notation
}
PIECE_POINTS = {
    "Pawn": 1, "Knight": 3, "Bishop": 3,
    "Rook": 5, "Queen": 9, "King": np.inf,
}


class Position(object):
    """
    Abstract Position on a Chess Board
    """

    def __init__(self, fileid: str, rankid: int):
        self.fileid = fileid
        self.rank = rankid
        self.coordinates = (rankid-1, FILES[fileid]-1)

    def __str__(self):
        return self.fileid+str(self.rank)

    def __repr__(self):
        return self.fileid+str(self.rank)+"\t"+str(self.coordinates)


class Board(object):
    def __init__(self):
        self.state = np.matrix([np.zeros(8) for i in range(8)]).T.astype(int)
        self.state[0] = np.ones(8)
        self.state[1] = np.ones(8)
        self.state[6] = np.ones(8)*-1
        self.state[7] = np.ones(8)*-1
        self.state[(0, 0)] = 8
        self.state[(0, 7)] = 8
        self.state[(0, 1)] = 3
        self.state[(0, 6)] = 3
        self.state[(0, 2)] = 5
        self.state[(0, 5)] = 5
        self.state[(0, 3)] = 13
        self.state[(0, 4)] = 21
        self.state[(7, 0)] = 8*-1
        self.state[(7, 7)] = 8*-1
        self.state[(7, 1)] = 3*-1
        self.state[(7, 6)] = 3*-1
        self.state[(7, 2)] = 5*-1
        self.state[(7, 5)] = 5*-1
        self.state[(7, 3)] = 13*-1
        self.state[(7, 4)] = 21*-1

    def __repr__(self):
        return str(self.state)

# Notation for moves: Each piece is indicated by the pieces uppercase letter,
# Plus the coordinate of the destination square e.g Be5 (move a bishop to e5).
# Nf3 (move a knight to f3) and e5 (Move a Pawn to e5)
# When a piece makes a Capture, an 'x' is inserted before the destination
# square e.g Bxe5 (bishop captures the piece on e5). and exd5 (pawm on e file
# captures piece on d5). or sometimes a : colon instead of x like (B:e5) and
# e:d5 or sometimes at the end (Be5:) and (ed5:)

# En-Peasant captires are indicated by specifying the pawn's file of departure,
# thes 'x', the destination square(not the square of the captured pawn) and
# (optionally) the suffix e.p. indicating the capture was en peassant: eg
# exd6e.p.

# For disambiguation of moves the moving piece is uniquely identifued by
# specifying the pieces letter, followed by (in descending order of preference)
# 1. The file of departure if they differ;or \
# 2. The Rank of departure (if files are the same but the ranks differ); or
# 3. Both the Rank and File if neither alone is sufficient to identify the
# pieces - which occurs only in rare cases where one or more pawns have
# promoted, resulting in a player having three or more identical pieces able to
# reach the same square for example   Qd1h5 and Captures Qh4xe1

# Pawn Promotion
# When a Pawn moves to the last rank and promotes, the piece promoted to is
# indicated at the end of the move notation, for example e8Q (promoting to
# queen) or sometomes equal or parentheses are used: e8=Q or e8(Q) but in pgn =
# is normally used

# Draws Offer in FIDE Laws of Chess an wual with parentheses '(=)' is used to
# write the offer of a draw next to a move

# Castling is indicate by the special notations 0-0 (for kingside castling) and
# 0-0-0 (for queenside castling). pgn however uses the uppercase letter O (O-O
# and O-O-O ).

# Check A move that places the king in check has the symbol '+'
# appended,alternatively sometimes a dagger † or the abbrebiation "ch" or for
# double check '++'

# Checkmate at the completion of moves can be represented by the symbol '#' or
# occasionally a double dagger ‡ or the "≠" or also by 'X','x' or "×".

# End of Game the notation 1-0 indicates white won and 0-1 indicates Black won
# while ½–½ indicates a draw or Resignation of either black or white due to
# time control or otherwise

# Example Notation of a Series of Moves In 2 cols black/white pairs
# 1. e4      e5
# 2. Nf3     Nc6
# 3. Bb5     a8
# 4. Ba4
# # Horizontally as
# # 1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4

# Annotation Symbols

# On moves
# ! an excellet move
# !! a particulary good--and usually surprising move
# ? a bad move; a mistake
# ?? a blunder
# !? an interesting move that may not be best
# ?! a dubious move or one that may turn out to be bad
# ⌓  a better move than the one played
# □  the only reasonable move, or the only move available

# On Positions
# =  equal chances for both players
# +/= (or ⩲)  White has a slight plus
# =/+ (or ⩱)  Black has a slight plus
# +/− (or ±)  White has a clear plus
# −/+ (or ∓)  Black has a clear plus
# +−  White has a winning advantage
# −+  Black has a winning advantage
# ∞  unclear whether either side has an advantage
# =/∞  whoever is down in material has compensation for it
