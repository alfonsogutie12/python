import time
class auto:
    cruceros=0
    frena=0
    velocidad=0
    def acelera(self, velocidad):
        for i in range (0,velocidad,5):
            print("aceleracion del auto: ",i, " km/h")
            time.sleep(0.5)
        print("la velocidad del auto es: ",velocidad, " km/h")
    
    def frenar(self, velocidad, frena):
        for i in range (velocidad, frena, -5):
            print("el auto esta frenando", i , " km/h")
            time.sleep(1)
        print("la velocidad del auto es: ",frena, " km/h")
    
    def crucero(self, frena, cruceros):
       
        print("a activado la velocidad crucero")
        for i in range(frena, cruceros, 10):
            print("aceleracion del auto: ",i, " km/h")
            time.sleep(0.5)
        print("velocidad crucero: ",cruceros, " km/h")
                       
       


m = auto()
m.acelera(60)
m.frenar(60,10)
m.crucero(10,60)