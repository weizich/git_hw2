n=int(input("Input the range number:"))
i=1
perfect_numbers=[]
while i<=n:
	total=0
	j=1
	while j<i:
		if i%j==0:
			total+=j
		j+=1
	if total==i:
		perfect_numbers.append(i)
	i+=1
print("Perfect numbers:",perfect_numbers)	