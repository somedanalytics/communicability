#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Orcun Gumus
import unittest
import networkx

from communicability import communicability


class TestCommunicabilityMethod(unittest.TestCase):

    def test_basic_calculate(self):
        network = networkx.Graph(
            [(0, 2),
             (1, 2),
             (2, 3),
             (2, 4),
             (3, 6),
             (3, 5),
             (4, 6),
             (4, 7),
             (6, 8),
             (5, 8),
             (6, 9),
             (7, 9),
             (9, 10),
             (8, 10),
             (10, 11),
             (10, 12)])

        # Example Graph:
        # https://snag.gy/YMubXO.jpg

        point = communicability(network, [2], [10], 3)
        self.assertAlmostEqual(point, 6.0/24.0, delta=0.001)

        point = communicability(network, [2], [5], 3)
        self.assertAlmostEqual(point, 10.0/24.0 + 1/2, delta=0.001)


if __name__ == '__main__':
    unittest.main()
