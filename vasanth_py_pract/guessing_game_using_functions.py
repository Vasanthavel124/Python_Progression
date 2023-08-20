def main():
    ip = input("\nDo you really want to play the Game ?  ")
    correct = ['YES','Y','y','yes']
    wrong = ['NO','N','no','n']
    if ip in correct:
        game()
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

def game():
    print("\n\t\t\t Come Lets Play")
    print("\t\t\t ==============\n")
    print("\t\t\t Do  What I Say")
    print("\t\t\t ==============\n")
    print("\t  Think of a Number between 1 and 10 and Answer Me")
    print("\t  ================================================\n")
    correct = ['yes','y','YES','Y']
    wrong = ['no','n','NO','N']
    i = 1
    while (i<11):
        ip = input(f"Is The Number {i} ?   ")
        if ip in correct:
            print(f'\nThe Number You Thought Was {i} and I Won the Game :)\n')
            break
        elif ip in wrong:
            if (i==10):
                print("\nThe Number you Thought was not in the Range :(\n")
                print("Please Go through the Instructions and play\n")
                game()
            print()
            i+=1
            continue
        elif ip not in (correct,wrong):
            print("\nAnswer Properly\n")
            print("\nRead Questions Clearly which is Asked\n")
        
main()
