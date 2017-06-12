n = 5
m = n
for i in range(0, n+1):
    print " " * n + "#" * i + " " * m + "#" * i
    n = n - 1

print " " * m + "~" * m
