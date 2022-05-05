products = []
while True:
	name = input('enter your product name: ')
	if name == 'q':
		break
	price = input('enter your product price: ')
	p = []
	p.append(name)
	p.append(price)   
	# 7.8.9 could be:  p = [name, price]  
	products.append(p)
	# 7.8.9.11 could be: products.append([name, price])
print(products)

print(products[0][1])

for product in products:
	print('the', product[0], 'price is: ', product[1])