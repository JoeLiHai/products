# 讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品, 價格' in line:
			continue   # 跳到下一個迴圈
		name, price = line.strip().split(',')    # strip() 把換行符號去掉，split切割
		products.append([name, price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)

# 印出所有購買紀錄
for product in products:
	print(product[0], '的價格是', product[1])

# 寫入檔案
with open ('products.csv', 'w', encoding='utf-8') as f: # 存csv檔可以用EXCEL開啟，要用逗點隔開
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')