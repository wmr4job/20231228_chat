# 對話紀錄格式整理

import os

# 讀取檔案
def read_file(filename):
	text = []
	with open(filename, 'r', encoding='utf-8-sig') as f: # -sig去除讀檔產生的編碼紀錄文字
		for line in f:
			text.append(line.strip('\n'))
	return text

#判斷人名，格式轉換
def whosays(text):
	new_chat = [] # 儲存轉換後內容
	who = None # 先宣告變數為"無"，避免第一行無人名時，程式執行發生錯誤
	for d in text:
		if 'Allen' in d:
			who = 'Allen: '
		elif 'Tom' in d:
			who = 'Tom: '
		elif who: # 如果who有值才執行
			new_chat.append(who + d)
	return new_chat

# 寫入檔案
def write_file(filename, new_chat):
	with open(filename, 'w', encoding='utf-8') as f:
		for d in new_chat:
			f.write(d + '\n')

# 主程式
def main():
	filename = 'input.txt'
	if os.path.isfile(filename): # 檢查檔案是否存在
		text = read_file(filename) # 紀錄讀取檔案後的內容
		new_chat = whosays(text) # 紀錄格式轉換後的內容
		write_file('output.txt', new_chat) # 寫入的檔案名稱、內容
		print('轉換完成！')
	else:
		print('檔案不存在')

main()


