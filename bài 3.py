# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:25:14 2026

@author: GHC
"""
#bt số nhỏ thứ hai
n = int(input())
a = list(map(int, input().split()))
b = sorted(set(a))
if len(b) < 2:
    print("Khong co")
else:
    x = b[1]
    for i in range(n):
        if a[i] == x:
            print(i + 1, end=' ')
