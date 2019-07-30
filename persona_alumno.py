

class persona():#clase persona.
    
    def _init_(self, nombre, edad):#se inicializa con nombre y edad.
        self.nombre = nombre
        self.edad = edad
        
    
    def octener_nombre(self):#metodo octener_nombre.
        self.nombre = input("Nombre  del alumno: ")#se pide el nombre.
        
    def octener_edad(self):#metodo octener_edad.
        self.edad = int(input("edad de alumno: "))#se pide la edad.
        
class alumno(persona):#clase alumno.
    
    def _init_(seft, nota, nombre, edad):#inicializamos con nota,(nombre y edad la pedimos de persona).
        persona._init_(seft, nombre, edad)#inicializamos la clase persona con nombre y edad.
        self.nota=nota
        
    def octener_nota(self):#metodo octener_nota.
        self.nota=float(input("nota de alumno"))#sepide la nota del alumno.
        
    def mostrar(self, nota, nombre, edad):#metodo mostrar.
        print("La norta es: ",self.nota)#imprime la nota.
        print("La edad es: ",self.edad)#imprime la edad.
        print("el nombre es: ",self.nombre)#imprime el nombre.
        

alu = alumno()
alu.octener_nombre()
alu.octener_edad()
alu.octener_nota()
alu.mostrar(0,"",0)