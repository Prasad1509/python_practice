def print_prasad():
    for row in range(7):
        # Letter P
        for col in range(7):
            if col == 0 or (row == 0 or row == 3) and col < 6 or (col == 6 and row > 0 and row < 3):
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

        # Letter R
        for col in range(7):
            if col == 0 or (row == 0 or row == 3) and col < 6 or (col == 6 and row > 0 and row < 3) or (row - col == 3):
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

        # Letter A
        for col in range(7):
            if (col == 0 or col == 6) and row != 0 or (row == 0 or row == 3) and (col > 0 and col < 6):
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

        # Letter S
        for col in range(7):
            if row == 0 or row == 3 or row == 6 or (col == 0 and row < 3) or (col == 6 and row > 3):
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

        # Letter A (again)
        for col in range(7):
            if (col == 0 or col == 6) and row != 0 or (row == 0 or row == 3) and (col > 0 and col < 6):
                print("*", end="")
            else:
                print(" ", end="")
        print("  ", end="")

        # Letter D
        for col in range(7):
            if col == 0 or (col == 6 and row != 0 and row != 6) or ((row == 0 or row == 6) and col < 6):
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Newline for next row

print_prasad()
