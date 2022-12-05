input_path = "./input.txt"

def power_calc(inp):
    j = 0
    l = len(inp[0])

    gamma = ""
    epsilon = ""
    while j < l:
        count_0 = 0
        count_1 = 0
        i=0
        while i < len(inp):
            if inp[i][j] == '1':
                count_1 += 1
            else:
                count_0 += 1
            i+=1
        if count_1 > count_0:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
        j += 1
    print("gamma: ",int(gamma,2), gamma)
    print("epsilon: ",int(epsilon,2), epsilon)
    print("result: ",int(gamma,2) * int(epsilon,2) )
   


def main():
    f = open(input_path, "r")
    inp = []
    for line in f:
        data = line.strip("\n")
        inp.append(data)
    power_calc(inp)
main()