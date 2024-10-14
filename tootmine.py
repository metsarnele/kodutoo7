# Funktsioon, mis arvutab uue laovaru pärast tootmist
def uuenda_laovaru(toodetud, laovaru, max_varu): # Funktsioon võtab argumendina toodetud ühikute arvu, laovaru ja maksimaalse laovaru
    if laovaru + toodetud <= max_varu:  # Kui laovaru ja toodetud summa on väiksem või võrdne maksimaalse laovaruga
        laovaru += toodetud # Suurendame laovaru toodetud ühikute võrra
        return laovaru, True  # Tagastame uue laovaru ja märgime, et tootmine õnnestus
    else: # Kui laovaru ja toodetud summa on suurem kui maksimaalne laovaru
        return laovaru, False  # Ei saanud toota rohkem, laovaru täis

# Peamine tootmisfunktsioon
def tooda(tootmis_kiirus, paevad, laovaru, max_varu): # Funktsioon võtab argumendina tootmis kiiruse, tootmise kestuse päevades, laovaru ja maksimaalse laovaru
    for paev in range(1, paevad+1): # Tsükkel, mis käib läbi kõik tootmise päevad
        print(f"\nPäev {paev}:") # Väljastame päeva numbrit
        toodetud = tootmis_kiirus # Toodetud ühikute arv on võrdne tootmis kiirusega
        laovaru, edukas = uuenda_laovaru(toodetud, laovaru, max_varu) # Uuendame laovaru ja kontrollime, kas tootmine õnnestus
        
        if edukas: # Kui tootmine õnnestus
            print(f"Toodeti {toodetud} ühikut. Uus laovaru on {laovaru} ühikut.") # Väljastame toodetud ühikute arvu ja uue laovaru
        else: # Kui tootmine ei õnnestunud
            print(f"Laovaru on täis! Ei saanud toota {toodetud} ühikut. Praegune laovaru: {laovaru} ühikut.") # Väljastame, et laovaru on täis ja tootmine ei õnnestunud
            break  # Peatame tootmise, kui laovaru on täis
    return laovaru # Tagastame lõpliku laovaru

# Põhiprogramm
def tootmine(): # Funktsioon, mis käivitab tootmise
    tootmis_kiirus = 10  # Päevas toodetud ühikute arv
    paevad = 7  # Tootmise kestus päevades
    max_varu = 50  # Maksimaalne laovaru
    laovaru = 0  # Algne laovaru

    print("Tootmise alustamine...") # Väljastame, et tootmine on alustatud
    laovaru = tooda(tootmis_kiirus, paevad, laovaru, max_varu) # Käivitame tootmise
    
    print(f"\nTootmine lõpetatud. Lõplik laovaru: {laovaru} ühikut.") # Väljastame lõpliku laovaru

# Käivitame tootmisprogrammi
tootmine()
