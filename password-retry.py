x = 0
while x < 3:
	x = x + 1
	password = input('請輸入密碼: ')
	if password == 'a12345678':
		print('登入成功!')
		break		
	else:
		print('密碼錯誤!')
		if x < 3:
			print('還剩',3 - x ,'機會!')
		else:
			print('GG~')