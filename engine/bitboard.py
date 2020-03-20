class Bitboard:
    def __init__(self, bitstr=f'{0:064b}', * args, **kwargs):
        if isinstance(bitstr, int):
            self.bval = f'{bitstr:064b}'
        self.bval = bitstr

    @property
    def as_int(self):
        return int(self.bval, 2)

    @property
    def lsb(self):
        return self & -self

    @property
    def with_reset_lsb(self):
        return self & self.__class__(f'{self.as_int-1:064b}')

    def __str__(self):
        return self.bval

    def __repr__(self):
        return self.bval

    def __add__(self, other):
        return self.__class__(f'{self.as_int+other.as_int:064b}')

    def __neg__(self):
        return self.__class__(f'{self.as_int*-1:064b}')

    def __sub__(self, other):
        return self.__class__(f'{self.as_int-other.as_int:064b}')

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
