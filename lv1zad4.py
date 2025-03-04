
# Funkcija za izračunavanje srednje pouzdanosti
def izracunaj_pouzdanost(datoteka):
    try:
        # Otvaranje datoteke u načinu za čitanje
        with open(datoteka, 'r') as fhand:
            # Lista za pohranu svih pouzdanosti
            pouzdanosti = []

            # Čitanje datoteke liniju po liniju
            for linija in fhand:
                linija = linija.strip()  # Uklanjanje suvišnih razmaka
                # Provjera da li linija sadrži traženi obrazac
                if linija.startswith("X-DSPAM-Confidence:"):
                    try:
                        # Izdvajanje broja nakon oznake X-DSPAM-Confidence:
                        povjerenje = float(linija.split(":")[1].strip())
                        pouzdanosti.append(povjerenje)
                    except ValueError:
                        # Ako nije broj, preskoči tu liniju
                        pass

            # Provjera da li imamo unesene pouzdanosti
            if len(pouzdanosti) > 0:
                # Izračunavanje srednje vrijednosti
                srednja_pouzdanost = sum(pouzdanosti) / len(pouzdanosti)
                print(f"Average X-DSPAM-Confidence: {srednja_pouzdanost}")
            else:
                print("Nema pronađenih X-DSPAM-Confidence linija u datoteci.")
    except FileNotFoundError:
        print("Datoteka nije pronađena. Provjerite ime datoteke.")

# Glavni program
datoteka = input("Ime datoteke: ")
izracunaj_pouzdanost(datoteka)
