
import numpy as np 
#numpy kütüphanesi dizilerle işlem yapmak için kulllanılır.
#Genellikle np aliası ile program içerisinde import edilir.

#Numpy version öğrenmek için aşağıdaki komutu çalışturabiliriz.
print(np.__version__)

#Numpy kullanarak array() ifadesi ile yeni bir dizi oluşturabiliriz.
arr = np.array([1, 2, 3, 4, 5])
print(arr)
#Oluşturduğumuz dizi tipi nedir diye baktığımız zaman numpy.ndarray olarak görürüz.
#type() built-in funcion dur verilen nesnenin türünü söyler.
print(type(arr))

#tuple kullanılarak da numpy array oluşturabiliriz.
tuplee=np.array((1,2,3,4,5))
print(type(tuplee))


#Nested arrays : Elemanları dizilerden oluşan dizilerdir.
arrr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', arrr[0, 1])



arr1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd dim: ', arr1[1, 4])

#???
arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr2[1, -1])


txt="run a lot"
#capitalize() string ifadenin ilk harfini büyük harfe çevirir.
print(txt.capitalize())
#casefold() string ifadenin ilk harfini küçük harfe çevirir.
print(txt.casefold())
#center() ortalanmış bir dize verir.
print(txt.center(20))
#string dizi içerisinde kaç defa geçmektedir onu verir.
print(txt.count("a"))
#string encoded version u geri döndürür.
print(txt.encode())
#string dizi eğer verilen ifade ile biterse true döndürür.
print(txt.endswith("t"))

#???
print(txt.expandtabs(25))

#string içerisinde verilen değeri arar ve eğer varsa konumunu döndürür.
print(txt.find("r"))

txt1= "For only {price:.2f} dollars!"
print(txt1.format(price = 49))

#format_map() ???
point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))

#string içerisinde verilen değeri arar ve bulunduğu yerin konumunu döndürür.
print(txt.index("run"))


print(txt.isalpha())

#isdecimal() Dizideki tüm karakterler ondalık ise True döndürür
print(txt.isdecimal())


#isDigit() dizideki tüm karakterler rakamsa true döndürür.
print(txt.isdigit())

#isidentifier() dizi bir tanımlayıcıysa true döndürür.
print(txt.isidentifier())

#Dizideki tüm karakterler küçük harf ie true döndürür.
print(txt.islower())

#Dizideki tüm karakterler sayısal ise true döndürür.
print(txt.isnumeric())

#Dizideki tüm karakterler yazdırılabilrse true döndürür.
print(txt.isprintable())

#Dizideki tüm karakterler boşluksa true döndürür.
print(txt.isspace())

#istitle() Dizideki her kelime büyük harfle başlıyor ise true döndürür.
print(txt.istitle())

#Dizideki tüm karakterler büyük harf ise true döndürür.
print(txt.isupper())


#Bir dizide öğelerin arasına verilen ifadeyi ekler.
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

#sola yaslanmış halini verir.
print(txt.ljust(12))

#tüm karakterleri küçük harfe çevirir.
print(txt.lower())


txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")












