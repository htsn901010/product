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

with open('product.csv', 'w', encoding = 'utf-8') as f:
	f.write('product,price,\n')
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')

# practice
data = [1, 3, 5, 7, 9] # 清單中裝著一些整數
with open('test.txt', 'w') as f:
    for g in data:
        f.write(str(g) + '\n')
