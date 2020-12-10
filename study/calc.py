from decimal import *


class Calc:
    getcontext().prec = 14

    def add(self, a, b):
        return Decimal(str(a)) + Decimal(str(b))

    def div(self, a, b):
        return Decimal(str(a)) / Decimal(str(b))
