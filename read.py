data = []
leng = 0
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		leng += len(data[count])
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

print('留言平均長度: ', leng/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆資料提到good')