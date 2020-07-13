p=input('請輸入身分證字號:')
i=int(len(p))
a=str(p[0].isupper())
if a=='True':
    print()
else:
    print('字母請大寫')
    exit()
if i%10==0:
    print()
else:
    print('不是有效身分證')
if p[1]=='1':
    print('男')
elif p[1]=='2':
    print('女')
else:
    print('不是有效身分證')