# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:40:52 2026

@author: GHC
"""

#sap xep mang
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    for j in range(i + 1, n):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

for x in a:
    print(x, end=" ")