# input_path = "./input.txt"
input_path = "./test.txt"
  
outcomes = [
    "A X", 1+3,
    "A Y", 2+6,
    "A Z", 3+0,
    "B X", 1+0,
    "B Y", 2+3,
    "B Z", 3+6,
    "C X", 1+6,
    "C Y", 2+0,
    "C Z", 3+3,
]

def main():
    f = open(input_path, "r")
    sum = 0
    for line in f:
        data = line.strip("\n")
        ind = outcomes.index(data)
        print(data)
        print("value of game is: " + data + " "+ str(outcomes[ind+1]))
        sum += outcomes[ind+1]
    print(sum)


if __name__ == "__main__":
    main()