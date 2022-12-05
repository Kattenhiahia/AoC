input_path = "./input.txt"

   


def main():
    f = open(input_path, "r")
    inp = []
    groups = []
    curr_group_val = 0
    max_val = 0
    group = 0
    for line in f:
        print("this is group: " + str(group))
        data = line.strip("\n")
        if data == "":
            groups.append(curr_group_val)
            if curr_group_val > max_val:
                max_val = curr_group_val
            curr_group_val = 0
            group += 1
        else:
            curr_group_val += int(data)


    print("max value is: " + str(max_val))
             

if __name__ == "__main__":
    main()