n = 5

# Upper Half
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Lower Half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
