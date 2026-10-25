import json

def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:

    esyalar = []

    if credits:  #bu satırlardaki ifadeler true ise oyuncu bu esyalara sahiptir
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motorlar")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar: #esyalar listesi boşsa bunun bool karşılığı false'tur. eğer en az bir eleman bile varsa bool karşılığı true'dur
        return ""

    return "Sende: " + "-".join(esyalar)

def hedef_menusu(hedefler:  list[str]) -> str:
    satirlar = ["Nereye gitmek istersin?"]

    sayac = 1

    for gezegen in hedefler:
        satirlar.append(f"[{sayac}] {gezegen}")
        sayac += 1

    return "\n".join(satirlar)

def galaksi_kur(gezegenler: list[str], baglantilar: dict, baslangic: str, **kwargs) -> dict:
    if baslangic not in gezegenler:
        raise ValueError(f"Baslangıç gezegeni gezegenler listesinde bulunamadı")

    yakit = kwargs.get("yakit",50)

    return {"gezegenler": gezegenler, "baglantilar": baglantilar, "konum": baslangic, "yakit": yakit}

