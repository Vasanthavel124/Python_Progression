def binary_search_guessing(low, high):
    while True:
        mid = (low + high) // 2
        print(f"Is the number {mid}?")
        input1 = input("Type higher, lower, yes: ")

        if input1 == 'yes':
            print(f"Guessed the number {mid}")
            break
        elif input1 == 'higher':
            low = mid + 1
        elif input1 == 'lower':
            high = mid - 1

def main():
    ip = input("\nDo you really want to play the Game? ")
    correct = ['YES', 'Y', 'y', 'yes']
    wrong = ['NO', 'N', 'no', 'n']
    
    if ip in correct:
        print("\n\t\t\t Come Let's Play")
        print("\t\t\t ==============\n")
        print("\t\t\t Do What I Say")
        print("\t\t\t ==============\n")
        print("\tThink of a Number between 1 and 100 (inclusive) and Answer Me")
        print("\t==========================================================\n")
        binary_search_guessing(1, 100)
        
        ip1 = input("Do you Want to Play Again? ")
        
        if ip1 in correct:
            main()
        elif ip1 in wrong:
            print("\nThanks for Playing with me...\n")
            print("Love You :)\n")
        elif ip1 not in (correct, wrong):
            print("\nAnswer Properly :(\n")
            print("\nRead Questions Clearly which is Asked...\n")
            main()
    elif ip in wrong:
        print("\nOk but, May I know the reason for not joining the Game?\n")
        input()
        print("\nThanks for the Information given...")
        print("\nLove you <:)\n")
    elif ip not in (correct, wrong):
        print("\nAnswer Properly :(\n")
        print("\nRead Questions Clearly which is Asked...\n")
        main()

main()
