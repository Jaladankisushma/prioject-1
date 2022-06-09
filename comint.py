def compound_interest(p,r,y):
	return p*(1+r/100)**y
	def compound_interest(p,r,y):
		if(y==0):
			return p
		else:
			return 
p=int(input("enter principal amount"))
r=float(input("enter rate:"))
y=int(input("enter years:"))
k=compound_interest(p,r,y)
ci=k-p
print("Comound interest",ci)
