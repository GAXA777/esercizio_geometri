import math

def quadrato():
    lato = None
    while lato is None:
        try:
            lato = float(input("Inserisci il lato del tuo quadrato: "))
        except ValueError:
            print("Errore: inserisci un numero valido.")

    perimetro = lato * 4
    print("Il perimetro del tuo quadrato è:", perimetro)


def cerchio():
    pi = math.pi
    pi_troncato = round(pi, 5)

    raggio = None
    while raggio is None:
        try:
            raggio = float(input("Inserisci il raggio del cerchio per calcolare la circonferenza: "))
        except ValueError:
            print("Errore: inserisci un numero valido.")
    
    circonferenza_cerchio = 2 * pi_troncato * raggio
    print("La circonferenza del tuo cerchio è:", circonferenza_cerchio)


def rettangolo():
    base = None
    while base is None:
        try:
            base = float(input("Inserisci qui la base del tuo rettangolo: "))
        except ValueError:
            print("Errore: inserisci un numero valido.")

    altezza = None
    while altezza is None:
        try:
            altezza = float(input("Inserisci qui l'altezza del tuo rettangolo: "))
        except ValueError:
            print("Errore: inserisci un numero valido.")
    
    perimetro = base * 2 + altezza * 2
    print("Il perimetro del tuo rettangolo è:", perimetro)


