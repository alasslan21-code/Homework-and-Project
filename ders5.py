import time
from functools import wraps

def sure_olc(func):
    @wraps(func)
    def sarmalayici(*args, **kwargs):
        baslangic=time.perf_counter()
        sonuc=func(*args,**kwargs)
        bitis=time.perf_counter()
        sure = bitis-baslangic

        print(f"{func.__name__}: {round(sure,4)} sn.")
        return sonuc
    return sarmalayici

print("test 0 - çalışıyor mu?")
@sure_olc
def test_fonksiyonu(a,b):
    return a+b

test0 = test_fonksiyonu(3,5)
print(test0)
print(" ")

print("test 1 - sonuç değişmeden dönüyor mu?")
test1 = test_fonksiyonu(3,5)
print(f"{test1} = {test1 == 8}")


