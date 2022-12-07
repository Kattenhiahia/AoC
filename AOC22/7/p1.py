input_path = "./input.txt"
"""
Not done yet
"""
class node_obj():
    node_size = 0
    node_name = ""
    node_parent = ""
    node_children = []


    def __init__(self,name):
        self.node_name = name
    def __str__(self):
        return self.node_name
    def __repr__(self):
        return self.node_name

def main():
    f = open(input_path, "r")
    working_directory = []
    file_tree = [node_obj("/")]
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

            s = file_obj()


        

if __name__ == "__main__":
    main()