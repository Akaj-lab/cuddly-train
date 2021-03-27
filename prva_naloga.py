def MoznaGesla(geslo):
    mozna_gesla = []
    geslo = list(geslo)
    for i in range(len(geslo)):
        geslo_new = geslo.copy()
        try:
            int(geslo[i])
        except ValueError:
            geslo_new[i] = geslo[i].upper()
    
        mozna_gesla.append(listtostring(geslo_new))

    gesla_s_piko = []
    for i in mozna_gesla:
        geslo_new = list(i)
        for j in range(len(geslo_new) + 1):
            appended = geslo_new.copy()
            appended.insert(j, ".")
            gesla_s_piko.append(listtostring(appended))
    

    return gesla_s_piko
        

def listtostring(seznam):
    output = ""
    for x in seznam:
        output += x
    
    return output





# v program najprej vnesemo geslo (male črke in številke)
# nato v seznam mozna_gesla doda vse možne kombinacije gesla z eno veliko črko 
#     iz stinga geslo najprej ustvari seznam, nato pa s for zanko gre od 1. do 
#     zadnjega elementa in na i-tem elementu spremeni i-to črko v veliko
# na isti način dodaja pike