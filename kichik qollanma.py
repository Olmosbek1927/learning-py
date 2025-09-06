# Python misollar to'plami — har buyruq uchun 1 ta misol va ishlash tartibi (O'zbekcha izohlar).

# 1) Chop etish (print)
print("Salom, dunyo!")
# Izoh: interpreter satrni yuqoridan pastga o'qiydi -> print() chaqiriladi -> argument konsolga chiqariladi -> keyingi qatorga o'tadi.

# 2) Foydalanuvchidan kiritish (input) - märk: interaktiv, shuning uchun kommentda
name = input("Ismingizni kiriting: ")
# Izoh: input() foydalanuvchidan satr kutadi; kiritilgan satr o'zgaruvchiga saqlanadi.

# 3) O'zgaruvchilar va turlar
x = 10        # int
y = 3.14      # float
s = "matn"    # str
b = True      # bool
print(x, y, s, b)
# Izoh: har bir tayinlash chapdagi nomga o'ngdagi qiymatni bog'laydi; print qiymatlarni konsolga chiqaradi.

# 4) Tipni tekshirish / konvertatsiya
print("type(x) ->", type(x))
n = int("5") + 2
print("int('5') + 2 ->", n)
# Izoh: type() obyekt turini qaytaradi; int() stringni butun songa aylantiradi.

# 5) Aritmetik operatorlar
a = 7 + 3
d = 7 / 3
e = 7 // 3
r = 7 % 3
p = 2 ** 3
print(a, d, e, r, p)
# Izoh: Python arifmetik operatorlarini bajaradi va natijani o'zgaruvchilarga yozadi.

# 6) Taqqoslash va mantiqiy operatorlar
print("5>3:", 5 > 3, "5==3:", 5 == 3, "not False:", not False)
# Izoh: taqqoslash True/False qaytaradi; mantiqiy operatorlar boolean kombinatsiyalarni hisoblaydi.

# 7) Shartlar (if/elif/else)
x = -1
if x > 0:
    print("musbat")
elif x == 0:
    print("nol")
else:
    print("manfiy")
# Izoh: shartlar ketma-ket tekshiriladi; birinchi True bo'lgan blok bajariladi.

# 8) For sikli va range
for i in range(3):   # range(3) -> 0,1,2
    print("for i:", i)
# Izoh: range generator elementlarini tartib bilan beradi; har element i ga beriladi va body bajariladi.

# 9) While sikli
i = 0
while i < 3:
    print("while i:", i)
    i += 1
# Izoh: condition True ekaniga qadar body bajariladi; i yangilanadi, condition False bo'lsa sikl to'xtaydi.

# 10) Break va continue
for n in range(6):
    if n == 4:
        break        # sikldan chiqadi
    if n % 2 == 0:
        continue     # qolgan body ni o'tkazib yuboradi
    print("odd n:", n)
# Izoh: har iteratsiyada shartlar tekshiriladi; continue keyingi iteratsiyaga o'tkazadi, break butun siklni to'xtatadi.

# 11) Ro'yxatlar (list) — append, pop, index, slicing
lst = [1, 2, 3]
lst.append(4)           # [1,2,3,4]
val = lst.pop()         # oladi va o'chiradi -> 4
print("lst:", lst, "popped:", val, "first:", lst[0], "slice 1:3:", lst[1:3])
# Izoh: append element qo'shadi; pop qiymat qaytaradi va elementni olib tashlaydi; slicing nusxa qaytaradi.

# 12) List comprehension
squares = [i * i for i in range(6)]
print("squares:", squares)
# Izoh: comprehension range elementlari ustida ishlaydi va yangi ro'yxat qaytaradi.

# 13) Tuple (o'zgarmas)
tup = (1, 2, 3)
print("tup[1]:", tup[1])
# Izoh: tuple indekslash orqali o'qiladi, lekin elementlar o'zgartirilmaydi.

# 14) Set (unikal elementlar)
st = {1, 2, 2, 3}
st.add(4)
print("set:", st)
# Izoh: set duplicate elementlarni olib tashlaydi; add yangi element qo'shadi; tartib belgilanmagan bo'lishi mumkin.

# 15) Lug'at (dict)
d = {"ism": "Ali", "yosh": 30}
print("ism:", d["ism"], "kasb(default):", d.get("kasb", "noma'lum"))
# Izoh: indekslash orqali qiymat olinadi; get mavjud bo'lmasa default qaytaradi va xato bermaydi.

# 16) Iteratsiya lug'atda
for k, v in d.items():
    print("kalit:", k, "-> qiymat:", v)
# Izoh: items() har bir (kalit, qiymat) juftligini beradi; har bir juftlik body da ishlanadi.

# 17) Funksiya yaratish va chaqirish
def kvadrat(x):
    """x ning kvadrati"""
    return x * x

print("kvadrat(6):", kvadrat(6))
# Izoh: def funksiyani yaratadi; chaqirilganda body bajariladi va return qiymat qaytariladi.

# 18) Lambda (anonim funksiya)
add = lambda a, b: a + b
print("lambda add:", add(2, 3))
# Izoh: lambda kichik funksiyani o'zgaruvchiga bog'laydi; chaqirilganda ifoda bajariladi.

# 19) Map, filter, reduce
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
from functools import reduce
summ = reduce(lambda a, b: a + b, nums)
print("doubled:", doubled, "evens:", evens, "sum:", summ)
# Izoh: map funksiyani har elementga qo'llaydi; filter shartga mos elementlarni oladi; reduce ro'yxatni bitta qiymatga qisqartiradi.

# 20) Fayl bilan ishlash (context manager)
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Salom fayl!\n")
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("Fayldan o'qildi:", content.strip())
# Izoh: with ochilganda fayl handleni oladi; blokdan chiqganda fayl avtomatik yopiladi.

# 21) Istisnolarni ushlash
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Nolga bo'linish xatosi ushlanmoqda")
except Exception as e:
    print("Boshqa xato:", e)
# Izoh: try ichida xato paydo bo'lsa mos except blokiga o'tadi; dastur to'xtamaydi.

# 22) Modul va import
import math
from datetime import datetime
print("sqrt(16):", math.sqrt(16), "hozir:", datetime.now().isoformat())
# Izoh: import modulni yuklaydi; modul funksiyalariga math.sqrt kabi murojaat qilinadi.

# 23) Klass va obyektlar (OOP)
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return "Salom, " + self.name + "!"

p = Person("Ali")
print(p.greet())
# Izoh: class definitsiyasi blueprint hosil qiladi; __init__ konstruktor, instance metodlar orqali ishlaydi.

# 24) Foydali built-in funksiyalar
lst2 = [3, 1, 2]
print("len:", len(lst2), "sorted:", sorted(lst2), "join:", " ".join(["salom", "dunyo"]))
print("split:", "a,b,c".split(","), "enumerate:", list(enumerate(["a", "b"])), "zip:", list(zip([1,2],[3,4])))
# Izoh: built-in funksiyalar tez-tez ishlatiladi va turli maqsadlarga xizmat qiladi.

# 25) Yakuniy eslatma
# Bu fayl misollar to'plami bo'lib, har bir bo'limda bitta misol va uning bajarilish tartibi (izoh) keltirilgan.
# Faylni ishga tushurish: Windows terminalda loyihalar papkasiga o'tib:
# python "c:\Users\Dell\Documents\loyiha