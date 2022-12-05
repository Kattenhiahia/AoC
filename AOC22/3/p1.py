input_path = "./input.txt"
points = {
    "a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,
    "A":27,"B":28,"C":29,"D":30,"E":31,"F":32,"G":33,"H":34,"I":35,"J":36,"K":37,"L":38,"M":39,"N":40,"O":41,"P":42,"Q":43,"R":44,"S":45,"T":46,"U":47,"V":48,"W":49,"X":50,"Y":51,"Z":52
}



def main():
    f = open(input_path, "r")
    common_letters = []
    priority_sum = 0
    for line in f:
        data = line.strip("\n")
        # print(int(len(data)/2))
        compartment_one = data[:int(len(data)/2)]
        compartment_two = data[int(len(data)/2):]
        dupe_found = False
        for letter in compartment_one:
            if letter in compartment_two and not dupe_found:
                print(" common letter is: "+letter)
                common_letters.append(letter)
                priority_sum += points[letter]
                dupe_found = True
            elif letter in compartment_two and dupe_found:
                print("multiple: " + letter +" in: " + compartment_two)
    print(len(common_letters))
    # print(len(f.readlines()))
    print(common_letters)
    print(priority_sum)


if __name__ == "__main__":
    main()