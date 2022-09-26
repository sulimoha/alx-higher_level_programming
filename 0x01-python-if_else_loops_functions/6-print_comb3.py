#!/usr/bin/python3
j = 10
k = 9
i = 0
a = 1
for i in range(0, k):
    for j in range(a, 10):
        if (i != j):
            if (i == 8 and j == 9):
                print("{:d}{:d}".format(i, j), end="\n")
            else:
                print("{:d}{:d}".format(i, j), end=", ")
    k = k - 1
    a = a + 1
