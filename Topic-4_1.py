def nhap(n):
    n_name = n
    while True:
        try:
            print('Hãy nhập giá trị của %s: ' %(n), end='')
            n = float(input(""))
        except ValueError:
            print('Bạn nhập không đúng. Bạn cần nhập một số thực. Xin vui lòng nhập lại.')
            continue
        else:
            if int(n) == n:
                n = int(n)
            print('Nhập liệu thành công. Hệ thống ghi nhận: %s = %s' %(n_name,n))
            return n
            break

def hangtu(n_name,n): #Hằng tử nha =))
    if n == 0: #Nếu hệ số bằng 0 thì không hiển thị hạng tử đó nữa
        hangtu = ''
    else:
        if n_name == 'a': #Nếu là hệ số a thì không cần chú ý dấu của hệ số
            if n == 1: #Nếu hệ số = 1 hoặc -1 thì không hiển thị hệ số trong hạng tử
                hangtu = 'x^2'
            elif n == -1:
                hangtu = '-x^2'
            else:
                hangtu = '%sx^2' %(n)
        else: #Nếu là hệ số b hoặc c thì cần chú ý dấu của hệ số theo đề bài yêu cầu
            if n == 1:
                hangtu = '+ '
            elif n == -1:
                hangtu = '- '
            elif n > 0:
                hangtu = '+ %s' %(n)
            else:
                if int(n) == n:
                    hangtu = '- %i' %(n)
                else:
                    hangtu = '- %s' %(abs(n))
            if n_name == 'b':
                hangtu += 'x'
    return hangtu

def print_debai():
    print(' ')
    if a0 + b0 + c0 != 0:
        print('Nhập liệu hoàn tất. Phương trình cần giải là: %s %s %s = 0 \n' %(hangtu('a',a0),hangtu('b',b0),hangtu('c',c0)))
    else:
        print('Nhập liệu hoàn tất. Phương trình cần giải là: 0x^2 + 0x + 0 = 0 \n')

def print_delta(a,b,c):
    if a0 != 0:
        print('Phương trình trên có: Delta = b^2 - 4ac = %s^2 - 4 * %s * %s = %s \n' %(b,a,c,delta))
    else:
        print('Phương trình trên không phải phương trình bậc 2.\n')

def print_nghiem(a,b,c):
    if a0 != 0:
        if delta == 0:
            nghiem = -b/(2*a)
            if int(nghiem) == nghiem:
                n = int(nghiem)
            print('Phương trình trên có một nghiệm kép: x1 = x2 = %s' %(nghiem))
        elif delta > 0:
            x1 = (-b+math.sqrt(delta))/(2*a)
            if int(x1) == x1:
                n = int(x1)
            x2 = (-b-math.sqrt(delta))/(2*a)
            if int(x2) == x2:
                n = int(x2)
            print('Phương trình trên có hai nghiệm:')
            print('x1 = %s' %(x1))
            print('x2 = %s' %(x2))
        else:
            print('Phương trình trên không có nghiệm thực.')
    elif b0 != 0:
        print('Phương trình trên là phương trình bậc nhất có nghiệm là: x = %s' %(-c/b))
    elif c0 != 0:
        print('Phương trình trên vô nghiệm.')
    else:
        print('Phương trình trên nghiệm đúng với mọi x.')

import math
print(' ')
print('>' *6, 'Ứng dụng giải phương trình bậc hai viết bằng Python', '<' *6)
print('Xin chào! Phương trình của chúng ta sẽ có dạng: ax^2 + bx + c = 0', '\n')
a0 = nhap('a')
b0 = nhap('b')
c0 = nhap('c')
delta = b0**2 -4*a0*c0
if int(delta) == delta:
    delta = int(delta)
print_debai()
print_delta(a0,b0,c0)
print_nghiem(a0,b0,c0)
