#!/usr/bin/env python3

import unittest
from walki_robotow import eliminate

class TestWalkiRobotow(unittest.TestCase):
    def test_przyklad_1(self):
        test_data = [
            [1, 4],
            [2, 3],
            [3, 2],
            [4, 1]]
        self.assertTrue(eliminate(test_data))

    def test_przyklad_2(self):
        test_data = [
            [1, 1],
            [2, 2]]
        self.assertFalse(eliminate(test_data))

    def test_1ocen(self):
        test_data = []
        for n in range(1, 9):
            test_data.append([n, 8-n])
        self.assertTrue(eliminate(test_data))

    def test_2ocen(self):
        test_data = []
        for n in range(1, 21):
            test_data.append([n, n])
        self.assertFalse(eliminate(test_data))

    def test_3ocen(self):
        test_data = [
            [1,2], [2,1],
            [3,4], [4,3],
            [5,6], [6,5],
            [7,8], [8,7],
            [9,10], [10,9]
        ]
        self.assertTrue(eliminate(test_data))

    def test_4ocen(self):
        test_data = []
        for n in range(1, 100001):
            test_data.append([n, n])
        for n in range(100001, 200001):
            test_data.append([n, 300000 - n + 1])
        self.assertTrue(eliminate(test_data))

    def test_5ocen(self):
        test_data=[[5, 2], [1, 1],[3, 3], [4, 5], [2, 4]]
        self.assertTrue(eliminate(test_data))

    def test_wal2ocen(self):
        test_data = [
            [19, 11], [1, 6],
            [10, 4], [7, 5],
            [14, 15], [3, 12],
            [5, 2], [15, 18],
            [8, 9], [18, 19],
            [11, 14], [4, 16],
            [12, 13], [17, 7],
            [6, 1], [9, 10],
            [16, 8], [2, 3],
            [13, 17], [20, 20]]
        self.assertFalse(eliminate(test_data))