while True:
    sP=input('請輸入身分證字號:')
    try:
        sP=repr(sP)
    except ValueError:
        print('不是有效身分證.請再輸入一次...')
        continue

    if len(sP)==12:
        break

sP=(sP[1:len(sP)-1])
print()
print("輸入的身分證字號是", sP)
m=0

s=list(sP)

if s[0]=='A':
    m=m+1
elif s[0]=='B':
    m=m+10
elif s[0]=='C':
    m=m+19
elif s[0]=='D':
    m=m+28
elif s[0]=='E':
    m=m+37
elif s[0]=='F':
    m=m+46
elif s[0]=='G':
    m=m+55
elif s[0]=='H':
    m=m+64
elif s[0]=='I':
    m=m+39
elif s[0]=='J':
    m=m+73
elif s[0]=='K':
    m=m+82
elif s[0]=='M':
    m=m+11
elif s[0]=='N':
    m=m+20
elif s[0]=='O':
    m=m+48
elif s[0]=='P':
    m=m+29
elif s[0]=='Q':
    m=m+38
elif s[0]=='T':
    m=m+65
elif s[0]=='U':
    m=m+74
elif s[0]=='V':
    m=m+83
elif s[0]=='W':
    m=m+21
elif s[0]=='X':
    m=m+3
elif s[0]=='Z':
    m=m+30
else:
    m=m+0

m1=8*int(s[1])+7*int(s[2])+6*int(s[3])+5*int(s[4])+4*int(s[5])+3*int(s[6])+2*int(s[7])+1*int(s[8])+int(s[9])
m=m+m1
m=m%10

if m==0:
    print("輸入的身分證字號", sP, "是正確的")
else:
    print("輸入的身分證字號", sP, "是不正確的")

