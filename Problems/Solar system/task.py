# create the planets.txt
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

solar_system = open("planets.txt", "w", encoding="utf-8")

for planet in planets:
    solar_system.write(planet + '\n')

solar_system.close()
