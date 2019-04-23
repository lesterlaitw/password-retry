x = 0
while x < 3:
	password = input('請輸入密碼: ')
	if password == 'a12345678':
		print('登入成功!')
		break		
	else:
		print('密碼錯誤，還剩',2 - x ,'機會')
	x = x + 1
print('拜拜~')