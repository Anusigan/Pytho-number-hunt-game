#Importing modules
import random
from datetime import datetime

#Initializing variables
current_date=0
current_time=0
random_number=0
attempt=0
life_score=0
final_score=0
selection=0
status=()
don=()
filename=()

#Creating a list for fighting numbers
fighting_numbers=[]

#Generating the file name with date,time and random number
current_date = datetime.now().strftime("%Y_%m_%d")
current_time = datetime.now().strftime("%H_%M_%S")
random_number = str(random.randint(0, 9999)).zfill(4)
filename = current_date + "_" + current_time + "_" + random_number + ".txt"

#Simple Function
def prompt():
    #Declaring global variables
    global attempt
    global final_score
    global don
    global selection
    global status
    global fo
    
    

    #Opening the file for recording stats
    fo= open(filename,"w")

    #interface and process
    print("Welcome to destroyer of numbers!!!")
    don=input("player name: ")
    fo.write("Player name: "+don)
    life_score=random.randrange(1,50)
    print(don, "'s initial life score is: ", life_score)

    while attempt<20:
        attempt=attempt+1
        fo.write("\n\nAttempt number: "+str(attempt))
        print("\nAttempt: ",attempt)
        print("Life score is: ",life_score)

       
        if 1<=attempt<=5:
            fighting_numbers=[random.randrange(15,100) for i in range (5)]
        elif 6<=attempt<=10:
            fighting_numbers=[random.randrange(250,2000) for i in range (5)]
        elif 11<=attempt<=15:
            fighting_numbers=[random.randrange(3000,10000) for i in range (5)]
        elif 16<=attempt<=20:
            fighting_numbers=[random.randrange(20000,100000) for i in range (5)]

        fo.write("\nPresented enimies: "+str(fighting_numbers))
        print("Numbers to fight: ", *fighting_numbers,sep=" ")
        
        
        #Error handling for user selection number
        try:
            selection=int(input("Select a number to fight: "))
            fo.write("\nUser input number: "+str(selection))
        except ValueError:
            print("selection should be an integer")
            break
            
        

        if selection in fighting_numbers:
            if selection<=life_score:
                print(don, "killed", selection)
                life_score=life_score+selection
                final_score=life_score
            else:
                print(selection, "killed", don)
                final_score=life_score
                break
        else:
            print("No such enemy")
            final_score=life_score
            status=(don, "was defeated!!!")
            break

        fo.write("\nLife score: "+str(life_score))


    if attempt==20:
        status=(don,"saved letter-kind")
    else:
        status=(don,"was defeated!!!")
    return
            

#Simple Function
def game_statistics(fo):
    print("\n***Game status***")
    print("Player name:",don)
    print("Total attempts:",attempt)
    print("Final score:",final_score)
    print(*status)
    
    fo.write("\n\n***Game status***")
    fo.write("\nPlayer name:"+str(don))
    fo.write("\nTotal attempts:"+str(attempt))
    fo.write("\nFinal score:"+str(final_score))
    fo.write("\n"+str(status))
    return

        
            
#Calling the functions
prompt()
game_statistics(fo)

#Closing the file
fo.close()


    
