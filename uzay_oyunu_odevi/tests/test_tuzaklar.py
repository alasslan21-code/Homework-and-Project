def yakit_ekle_tuzak(miktar, depo=[]):
    depo.append(miktar)
    return depo

def yakit_ekle(miktar, depo=None):
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo

def test_yakit_ekle_tuzak_hatasi():
    """
    İlk çağrıda 10 döner. 
    İkinci çağrıda depo verilmezse sıfırdan 20 dönmesi gerekirken hafızadaki liste kaldığı için [10, 20] döner!
    """
    depo1 = yakit_ekle_tuzak(10)
    assert depo1 == [10]
    

    depo2 = yakit_ekle_tuzak(20)
    assert depo2 == [10, 20]  


def test_yakit_ekle_duzeltilmis():
    """
    Her çağrıda yeni ve bağımsız bir liste oluşur.
    """
    depo1 = yakit_ekle(10)
    assert depo1 == [10]
    
    depo2 = yakit_ekle(20)
    assert depo2 == [20] 