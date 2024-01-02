import random
import time

print("Witaj w szczurowym quizie ")


def pole_rombu1():
    a = random.randint(3, 9)
    h = random.randint(2, 8)
    wynik = a * h

    print(f"Pole rombu o podstawie {a} i wysokosci {h} wynosi:")

    odp1 = wynik + random.randint(2, 8)
    odp2 = int(wynik / 2)
    odp3 = max(1, wynik - random.randint(2, 8))
    odp4 = 4 * h
    odp5 = 4 * a

    return wynik, [odp1, odp2, odp3, odp4, odp5]


def trojkat():
    a = random.randint(3, 9)
    h = random.randint(3, 9)
    wynik_ = a * h / 2
    print(f"Pole trojkata o podstawie {a} i wysokosci {h}:")
    odp1 = wynik_ + random.randint(2, 8)
    odp2 = int(wynik_ * 2)
    odp3 = max(1, wynik_ - random.randint(2, 8))
    odp4 = int(wynik_ * 1.5)
    odp5 = (a + 1) * (h - 1) / 2
    return wynik_, [odp1, odp2, odp3, odp4, odp5]


def pole_rombu2():
    x = random.randint(3, 9)
    y = random.randint(2, 8)
    wynik = x * y / 2

    print(f"Pole rombu o przekatnych {x} i {y}:")
    odp1 = wynik + random.randint(2, 8)
    odp2 = int(wynik / 2)
    odp3 = max(1, wynik - random.randint(2, 8))
    odp4 = 4 * y
    odp5 = 4 * x

    return wynik, [odp1, odp2, odp3, odp4, odp5]


def obwod_prostokata():
    a = random.randint(1, 4)
    b = random.randint(4, 9)

    wynik = a * 2 + b * 2
    print(f"Obwod prostakata o dlugosci bokow {a} i {b}")

    odp1 = wynik + random.randint(2, 8)
    odp2 = a * 3 + b
    odp3 = max(a * 5 - b, b * 5 - a)
    odp4 = a + b
    odp5 = 3 * (a + b)

    return wynik, [odp1, odp2, odp3, odp4, odp5]


def print_literki(odpowiedzi):
    i = 0
    for odp in odpowiedzi:
        print(f"{i}) {odp}")
        i = i + 1


lista_zadan = [pole_rombu2, pole_rombu1, trojkat, obwod_prostokata]
random.shuffle(lista_zadan)
punkty = 0


if __name__ == "__main__":
    for zadanie in lista_zadan:
        print("_" * 100)
        good_wynik, odpowiedzi = zadanie()
        odpowiedzi.append(good_wynik)
        odpowiedzi = list(set(odpowiedzi))
        random.shuffle(odpowiedzi)
        print_literki(odpowiedzi)
        twoja_odp = int(input())
        twoj_wynik = odpowiedzi[twoja_odp]

        if twoj_wynik == good_wynik:
            print("jestes szczur maciek")
            punkty = punkty + 1
        else:
            print(
                f"jestes lamus bo prawidlowa odpowiedz to {good_wynik} a nie {twoj_wynik}"
            )

        time.sleep(1)

    print(f"Zdobyto {punkty} z {len(lista_zadan)} pkt.")
