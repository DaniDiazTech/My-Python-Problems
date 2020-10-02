# read animals.txt
# and write animals_new.txt

animals_old = open("animals.txt")
animals_new = open("animals_new.txt", "w")

animals_line = ""

for animals in animals_old:
    animals_line += animals.rstrip("\n")
    animals_line += " "

animals_new.write(animals_line)

animals_old.close()
animals_new.close()
