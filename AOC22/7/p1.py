input_path = "./input.txt"
"""
Not done yet
"""
def main():
    f = open(input_path, "r")
    working_directory = []
    file_tree = {}

    for line in f:
        data = line.strip("\n").split()
        if data[0] == "$": # command
            # print(data)
            if data[1] == "cd":
                if data[2] == "..":
                    working_directory.pop()
                elif data[2] == "/":
                    working_directory.append("/")
                else:
                    working_directory.append(data[2])
            # print(working_directory)
            elif data[1] == "ls":
                continue # read the listing into the file_tree
            else:
                print("should not happen")
        else:
            print(working_directory)
            print (data)


        

if __name__ == "__main__":
    main()