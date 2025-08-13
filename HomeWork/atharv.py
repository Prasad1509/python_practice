def print_atharv():
    for row in range(4):
        # Letter A
        for col in range(7):
            if ((col == 0 or col == 6) and row != 0) or ((row == 0 or row == 2) and 0 < col < 6):
                print("*", end="")
            else:
                print(" ", end="")
        print(" ", end="")

        # Letter T
        for col in range(7):
            if row == 0 or col == 3:
                print("*", end="")
            else:
                print(" ", end="")
        print(" ", end="")

        # Letter H
        for col in range(7):
            if col == 0 or col == 6 or row == 2:
                print("*", end="")
            else:
                print(" ", end="")
        print(" ", end="")

        # Letter A (again)
        for col in range(7):
            if ((col == 0 or col == 6) and row != 0) or ((row == 0 or row == 2) and 0 < col < 6):
                print("*", end="")
            else:
                print(" ", end="")
        print(" ", end="")

        # Letter R
        for col in range(7):
            if col == 0 or (row == 0 or row == 2) and col < 6 or (col == 6 and row == 1) or (row == 3 and col == 3):
                print("*", end="")
            else:
                print(" ", end="")
        print(" ", end="")

        # Letter V (exactly as you want)
        for col in range(7):
            if (row == 0 and (col == 0 or col == 6)) or \
               (row == 1 and (col == 1 or col == 5)) or \
               (row == 2 and (col == 2 or col == 4)) or \
               (row == 3 and col == 3):
                print("*", end="")
            else:
                print(" ", end="")

        print()  # Move to next row

print_atharv()
