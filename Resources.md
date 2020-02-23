# Resources
[TalkChess]( talkchess.com )
[Chess Programming Wikispaces]( chessprogramming.wikispaces.com )
Bruce mooreland
[Robert Hyatt](www.cis.uab.edu/hyatt )
[Computer Chess](www.computerchess.org.uk/ccrl/4040/ )
WinBoard GUI/Xboard
[Play With Arena GUI](playwitharena.com)
UCI Protocol

# Outline
Name of Engine Cheza
Definitions
## board structure
- Pieces
- pawns[black,white,all]
- Kingsquare[black,white]
- side_to_move
- en_pass square
- fiftymovecounter
- ply [moves in current search]
- histply [record repetitions]
- positionKey
- piecesNum[type_of_piece]
- noofbigpieces[by_color]
- minorpieces[by_color] num
- majorpieces[by_color] num
- History:Undo_struct

WKCA,WQCA,BKCA,BQCA [1,2,4,8]=> 0000
+ WhiteKingSideCastle,WhiteQueenSideCastle
+ BlackKingCastle,BlackQueenCastle
## Recording history of moves
2048 half moves or 1024 moves per game in history
UNDO_struct( move:int,castleperm,enpass,fiftymove,poskey ) array of 2048 size
List of Pieces
- Array of each piece by type and color to be updated at runtime
