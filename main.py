import time
class auto:
    
    def __init__(self, )
    
    def acelera(self, velocidad):
        for i in range (0,velocidad,5):
            print("aceleracion del auto: ",i, " km/h")
            time.sleep(0.5)
        print("la velocidad del auto es: ",i, " km/h")
    
    def frenar(self, velocidad, frena):
        for i in range (velocidad, frena, -5):
            n = int(input("quiere frenar: si = 1, no = 2: "))
            if (n == 1):
                print("el auto esta frenando", i , " km/h")
                time.sleep(0.5)
            else:
                print("la velocidad del auto es: ",i, " km/h")
                break
            
    
    def crucero(self, frena, cruceros):
       
        print("a activado la velocidad crucero")
        for i in range(frena, cruceros, 50):
            print("aceleracion del auto: ",i, " km/h")
            time.sleep(0.5)
        print("velocidad crucero: ",i, " km/h")
                       
       


m = auto()
m.acelera(60)
m.frenar(60,10)
m.crucero(10,60)
