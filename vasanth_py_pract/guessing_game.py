def game(low,high):
    correct = ['yes','y','YES','Y']
    wrong = ['no','n','NO','N']
    more = ['high','higher','H','HIGHER','h','HIGH','greater than','more']
    less = ['low','lower','l','LOWER','L','LOW','lesser than','less']
    mid = (low+high)//2
    ip1 = input(f"Is The Number {mid} ?   ")
    if ip1 in correct:
        print(f'\nThe Number You Thought Was {mid} and I Won the Game :)\n')
    elif ip1 in more:
            game(mid+1,high)
    elif ip1 in less:
            game(low,mid-1)
    elif ip1 not in (correct,more,less):
            print("\nAnswer Properly\n")
            print("\nRead Questions Clearly which is Asked\n")
    elif ip1 in wrong:
            print("\nThe Number you Thought was not in the Range :(\n")
            print("Please Go through the Instructions and play\n")
            game()
            print()

def main():
    ip = input("\nDo you really want to play the Game ?  ")
    correct = ['YES','Y','y','yes']
    wrong = ['NO','N','no','n']
    if ip in correct:
        print("\n\t\t\t Come Lets Play")
        print("\t\t\t ==============\n")
        print("\t\t\t Do  What I Say")
        print("\t\t\t ==============\n")
        print("\t  Think of a Number between 1 and 100 and Answer Me")
        print("\t  ================================================\n")
        game(1,100)
        ip1 = input("Do you Want to Play Again ?  ")
        if ip1 in correct:
            main()
        elif ip1 in wrong:
            print("\nThanks for Playing with me...\n")
            print("Love You :)\n")
        elif ip not in (correct,wrong):
            print("\nAnswer Properly :(\n")
            print("\nRead Questions Clearly which is Asked...\n") 
            main()
    elif ip in wrong:
        print("\nOk but, May I know the reason for not joining into the Game ?\n")
        input()
        print("\nThanks for the Information given...")
        print("\nLove you <:)\n")
    elif ip not in (correct,wrong):
            print("\nAnswer Properly :(\n")
            print("\nRead Questions Clearly which is Asked...\n")
            main()
main()
game(1,100)


