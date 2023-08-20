print("\nWelcome to the  Game !!!!!!!!!!!!!")
print("**********************************")
input()
print("Please Follow the Instructions Given Below :")
print("*******************************************\n")
input()
print("You are Advised to Think of a Number Between 1 and 3  And  Answer for the further Questions:")
print("********************************************************************************************\n")
input()
print("Is the Number is odd? Tell Yes or No\n")
Correct = ['Yes','Y','yes','y']
Wrong = ('No','N','no','n')
Number = input()
if Number in Correct:
    print("Tell that the Number is Greater than 2")
    print("Tell Yes or No")
    Number1=input()
    if Number1 in Correct:
        print("The Number you Thought was 3 And I won the Game :)\n")
    else:
        print("The Number you Thought was 1 And I won the Game :)\n")
elif Number in Wrong:
    print("\nThe Number You Thought was 2 And I Won the Game :)\n")

# Surya Wrote This 
'''ip = input('Is the Number 1?')
if ip == 'yes':
    print('guessed')
    ip = input('Is the Number 2?')
elif ip =='yes':
    print('guessed')
    ip = input('Is the Number 3?')
elif ip == 'no':
    print('Your number is 3')'''

# Paul Wrote This 

'''ip = input("is the number is 1 ?")
if ip == 'yes':
    print("1 guessed")
ip = input("is the number is 2 ?")
if ip == 'yes':
    print("2 guessed")
else:
    print("3 guessed")'''
