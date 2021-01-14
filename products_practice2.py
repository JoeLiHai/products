# 檢查是否有相同檔名的檔案
import os

# 檢查檔案是否存在，是的話，就開啟檔案，並把每一列的商品名稱及對應的商品價格作為一個列表，再放進products列表中
def file_check(filename):
	products =[]
	if os.path.isfile(filename):
		with open (filename, 'r') as f:
			for line in f:
				if '商品名稱, 商品價格' in line:
					continue
				pd_name, pd_price = line.strip().split(',')
				products.append([pd_name, pd_price])
		print('找到檔案，初始資料為: ', products)
	else:
		print('沒有這個檔案，請輸入資料重新建立! ')
	return products

# 讓使用者輸入資料
def input_data(products):
	while True:
		pd_name = input('請輸入商品名稱，或輸入q結束: ')
		if pd_name == 'q':
			break
		pd_price = input('請輸入商品價格: ')
		products.append([pd_name, pd_price])
	return products

# 印出所有購買紀錄
def print_file(products):
	print(products)
	for data in products:
		print(data[0],'的價格是', data[1], '\n')

# 寫入資料
def save_file(filename, products):
	with open (filename, 'w') as f:
		f.write('商品名稱, 商品價格\n')
		for data in products:
			f.write(data[0] + ', ' + data[1] + '\n')


products = file_check('products_practice.csv')
products = input_data(products)
print_file(products)
save_file('products_practice.csv', products)