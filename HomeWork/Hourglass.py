n = 5
# Top
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
# Bottom
for i in range(2, n + 1):
    print(" " * (n - i) + "* " * i)
