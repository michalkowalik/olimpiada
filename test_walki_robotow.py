#!/usr/bin/env python3

import unittest
from walki_robotow import eliminate_pairs

class TestWalkiRobotow(unittest.TestCase):
    def test_przyklad_1(self):
        test_data = [
            [1, 4],
            [2, 3],
            [3, 2],
            [4, 1]]
        self.assertTrue(eliminate_pairs(test_data))

    def test_przyklad_2(self):
        test_data = [
            [1, 1],
            [2, 2]]
        self.assertFalse(eliminate_pairs(test_data))

    def test_1ocen(self):
        test_data = []
        for n in range(1, 9):
            test_data.append([n, 9-n])
        self.assertTrue(eliminate_pairs(test_data))

    def test_2ocen(self):
        test_data = []
        for n in range(1, 21):
            test_data.append([n, n])
        self.assertFalse(eliminate_pairs(test_data))

    def test_3ocen(self):
        test_data = [
            [1,2], [2,1],
            [3,4], [4,3],
            [5,6], [6,5],
            [7,8], [8,7],
            [9,10], [10,9]
        ]
        self.assertTrue(eliminate_pairs(test_data))

    def test_4ocen(self):
        test_data = []
        for n in range(1, 100001):
            test_data.append([n, n])
        for n in range(100001, 200001):
            test_data.append([n, 300000 - n + 1])
        self.assertTrue(eliminate_pairs(test_data))

    def test_5ocen(self):
        test_data=[[5, 2], [1, 1],[3, 3], [4, 5], [2, 4]]
        self.assertTrue(eliminate_pairs(test_data))

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
        self.assertFalse(eliminate_pairs(test_data))

    def test2in(self):
        test_data = [
            [3, 5],
            [4, 3],
            [2, 1],
            [1, 2],
            [5, 4]]
        self.assertTrue(eliminate_pairs(test_data))

    def test1in(self):
        test_data = [
            [0, 3],
            [5, 0],
            [3, 2],
            [4, 4],
            [1, 5],
            [2, 1]]
        self.assertTrue(eliminate_pairs(test_data))

    def test17(self):
        data = [
            [2,2],
            [1,3],
            [3,1]]
        self.assertFalse(eliminate_pairs(data))

    def test25(self):
        data = [
            [3, 3],
            [1, 5],
            [4, 1], 
            [6, 0],
            [5, 4],
            [2, 6],
            [0, 2]]
        self.assertTrue(eliminate_pairs(data))

    def test35(self):
        data = [
            [0, 5],
            [1, 1],
            [3, 4],
            [4, 6],
            [5, 2],
            [6, 0],
            [2, 3]]
        self.assertTrue(eliminate_pairs(data))

    def test87(self):
        data = [
            [0, 0],
            [5, 3],
            [1, 1],
            [3, 6],
            [2, 2],
            [6, 4],
            [4, 5]]
        self.assertTrue(eliminate_pairs(data))