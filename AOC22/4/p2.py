input_path = "./input.txt"
assignments = {}
def main():
    dupe_count = 0
    f = open(input_path, "r")
    for line in f:
        data = line.strip("\n")
        data = data.replace("-",",").split(",")
        print(data)
        for g1_selector in range(int(data[0]),int(data[1])+1):
            if g1_selector in assignments.keys():
                assignments[g1_selector] += 1
            else:
                assignments[g1_selector] = 1
        for g2_selector in range(int(data[2]),int(data[3])+1):
            if g2_selector in assignments.keys():
                assignments[g2_selector] += 1
            else:
                assignments[g2_selector] = 1
        
        for item in assignments.values():
            if item > 1:
                dupe_count += 1
                break
        assignments.clear()
    print(dupe_count)   


if __name__ == "__main__":
    main()