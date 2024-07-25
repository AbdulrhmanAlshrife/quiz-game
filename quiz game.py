print("welcome to my quiz ")

player=input("do you want start the quiz? ")
if player.lower().strip() != "yes":
    quit()

score=0
answer=input("what does CPU stand for? ")
if answer.lower().strip() =="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Uncorrenct!")

answer=input("what does RAM stand for? ")
if answer.lower().strip() =="random access memory":
    print("Correct!")
    score+=1
else:
    print("Uncorrenct!")


answer=input("what does GPU stand for? ")
if answer.lower().strip() =="graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Uncorrenct!")    

print("the Coreect answer " + str( score ) )
