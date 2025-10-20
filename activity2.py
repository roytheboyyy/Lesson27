import random
def PC_Number():
    
    
    while True:
        x = int(input("I will make you guess a number! Get ready."))
        pc_num = random.randint(1, 10)
        if x == pc_num:
            print("Wow! You guessed it right! It was" , pc_num)
        else:
            print("Try again! It was" , pc_num , ".")
            continue
PC_Number()
