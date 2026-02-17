date = int(input())
month = int(input())
year = int(input())
flag = "true"
if month<0 or month>12 or year<0:
	flag = False
if flag:
	if month in (1, 3, 5, 7, 8, 10, 12):
		max=31
	elif month in (4, 6, 9, 11):
		max=30
	elif month == 2:
		if year%4==0:
			max=29
		else:
			max=28
	else:
		flag = False
if flag:
	if month == 12 and date ==31:
		date=1
		month=1
		year+=1
	elif date==max:
		month+=1
		date = 1
	elif date<max:
		date+=1
	else:
		flag=False
if flag==False:
	print("Invalid Date")
else:
	print(f"{date:02d}-{month:02d}-{year}")
