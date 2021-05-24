n=int(input())
if 1000<=n<2000:
	print('total bill is',n)
        d=(10*n)/100
	print('Discount on billed amount is',d)
	print('paid bill is',n-d)
elif 2000<=n<3000:
	print('total bill is',n)
        d=(20*n)/100
	print('Discount on billed amount is',d)
	print('paid bill is',n-d)
elif 3000<=n<5000:
	print('total bill is',n)
        d=(30*n)/100
	print('Discount on billed amount is',d)
	print('paid bill is',n-d)		
elif n>5000:
	print('total bill is',n)
        d=(40*n)/100
	print('Discount on billed amount is',d)
	print('paid bill is',n-d)	
else:
	print('no discount' )
	
	'''
	output:
	1000
	total bill is 1000
	discount on billed amount is 100
	paid bill is 900
	
