from bitboard import Bitboard


def clear_rank(i: int):
    return ~Bitboard(f'{sum([2**i for i in range(8*(i-1),i*8)]):064b}')


def clear_file(i: int):
    return ~Bitboard(f'{sum([2**i for i in range(i-1,64,8)]):064b}')
