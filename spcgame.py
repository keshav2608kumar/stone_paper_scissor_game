#stone paper scissor
import time
import random
dict={1:"stone",2:"paper",3:"scissors"}
def game():
    computer=random.choice([1,2,3])
    print("enter \n1 for stone\n2 for paper\n3 for scissors\n")
    print("========================================================\n")

    your_choice=int(input("enter your choice: "))
    if your_choice in [1, 2, 3]:
        print(f"you chose {dict[your_choice]}")
        print("======================================================\n")

        print("\nwaiting for computer answer----------\n")
        time.sleep(2)
        print(f"computer chose {dict[computer]}")

        if your_choice==computer:
            print("\nresult: draw!")
        elif your_choice==1 and computer==2:
            print("\nresult: computer win!")
        elif your_choice==1 and computer==3:
            print("\nresult: you win!")
        elif your_choice==2 and computer==3:
            print("result: computer win!")
        elif your_choice==2 and computer==1:
            print("result: you win!")
        elif your_choice==3 and computer==2:
            print("result: you win!")
        elif your_choice==3 and computer==1:
            print("result: computer win!")
    else:
        print("invalid choice input should be 1,2 or 3")

            

while True:
    print("\n===============================================================\n")
    print("press any button except 'e'  for  playing \npress  E for exit \n")
    print("\n===============================================================\n")
    k=input("enter input: ")
    print("\n************************************************************\n")
    if k=='E' or k=='e':
        break
    else:
        game()
       