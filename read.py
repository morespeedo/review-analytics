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

avg = leng/len(data)
print('留言平均長度: ', avg)