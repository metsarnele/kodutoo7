# Funktsioon, mis arvutab uue laovaru pärast tootmist
def uuenda_laovaru(toodetud, laovaru, max_varu):
    if laovaru + toodetud <= max_varu:
        laovaru += toodetud
        return laovaru, True  # Tagastame uue laovaru ja märgime, et tootmine õnnestus
    else:
        return laovaru, False  # Ei saanud toota rohkem, laovaru täis

# Peamine tootmisfunktsioon
def tooda(tootmis_kiirus, paevad, laovaru, max_varu):
    for paev in range(1, paevad+1):
        print(f"\nPäev {paev}:")
        toodetud = tootmis_kiirus
        laovaru, edukas = uuenda_laovaru(toodetud, laovaru, max_varu)
        
        if edukas:
            print(f"Toodeti {toodetud} ühikut. Uus laovaru on {laovaru} ühikut.")
        else:
            print(f"Laovaru on täis! Ei saanud toota {toodetud} ühikut. Praegune laovaru: {laovaru} ühikut.")
            break  # Peatame tootmise, kui laovaru on täis
    return laovaru

# Põhiprogramm
def tootmine():
    tootmis_kiirus = 10  # Päevas toodetud ühikute arv
    paevad = 7  # Tootmise kestus päevades
    max_varu = 50  # Maksimaalne laovaru
    laovaru = 0  # Algne laovaru

    print("Tootmise alustamine...")
    laovaru = tooda(tootmis_kiirus, paevad, laovaru, max_varu)
    
    print(f"\nTootmine lõpetatud. Lõplik laovaru: {laovaru} ühikut.")

# Käivitame tootmisprogrammi
tootmine()
