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
:CREATED: 	2020-02-04  02:00

:FILENAME:	pieces.py
=======================================================================


    DESCRIPTION OF pieces MODULE:

Defining the Chess Pieces
"""


class Piece(object):
    """
    Abstract Chess Piece
    Derived classes should implement their own initializer,
    str repr  the following interfaces:
    move()
    get_legal_moves()
    attributes:
    name:str, position:Position,prev_position:Position

    """

    def __str__(self):
        raise NotImplementedError(self)

    def move(self):
        raise NotImplementedError(self)

    def get_legal_moves(self):
        raise NotImplementedError(self)


class King(Piece):
    def __init__(self, color: int):
        self.color = color
        self.whites = "♔"
        self.blacks = "♚"


class Queen(Piece):
    def __init__(self, color: int):
        self.color = color
        self.whites = "♕"
        self.blacks = "♛"


class Rook(Piece):
    def __init__(self, color: int, kingside: int):
        self.color = color
        self.whites = "♖"
        self.blacks = "♜"
        self.kingside = kingside


class Bishop(Piece):
    def __init__(self, color: int, kingside: int):
        self.color = color
        self.whites = "♗"
        self.blacks = "♝"
        self.kingside = kingside


class Knight(Piece):
    def __init__(self, color: int, kingside: int):
        self.color = color
        self.whites = "♘"
        self.blacks = "♞"
        self.kingside = kingside


class Pawn(Piece):
    def __init__(self, color: int, fileid: str):
        self.color = color
        self.whites = "♙"
        self.blacks = "♟"
        self.fileid = fileid
