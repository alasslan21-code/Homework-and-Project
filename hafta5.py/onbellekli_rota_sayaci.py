from functools import lru_cache

def rota_sayaci(baglantilar):
    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen,adim):
        if adim == 0:
            return 1
        
        toplam_rota = 0
        komsular = baglantilar.get(gezegen,[])
        for komsu in komsular:
            toplam_rota += rota_sayisi(komsu,adim - 1)
        
        return toplam_rota
    return rota_sayisi

dev_galaksi = {
    'Dünya': ['Mars', 'Venüs', 'Jüpiter'],
    'Mars': ['Dünya', 'Satürn', 'Neptün', 'Plüton'],
    'Venüs': ['Dünya', 'Jüpiter', 'Merkür'],
    'Jüpiter': ['Dünya', 'Venüs', 'Satürn', 'Uranüs'],
    'Satürn': ['Mars', 'Jüpiter', 'Uranüs', 'Neptün'],
    'Uranüs': ['Jüpiter', 'Satürn', 'Neptün', 'Plüton'],
    'Neptün': ['Mars', 'Satürn', 'Uranüs', 'Plüton'],
    'Plüton': ['Mars', 'Uranüs', 'Neptün'],
    'Merkür': ['Venüs'] }

hesapla = rota_sayaci(dev_galaksi)
#ya da rota_sayaci(dev_galaksi)("Dünya",30)

print(hesapla("Dünya",30))