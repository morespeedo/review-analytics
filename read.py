data = []
#leng = 0
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
#		leng += len(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 100:
		print(word,wc[word])

print(len(wc))

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔！')
print('感謝使用本查詢功能')







#print('留言平均長度: ', leng/len(data))

#new = []
#for d in data:
#	if len(d) < 100:
#		new.append(d)
#print('一共有', len(new), '筆留言長度小於100')

#good = []
#for d in data:
#	if 'good' in d:
#		good.append(d)
#print('一共有', len(good), '筆資料提到good')

#good = [d for d in data if 'good' in d]

#print('一共有', len(good), '筆資料提到good')

#bad = ['bad' in d for d in data]
#print(bad)