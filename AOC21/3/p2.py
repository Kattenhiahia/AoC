input_path = "./input.txt"
black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'
reset='\033[0m'


def get_list(inp, index, filter):
    i = 0
    r_list = []
    while i < len(inp):
        if inp[i][index] == filter:
            r_list.append(inp[i])
        i += 1
    return r_list

def oxygen(inp):
    j = 0
    l = len(inp[0])
    n_inp = inp
    while j < l:
        count_0 = 0
        count_1 = 0
        i=0
        print(green, len(n_inp),reset)
        if len(n_inp) == 1:
           return print(n_inp)
        else:   
            while i < len(n_inp):
                if n_inp[i][j] == '1':
                    count_1 += 1
                else:
                    count_0 += 1
                i+=1
        if count_1 >= count_0:
            n_inp = get_list(n_inp, j, '1')
        else:
            n_inp = get_list(n_inp, j, '0')        
        j += 1
    print(green, len(n_inp),reset)
    return n_inp
    
def co2(inp):
    j = 0
    l = len(inp[0])
    n_inp = inp
    while j < l:
        count_0 = 0
        count_1 = 0
        i=0
        print(green, len(n_inp),reset)
        if len(n_inp) == 1:
           return n_inp
        else:   
            while i < len(n_inp):
                if n_inp[i][j] == '1':
                    count_1 += 1
                else:
                    count_0 += 1
                i+=1
        if count_1 < count_0:
            n_inp = get_list(n_inp, j, '1')
        else:
            n_inp = get_list(n_inp, j, '0')        
        j += 1
    print(green, len(n_inp),reset)
    return n_inp

def compute(inp, mode):
    print("!!"+mode+" mode!!")

    j = 0
    l = len(inp[0])
    n_inp = inp
    while j < l:
        count_0 = 0
        count_1 = 0
        i=0
        print(green, len(n_inp),reset)
        if len(n_inp) == 1:
           return n_inp[0]
        else:   
            while i < len(n_inp):
                if n_inp[i][j] == '1':
                    count_1 += 1
                else:
                    count_0 += 1
                i+=1
        if mode == "co2":
            if count_1 < count_0:
                n_inp = get_list(n_inp, j, '1')
            else:
                n_inp = get_list(n_inp, j, '0')        
        elif mode == "oxygen":
            if count_1 >= count_0:
                n_inp = get_list(n_inp, j, '1')
            else:
                n_inp = get_list(n_inp, j, '0')
        else:
            print("!!invalid mode!!")
            return -1

        j += 1
    print(green, len(n_inp),reset)
    return n_inp[0]



def main():
    f = open(input_path, "r")
    inp = []
    for line in f:
        data = line.strip("\n")
        inp.append(data)
    # oxygen(inp)
    o = compute(inp, "oxygen")

    # co2(inp)
    co2 = compute(inp, "co2")
    print(int(o,2)*int(co2,2))
main()