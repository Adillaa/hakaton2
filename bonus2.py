import random as rd
random_number = rd.randint(0,10)
print(random_number)
a=0
while 2>1:
	ans=input("num?: ")
	ans=int(ans)
	if ans==random_number:
		print("you win")
		break
	else:
		print("try again")
		a=a+1
		if a==3:
			print("loh, ty proigral")
			break
