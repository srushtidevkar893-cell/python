# INVOICE BORDER PATTERN
row = 7
coloum = 30
for i in range(row):
    for j in range(coloum):
        if i == 0 or i == row - 1 or j == 0 or j == coloum - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# RECEIPY PATTERN
 
row = 8
for i in range(row):
    for j in range(20):
         print("*", end="")
         print()

# Invoice Number Pattern

rows = 5

for i in range(1, rows + 1):
    for j in range(1, 6):
        print(j, end=" ")
    print()


# Receipt Serial Number Pattern

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Star Triangle

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# Inverted Star Pattern

rows = 5

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()