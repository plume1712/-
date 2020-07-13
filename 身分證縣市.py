ps=input('輸入身分證字號:')
i=int(len(ps))
a=str(ps[0].isupper())
t=str(ps.isalnum())
w=str(ps[1:11].isdigit())
z=str(ps.isspace())
s=str(ps[0].isalpha())
if w=='True':
    if t=='True':
        if i%10==0:
            if z=='False':
                if s=='True':
                    if a=='True':
                        print()
                    else:
                        print('字母請大寫')
                        exit()
                else:
                    print('不是有效身分證')
                    exit()
            else:
                print('不是有效身分證')
                exit()
        else:
            print('不是有效身分證')
            exit()
    else:
        print('不是有效身分證')
        exit()
else:
    print('不是有效身分證')
    exit()
if ps[0]=='A':
    print('台北市')
elif ps[0]=='B':
    print('台中市')
elif ps[0]=='C':
    print('基隆市')
elif ps[0]=='D':
    print('台南市')
elif ps[0]=='E':
    print('高雄市')
elif ps[0]=='F':
    print('新北市')
elif ps[0]=='G':
    print('宜蘭縣')
elif ps[0]=='H':
    print('桃園市')
elif ps[0]=='I':
    print('嘉義市')
elif ps[0]=='J':
    print('新竹縣')
elif ps[0]=='K':
    print('苗栗縣')
elif ps[0]=='M':
    print('南投縣')
elif ps[0]=='N':
    print('彰化縣')
elif ps[0]=='O':
    print('新竹市')
elif ps[0]=='P':
    print('雲林縣')
elif ps[0]=='Q':
    print('嘉義縣')
elif ps[0]=='T':
    print('屏東縣')
elif ps[0]=='U':
    print('花蓮縣')
elif ps[0]=='V':
    print('台東縣')
elif ps[0]=='W':
    print('金門縣')
elif ps[0]=='X':
    print('澎湖縣')
elif ps[0]=='Z':
    print('連江縣')
else:
    print('已停用代碼')