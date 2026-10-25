def gorev_kaydi(baslik:str ,*adimlar, oncelik = "normal", **ekler) -> str:
    satirlar = []

    satirlar.append(f"[{oncelik.upper()}] {baslik}")

    sayac = 1
    for adim in adimlar:
        satirlar.append(f"[{sayac}]: {adim}")
        sayac+=1
    
    for anahtar,deger in ekler.items():
        satirlar.append(f"{anahtar}: {deger}")

    return "\n".join(satirlar)

if __name__ == "__main__":
    print("test 1 - doğrudan çağrı")
    gorev1 = gorev_kaydi("Kara deliğe atla","Kredi kazan", "Pilot bul", "Hiperdrive al",oncelik="YÜKSEK",sorumlu="Ayşe")
    print(gorev1)
    print("")

    print("test2 - * ve ** kullanarak çağrı")
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Ayşe"}

    gorev0 = gorev_kaydi("Kara deliğe atla",*adimlar,oncelik="YÜKSEK",**ekler)
    print(gorev0)

