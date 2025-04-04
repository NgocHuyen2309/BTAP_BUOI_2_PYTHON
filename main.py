# #1.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
# print("Do dai chuoi: ",len(s))
#
# #2.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# while s != "":
#     count = 0
#     left = ""
#     c = s[0].lower()
#     for i in s:
#         if c == i.lower():
#             count += 1
#         else:
#             left = left + i
#     s = left
#     print(c,": ", count, ";")
#
# #3.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# newstr = ""
# if len(s) > 2:
#     newstr = s[0:2] + s[-2:]
#     print("Chuoi moi: ",newstr)
# else:
#     print("Empty string")
#
# #4.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# c = s[0]
# newstr = c
# for i in s[1:]:
#     if i == c:
#         newstr += "$"
#     else:
#         newstr += i
# s = newstr
# print("Chuoi moi la: ",s)
#
# #5.
# s1 = input("Nhap chuoi dau: ")
# print("Chuoi dau la: ",s1)
#
# s2 = input("Nhap chuoi thu hai: ")
# print("Chuoi thu hai la: ",s2)
# newstr = ""
# if len(s) >= 2:
#     newstr = s2[0:2] + " " + s1[0:2]
#     print("Chuoi moi: ",newstr)
# else:
#     print("Empty string")
#
# #6.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# newstr = ""
# if len(s) >= 3:
#     if s[-3:] == "ing":
#         newstr = s + "ly"
#         print("Chuoi moi: ",newstr)
#     else:
#         newstr = s + "ing"
#         print("Chuoi moi: ",newstr)
# else:
#     print("Chuoi moi van la: ",s)
#
# #7.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# newstr = ""
# x = s.find("not")
# y = s.find("poor")
#
# if x != -1 and y != -1 and x < y:
#     newstr = s[:x] + "good" + s[y+4:]
#     print("Chuoi moi: ",newstr)
# else:
#     print("Chuoi moi van la: ",s)
#
# #8.
# def find_longest_word(n):
#     danhsach = []
#     tuDaiNhat = ""
#     for i in range(n):
#         danhsach.append(input("Nhap du lieu: "))
#     print("Danh sach da nhap:", danhsach)
#     for i in danhsach:
#         if tuDaiNhat < i:
#             tuDaiNhat = i
#     return tuDaiNhat
#
# n = int(input("Nhap so luong du lieu: "))
#
# tuDaiNhat = find_longest_word(n)
# print("Tu dai nhat:", tuDaiNhat)
# print("Do dai tu dai nhat: ", len(tuDaiNhat))
#
# #9.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# n = int(input("Nhap vi tri ki tu muon bo: "))
# if len(s) != 0 & (0<= n <= len(s)):
#     s = s[:n] + s[n+1:]
#     print("Chuoi moi: ",s)
#
# #10.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# if len(s) >= 2:
#     s = s[-1:]+ s[1:-1] + s[:1]
#     print("Chuoi moi: ",s)
#
# #11.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# if len(s) != 0:
#     s = s[::2]
#     print("Chuoi moi: ",s)
#
# #12.
# import re
# s = input("Nhap chuoi cau: ")
# print("Chuoi la: ",s)
#
# s = re.sub(r'[^\w\s]', '', s).lower()
#
# danhSachTu = s.split(" ")
# print("Cac tu trong chuoi: ",danhSachTu)
#
# tanSuatTu = {}
#
# for tu in danhSachTu:
#     tu = tu.lower()
#     if tu in tanSuatTu:
#         tanSuatTu[tu] += 1
#     else:
#         tanSuatTu[tu] = 1
#
# # In kết quả
# for tu, soLan in tanSuatTu.items():
#     print(f"{tu}: {soLan}")
#
# #13.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# print("Chuoi khi duoc viet in hoa: ", s.upper())
# print("Chuoi khi duoc viet thuong: ", s.lower())
#
# #14.
# s = input("Nhap chuoi tu (cach nhau bang dau phay: ")
# print("Chuoi la: ",s)
#
# danhSachTu = [tu.strip() for tu in s.split(",")]
# tuKoTrung = list(set(danhSachTu))
#
# n = len(tuKoTrung)
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if tuKoTrung[j] > tuKoTrung[j + 1]:
#             tuKoTrung[j], tuKoTrung[j + 1] = tuKoTrung[j + 1], tuKoTrung[j]
#
# print(",".join(tuKoTrung))
#
# #15.
# def add_html_tag(tag, tu):
#     return f"<{tag}>{tu}</{tag}>"
#
# tag = input("Nhap tag: ")
# tu = input("Nhap tu: ")
#
# html_string = add_html_tag(tag, tu)
#
# print(html_string)
#
# #16.
# def insert_string_middle(mainstr, insertstr):
#     mid = len(mainstr) // 2
#     return mainstr[:mid] + insertstr + mainstr[mid:]
# mainstr = "[[]]"
# insertstr = input("Nhap chuoi: ")
#
# newstr = insert_string_middle(mainstr, insertstr)
# print("Chuoi moi la: ",newstr)
#
# #17.
# def repeat_last_two_chars(s):
#     if len(s) >= 2:
#         return s[-2:] * 4
#     else:
#         return "Empty new string"
#
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# newstr = repeat_last_two_chars(s)
# print("Chuoi moi: ", newstr)
#
# #18.
# def get_first_three_chars(s):
#     if len(s) < 3:
#         return s
#     return s[:3]
#
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# newstr = get_first_three_chars(s)
# print("Chuoi moi: ", newstr)
#
# #19.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# kyTu = input("Nhap ky tu: ")
# print("Ky tu xac dinh la: ",kyTu)
# newstr = ""
# viTri = s.rfind(kyTu)
# if viTri != -1:
#     newstr = s[:viTri]
#     print("Chuoi moi: ", newstr)
# else:
#     print("Chuoi van la: ", s)
#
# #20.
# def reverse_a_string(s):
#     if len(s) % 4 ==0:
#         return s[::-1]
#     else:
#         return s
#
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# newstr = reverse_a_string(s)
# print("Chuoi moi: ", newstr)
#
# #21.
# def convert_the_string(s):
#     first_four_chars = s[:4]
#     uppercase_word_count = 0
#
#     for char in first_four_chars:
#         if char.isupper():
#             uppercase_word_count += 1
#     if uppercase_word_count >= 2:
#         return s.upper()
#     else:
#         return s
#
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# newstr = convert_the_string(s)
# print("Chuoi moi: ", newstr)
#
# #22.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ", s)
#
# s_list = list(s)
#
# for i in range(len(s_list) - 1):
#     for j in range(len(s_list) - i - 1):
#         if s_list[j] > s_list[j + 1]:
#             s_list[j], s_list[j + 1] = s_list[j + 1], s_list[j]
#
# sorted_s = ''.join(s_list)
#
# print("Chuoi sau khi sap xep: ", sorted_s)
#
# #23.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# s = s.replace("\n", "")
# print("Chuoi sau khi loai bo newline: ", s)
#
# #24.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# batdau = input("Nhap chuoi can kiem tra: ")
# print("Chuoi can kiem tra: ", batdau)
#
# if s[:len(batdau)] == batdau:
#     print(f"Chuoi '{s}' bat dau voi '{batdau}'.")
# else:
#     print(f"Chuoi '{s}' khong bat dau voi '{batdau}'.")
#
# #25.
# def caesar_encrypt(text, shift):
#     result = ""
#
#     for char in text:
#         if char.isupper():
#             result += chr((ord(char) + shift - 65) % 26 + 65)
#         elif char.islower():
#             result += chr((ord(char) + shift - 97) % 26 + 97)
#         else:
#             result += char
#
#     return result
#
# text = input("Nhap chuoi can ma hoa: ")
# print("Chuoi can ma hoa la: ",text)
# shift = int(input("Nhap so buoc dich chuyen: "))
# print(f"Dich chuyen {shift} buoc.")
#
# encrypted_text = caesar_encrypt(text, shift)
# print("Chuoi sau khi ma hoa: ", encrypted_text)
#
# #26.
# import textwrap
#
# text = input("Nhap chuoi: ")
# print("Chuoi la: ",text)
#
# formatted_text = textwrap.fill(text, width=50)
#
# print("Chuoi sau khi can chinh:")
# print(formatted_text)
#
# #27.
# text = input("Nhap chuoi: ")
# print("Chuoi la: ",text)
#
# lines = text.splitlines()
# no_indent_text = '\n'.join(line.lstrip() for line in lines)
#
# print("Van ban sau khi bo thut dong:")
# print(no_indent_text)
#
# #28.
# text = input("Nhap chuoi: ")
# print("Chuoi la: ",text)
#
# prefix = input("Nhap tien to: ")
# print("Tien to: ", prefix)
#
# lines = text.splitlines()
# prefixed_text = '\n'.join(prefix + " " + line for line in lines)
#
# print("Chuoi sau khi them tien to:")
# print(prefixed_text)
#
# #29.
# text = input("Nhap chuoi: ")
# print("Chuoi la: ")
# print(text)
#
# num_spaces = int(input("Nhập số khoảng trắng thụt lề cho dòng đầu tiên: "))
# indentation = " " * num_spaces
#
# lines = text.splitlines()
#
# if len(lines) > 0:
#     lines[0] = indentation + lines[0]
#
# indented_text = '\n'.join(lines)
#
# print("Chuoi sau khi thut le dong dau tien:")
# print(indented_text)
#
# #30.
# so = float(input("Nhap so: "))
# print(f"So {so} vs 2 chu so thap phan: {so:.2f}")
#
# #31.
# so = float(input("Nhap so: "))
# print(f"So {so} vs 2 chu so thap phan: {so:+.2f}")
#
# #32.
# so = float(input("Nhap so: "))
# print(f"So {so} khong chu so thap phan: {so:+.0f}")
#
# #33.
# so = int(input("Nhap so: "))
#
# width = int(input("Nhap do rong toi thieu: "))
# print("Do rong: ",width)
# print(f"So {so} duoc can trai voi so 0: {so:0<{width}d}")
#
# #34.
# so = int(input("Nhap so: "))
#
# width = int(input("Nhap do rong toi thieu: "))
# print("Do rong: ",width)
# print(f"So {so} duoc can phai voi '*': {so:*>{width}d}")
#
# #35.
# so = int(input("Nhap so: "))
# print(f"So {so} voi dau phay ngan cach: {so:,}")
#
# #36.
# so = float(input("Nhap so: "))
#
# print(f"So {so} duoi dang phan tram: {so:.2%}")
#
# #37.
# so = int(input("Nhap so: "))
#
# so_str = str(so)
#
# print(f"So {so} duoc can trai: '{so:<10}'")
# print(f"So {so} duoc can phai: '{so:>10}'")
# print(f"So {so} duoc can giua: '{so:^10}'")
#
# #38.
# chuoi = input("Nhap chuoi: ")
# print("Chuoi la: ",chuoi)
#
# chuoiCon = input("Nhap chuoi con: ")
# print("Chuoi con la: ",chuoiCon)
#
# count = chuoi.count(chuoiCon)
#
# print(f"Chuoi con '{chuoiCon}' xuat hien {count} lan trong chuoi chinh.")
#
# #39.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# if len(s) > 0:
#     print("Chuoi sau khi dao nguoc la: ", s[::-1])
#
# #40.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# cacTu = s.split()
# print(f"Cac tu trong chuoi truoc khi dao nguoc: {cacTu}")
# print(f"Cac tu trong chuoi sau khi dao nguoc la: {cacTu[::-1]}")
# chuoi_dao_nguoc = ' '.join(cacTu[::-1])
# print(f"Chuoi sau khi dao nguoc: {chuoi_dao_nguoc}")
#
# #41.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
# kyTu = input("Nhap cac ky tu can loai bo: ")
#
# for ky in kyTu:
#     s = s.replace(ky, "")
#
# print(f"Chuoi sau khi loai bo cac ky tu: {s}")
#
# #42.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# while s != "":
#     count = 0
#     left = ""
#     c = s[0].lower()
#     for i in s:
#         if c == i.lower():
#             count += 1
#         else:
#             left = left + i
#     s = left
#     if count >1:
#         print(c,": ", count, ";")
#
# #43.
# import math
#
# chieu_dai = float(input("Nhap chieu dai hinh chu nhat (cm): "))
# chieu_rong = float(input("Nhap chieu rong hinh chu nhat (cm): "))
# print(f"Chieu dai va chieu rong hcn: {chieu_dai}, {chieu_rong}")
#
# dien_tich = chieu_dai * chieu_rong
# print(f"Dien tich hinh chu nhat la: {dien_tich:.2f}cm²")
#
# ban_kinh = float(input("Nhap ban kinh hinh tru (cm): "))
# chieu_cao = float(input("Nhap chieu cao hinh tru (cm): "))
# print(f"Ban kinh va chieu cao hinh tru: {ban_kinh}, {chieu_cao}")
#
# the_tich = math.pi * ban_kinh**2 * chieu_cao
# print(f"Ban kinh hinh tru la: {the_tich:.3f}cm³")
#
# #44.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# for i in range(len(s)):
#     kyTu = s[i]
#     print(f"Ky tu {kyTu} co vi tri {i}.")
#
# #45.
# import string
#
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# bangChuCai = string.ascii_lowercase
#
# for ky in bangChuCai:
#     if ky not in s.lower():
#         print("Chuoi khong chua tat ca cac chu cai trong bang chu cai.")
#         break
# else:
#     print("Chuoi chua tat ca chu cai trong bang chu cai.")
#
# #46.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# danhSachTu = s.split(" ")
# print("Danh sach cac tu trong chuoi: ",danhSachTu)
#
# #47.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
# n = int(input("Nhap so n: "))
# print("So ky tu muon doi: ",n)
#
# newstr = s[:n].lower() + s[n:]
#
# print("Chuoi sau khi doi:", newstr)
#
# #48.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# newstr = s.replace('.', 'temp').replace(',', '.').replace('temp', ',')
# print("Chuoi sau khi doi:", newstr)
#
# #49.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
#
# nguyen_am = 'aeiouAEIOU'
#
# dem_nguyen_am = 0
#
# for ky in s:
#     if ky in nguyen_am:
#         dem_nguyen_am += 1
#
# print(f"So nguyen am co trong chuoi: {dem_nguyen_am}")
#
# #50.
# s = input("Nhap chuoi: ")
# print("Chuoi la: ",s)
# delimiter = input("Nhap dau phan cach: ")
# print("Dau phan cach: ",delimiter)
#
# ketQua = s.rsplit(delimiter, 1)
#
# print("Sau khi tach:", ketQua)
#
