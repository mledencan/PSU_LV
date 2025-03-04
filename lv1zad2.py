
# Unos ocjene od korisnika
ocjena = float(input("Unesite ocjenu (između 0.0 i 1.0): "))

# Provjera uvjeta i ispis odgovarajuće kategorije
if ocjena >= 0.9:
    print("Ocjena: A")
elif ocjena >= 0.8:
    print("Ocjena: B")
elif ocjena >= 0.7:
    print("Ocjena: C")
elif ocjena >= 0.6:
    print("Ocjena: D")
else:
    print("Ocjena: F")
