import time
class auto:
    
    def acelera(self, velocidad):
        for i in range (0,velocidad,5):
            print("aceleracion del auto: ",i, " km/h")
            time.sleep(0.5)
        print("la velocidad del auto es: ",i, " km/h")
    
    def frenar(self, velocidad, frena):
        for e in range (velocidad, frena, -5):
            n = int(input("quiere frenar: si = 1, no = 2: "))
            if (n == 1):
                print("el auto esta frenando", e , " km/h")
                time.sleep(0.5)
            else:
                print("la velocidad del auto es: ",e, " km/h")
                break
        n = int(input("quiere activar velocidad crucero: si=1 no=2: "))
        if (n == 1):
            print("aceleracion del auto: ",60, " km/h")
            time.sleep(0.5)
            print("uste esta en velocidad crucero: ",60, " km/h")
        else:
            print("velocidad: ", e ,"km/h")
       
    

m = auto()
m.acelera(60)
m.frenar(60,10)
