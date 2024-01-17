# Help! Een vriend is vandaag jarig en we hebben geen verjaardagskaart gekocht…
#
# Schrijf een functie genaamd genereer_verjaardagskaart die een verjaardagskaart genereert.
# Gebruik de functie om een gepersonaliseerde verjaardagsboodschap voor de jarige te maken.
# Dankzij de functie kunnen we die makkelijk voor volgende verjaardagen gebruiken 😉
# Voorbeeldgebruik:
#
# # Gegevens van de jarige
# naam = "Alex"
# leeftijd = 12
#
# print(genereer_verjaardagskaart(naam, leeftijd))
#
# Voorbeelduitvoer:
#
# Gefeliciteerd met je verjaardag, Alex!
# Je bent nu 12 jaar oud.
# Moge je dag gevuld zijn met vreugde en lach! 🎉🎂


def genereer_verjaardagskaart(voornaam, leeftijd):
    boodschap = "Gefeliciteerd met je verjaardag, " + voornaam + "!\n"
    leeftijdsboodschap = "Je bent nu " + str(leeftijd) + " jaar oud.\n"
    wens = "Moge je dag gevuld zijn met vreugde en lach! 🎉🎂"
    verjaardagskaart = boodschap + leeftijdsboodschap + wens
    return verjaardagskaart


# Gegevens van de jarige
naam = "Alex"
leeftijd = 12
print(genereer_verjaardagskaart(naam, leeftijd))