year = int(input("Enter an Year: "))
if(year%400==0):
	print("leap year")
elif(year%4==0) and (year%100!=0):
	print("leap year")
else:
	print("non leap year")


# single line statement......
'''
x=int(input("Enter an year "))
result="leap year" if x%400==0 else "leap yesr" if x%4==0 and x%100!=0 else "no leap year"
print(result)
'''