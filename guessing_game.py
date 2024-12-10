import random

numero_maxim = 100

def main():
    print('Benvingut al Guessing Game!')
    print('Intenta adivinar el número correcte amb el menor número d\'intents possibles.')
    
    total_partides = 0
    intents_totals = 0
    millor_partida = float('inf')

    while True:
        print('\nNova partida!')
        intents = joc()
        total_partides += 1
        intents_totals += intents
        millor_partida = min(millor_partida, intents)

        jugar_de_nou = input('Vols jugar una altra partida? (sí/no): ').strip().lower()
        if jugar_de_nou not in ['sí', 'si', 's', 'yes', 'y']:
            break

    print('\nEstadístiques finals:')
    print(f'Total de partides jugades: {total_partides}')
    print(f'Intents totals: {intents_totals}')
    print(f'Mitjana d\'intents per partida: {round(intents_totals / total_partides, 1)}')
    print(f'Intents en la millor partida: {millor_partida}')
    print('Gràcies per jugar!')

def joc():
    numero = random.randrange(1, numero_maxim)
    intents = 0
    print(f'Estic pensant un número entre 1 i {numero_maxim}.')
    
    while True:
        try:
            guess = int(input('Quin número vols provar? '))
            intents += 1
            if guess > numero:
                print('És més baix.')
            elif guess < numero:
                print('És més alt.')
            else:
                print(f'Has endevinat el número en {intents} intents!')
                return intents
        except ValueError:
            print('Si us plau, introdueix un número vàlid.')


main()
