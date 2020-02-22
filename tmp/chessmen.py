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

:FILENAME:	chessmen.py
=======================================================================


    DESCRIPTION OF chessmen MODULE:

Defining the Chess Pieces
"""
from chessboard import Position


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
        self.position = self.initial_position

    @property
    def initial_position(self):
        if self.color:
            return Position(fileid='e', rankid=1)
        else:
            return Position(fileid='e', rankid=8)


class Queen(Piece):
    def __init__(self, color: int):
        self.color = color
        self.position = self.initial_position

    @property
    def initial_position(self):
        if self.color:
            return Position(fileid='d', rankid=1)
        else:
            return Position(fileid='d', rankid=8)


class Rook(Piece):
    def __init__(self, color: int, kingside: int):
        self.color = color
        self.kingside = kingside
        self.position = self.initial_position

    @property
    def initial_position(self):
        if self.color:
            if not self.kingside:
                return Position(fileid='a', rankid=1)
            else:
                return Position(fileid='h', rankid=1)
        else:
            if not self.kingside:
                return Position(fileid='a', rankid=8)
            else:
                return Position(fileid='h', rankid=8)


class Bishop(Piece):
    def __init__(self, color: int, kingside: int):
        self.color = color
        self.kingside = kingside
        self.position = self.initial_position

    @property
    def initial_position(self):
        if self.color:
            if not self.kingside:
                return Position(fileid='c', rankid=1)
            else:
                return Position(fileid='f', rankid=1)
        else:
            if not self.kingside:
                return Position(fileid='c', rankid=8)
            else:
                return Position(fileid='f', rankid=8)


class Knight(Piece):
    def __init__(self, color: int, kingside: int):
        self.color = color
        self.kingside = kingside
        self.position = self.initial_position

    @property
    def initial_position(self):
        if self.color:
            if not self.kingside:
                return Position(fileid='b', rankid=1)
            else:
                return Position(fileid='g', rankid=1)
        else:
            if not self.kingside:
                return Position(fileid='b', rankid=8)
            else:
                return Position(fileid='g', rankid=8)


class Pawn(Piece):
    def __init__(self, color: int, fileid: str):
        self.color = color
        self.fileid = fileid
        self.position = self.initial_position

    @property
    def initial_position(self):
        if self.color:
            return Position(fileid=self.fileid, rankid=2)
        else:
            return Position(fileid=self.fileid, rankid=7)
