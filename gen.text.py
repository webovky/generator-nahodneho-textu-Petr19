from random import choice, randint

souhlasky = "qwrtpsdfghjklzxcvbnm"
samohlasky = "aeiouy"
pismena = "aeiouyqwrtpsdfghjklzxcvbnm"

while True:
    try:
        pocetslov = int(input("počet slov  > "))
        nazevsouboru = input("jméno souboru  > ")
        with open(nazevsouboru, 'w') as f:
            pocet = 1
            slovo = ""
            delka_radku = 0

            while pocet <= pocetslov:
                delka_slova = randint(1, 7)
                slovo = ""
                for i in range(delka_slova):
                    if i == 0:
                        slovo += choice(pismena)
                    else:
                        if slovo[i - 1] in samohlasky:
                            slovo += choice(souhlasky)
                        else:
                            slovo += choice(samohlasky)
                slovo += " "
                f.write(slovo)

                delka_radku += len(slovo)
                if 70 <= delka_radku <= 80:
                    f.write("\n")
                    delka_radku = 0
    
                pocet += 1
        break
    except:
        print("Název souboru např. text.txt")
        