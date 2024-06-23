for i in range(9,0,-3):
	for j in range(9,0,-1):
		print(i,"x",j,"=",i*j,end="\t")
		print(i-1,"x",j,"=",(i-1)*j,end="\t")
		print(i-2,"x",j,"=",(i-2)*j,end="\n")
	print()
