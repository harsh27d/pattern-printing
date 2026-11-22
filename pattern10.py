n = 5

# Print 5 rows
for i in range(n):

    # Print 5 columns
    for j in range(n):

        # Check if it is the boundary of square
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    # Move to next line
    print()