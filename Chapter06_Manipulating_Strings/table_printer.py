"""Print a list of strings into a right justfied table."""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(array):
    """Prints formated array, right justfied by length of longest word in column"""
    col_widths = [0] * len(array)
    # Assign value of longest word in row to colWidth list
    for i, row in enumerate(array):
        for word in row:
            if col_widths[i] < len(word):
                col_widths[i] = len(word)
    # Loop through array[innerLoop][outerloop] to get 0 index in each list in first pass
    # Then 1 index of each list, then 2...
    for x in range(len(array[0])):
        for y in range(len(array)):
            # Print right justified based on col_width of the inner loop index
            print(array[y][x].rjust(col_widths[y]), end=" ")
        print('')

def main():
    """Main Function"""
    print_table(tableData)

if __name__ == '__main__':
    main()
