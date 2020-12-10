from decimal import Decimal

import pytest
import yaml

from study.calc import Calc


class Test_Cal:
    with open('../datas/cal.yml') as f:
        params = yaml.safe_load(f)

    def setup_class(self):
        self.cal = Calc()

    @pytest.mark.add
    @pytest.mark.parametrize(params[0], params[1], ids=params[2]['ids'])
    # ('a', 'b', 'result'),
    #                      [(1, 1, 2),
    #                       (2, 2, 4),
    #                       (1000, 1000, 2000),
    #                       (1.2, 2.2, Decimal('3.4')),
    #                       (0.01, 0.00, Decimal('0.01')),
    #                       ],
    #                      ids=['int', 'int', 'bigint', 'float', 'double'])
    def test_add(self, calcomment, a, b, result):
        assert result == self.cal.add(a, b)

    @pytest.mark.div
    @pytest.mark.parametrize(('a', 'b', 'result'),
                             [(1, 1, 1),
                              (4, 5, Decimal('0.8')),
                              (5, 3, Decimal('1.6666666666667')),
                              (1.2, 2.2, Decimal('0.54545454545455'))
                              ],
                             ids=['int', 'int', 'bigint', 'double'])
    def test_div(self, calcomment, a, b, result):
        assert result == self.cal.div(a, b)
