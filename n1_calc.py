#calculator

def calc(sign):
	c=input("your first num: ")
	a=int(c)
	d=input("your second num: ")
	b=int(d)
	if b=="0":
		print("imposssible")
	if sign=="+":
		ans= a+b
		print(ans)
	elif sign=="-":
		ans=a-b
		print(ans)
	elif sign=="/":
		ans= a/b
		print(ans)
	elif sign=="*":
		ans==a*b
		print(ans)
	else:
		print("wrong sign")
	con=input("one more time?").lower()
	if con == 'y':
		sign=input("enter sign   ")
		calc(sign)
	elif con == 'n':
		print("calculator ostanovlen")
	else :
		print("kalkulator slomalsyaa")

#osnovnoi kod

will= input("want to run calculator? Y/N   ").lower()
if will == 'n':
        print("calculator obidelsya")
elif will == 'y':
	sign=input("enter sign   ")
	calc(sign)
else:
	print("ok")




