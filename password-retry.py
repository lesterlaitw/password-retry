#看題做答自寫
#x = 0
#while x < 3:
#	x = x + 1
#	password = input('請輸入密碼: ')
#	if password == 'a12345678':
#		print('登入成功!')
#		break		
#	else:
#		print('密碼錯誤!')
#		if x < 3:
#			print('還剩',3 - x ,'機會!')
#		else:
#			print('GG~')


#講師版本
password = 'a12345678'
i = 3 #剩餘次數
while i >0:
	i = i - 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break #逃出迴圈 
	else:
		print('密碼錯誤!')
		if i > 0:
			print('還有', i,'次機會')
		else:
			print('沒機會嘗試了!')