class Bitboard:
    def __init__(self, bitstr=f'{0:064b}', * args, **kwargs):
        self.bval = bitstr

    @property
    def as_int(self):
        return int(self.bval, 2)

    def __str__(self):
        return self.bval

    def __repr__(self):
        return self.bval

    def __and__(self, other):
        return self.__class__(f'{self.as_int&other.as_int:064b}')

    def __or__(self, other):
        return self.__class__(f'{self.as_int|other.as_int:064b}')

    def __xor__(self, other):
        return self.__class__(f'{self.as_int^other.as_int:064b}')

    def __lshift__(self, N: int):
        return self.__class__(f'{self.as_int<<N:064b}')

    def __rshift__(self, N: int):
        return self.__class__(f'{self.as_int>>N:064b}')

    def __invert__(self):
        return self.__class__(self.bval.replace('1', '2').replace('0', '1').replace('2', '0'))
