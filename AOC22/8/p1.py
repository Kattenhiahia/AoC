input_path = "./input.txt"


def main():
    f = open(input_path, "r")
    row = 0
    column = 0
    forest = []
    result = 0
    for line in f:
        data = line.strip("\n")
        forest.append([])
        column = 0
        while column < len(data): 
            forest[row].append(int(data[column]))
            column += 1
        row += 1
    print(forest)
    row, column = 0, 0
    while row < len(forest):
        while column < len(forest[row]):
            if row == 0 and column == 0:
                # upper left corner
            elif row == 0: 
                # top row
            elif column == 0:
                # left-most column
            elif column == len(forest[row])-1:
                # right-most column
            elif row == len(forest)-1:
                # last row
            elif column == len(forest[row]) and row == len(forest)-1:
                # bottom right corner
            else:
                              
            tree = forest[row][column]
            print(tree)
            
            column += 1
        row += 1

if __name__ == "__main__":
    main()