n = 5
for i in range(5, 0, -1):  # Starting from 5 and going backwards
    for j in range(5-i): # Printing spaces at the beginning
        print(" ", end="")# Giving space

    for j in range(i):# Printing stars in each row
        print("*", end=" ")

    print()