import random


def game():

    
    user = input("What is your choice? enter 'r' for rock, 'p' for paper, 's' for scissors. Good Luck!\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie! try again.\n The computer input was obviously ', computer
    if is_win(user, computer):
        return 'You won! Yay you! The computer input was ', computer
                    
    return 'You lost :( The computer input was', computer
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True   
consent = True
result=game()
print(result[0]+result[1])
while(consent):
    c = input('do you wanna play again? Y/n\n')
    if (c == 'Y') or (c== 'y'):
        result=game()
        print(result[0]+ result[1])
    elif (c == 'n') or (c == 'N'):
        consent = False
        break
    else:
        print("I don't understand your input!\n")
        continue
        
        




