
from random import randint


if __name__=='__main__':
    
    print(" -: Welcome To SNAKE WATER GUN GAME :- ")
    options=((0,1),(1,2),(2,0),(1,0),(0,2),(2,1),(0,0),(1,1),(2,2))
    option={0:"Snake",1:"Water",2:"Gun"}
    score=0
    round=1
    while True:
        print(f"\nRound = {round}")
        user_choice=int(input("Enter Your Choice \n0.Snake 1.Water 2.Gun 3.exit : " ))
        if user_choice not in option:
            print("Invalid choice!")
            continue
        round+=1
        if user_choice==3:
            print("See u AGain \nYour Score is :  ",score)
            exit()
        computer_choice=randint(0,2)
    
        print(f"User Choice is : {option[user_choice]}")
        print(f"Computer Choice is : {option[computer_choice]}")
    
        index=options.index((computer_choice,user_choice))
    
        if(index<3):
            print("User Win")
            score+=1
        elif (index <6):
            print("Computer Wins")
            score-=1
        else:
            print("Draw")