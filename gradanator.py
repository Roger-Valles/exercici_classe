def main():
    Introducció()
    Parcial1, Parcial2, Final, Pes1, Pes2, Pes4, Treballs, Pes3 = preguntes()
    NotaFinal = SumaNotes(Parcial1, Parcial2, Final, Pes1, Pes2, Pes4, Treballs, Pes3)
    Missatge_Nota(NotaFinal)

def Introducció():
    print('Benvingut al programa de càlcul de notes!')
    print('Introdueixi les notes de l\'alumne, tenint en compte que les notes van del 1 al 100')

def preguntes():
    print('Nota del primer parcial: ')
    Parcial1 = int(input())
    Parcial1 = min(Parcial1, 100)
    
    print('Introdueix el pes de l\'examen: ')
    Pes1 = int(input())
    
    print('Nota del segon parcial: ')
    Parcial2 = int(input())
    Parcial2 = min(Parcial2, 100)
    
    print('Introdueix el pes de l\'examen: ')
    Pes2 = int(input())
    
    print('Nota del examen final: ')
    Final = int(input())
    Final = min(Final, 100)
    
    print('Introdueix el pes de l\'examen: ')
    Pes4 = int(input())

    print('Quants treballs hi han hagut? ')
    NumeroTreballs = int(input())
    
    print('Introdueix el pes dels treballs: ')
    Pes3 = int(input())
    
    nota_treball = 0
    nota_max_treball = 0
    
    for x in range(1, NumeroTreballs + 1):
        print(f'Nota del treball nº{x}')
        nota_max = int(input('Nota màxima del treball: '))
        nota = int(input('Nota assolida del treball: '))
        nota_treball += nota
        nota_max_treball += nota_max

    Treballs = min(nota_treball, nota_max_treball)

    return Parcial1, Parcial2, Final, Pes1, Pes2, Pes4, Treballs, Pes3

def SumaNotes(Parcial1, Parcial2, Final, Pes1, Pes2, Pes4, Treballs, Pes3):
    NotaFinal = (Parcial1 / 100 * Pes1) + (Parcial2 / 100 * Pes2) + (Treballs / 100 * Pes3) + (Final / 100 * Pes4)
    print(f'La nota final de l\'alumne és de: {round(NotaFinal, 1)}')
    return NotaFinal

def Missatge_Nota(NotaFinal):
    if NotaFinal >= 90:
        print('L\'alumne ha assolit amb una A')
    elif NotaFinal >= 80:
        print('L\'alumne ha assolit amb una B')
    elif NotaFinal >= 70:
        print('L\'alumne ha assolit amb una C')
    elif NotaFinal >= 60:
        print('L\'alumne ha assolit amb una D')
    else:
        print('L\'alumne no ha assolit, per tant té una F')

main()
