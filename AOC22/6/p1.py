input_path = "./input.txt"

def main():
    f = open(input_path, "r")
    incoming_codes = []
    marker_pos = -1
    for line in f:
        data = line.strip("\n")
        for letter_pos in range(0,len(data)):
            incoming_codes.append(data[letter_pos])
            if len(incoming_codes) < 4:
                continue
            else:
                set_of_codes = set(incoming_codes[-4:])
                print(len(set_of_codes)) 
                print(len(incoming_codes[-4:]))
                if len(set_of_codes) != len(incoming_codes[-4:]):
                    print("no marker received")
                else:
                    print(incoming_codes)
                    print("MARKER RECEIVED")
                    print(incoming_codes[-4:])
                    marker_pos = letter_pos+1
                    break
    print(marker_pos)

if __name__ == "__main__":
    main()