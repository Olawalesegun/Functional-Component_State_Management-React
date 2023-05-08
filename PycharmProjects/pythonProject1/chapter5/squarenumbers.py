# Create a 4-by-4 list containing zeros
square_list = [[0 for j in range(4)] for i in range(4)]

# Set the value of the element in the third row and third column to 1
square_list[2][2] = 1

# Display the list in tabular format
print('  | 0  1  2  3')
print('--+-----------')
for i in range(4):
    print(f'{i} | {"  ".join(str(square_list[i][j]) for j in range(4))}')
