"""
Guessing Game

Created By  Ahmad Taha

"""

from random import randint

A = (randint(1,10))


N = 3

print("You Have " + str(N) + " Life")



while(N>0):
    
    B = int(input("Guess The Correct Number From 1 to 10     "))
    
    if(A != B):
        N -=1

        if N>0:
            print("\n\nYou Have " + str(N) + " Life ")
        
    elif(A == B):
        print("\n\nYou Win ")
        break

if N==0 :
    print("\n\nGame Over")
    
print("The Correct Number is " , A )
