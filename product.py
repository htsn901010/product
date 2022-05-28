import os # operating system

def read_files(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if 'product,price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# user's input
def user_input(products):
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
	return products

# print all purchase records
def print_products(products):
	for product in products:
		print('the', product[0], 'price is: ', product[1])

# write into the file
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('product,price\n')
		for product in products:
			f.write(product[0] + ',' + str(product[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # check files
		print('yes, find it')
		products = read_files(filename)
	else:
		print('no, cannot find it')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()