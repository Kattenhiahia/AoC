input_path = "./input.txt"

   


def main():
    f = open(input_path, "r")
    inp = []
    groups = []
    curr_group_val = 0
    max_val = 0
    group = 0
    for line in f:
        data = line.strip("\n")
        if data == "":
            groups.append(curr_group_val)
            if curr_group_val > max_val:
                max_val = curr_group_val
            curr_group_val = 0
            group += 1
        else:
            curr_group_val += int(data)
    
    print(sorted(groups))
    print("max value is: " + str(sorted(groups)[-1]))
    print("sum of top three is: " + str(sorted(groups)[-1]+sorted(groups)[-2]+sorted(groups)[-3]))
             

if __name__ == "__main__":
    main()