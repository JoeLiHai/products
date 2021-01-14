# 檢查是否有相同檔名的檔案
import os
products =[]

# 檢查檔案是否存在，是的話，就開啟檔案，並把每一列的商品名稱及對應的商品價格作為一個列表，再放進products列表中
if os.path.isfile('products_practice.csv'):
	with open ('products_practice.csv', 'r') as f:
		for line in f:
			if '商品名稱, 商品價格' in line:
				continue
			pd_name, pd_price = line.strip().split(',')
			products.append([pd_name, pd_price])

# 讓使用者輸入資料
while True:
	pd_name = input('請輸入商品名稱，或輸入q結束: ')
	if pd_name == 'q':
		break
	pd_price = input('請輸入商品價格: ')
	products.append([pd_name, pd_price])

# 印出所有購買紀錄
print(products)
for data in products:
	print(data[0], '的價格是', data[1])

# 寫入資料
with open ('products_practice.csv', 'w') as f:
	f.write('商品名稱, 商品價格\n')
	for data in products:
		f.write(data[0]+ ','+ data[1]+ '\n')