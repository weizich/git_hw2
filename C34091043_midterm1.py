i,j=9,9#i,j一開始都是9
while j>=1:#製造一個while迴圈，只要j>=1就會一直執行
	while i>=1:#製造一個while迴圈，只要i>=1就會一直執行
		print(i,"x",j,"=",i*j, end="\t")	
		print(i,"x",(j-1),"=",i*(j-1), end="\t")	
		print(i,"x",(j-2),"=",i*(j-2), end="\n")
		i-=1#i逐漸變小
	print()#在j-3的時候要空一格
	j-=3#j逐漸變小
	i=9#i要重置