__author__ = 'nbenmena'

import logging
import unittest
from parameterized import parameterized

logger = logging.getLogger('fibo_list')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
logger.addHandler(ch)


def create_fibo(index):

    if index == 0: return [1]

    fibo_list = [1, 1]

    for i in xrange(1, index):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i])

    return fibo_list


def assign_fibo_to_list(fibo_index_list):

    max_fibo_index = max(fibo_index_list)
    fibo_list = create_fibo(max_fibo_index)

    for i, val in enumerate(fibo_index_list):
        fibo_index_list[i] = fibo_list[fibo_index_list[i]]

    return fibo_index_list


class TestFibo(unittest.TestCase):

    @parameterized.expand([
        (2, [1, 1, 2]),
        (1, [1, 1]),
        (0, [1]),
        (3, [1, 1, 2, 3]),
        (4, [1, 1, 2, 3, 5]),
    ])
    def test_fibo(self, index, expected):
        assert create_fibo(index) == expected


    @parameterized.expand([
        ([0], [1]),
        ([0,  0], [1, 1]),
        ([0,  1], [1, 1]),
        ([0,  2], [1, 2]),
        ([6,  3], [13, 3])

    ])
    def test_fibo_list(self, fibo_index_list, reslut_list):
        assert assign_fibo_to_list(fibo_index_list) == reslut_list


if __name__ == '__main__':
    unittest.main()