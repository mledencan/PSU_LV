
# Inicijalizacija prazne liste za pohranu brojeva
brojevi = []

# Beskonačna petlja za unos brojeva
while True:
    unos = input("Unesite broj (ili 'Done' za završetak): ")

    # Ako korisnik upiše 'Done', izlazi iz petlje
    if unos.lower() == 'done':
        break

    try:
        # Pokušaj pretvorbe unosa u broj
        broj = float(unos)
        brojevi.append(broj)
    except ValueError:
        # Ako unos nije broj, ispisuje poruku o grešci
        print("Pogrešan unos! Molimo unesite broj.")

# Provjera da li je lista prazna
if len(brojevi) > 0:
    # Računanje srednje, minimalne i maksimalne vrijednosti
    srednja = sum(brojevi) / len(brojevi)
    minimalna = min(brojevi)
    maksimalna = max(brojevi)

    # Ispis statistike
    print(f"\nBroj unesenih brojeva: {len(brojevi)}")
    print(f"Srednja vrijednost: {srednja:.2f}")
    print(f"Minimalna vrijednost: {minimalna}")
    print(f"Maksimalna vrijednost: {maksimalna}")

    # Sortiranje liste i ispis
    brojevi.sort()
    print("Sortirana lista brojeva:", brojevi)
else:
    print("Niste unijeli niti jedan broj.")
