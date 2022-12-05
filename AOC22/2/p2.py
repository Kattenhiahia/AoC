input_path = "./input.txt"
  
outcomes = [
    "A X", 3+0, #Rock, Lose, Scissor
    "A Y", 1+3, #Rock, Draw, Rock
    "A Z", 2+6, #Rock,  Win, Paper
    "B X", 1+0, #Paper, Lose, Rock
    "B Y", 2+3, #Paper, Draw, Paper
    "B Z", 3+6, #Paper,  Win, Scissor 
    "C X", 2+0, #Scissor, Lose, Paper
    "C Y", 3+3, #Scissor, Draw, Scissor
    "C Z", 1+6, #Scissor,  Win, Rock
]

def main():
    f = open(input_path, "r")
    sum = 0
    for line in f:
        data = line.strip("\n")
        ind = outcomes.index(data)
        print("value of game is: " + data + " "+ str(outcomes[ind+1]))
        sum += outcomes[ind+1]
    print(sum)


if __name__ == "__main__":
    main()