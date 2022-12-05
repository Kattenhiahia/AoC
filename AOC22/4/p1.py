input_path = "./input.txt"
group1 = {}
group2 = {}
def main():
    subset_count = 0
    f = open(input_path, "r")
    for line in f:
        data = line.strip("\n")
        data = data.replace("-",",").split(",")
        print(data)
        for g1_selector in range(int(data[0]),int(data[1])+1):
            group1[g1_selector] = 1
        print(group1)
        for g2_selector in range(int(data[2]),int(data[3])+1):
            group2[g2_selector] = 1
        print(group2)
        g2_in_g1 = group2.items() <= group1.items()

        g1_in_g2 = group1.items() <= group2.items()
        if g1_in_g2 or g2_in_g1:
            subset_count += 1
        group1.clear()
        group2.clear()

    print(subset_count)

if __name__ == "__main__":
    main()