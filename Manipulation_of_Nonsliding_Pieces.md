Nonsliding Pieces
=================

Why nonsliding?
---------------

The nonsliding piece on the chess board are the **King, Knight,** and
**Pawn**. We differentiate them from the other sliding pieces since the
algorithms for nonsliding pieces are simpler to understand and compute
than for sliding pieces. Technically the pawn is also a sliding piece
under very special circumstances, but we can still treat it as if it was
a nonsliding piece.

While many bitboard algorithms can be computed with nonsliding pieces,
we are currently only interested in the most basic of computation such
as where can a piece move, where can it attack, and the combination of
those two resulting in the valid moves for the piece. The valid moves
shall be congnizant of other pieces on the board as well, as a pawn
can't move to a place that holds or attack another piece of the same
color. At this point, we aren't worried about a piece moving into
danger as detection of that is talked about later.

Resolution of Valid Moves
-------------------------

So how do we start to formulate how to determine the valid moves for a
nonsliding piece in the context of a board containing multiple pieces?
For example, a white piece can not attack another white piece, nor move
there. We will see how step by step the information from the lookup
tables are joined and then filtered by what is actually on the board to
produce true valid moves.

The bitboards that we will be ultimately computing are:
**WhiteKingValid, BlackKindValid, WhiteKnightValid, BlackKnightValid,
WhitePawnValid,** and **BlackPawnValid**. The differences in the
algorithms between different colors of the same piece style are very
regular--mainly shifting direction and changing which color side's
pieces affect the current piece in question.

These bitboard computations shall only be for **specific** pieces on the
chess board such that a human might specify when playing against another
human player. However, it will be shown later how it is possible to use
these algorithms for all the pieces of the same kind and color on the
board at the same time.

**WARNING: For the purposes of the discussion on this page: check,
checkmate detection, and valid castling moves concerning the king's (of
any color) computed valid moves and en passant of a pawn will be delayed
until later in this tutorial, where we will revisit them and complete
their description.**

### Movement of the King

Inspection of the King (of any color) shows us that a white and black
king move identically (with respect to their color) when placed on the
same square on a chess board. We are going to mark every place an
arbitrary king can move with a number so we can see how to calculate
each location to see if it is available for movement or attacking and
then logcally OR them all together to form the valid movement bitboard.
Here is the numbering scheme for the King with its positional bitboard
on the right.

+-----------------------------------+-----------------------------------+
|   --- --- --- --- --- --- --- --- |   --- --- --- --- --- --- --- --- |
|                                   |   0   0   0   0   0   0   0   0   |
|                                   |   0   0   0   0   0   0   0   0   |
|                                   |   0   0   0   0   0   0   0   0   |
|           1   2   3               |   0   0   0   0   0   0   0   0   |
|           8   K   4               |   0   0   0   1   0   0   0   0   |
|           7   6   5               |   0   0   0   0   0   0   0   0   |
|                                   |   0   0   0   0   0   0   0   0   |
|                                   |   0   0   0   0   0   0   0   0   |
|   --- --- --- --- --- --- --- --- |   --- --- --- --- --- --- --- --- |
+-----------------------------------+-----------------------------------+

So, suppose I wanted to see if the king, suppose white, could move into
spot 8, I could take the above bitboard and shift it right **(because a
shift right is toward the LSB side of the 64 bit integer, remember the
representation!)** 1 bit. The green location is the new bitboard which
represents a possible movement left, the yellow location is where the
king used to be, for our reference. We could now take this bitboard and
logically AND it against the complement of all of the white pieces to
see if the king could actually move to spot 8.

  --- --- --- --- --- --- --- ---
  0   0   0   0   0   0   0   0
  0   0   0   0   0   0   0   0
  0   0   0   0   0   0   0   0
  0   0   0   0   0   0   0   0
  0   0   1   0   0   0   0   0
  0   0   0   0   0   0   0   0
  0   0   0   0   0   0   0   0
  0   0   0   0   0   0   0   0
  --- --- --- --- --- --- --- ---

We will do something similar for all of the rest of the spots by
shifting the position of the king the correct number of bits to mark off
another spot it could have moved to on the board and then logically
ORing all of those partial spot movement boards together. But what about
if the King is in file A? Surely a shift right by one bit will create a
place the king cannot move (incorrect move marked in blue):

+-----------------------------------+-----------------------------------+
|   --- --- --- --- --- --- --- --- |   --- --- --- --- --- --- --- --- |
|   0   0   0   0   0   0   0   0   |   0   0   0   0   0   0   0   0   |
|   0   0   0   0   0   0   0   0   |   0   0   0   0   0   0   0   0   |
|   0   0   0   0   0   0   0   0   |   0   0   0   0   0   0   0   0   |
|   0   0   0   0   0   0   0   0   |   0   0   0   0   0   0   0   0   |
|   1   0   0   0   0   0   0   0   |   0   0   0   0   0   0   0   0   |
|   0   0   0   0   0   0   0   0   |   0   0   0   0   0   0   0   1   |
|   0   0   0   0   0   0   0   0   |   0   0   0   0   0   0   0   0   |
|   0   0   0   0   0   0   0   0   |   0   0   0   0   0   0   0   0   |
|   --- --- --- --- --- --- --- --- |   --- --- --- --- --- --- --- --- |
+-----------------------------------+-----------------------------------+

We solve this by simply clearing the king from file A (if it happens to
be there) when performing the checks for spots 1, 8, and 7, and clearing
the king from file H (if it happens to be there) checking for spots 3,
4, and 5. If the king gets cleared out, then a bitboard full of zeros is
made upon which any shifting in any direction still produces a bitboard
full of zeros, and that means no valid move in this context. So for the
above example for the computation of spot 8 when a king is on A4:

+-------------+-------------+-------------+-------------+-------------+
|   --- --- - | **AND**     |   --- --- - | **=**       |   --- --- - |
| -- --- ---  |             | -- --- ---  |             | -- --- ---  |
| --- --- --- |             | --- --- --- |             | --- --- --- |
|   0   0   0 |             |   0   1   1 |             |   0   0   0 |
|    0   0    |             |    1   1    |             |    0   0    |
| 0   0   0   |             | 1   1   1   |             | 0   0   0   |
|   0   0   0 |             |   0   1   1 |             |   0   0   0 |
|    0   0    |             |    1   1    |             |    0   0    |
| 0   0   0   |             | 1   1   1   |             | 0   0   0   |
|   0   0   0 |             |   0   1   1 |             |   0   0   0 |
|    0   0    |             |    1   1    |             |    0   0    |
| 0   0   0   |             | 1   1   1   |             | 0   0   0   |
|   0   0   0 |             |   0   1   1 |             |   0   0   0 |
|    0   0    |             |    1   1    |             |    0   0    |
| 0   0   0   |             | 1   1   1   |             | 0   0   0   |
|   1   0   0 |             |   0   1   1 |             |   0   0   0 |
|    0   0    |             |    1   1    |             |    0   0    |
| 0   0   0   |             | 1   1   1   |             | 0   0   0   |
|   0   0   0 |             |   0   1   1 |             |   0   0   0 |
|    0   0    |             |    1   1    |             |    0   0    |
| 0   0   0   |             | 1   1   1   |             | 0   0   0   |
|   0   0   0 |             |   0   1   1 |             |   0   0   0 |
|    0   0    |             |    1   1    |             |    0   0    |
| 0   0   0   |             | 1   1   1   |             | 0   0   0   |
|   0   0   0 |             |   0   1   1 |             |   0   0   0 |
|    0   0    |             |    1   1    |             |    0   0    |
| 0   0   0   |             | 1   1   1   |             | 0   0   0   |
|   --- --- - |             |   --- --- - |             |   --- --- - |
| -- --- ---  |             | -- --- ---  |             | -- --- ---  |
| --- --- --- |             | --- --- --- |             | --- --- --- |
+-------------+-------------+-------------+-------------+-------------+

Then take the resultant bitboard from the operation above (which is
empty) and shift it right one bit, which ends up being:

  --- --- --- --- --- --- --- ---
  0   0   0   0   0   0   0   0
  0   0   0   0   0   0   0   0
  0   0   0   0   0   0   0   0
  0   0   0   0   0   0   0   0
  0   0   0   0   0   0   0   0
  0   0   0   0   0   0   0   0
  0   0   0   0   0   0   0   0
  0   0   0   0   0   0   0   0
  --- --- --- --- --- --- --- ---

Hence, no allowable movement for spot 8.

For spots 2 and 6, (technically spots 1, 2, 3 and 5, 6, 7) we don't
have to do anything with respect to the ranks because if the shifting of
the bitboard takes the physical location off of the board either on the
white side or the black side due to shifting too far, then we are simply
left with a bitboard of all zeros--no valid moves. This is precisely
what we want.

Given the above information, here is how we extend it to calculate every
possible position of movement and attack for any color king.

    /* LookupTables is a structure which contains all precomputed lookup tables */
    Bitboard compute_king_incomplete(Bitboard king_loc, Bitboard own_side, LookupTables *tbls)
    {
        /* we can ignore the rank clipping since the overflow/underflow with
            respect to rank simply vanishes. We only care about the file
            overflow/underflow. */

        king_clip_file_h = king_loc & tbls->ClearFile[FILE_H];
        king_clip_file_a = king_loc & tbls->ClearFile[FILE_A];

        /* remember the representation of the board in relation to the bitindex
            when looking at these shifts.... */
        spot_1 = king_clip_file_h << 7;
        spot_2 = king_loc << 8;
        spot_3 = king_clip_file_h << 9;
        spot_4 = king_clip_file_h << 1;

        spot_5 = king_clip_file_a >> 7;
        spot_6 = king_loc >> 8;
        spot_7 = king_clip_file_a >> 9;
        spot_8 = king_clip_file_a >> 1;

        king_moves = spot_1 | spot_2 | spot_3 | spot_4 | spot_5 | spot_6 |
                            spot_7 | spot_8;

        KingValid = king_moves & ~own_side;

        /* compute only the places where the king can move and attack. The caller
            will interpret this as a white or black king. */
        return KingValid;
    }

The important thing to realize above is that we are using the bitboard
of the position of the king **itself** as the seed value for the
calculation of the masks for movement determination.

Here is an example for how you'd call the above function to determine
how a White King on E1 could move if it knew where all of its white
pieces were:

    WhiteKingValid = compute_king_incomplete(Piece[E1], AllWhitePieces, lookup_tables);

Here is a [detailed](./whitekingvalid_incomplete.html) visualization of
the above code for a White King at E1 on a sample board filled with
other pieces.

### BlackKingValid

You'll notice that the code for this case is almost identical than for
the above case. I can use the same exact function call above to compute
a Black King on F4 instead:

    BlackKingValid = compute_king_incomplete(Piece[F4], AllBlackPieces, lookup_tables);

Here is a [detailed](./blackkingvalid_incomplete.html) visualization of
the above code for a Black King at F4 on a sample board filled with
other pieces.

### WhiteKnightValid

We will use the same technique as above to compute how a knight moves.
We can also use the same algorithm for both the white and black nights
since they move identically (with repsect to their own kind) when a
knight of each color is placed onto the same square. Here is a labelling
of each spot a knight can move or attack with the knight's position
bitboard on the right:

+-----------------------------------+-----------------------------------+
|   --- --- --- --- --- --- --- --- |   --- --- --- --- --- --- --- --- |
|                                   |   0   0   0   0   0   0   0   0   |
|                                   |   0   0   0   0   0   0   0   0   |
|           2       3               |   0   0   0   0   0   0   0   0   |
|       1               4           |   0   0   0   0   0   0   0   0   |
|               N                   |   0   0   0   1   0   0   0   0   |
|       8               5           |   0   0   0   0   0   0   0   0   |
|           7       6               |   0   0   0   0   0   0   0   0   |
|                                   |   0   0   0   0   0   0   0   0   |
|   --- --- --- --- --- --- --- --- |   --- --- --- --- --- --- --- --- |
+-----------------------------------+-----------------------------------+

The only new concept is an extension of the clipping procedure that we
learned from the king algorithm. The Knight has two overflow files
instead of one. For example, if a white knight was in location B4, spots
1 and 8 would be clipped out (otherwise the shift to compute them will
rollover to the other side of the board). If the white knight was on A4,
then spots 1, 2, 7, and 8 would all be clipped. The below algorithm
explicitly takes care of clipping files A, B, and G, H for each
individual movement/attack spot.

    /* LookupTables is a structure which contains all precomputed lookup tables */
    Bitboard compute_knight(Bitboard knight_loc, Bitboard own_side, LookupTables *tbls)
    {
        /* we can ignore the rank clipping since the overflow/underflow with
            respect to rank simply vanishes. We only care about the file
            overflow/underflow which is much more work for a knight. */

        spot_1_clip = tbls->ClearFile[FILE_A] & tbls->ClearFile[FILE_B];
        spot_2_clip = tbls->ClearFile[FILE_A];
        spot_3_clip = tbls->ClearFile[FILE_H];
        spot_4_clip = tbls->ClearFile[FILE_H] & tbls->ClearFile[FILE_G];

        spot_5_clip = tbls->ClearFile[FILE_H] & tbls->ClearFile[FILE_G];
        spot_6_clip = tbls->ClearFile[FILE_H];
        spot_7_clip = tbls->ClearFile[FILE_A];
        spot_8_clip = tbls->ClearFile[FILE_A] & tbls->ClearFile[FILE_B];

        /* The clipping masks we just created will be used to ensure that no
            under or overflow positions are computed when calculating the
            possible moves of the knight in certain files. */

        spot_1 = (knight_loc & spot_1_clip) << 6;
        spot_2 = (knight_loc & spot_2_clip) << 15;
        spot_3 = (knight_loc & spot_3_clip) << 17;
        spot_4 = (knight_loc & spot_4_clip) << 10;

        spot_5 = (knight_loc & spot_5_clip) >> 6;
        spot_6 = (knight_loc & spot_6_clip) >> 15;
        spot_7 = (knight_loc & spot_7_clip) >> 17;
        spot_8 = (knight_loc & spot_8_clip) >> 10;

        KnightValid = spot_1 | spot_2 | spot_3 | spot_4 | spot_5 | spot_6 |
                        spot_7 | spot_8;

        /* compute only the places where the knight can move and attack. The
            caller will determine if this is a white or black night. */
        return KnightValid & ~own_side;
    }

It would be invoked like this for a White Knight on B4:

    WhiteKnightValid = compute_knight(Piece[B4], AllWhitePieces, lookup_tables);

Here is a [detailed](./whiteknightvalid.html) visualization of the above
code for a White Knight at B4 on a sample board filled with other
pieces.

### BlackKnightValid

You'll notice that the code for this case is almost identical than for
the above case. I can use the same exact function call above to compute
a Black Knight on D4 instead:

    BlackKnightValid = compute_knight(Piece[D4], AllBlackPieces, lookup_tables);

Here is a [detailed](./blackknightvalid.html) visualization of the above
code for a Black Knight at D4 on a sample board filled with other
pieces.

### WhitePawnValid

How would we compute the valid movements of the pawn at D2? These
particular algorithms are shift sensitive. Meaning if I was asking about
a black pawn, I will have to flip the shifts to be the other direction
(along with a few other change, like **AllBlackPieces** becoming
**AllWhitePieces**).


    /* unlike the king and knight algorithms, pawns move in fundamentally
        different ways for each color, so we need to seperate functions to
        deal with the change in shifting and the opponents color. This is
        the one for computing a white pawn movement. */
    Bitboard compute_white_pawns(Bitboard white_pawn_loc, Bitboard all_pieces,
        Bitboard all_black_pieces, LookupTables *lbts)
    {
        /* check the single space infront of the white pawn */
        white_pawn_one_step = (white_pawn_loc << 8) & ~all_pieces;

        /* for all moves that came from rank 2 (home row) and passed the above
            filter, thereby being on rank 3, check and see if I can move forward
            one more */
        white_pawn_two_steps =
            ((white_pawn_one_step & MaskRank[RANK_3]) << 8) & ~all_pieces;

        /* the union of the movements dictate the possible moves forward
            available */
        white_pawn_valid_moves = white_pawn_one_step | white_pawn_two_steps;

        /* next we calculate the pawn attacks */

        /* check the left side of the pawn, minding the underflow File A */
        white_pawn_left_attack = (white_pawn_loc & ClearFile[FILE_A]) << 7;

        /* then check the right side of the pawn, minding the overflow File H */
        white_pawn_right_attack = (white_pawn_loc & ClearFile[FILE_H]) << 9;

        /* the union of the left and right attacks together make up all the
            possible attacks */
        white_pawn_attacks = white_pawn_left_attack | white_pawn_right_attack;

        /* Calculate where I can _actually_ attack something */
        white_pawn_valid_attacks = white_pawn_attacks & all_black_pieces;

        /* then we combine the two situations in which a white pawn can legally
            attack/move. */
        WhitePawnValid = white_pawn_valid_moves | white_pawn_valid_attacks;

        return WhitePawnValid;
    }

It would be invoked like this for a White Pawn on B2:

    WhitePawnValid = compute_white_pawn(Piece[B2], AllPieces, AllBlackPieces, lookup_tables);

Uh, what just happened?

We'll slowly dissect the expressions above so you can see visually what
happens. A pawn takes some work to compute because it is the only piece
that can move to a square it can't attack and can attack when there is
a square occupied by an opponent to which it cannot move otherwise in
addition to special movement rules for the initial move. We **must**
keep these kinds of constraints when bitboard algorithms are designed.

Here it is in [slow motion](./whitepawnvalid_incomplete.html).
