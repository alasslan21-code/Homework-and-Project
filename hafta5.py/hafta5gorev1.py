## mehmet ali aslan - 20253005005 - (github reposu)

import time
from functools import wraps
from onbellekli_rota_sayaci import rota_sayaci, dev_galaksi

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
    """bu fonksiyon yazılan a ve b değerlerini toplar"""
    return a+b

test0 = test_fonksiyonu(3,5)
print(test0)
print(" ")

print("test 1 - sonuç değişmeden dönüyor mu?")
test1 = test_fonksiyonu(3,5)
print(f"test1 = 8: {test1 == 8}") #evet sonuç değişmeden dönüyor
print(" ") 

print("test 2 - adlı argümanlarla çalışıyor mu?")
test2 = test_fonksiyonu(a=3,b=5)
print(f"test 2 = 8: {test2 == 8}")
print(" ")

print("test 3 - __name__ ve __doc__ korunuyor mu ?")
korunma_durumu_name=test_fonksiyonu.__name__
korunma_durumu_doc=test_fonksiyonu.__doc__
print(f"__name__ korunma durumu: {korunma_durumu_name == "test_fonksiyonu"}")
print(f"__doc__ korunma durumu: {korunma_durumu_doc == """bu fonksiyon yazılan a ve b değerlerini toplar"""}")
print(" ")

print("Ön bellekli rota sayacı için süre ölçümü")
@sure_olc
def rota_hesapla(baslangic_gezegeni,adim_sayisi):
    return rota_sayaci(dev_galaksi)(baslangic_gezegeni, adim_sayisi)

rota_hesapla("Dünya",20)

