# Schrijf een Python-programma dat informatie weergeeft over een dier in een dierentuin.
#
# De functie heeft twee parameters: dier_soort en locatie. Enkel de locatie is optioneel, als die niet ingevuld wordt, wordt de waarde “onbekend” genomen.
# De functie moet niets teruggeven, enkel printen.
# 
# Voorbeeldgebruik functies
#
# dierentuin_info("olifant", "Aziatisch gebied")
# dierentuin_info("leeuw")
#
# Uitvoer
#
# In de dierentuin is er een olifant
# Die olifant bevindt zich op locatie: Aziatisch gebied
#
# In de dierentuin is er een leeuw
# Die leeuw bevindt zich op locatie: onbekend

def dierentuin_info(dier_soort, locatie="onbekend"):
    print("In de dierentuin is er een", dier_soort)
    print("Die", dier_soort, "bevindt zich op locatie:", locatie, "\n")


# Voorbeeldgebruik van de functie
dierentuin_info("olifant", "Aziatisch gebied")
dierentuin_info("leeuw")
dierentuin_info("pinguïn", "Poolgebied")