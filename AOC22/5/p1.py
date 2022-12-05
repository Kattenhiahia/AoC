input_path = "./input.txt"
selector_list = [1,5,9,13,17,21,25,29,33]
move_amount_index = 1
from_index = 3
to_index = 5

def main():
    f = open(input_path, "r")
    i = 0
    cargo = [[],[],[],[],[],[],[],[],[]]
    amount, src, dest = 0, 0, 0

    for line in f:
        data = line.strip("\n")
        if i < 8 and len(data)>1:
            for selector in selector_list:
                if data[selector] != " ":
                    cargo[selector_list.index(selector)].insert(0, data[selector])
        elif i > 9:
            operation = data.split()
            amount = int(operation[move_amount_index])
            src = int(operation[from_index])-1
            dest = int(operation[to_index])-1
            print 
            for amount_counter in range(1,amount+1):
                print("b4")
                print(cargo[src])
                print(cargo[dest])
                cargo[dest].append(cargo[src].pop())
                print("after")
                print(cargo[src])
                print(cargo[dest])
            print("-----------------")

        i += 1
    somestring = ""
    for item in cargo:
        somestring += item[-1]
    print("result? " + somestring)
    print(cargo)
    print(i)

if __name__ == "__main__":
    main()