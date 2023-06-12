Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> friend = 'สมชาย'
>>> money = 10
>>> print(friend + 'ยืมเงิน ' + str(money) + ' บาท')
สมชายยืมเงิน 10 บาท
>>> ##การใช้ .format
>>> 
>>> print('{}ยืมเงิน {} บาท'.format(fiend,money))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print('{}ยืมเงิน {} บาท'.format(fiend,money))
NameError: name 'fiend' is not defined. Did you mean: 'friend'?
>>> print('{}ยืมเงิน {} บาท'.format(friend,money))
สมชายยืมเงิน 10 บาท
>>> print(f'{friend}ยืมเงิน {money} บาท') ##ใช้คีย์ลัด
สมชายยืมเงิน 10 บาท
>>> 
>>> ##การสั่งให้ใส่ลูกน้ำใน data
>>> money = 1454541111534
>>> print(f'{money:,}')
1,454,541,111,534
>>> ##การใส่จุดทศนิยม
>>> print(f'{money:,.2f}') #.2f --> flaoting
1,454,541,111,534.00
