import random as rnd

def hod_kostkou():
    return rnd.randint(1, 6)

while True:
    val = input("Pro hod kostkou zmackni h, pro ukonceni q\n")
    if val == "h":
        print("tento hod je:\n", hod_kostkou())
    elif val == "q":
        print("Konec hry\n")
        break