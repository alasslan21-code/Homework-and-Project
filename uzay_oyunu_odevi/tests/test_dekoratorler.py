from uzay_oyunu.dekoratorler import sure_olc
from uzay_oyunu.akis import rota_sayaci  # Hafta 4'te yazdığımız rota_sayaci fonksiyonu

def test_sure_olc():
    @sure_olc
    def test_fonksiyonu(a, b):
        """bu fonksiyon yazılan a ve b değerlerini toplar"""
        return a + b

 
    assert test_fonksiyonu(3, 5) == 8


    assert test_fonksiyonu(a=3, b=5) == 8


    assert test_fonksiyonu.__name__ == "test_fonksiyonu"
    assert test_fonksiyonu.__doc__ == "bu fonksiyon yazılan a ve b değerlerini toplar"

def test_onbelleksiz_rota_sayaci_sure_olculu():
    dev_galaksi = {
        'Dünya': ['Mars', 'Venüs'],
        'Mars': ['Dünya']
    }
    
    @sure_olc
    def rota_hesapla(baslangic_gezegeni, adim_sayisi):
        return rota_sayaci(dev_galaksi)(baslangic_gezegeni, adim_sayisi)

    sonuc = rota_hesapla("Dünya", 20)
    assert sonuc > 0

from uzay_oyunu.dekoratorler import sinirla, yakit_harca

def test_yakit_harca_gecerli_degerler():
    
    assert yakit_harca(30) == 70
    
    assert yakit_harca(0) == 100
    assert yakit_harca(100) == 0

def test_yakit_harca_gecersiz_degerler():
    
    with pytest.raises(ValueError) as excinfo:
        yakit_harca(-10)
    assert "yakit_harca: -10 değeri 0-100 aralığında değil" in str(excinfo.value)

    
    with pytest.raises(ValueError) as excinfo:
        yakit_harca(150)
    assert "yakit_harca: 150 değeri 0-100 aralığında değil" in str(excinfo.value)