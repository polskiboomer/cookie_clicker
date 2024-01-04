import random
import time
import sys


emoji_success = ["\U0001F60E", "\U0001F44D", "\U0001F389"]


def mnozenie_dziesietnego_przez_potege10():
    a = random.randint(10, 90)
    b = random.choice([10, 100, 1000, 1000000])
    wynik_ = float(a * b)
    print(f"Iloczyn liczb {a} i {b} wynosi:")
    odp1 = a + b
    odp2 = a / b
    odp3 = int(a * b / 100)
    odp4 = a * b * 10
    odp5 = a * b * 100
    odp6 = a * b * 1000
    odp7 = int(a * b / 10)

    return wynik_, [odp1, odp2, odp3, odp4, odp5, odp6, odp7]


def pole_trapezu():
    while True:
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        h = random.randint(2, 5)

        wynik_ = (a + b) * h / 2

        if wynik_ % 2 == 0:
            wynik_ = int(wynik_)  # zamien ulamek 10-tny na liczbe calkowita
            break

    print(f"Pole trapezu o podstawach {a} i {b} i wysokosci {h} wynosi:")
    odp1 = wynik_ + random.randint(2, 8)
    odp2 = int(wynik_ / 2)
    odp3 = max(1, wynik_ - random.randint(2, 8))
    odp4 = int(a * h / 2)
    odp5 = int(a + b + h) * 2
    odp6 = wynik_ * 2

    return wynik_, [odp1, odp2, odp3, odp4, odp5]


def trojkat():
    while True:
        a = random.randint(3, 9)
        h = random.randint(3, 9)
        pole = a * h / 2

        if pole % 2 == 0:
            pole = int(pole)  # zamien ulamek 10-tny na liczbe calkowita
            break

    print(
        f"Pole trojkata o podstawie {a} wynosi {pole}. Wysokosc tego trojkata wynosi:"
    )

    wynik_ = h

    odp1 = wynik_ + random.randint(2, 8)
    odp2 = wynik_ - 1
    odp3 = max(1, wynik_ - random.randint(2, 8))
    odp4 = int(wynik_ * 1.5)
    odp5 = wynik_ + 2
    return wynik_, [odp1, odp2, odp3, odp4, odp5]


def mnozenie_dziesietnego_przez_dziesietny():
    c = random.choice([10, 100])
    a = random.randint(1, 9) / c
    b = random.randint(1, 9) / c
    wynik_ = a * b
    print(f"Iloczyn ulamkow {a} i {b} wynosi:")
    odp1 = wynik_ * 10
    odp2 = wynik_ * 100
    odp3 = wynik_ * 1000
    odp4 = wynik_ / 10
    odp5 = wynik_ / 100
    odp6 = wynik_ / 1000

    return wynik_, [odp1, odp2, odp3, odp4, odp5, odp6]


def pole_rombu():
    while True:
        x = random.randint(3, 9)
        y = random.randint(2, 8)
        wynik_ = x * y / 2
        if wynik_ % 2 == 0:
            wynik_ = int(wynik_)  # zamien ulamek 10-tny na liczbe calkowita
            break

    print(f"Pole rombu o przekatnych {x} i {y}:")
    odp1 = wynik_ + random.randint(2, 8)
    odp2 = int(wynik_ / 2)
    odp3 = max(1, wynik_ - random.randint(2, 8))
    odp4 = 4 * y
    odp5 = 4 * x

    return wynik_, [odp1, odp2, odp3, odp4, odp5]


def obwod_prostokata():
    a = random.randint(1, 4)
    b = random.randint(4, 9)
    wynik_ = a * 2 + b * 2
    print(f"Obwod prostokata o dlugosci bokow {a} i {b}")
    odp1 = wynik_ + random.randint(2, 8)
    odp2 = a * 3 + b
    odp3 = max(a * 5 - b, b * 5 - a)
    odp4 = a + b
    odp5 = 3 * (a + b)

    return wynik_, [odp1, odp2, odp3, odp4, odp5]


def print_literki(odpowiedzi):
    i = 0
    for odp in odpowiedzi:
        print(f"{i}) {odp}")
        i = i + 1


def trzeci_kat_trojkata():
    a = random.randint(5, 120)
    b = random.randint(5, 180 - a)
    wynik_ = 180 - a - b
    print(f"Trojkat ma katy {a} i {b}. Trzeci kat tego trojkata wynosi wynosi:")
    odp1 = 190 - a - b
    odp2 = wynik_ - 10
    odp3 = wynik_ + 10
    odp4 = 90 - a
    odp5 = 100 - b
    odp6 = 2 * a
    odp7 = 270 - a - b
    odp8 = a + b - 100

    odpowiedzi = [odp1, odp2, odp3, odp4, odp5, odp6, odp7, odp8]
    # odrzuc ujemne katy
    odpowiedzi = [odp for odp in odpowiedzi if odp > 0]

    return wynik_, odpowiedzi


def kat_przylegly():
    a = random.randint(5, 175)
    wynik_ = 180 - a
    print(f"Kat przylegly do {a} wynosi:")
    odp1 = 190 - a
    odp2 = wynik_ - 10
    odp3 = wynik_ + 10
    odp4 = 90 - a
    odp5 = 100 - a
    odp6 = 2 * a
    odp7 = 270 - a
    odp8 = a - 100

    odpowiedzi = [odp1, odp2, odp3, odp4, odp5, odp6, odp7, odp8]

    # odrzuc ujemne katy
    odpowiedzi = [odp for odp in odpowiedzi if odp > 0]

    return wynik_, odpowiedzi


def wpisz_wynik(liczba_odpowiedzi):
    while True:
        twoja_odp = input()

        if twoja_odp == "x":
            sys.exit()  # zamknij program

        try:
            twoja_odp = int(twoja_odp)

            if twoja_odp >= liczba_odpowiedzi:
                print(f"Blad. Musisz wpisac liczbe od 0 do {liczba_odpowiedzi-1}")
                continue

            return twoja_odp
        except:
            print(f"Blad. Musisz wpisac liczbe od 0 do {liczba_odpowiedzi-1}")


def objetosc():
    a = random.randint(1, 5)
    wynik_ = a * a * a
    print(f"UWAGA ZADANIE Z KLASY 6. Objetosc bryly o krawedzi {a} wynosi:")
    odp1 = a + a + a
    odp2 = a * a
    odp3 = a * a + a * a
    odp4 = a**4
    return wynik_, [odp1, odp2, odp3, odp4]


def kat_ostry_czy_rozwarty():
    a = random.randint(2, 150)
    wynik_ = "prosty"
    if a > 90:
        wynik_ = "rozwarty"
    else:
        wynik_ = "ostry"

    print(f"Kat {a} stopni jest:")

    return wynik_, ["prosty", "ostry", "rozwarty"]


lista_zadan = [
    pole_rombu,
    pole_trapezu,
    trojkat,
    obwod_prostokata,
    objetosc,
    mnozenie_dziesietnego_przez_potege10,
    mnozenie_dziesietnego_przez_dziesietny,
    kat_przylegly,
    trzeci_kat_trojkata,
    kat_ostry_czy_rozwarty,
]

lista_zadan_nie_sortuj = [
    mnozenie_dziesietnego_przez_potege10,
    mnozenie_dziesietnego_przez_dziesietny,
]

random.shuffle(lista_zadan)
punkty = 0


if __name__ == "__main__":
    print("Witaj w quizie matematycznym!")
    print(f"Zadamy ci {len(lista_zadan)} pytan.")
    print("(Zeby wyjsc z programu wcisnij x)")
    input("Kliknij enter aby rozpoczac...")

    numer_zadania = 1
    for zadanie in lista_zadan:
        print(f"Losuje pytanie {numer_zadania} \u231B ...")
        time.sleep(1)
        print("_" * 100)
        print(f"{numer_zadania}. ", end="")
        good_wynik_, odpowiedzi = zadanie()
        odpowiedzi.append(good_wynik_)
        odpowiedzi = sorted(set(odpowiedzi))
        odpowiedzi = [
            odp for odp in odpowiedzi if "e-" not in str(odp)
        ]  # usuwianie skrajnie malych liczb
        if zadanie in lista_zadan_nie_sortuj:
            random.shuffle(odpowiedzi)
        print_literki(odpowiedzi)
        twoja_odp = wpisz_wynik(len(odpowiedzi))
        twoj_wynik_ = odpowiedzi[twoja_odp]

        if twoj_wynik_ == good_wynik_:
            punkty = punkty + 1
            print(f"Brawo! {random.choice(emoji_success)} Masz {punkty} pkt.")
        else:
            print(
                f"No niestety prawidlowa odp to {good_wynik_} a nie {twoj_wynik_} \U0001F622"
            )

    procent = int(punkty * 100 / len(lista_zadan))
    print(
        f"Zdobyto {punkty} z {len(lista_zadan)} pkt. czyli {procent}%. Zagraj jeszcze raz!"
    )
