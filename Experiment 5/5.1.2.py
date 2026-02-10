# Write your code here...
a, b, c, d = map(int,input().split())
print(a+b+c+d)
per = ((a+b+c+d)/400)*100
print(f"{per:.2f}")
if per>75:
	print("Distinction")
elif per>=60 and per<75:
	print("First Division")
elif per>=50 and per<60:
	print("Second Division")
elif per>=40 and per<50:
	print("Third Division")
else:
	print("Fail")
