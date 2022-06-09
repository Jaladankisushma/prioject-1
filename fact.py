#factorial
def fact(n):
    if (n==1 or n==0):
	 return 1
    else:
	x=n*fact(n-1)
	return x
key=int(input("enter the number"))
print("the factorial of",key,"is",fact(key))

