print("\n\t\t\t\t   Welcome to the  Game ")
print("\t\t\t\t   ////////////////////")
input()
print("\t\t\tPlease Follow the Instructions Given Below ")
print("\t\t\t//////////////////////////////////////////\n")
input()
print("You are Advised to Think of a Number Between 1 and 10  And  Answer for the further Questions")
print("////////////////////////////////////////////////////////////////////////////////////////////\n")
input()
print("Is the Number is odd? Tell Yes or No\n")
Correct = ['Yes','Y','yes','y']
Wrong = ('No','N','no','n')
Number = input()
if Number in Correct:
    print("Is the Number is 5 ?\n")
    Number1 = input()
    if Number1 in Correct:
        print("The Number you Thought was 5 And I won the Game :)")
    elif Number1 in Wrong:
        print("Tell that the Number is Greater than 5\n")
        print("Tell Yes or No")
        Number2 = input()
        if Number2 in Correct:
            print("Is the Number is 7 ?\n")
            Number3 = input()
            if Number3 in Correct:
                print("The Number you Thought was 7 And I won the Game :)")
            else:
                print("The Number you Thought was 9 And I won the Game :)")
        elif Number2 in Wrong:
            print("Is the Number is 3?\n")
            Number4 = input()
            if Number4 in Correct:
                print("The Number you Thought was 3 And I won the Game :)")
            else:
                print("The Number you Thought was 1 And I won the Game :)")
else:
    print("Is the Number is 6 ?\n")
    Number5 = input()
    if Number5 in Correct:
        print("The Number you Thought was 6 And I won the Game :)")
    elif Number5 in Wrong:
        print("Tell that the Number is Greater than 6\n")
        print("Tell Yes or No")
        Number6 = input()
        if Number6 in Correct:
            print("Is the Number is 8 ?\n")
            Number7 = input()
            if Number7 in Correct:
                print("The Number you Thought was 8 And I won the Game :)")
            else:
                print("The Number you Thought was 10 And I won the Game :)")
        elif Number6 in Wrong:
            print("Is the Number is 4 ?\n")
            Number7 = input()
            if Number7 in Correct:
                print("The Number you Thought was 4 And I won the Game :)")
            else:
                print("The Number you Thought was 2 And I won the Game :)")