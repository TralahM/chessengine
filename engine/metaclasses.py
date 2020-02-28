class ReversedStr:
    def __set__(self, instance, val):
        instance.__bval = val

    def __get__(self, instance, cls=None):
        return instance.__bval[::-1]


class Test:
    bval = ReversedStr()


def printbb(Bb):
    s = Bb.bval
    chs = [['\033[41m%s\033[0m' % j if i % 2 == 0 else '\033[42m%s\033[0m' %
            j for i, j in enumerate(f[::-1])] for f in [s[8*n:8*n+8] for n in range(8)]]
    for row in chs:
        print(''.join(row))
