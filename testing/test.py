from decimal import Decimal


def test1():
    return Decimal('1.1') + Decimal('3.3')


if __name__ == '__main__':
    print(type(Decimal('1.1')))
