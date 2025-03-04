
# Funkcija koja izračunava ukupnu zaradu
def total_euro(radni_sati, eura_po_satu):
    return radni_sati * eura_po_satu

# Unos od korisnika
radni_sati = float(input("Radni sati: "))
eura_po_satu = float(input("eura/h: "))

# Pozivanje funkcije za izračun
ukupno = total_euro(radni_sati, eura_po_satu)

# Ispis rezultata
print(f"Ukupno: {ukupno} eura")
