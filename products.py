# 我要建立一個清單，讓使用者可以持續輸入商品名稱
products = [] # 使用者輸入完的商品要丟到清單裡，所以理當你應該開個清單讓消費者輸入的內容裝進去

while True:
	name = input('請輸入商品名稱： ')
	# products.append(name) -> 如果寫在這邊會有什麼問題？
	# 程式碼是從上讀到下，變成你輸入'q'之後，你會把先把q存進去
	# 接下來去判斷「name == q」，然後才break這樣就不對了
	if name == 'q':
		break
	# 可是只有商品沒有價格很怪耶，那我要建立一個二維清單怎麼做呢？
	price = input('請輸入商品價過： ')
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

# 字串(str)可以做 + 跟 ＊，但不能做- 跟 /
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# 接下來我要做的事情是，我要把這個清單裡的東西一個一個叫出來，並且存出去在電腦裡！
with open('products.csv', 'w') as f:
	# open就是打開電腦檔案，電腦原先有沒有這個檔案不重要，有的話也會複寫過去
	# 沒有的話也沒有關係，因為現在是寫入模式'w'，所以他會產生這個檔案
	# as f 是什麼意思？複習一下就是「當作f」的意思
	# 所以接下來如果我有任何要對'products.txt'這個檔案做任何動作，我就只需要叫動f就可以了
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') # 字串是可以做加總的
										  # p[]是小清單，不要忘記了
										  # 我們針對我們open的檔案(就是f)，我做出一個write的動作(.write)
										  # \n 是換行符號喔！！
