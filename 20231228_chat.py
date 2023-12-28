# 對話紀錄格式整理

import os

# 讀取檔案
def read_file(filename):
	text = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			text.append(line.strip('\n'))
	print(text)
	return text

#判斷人名，調整內容
def whosays(text):
	chat = []
	for d in text:
		if 'Allen' in d:
			who = 'Allen: '
		elif 'Tom' in d:
			who = 'Tom: '
		else:
			chat.append([who, d])
	# print(chat)
	return chat

# 寫入檔案
def write_file(filename, chat):
	with open(filename, 'w', encoding='utf-8') as f:
		for d in range(len(chat)):
			for i in range(2):
				f.write(chat[d][i])
			f.write('\n')


# 檢查檔案是否存在
filename = 'input.txt'
if os.path.isfile(filename):
	text = read_file(filename)
	chat = whosays(text)
	print(chat)
	write_file('output.txt', chat)
else:
	print('檔案不存在')




