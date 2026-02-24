# Type Content here...
a,b,c = input().split()
list1 = [a,b,c]
for i in range(3):
	for j in range(3):
		for k in range(3):
			if i!=j and i!=k and j!=k:
				print(list1[i]+list1[j]+list1[k])
