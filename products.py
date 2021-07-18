# 增加新功能！(ver.4)
# 讓使用者輸入前，先讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:# 在f中的每一行(line)，line是我自己取名的變數
		if '商品,價格' in line:
			continue
		name, price = line.strip().split(',') 
		products.append([name, price])
print(products)

# 這邊當然可以寫成：
			# s = line.strip().split(',')
			# name = s[0]
			# price = s[1]
			# 但因為這個檔案他有兩個變數，所以我們可以直接取名字後，將剛剛分割出來的這兩塊，按順序([0], [1])分別存入name 跟 price
		# 我們看到的檔案，他會換行，是因為每一行(line)裡面都包含換行符號'\n'，所以要先.strip()掉
		# 因為line本身是字串，以目前的檔案來說他的第一行是「ramen,120」，
		# 如果今天沒有用split來切的話，他在print出來的樣子就是 ramen,120 的字串
		# 可是我今天讀取的目的就是要讓我能夠「單獨」「取出」個別資訊(ex.ramen)
		# 我們學過什麼東西他是「可以一個包含多項資訊在內」的東西？
		# 沒錯，就是list(清單) -> 所以我們就要用.split()把東西做分割
		# 用.split()分割完之後就會儲存成list(清單)，以第一行來說「ramen,120」
		# 他就讀取ramen跟120中間的','，並且從中間把它切開，再把兩者存回一個小清單當中[]，這樣就可以分別去讀取他們(ex. s[0])
		# 用.spilt(',')來做分割 -> 意思是，在每一行(line)裡只要遇到','，就會被分割掉
		# 所以換句話說，如果是用別的字串(ex. 'x')來分割，效果將有所不同

# ------------------------------------------------------------------------------------------------

# 我要建立一個清單，讓使用者可以持續輸入商品名稱
# products = [] # 使用者輸入完的商品要丟到清單裡，所以理當你應該開個清單讓消費者輸入的內容裝進去
while True:
	name = input('請輸入商品名稱： ')
	# products.append(name) -> 如果寫在這邊會有什麼問題？
	# 程式碼是從上讀到下，變成你輸入'q'之後，你會把先把q存進去
	# 接下來去判斷「name == q」，然後才break這樣就不對了
	if name == 'q':
		break
	# 可是只有商品沒有價格很怪耶，那我要建立一個二維清單怎麼做呢？
	price = input('請輸入商品價格： ')
	# p = [] # 建立一個小清單
	# p.append(name) # 輸入的商品名稱裝進小清單[p]裡
	# p.append(price) # 輸入的商品價格裝進小清單[p]裡
	products.append([name, price]) # 然後再把剛剛建立的小清單裝進大清單[products]
								   # 這邊很巧妙地做一個大優化：
								   # 我們可以不用那麼辛苦先開一個小清單[p]
								   # 而是直接把我們剛剛輸入的name & price 直接透過.append加入進大清單[products]
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

# 接下來我要做的事情是，我要把這個清單裡的東西一個一個叫出來，並且存出去在電腦裡！
with open('products.csv', 'w', encoding='utf-8') as f:
	# open就是打開電腦檔案，電腦原先有沒有這個檔案不重要，有的話也會複寫過去
	# 沒有的話也沒有關係，因為現在是寫入模式'w'，所以他會產生這個檔案
	# as f 是什麼意思？複習一下就是「當作f」的意思
	# 所以接下來如果我有任何要對'products.txt'這個檔案做任何動作，我就只需要叫動f就可以了
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') # 字串是可以做加總的
										  # p[]是小清單，不要忘記了
										  # 我們針對我們open的檔案(就是f)，我做出一個write的動作(.write)
										  # \n 是換行符號喔！！

# 字串(str)可以做 + 跟 ＊，但不能做- 跟 /
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'