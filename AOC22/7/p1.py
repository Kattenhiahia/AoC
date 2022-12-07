input_path = "./AOC22/7/input.txt"
"""
Not done yet
"""
class node_obj():
    size = 0
    name = ""
    parent = None
    children = {}

    def __init__(self,name,parent):
        self.name = name

    def __str__(self):
        return self.name 
    def __repr__(self):
        return self.name + str(self.children)

def print_tree(tree:node_obj):
    print(tree)

def main():
    i = 0
    f = open(input_path, "r")
    working_directory = []
    newdir = None
    newfile = None
    file_tree = node_obj("/", None)
    current_node = file_tree # current_node points to file_tree
    for line in f:
        i += 1
        data = line.strip("\n").split()
        print()
        print(i)
        print(working_directory)
        print(data)
        # print_tree(file_tree)
        if data[0] == "$": # command
            if data[1] == "cd":
                if data[2] == "..":
                    working_directory.pop()
                    print("UPDATE ..")

                    print(str(id(current_node)) +"  "+ current_node.__str__())
                    print(str(id(current_node.parent)) +"  "+ current_node.parent.__str__())
                    current_node = current_node.parent
                    print("to")
                    print(str(id(current_node)) +"  "+ current_node.__str__())
                    print(str(id(current_node.parent)) +"  "+ current_node.parent.__str__())

                elif data[2] == "/":
                    working_directory = ["/"]
                else: # $ cd DIRECTORY
                    working_directory.append(data[2])
                    print("UPDATE "+data[2])

                    print(str(id(current_node)) +"  "+ current_node.__str__())
                    print(str(id(current_node.children[data[2]])) +"  "+ current_node.children[data[2]].__str__())
                    current_node = current_node.children[data[2]]
                    print("to")
                    print(str(id(current_node)) +"  "+ current_node.__str__())
                    print(current_node.children)
            elif data[1] == "ls":
                continue # read the listing into the file_tree
            else:
                print("should not happen")
        else:
            if data[0] == "dir":
                print("creating dir - PRE")
                print(str(id(newdir)) +"  "+ newdir.__str__())
                newdir = node_obj(data[1],current_node) ## current node pekar på sig själv och skapar barn för barnet...
                print("creating dir")
                print(str(id(current_node)) +"  "+ current_node.__str__())
                print(str(id(newdir)) +"  "+ newdir.__str__())
                current_node.children.update({data[1] :newdir})
                print(current_node.children)
                print(current_node.children[data[1]].children)
            else: # NUMBER FILE_NAME
                print("creating file - PRE")
                print(str(id(newfile)) +"  "+ newfile.__str__())
                newfile = node_obj(data[1],current_node)
                newfile.size = int(data[0])
                print("creating file")
                print(str(id(current_node)) +"  "+ current_node.__str__())
                print(str(id(newfile)) +"  "+ newfile.__str__())
                current_node.children.update({data[1] :newfile})
                print(current_node.children)
                print(current_node.children[data[1]].children)



        

if __name__ == "__main__":
    main()