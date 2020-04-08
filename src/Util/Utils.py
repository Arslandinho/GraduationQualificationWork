import numpy as np


class Utils:
    @staticmethod
    def chunk(number):
        return sorted(np.histogram(np.arange(number, dtype=int), bins='auto')[0], reverse=True)

    @staticmethod
    def split(x, n):
        if x < n:
            return None
        elif x % n == 0:
            for i in range(n):
                return x // n
        else:
            zp = n - (x % n)
            pp = x // n
            result = []
            for i in range(n):
                if i >= zp:
                    result.append(pp + 1)
                else:
                    result.append(pp)

            return sorted(result, reverse=True)
