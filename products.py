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