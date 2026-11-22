n = 5  #Set the n = 5
# Print rows
for i in range(1, n + 1):
    # Print columns
    for j in range(1, i + 1):
        # Print stars on boundary
        if j == 1 or j == i or i == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()