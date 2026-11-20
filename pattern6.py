n=5
for i in range (1 , n+1):  # Runs the loop from 1 to 5
    for j in range(n-i):  # Prints spaces before the stars
        print(" " , end = " ")  # Prints space on the same line
    for k in range(i):   # Controls the number of stars
        print("*", end=" ")
    print()

