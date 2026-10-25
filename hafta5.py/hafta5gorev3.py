from functools import  wraps

def hedef_menusu(hedefler:  list[str]) -> str:
    satirlar = ["Nereye gitmek istersiniz?"]

    sayac = 1

    for gezegen in hedefler:
        satirlar.append(f"[{sayac}] {gezegen}")
        sayac += 1

    return "\n".join(satirlar)





