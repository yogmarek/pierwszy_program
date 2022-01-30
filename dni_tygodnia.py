dzien = input('Podaj dzień tygodnia:')
dni_pracujace = [
    'Poniedziałek',
    'Wtorek',
    'Środa',
    'Czwartek',
    'Piątek',
]
weekend = [
    'Sobota',
    'Niedziela',
]
if dzien in dni_pracujace:
    print(dzien + ' ''to jest dzień pracujący')
elif dzien in weekend:
    print(dzien + ' ''to jest weekend')
else:
    print('Źle napisałeś dzień tygodnia. Podaj z dużej litery')
