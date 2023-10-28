#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:48:28 2023

@author: tonyyao
"""

def fibonacciGenerator(n):
    if n < 4:
        fibonacci.append(sum(fibonacci))
    else:
        fibonacci.append(sum(fibonacciGenerator(n - 1)[-2:]))
    return fibonacci

while True == False:
    n = int(input("Enter n to calculate Fibonacci Sequence: "))
    fibonacci = [0, 1]
    print(fibonacciGenerator(n))    
    
    