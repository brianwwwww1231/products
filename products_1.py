import os # operating system

# 讀取檔案
def read_file(filename):
	# read_file('products.csv')的意思是
	# 宣告 filename = 'products.csv'
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue 
			name, price = line.strip().split(',')
			products.append([name, price])
		print('目前擁有的記帳資訊： ', products)
	return products

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱： ')
		if name == 'q':
			break
		price = input('請輸入商品價格： ')
		products.append([name, price]) 
	print('本次新增的記帳資訊：', products)
	return products

# 印出所有購買紀錄
def print_out(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	# 檢查檔案在不在
	filename = 'products.csv'
	if os.path.isfile(filename):
		products = read_file(filename)
		print('Yeah!!找到檔案了！！')
	else:
		print('找不到檔案耶')
	products = user_input(products)
	# products -> user_input()不是因為這裡products跟products = read_file('...')裡的products名字一樣，電腦就會自動把兩個連上關係
	# 而是因為func(函式)外面有一個變數叫做products，他有被宣告說他的value是read_file('...')return出來的value
	# 當products -> use_input()，電腦是把products裡被宣告的數值丟進user_input()這個func(函式)裡去執行

	print_out(products)
	# 電腦處理機制同上方說明
	write_file('products.csv', products)

name = 'main'

if name == 'main':
	main()

main()