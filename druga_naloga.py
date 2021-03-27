marsovci = input()
naloge = {}
for i in range(int(marsovci)):
    zna = input()
    zna = zna.split()
    zna = list(map(int, zna))
    for j in range(len(zna)):
        try:
            naloge[zna[j]] = naloge[zna[j]] + 1
        except KeyError:
            naloge[zna[j]] = 1


n_razlicnih = len(set(naloge.values()))

if n_razlicnih > 2:
    print("Ne")
else:
    print("Da")


# program najprej prebere standardni vhod in v spremenjlivko marsovci sharani število različnih marsovcev
# s for zanko za vsakega marsovca pregleda katere naloge zna opraviti (in jih shrani v spremenljivko zna)
# v primeru da nalogo vidi prvič jo kot index doda v slovar naloge (vrednost je 1)
# v primeru da naloga že obstaja vrednosti v slovarju naloge za doda 1

# v 14 vrstici:
# najprej iz slovarja prebere samo vrednosti brez indeksov in jih spravi v seznam
# nato iz seznama ustvari množico (set) saj so v njej lahko samo različni elementi (v seznamu imamo lahko več istih vrednosti)
#     (npr. iz seznama 1, 1, 2, 3, 4, 4, 3, 5, 5, 2, naredi množico 1, 2, 3, 4, 5)

# če ima množica več kot 2 elementa pomeni da je razlika med največjim in najmanjšim vsaj 2 -> naloge niso enakomerno porazdeljene