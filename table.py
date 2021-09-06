#!/bin/python
import random 


print ("Table Practice Program")

#taking inputs for Multiplicables

num1 = int(input("Enter the first Multiplicable Limit: "))
num2 = int(input("Enter the second Multiplicable Limit: "))





#how many questions to display

times = int(input("How many problems you want to solve?:"))

limit = 0

while (limit != times):
	d1 = random.randint(2,num1)
	d2 = random.randint(2,num2)
	
	ans = input(str(d1)+"x"+str(d2)+":")
	int_ans = int(ans)
	c_ans = d1*d2
	if (int_ans == c_ans):
		limit += 1
	else:
		print("The Correct Answer is:") 
		print(c_ans)
		
	
	
	
