    
from operazioni import quadrato, cerchio, rettangolo



forma_quadrato= '''
#####
#   #
#   #
#   #
#####
'''
forma_cerchio= '''
    ***
 *       *
*         *
*         *
 *       *
    ***
'''
forma_rettangolo='''
********
*        *
*        *
*        *
*******
'''


immagini_geometriche =[forma_quadrato,forma_cerchio,forma_rettangolo]


while True:
    print("Quale figura geometrica hai bisogno di calcolare?")
    
    scelta_utente = 0
    
    while scelta_utente not in [1, 2, 3]:
        try:
            scelta_utente = int(input("Quadrato premi 1, cerchio premi 2, rettangolo premi 3: "))
            print (immagini_geometriche[scelta_utente - 1])
            if scelta_utente == 1:
                quadrato()
            elif scelta_utente == 2:
                cerchio()
            elif scelta_utente == 3:
                rettangolo()
            else:
                print("Scelta non valida")
        
        except ValueError:
            print("Errore: devi inserire un numero come scelta.")
    
    scelta = input("Vuoi calcolare un'altra figura geometrica? (s/n): ")
    
    if scelta.lower() != 's':
        break


