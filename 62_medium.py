#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:17:48 2024

@author: tonyyao
"""

class Solution:
    store = dict()
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        elif (max(m, n), min(m, n)) in self.store.keys():
            return self.store[(max(m, n), min(m, n))]
        else:
            self.store[(max(m, n), min(m, n))] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
            return self.store[(max(m, n), min(m, n))]