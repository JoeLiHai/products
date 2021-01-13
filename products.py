products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)

for product in products:
	print(product[0], '的價格是', product[1])

with open ('products.csv', 'w', encoding='utf-8') as f: # 存csv檔可以用EXCEL開啟，要用逗點隔開
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')