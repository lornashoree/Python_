import math


def krzel_shop():
   while True:

        towar ={"Kapusta":15,"Cebula":20,"Ziemniak":30,"Seler":12}
        cena = {"Kapusta":35,"Cebula":40,"Ziemniak":50,"Seler":62}
        produkt = {0:"Kapusta",1:"Cebula",2:"Ziemniak",3:"Seler"}
        tablica = []
        max_waga = 0
        koszyk = 0

        for warzywo, waga in towar.items():
            print(f"{warzywo}- paczka {waga}kg - {cena[warzywo]} zł")
        print("")

    
        for i in range(4):
            print(f"Ile paczek {produkt[i]}, chcesz kupić ?")
            tablica.append(int(input("")))
        

        

        
        max_waga = tablica[0]*towar["Kapusta"]+tablica[1]*towar["Cebula"]+tablica[2]*towar["Ziemniak"]+tablica[3]*towar["Seler"]
        koszyk  = tablica[0]*cena["Kapusta"]+tablica[1]*cena["Cebula"]+tablica[2]*cena["Ziemniak"]+tablica[3]*cena["Seler"]

        rabat = koszyk*0.1

        cena_z_rabatem = koszyk - rabat



        if max_waga > 3000:
            print(f"Twoj waga jest równa {max_waga}kg więc jest zbyt duża, spróbuj ponownie\n")
            
        else:
            print(f" waga jest równa: {max_waga}kg\n")
            break
        
        if koszyk > 2000:
            print(f"Przekroczyłeś 2000zł więc otrzymujesz rabat 10% i płacisz {cena_z_rabatem}zł a nie {koszyk}zł\n")

        else:
            print(f"Płacisz {koszyk}zł\n")
    
   
krzel_shop()

