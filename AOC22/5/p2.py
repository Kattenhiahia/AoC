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
    buffer_list = []

    for line in f:
        data = line.strip("\n")
        if i < 8 and len(data)>1:
            for selector in selector_list:
                if data[selector] != " ":
                    cargo[selector_list.index(selector)].insert(0, data[selector])
        elif i > 9 :#and i < 15:
            buffer_list.clear()
            operation = data.split()
            amount = int(operation[move_amount_index])
            src = int(operation[from_index])-1
            dest = int(operation[to_index])-1
            print(data)
            print("b4")
            print(cargo[src])
            print(cargo[dest])
            for amount_counter in range(amount,0,-1):
                buffer_list.append(cargo[src].pop(-amount_counter))
                print(amount_counter)
                print(buffer_list)
            cargo[dest].extend(buffer_list)
            print("After")
            print(cargo[src])
            print(cargo[dest])
            print("--------------------------------------------------------------")

        i += 1
    somestring = ""
    for item in cargo:
        somestring += item[-1]
    print("result? " + somestring)

if __name__ == "__main__":
    main()
