import random


computer =random.randint(1,100)

print("Guess the computer number between (1-100)")
# yournumber=int(input("enter your number"))
# print(f"computer number ={computer}")
n=100
count =0
for i in range(1,n+1):
    yournumber=int(input("Enter your number : "))

    if(yournumber >computer):

        print(f"your number {yournumber} is greater than computer ")
        

    elif(yournumber <computer):

        print(f"your number {yournumber} is less than computer ")
        

    elif(yournumber ==computer):
        count+=1
        print(f"your number {yournumber} is equal to computer ")
        break

    else:("something went wrong")
    count+=1
i=1+1


print(f"you guessed the number in {count} iterations !!")






