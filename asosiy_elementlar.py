
# print('salom') #salom sozini conslolga chiqarib beradi 

# print('salom ismim "Olmosbek"') # qoshtirnoqli sozlarni chiqarib beradi

# print('men o`qishni yaxshi bitirdin') # bir tirnoqli sozlarini ch.beradi

# print('''salom qalesan 
# kjkaashnkdhakf
# lakfndfn''') #bir printni ichiga kop satrli sozlarni yozib beradi

# print("to`rtburchak yuzi: " , 4 * 6)# sozli natija

# print('olmosbek\nbaxodirov') #pastgi qatordan yozib beradi 

# print('olmosbek\tBaxodirov') # tab bilan ajratadi 

# input("soz kiriting: ") #foydalanuvchidan soz kiritishini kutadi

# a=input('ismingizni kiriting: ') 
# print(' assalomu alaykum ', a ) # a-ozgaruvchiga foydalanuvchi kiritgan ismini saqlaydi

# x = "Dastur" # tipi string
# y = 5 # tipi int
# print(x , y) # bir vaqtda uzharuvchilarni chiqaradi 

# x=10
# print("type(x)= ", type(x)) #type() obyekt turini qaytaradi;

# n = int(5) + int(2)
# print("int(5) + int(2) = ", n) #int() stringni butun songa aylantiradi.

# x = 10        # int
# y = 3.14      # float
# s = "matn"    # str
# b = True      # bool
# print(x, y, s, b)
# # print qiymatlarni konsolga chiqaradi.

# a = 7 + 3
# d = 7 / 3
# e = 7 // 3
# r = 7 % 3
# p = 2 ** 3
# print(a, d, e, r, p)
# Izoh: Python arifmetik operatorlarini bajaradi va natijani o'zgaruvchilarga yozadi.

# x = 88
# if x > 0:
#     print("musbat")
# elif x == 0:
#     print("nol")
# else:
#     print("manfiy")
# Izoh: shartlar ketma-ket tekshiriladi; birinchi True bo'lgan blok bajariladi.

# for i in range(10):   # range(3) -> 0,1,2
#     print( i)
# Izoh: range generator elementlarini tartib bilan beradi; har element i ga beriladi va takror bajariladi.

# i = 0
# while i < 10:
#     print( i)
#     i += 3
# Izoh: condition True ekaniga qadar body bajariladi; i yangilanadi, condition False bo'lsa sikl to'xtaydi.

# for n in range(6):
#     if n == 4:
#         break        # sikldan chiqadi
#     if n % 2 == 0:
#         continue     # qolgan body ni o'tkazib yuboradi
#     print("odd n:", n)
# Izoh: har iteratsiyada shartlar tekshiriladi; continue keyingi iteratsiyaga o'tkazadi, break butun siklni to'xtatadi.

# lst = [1, 2, 3]
# lst.append(4)           # [1,2,3,4]
# val = lst.pop()         # oladi va o'chiradi -> 4
# print("lst:", lst, "popped:", val, "first:", lst[0], "slice 1:3:", lst[1:3])\

# squares = [i * i for i in range(6)]
# print("squares:", squares)
# # Izoh: comprehension range elementlari ustida ishlaydi va yangi ro'yxat qaytaradi.

# for i in range(10):   # range(3) -> 0,1,2, ...9
#     print("tup[i]:", ( i))
# Izoh: tuple indekslash orqali o'qiladi, lekin elementlar o'zgartirilmaydi.

# st = {1, 2, 2, 3}
# st.add(19)
# print("set:", st)
# Izoh: set duplicate elementlarni olib tashlaydi; add yangi element qo'shadi; tartib belgilanmagan bo'lishi mumkin.

# d = {"ism": "Ali", "yosh": 30}  # (agar mavjud bo'lsa uncomment qiling yoki quyidagi tekshiruvni qoldiring)
# for k, v in d.items():
#     print("kalit:", k, "-> qiymat:", v)
# Izoh: items() har bir (kalit, qiymat) juftligini beradi; har bir juftlik body da ishlanadi.

# x=int(input('son kiriting: '))
# y=int(input('nechanchi darasi bolsin: '))
# a=x**y
# print(f'{x} ning {y} darajasi {a} ga teng')

# def kvadrat(x):
#     return x * x
# print("kvadrat(6):", kvadrat(6))
# Izoh: def funksiyani yaratadi; chaqirilganda body bajariladi va return qiymat qaytariladi.

# add = lambda a, b: a + b
# print("lambda add:", add(2, 3))
# Izoh: lambda kichik funksiyani o'zgaruvchiga bog'laydi; chaqirilganda ifoda bajariladi.

# nums = [1, 2, 3, 4]
# doubled = list(map(lambda x: x * 2, nums))
# evens = list(filter(lambda x: x % 2 == 0, nums))
# from functools import reduce
# summ = reduce(lambda a, b: a + b, nums)
# print("doubled:", doubled, "evens:", evens, "sum:", summ)
# Izoh: map funksiyani har elementga qo'llaydi; filter shartga mos elementlarni oladi; reduce ro'yxatni bitta qiymatga qisqartiradi.

# x = int(input('son kiriting: '))
# y=int(input('darajasini ayting: '))
# def a():
#     print(x ** y)
# a()  # funksiya uzgaruvchi funksiyadan tashqarida berilgan

# def funksiya():
#     global x , y
#     x = int(input('son kiriting: '))
#     y=int(input('darajasini ayting: ')) 
#     print(x ** y)
# funksiya() # funksiya ichida uzgaruvchi bor

# uzlashtirish operatori
# = x = 5 x=5
# += x += 3 x = x + 3
# - = x -= 3 x= x - 3
# *= x *= 3 x= x * 3
# /= x /= 5 x = x / 5
# %= x %= 5 x = x % 5
# //= x //= 5 x = x // 5
# **= x **= 5 x = x ** 3
# &= x &= 3 x = x & 3
# |= x |= 3 x = x |3
# ^= x ^= 3 x = x ^ 3
# >>= x >>= 3 x = x >> 3
# <<= x <<= 3 x = x << 3 


# Taqqoslash operatorlari qiymatlarni o’zaro taqqoslash uchuyn ishlatiladi:
# = = Teng x == y
# != Teng emas x != y
# > Katta x > y
# < Kichik x < y
# >= Katta yoki teng x >= y
# <= Kichik yoki teng x <= y

# a = 5
# print (a>3 and a<10)
# print (a>3 or a<4)
# print (not(a>3 and a<10)) #mantiq operatori

# x = ["olma", "banan"]
# y = ["olma", "banan"]
# z = x
# print(x is z)
# print(x is y)
# print(x == z)
# #------------------------------------------------------------------------
# print(x is not z)
# print(x is not y)
# print(x != z) #aniqlash operatori

