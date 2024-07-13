#C04-14

#Computer-Assisted Instructions (CAI)
import random

print("\nThe use of computers in education is referred to as computer-assisted instruction (CAI)."
" As computer costs decline, it becomes feasible for every student, regardless of economic circumstance, to have a computer and use it in school. This creates exciting possibilities for improving the"
" educational experience of all students worldwide.\n");
print("The following program will ask an elementary student multpilication questions. This program focuses on educating students using CAI.\n");
def computerAssistedInstruction():
    num1 = random.randrange(1, 10);
    num2 = random.randrange(1, 10);
    product = num1 * num2;
    
    print("\nHow much is " + str(num1) + " times " + str(num2) +"?");
    answer = int(input("Answer: "));
    if(answer == product):
        
        response = random.randrange(1, 5);
        if(1 == response):
            response = "\nVery good!";
        elif(2 == response):
            response = "\nExcellent!";
        elif(3 == response):
            response = "\nNice work!";   
        else:
            response = "\nKeep up the good work!";
        print(response);       
        computerAssistedInstruction();
        
    else:
        while(True):
            response = random.randrange(1, 5);
            if(1 == response):
                response = "\nNo. Please try again.";
            elif(2 == response):
                response = "\nWrong. Try once more.";
            elif(3 == response):
                response = "\nDont give up!";   
            else:
                response = "\nNo. Keep trying.";
                
            print(response)
            answer = int(input("Answer: "));
            if(answer == product):
                print("\nHard work pays off. Now on to the next.");
                computerAssistedInstruction();
                
    
computerAssistedInstruction();
