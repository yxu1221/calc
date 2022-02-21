data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0
			print(len(data))
print('檔案讀完了, 總共有', len(data),'筆資料')


sun_len = 0
for d in data:
	sun_len = sun_len + len(d)
	print(sun_len)

print('留言平均長度是', sun_len/len(data))