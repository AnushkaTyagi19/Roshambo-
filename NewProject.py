From random import randint


def competition(you, computer):
    """stone~paper
       paper~paper
       scissor~paper 
       scissor~stone 
       stone~stone 
       paper~stone  
       paper~scissor
       scissor~scisssor 
       stone~scissor
    """
    if you == 'stone' and computer == 'paper':
        return -1
    elif you == 'paper' and computer == 'paper':
        return 0
    elif you == 'scissor' and computer == 'paper':
        return 1
    if you == 'scissor' and computer == 'stone':
        return -1
    elif you == 'stone' and computer == 'stone':
        return 0
    elif you == 'paper' and computer == 'stone':
        return 1
    if you == 'paper' and computer == 'scissor':
        return -1
    elif you == 'scissor' and computer == 'scissor':
        return 0
    elif you == 'stone' and computer == 'scissor':
        return 1


print("This is the game of Stone , Paper and Scissor")
random = randint(1, 100)
if random < 35:
    computer = 'stone'
elif random >= 35 and random <= 70:
    computer = 'paper'
else:
    computer = 'scissor'
you = input("Enter 'Stone','Paper','Scissor' to Play with Computer:")
result = competition(you, computer)
if (result == -1):
    print("Computer Won")
elif (result == 0):
    print("Match Draw")
else:
    print("You Won")
print(f"You Enter: {you} and Computer Enter: {computer}")