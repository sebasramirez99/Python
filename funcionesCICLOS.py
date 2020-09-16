import datetime

def superarpoblacion(poblacionA, poblacionB, tasaA, tasaB):
    year = datetime.date.today().year
    while poblacionB < poblacionA:
        poblacionA = poblacionA * (1+tasaA)
        poblacionB = poblacionB * (1+tasaB)
        year += 1
        print(year)
    return year

def multiplosrango(limiteinferior, limitesuperior, numero):
    multiplos = []
    if limiteinferior > 0 and limitesuperior > 0:
        if limiteinferior > limitesuperior:
            limiteinferior, limitesuperior = limitesuperior, limiteinferior
        limitesuperior += 1
        for i in range(limiteinferior, limitesuperior):
            if (i % numero) == 0:
                multiplos.append(i)
    return multiplos