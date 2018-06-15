str_goc = str(input('Hãy nhập một chuỗi kí tự X bất kì: '))

str_up = str_goc.upper()
print('Chuôi kí tự X viết ở chế độ in hoa toàn bộ như sau: %s' %(str_up))

str_low = str_up.lower()
print('Chuôi kí tự X viết ở chế độ in thường toàn bộ như sau: %s' %(str_low))

str_1st_up = str_low[0].upper()
for i in range(1,len(str_low)):
    if str_low[i-1] == ' ':
        str_1st_up += str_low[i].upper()
    else:
        str_1st_up += str_low[i].lower()
print('Chuôi kí tự X có kí tự đầu tiên của từng chữ in hoa: %s' % (str_1st_up))

str_low2 = str_1st_up.lower()
str_369_up = str_low2[0]
stt_chu = 0
for i in range(1,len(str_low2)):
    if str_low2[i-1] == ' ':
        stt_chu += 1
        if stt_chu % 3 == 2:
            str_369_up += str_low2[i].upper()
        else:
            str_369_up += str_low2[i].lower()
    else:
        str_369_up += str_low2[i].lower()
print('Chuôi kí tự X có các kí tự ở vị trí 3, 6, 9,... in hoa: %s' % (str_369_up))

str_low3 = str_369_up.lower()
str_saudaucham_up = str_low3[0].upper()
for i in range(1,len(str_low3)):
    if str_low3[i-2] == '.' and str_low3[i-1] == ' ':
        str_saudaucham_up += str_low3[i].upper()
    else:
        str_saudaucham_up += str_low3[i].lower()
print('Chuôi kí tự X có các kí tự sau dấu chấm thì in hoa: %s' % (str_saudaucham_up))
