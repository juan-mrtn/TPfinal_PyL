class AFD:
    def __init__(self):
        self.estado_actual = 'q0'
        self.estado_final = {'q7'}
        self.transiciones = {
            'q0': {'M': 'q1', 'D': 'muerto', 'S': 'muerto', 'm': 'muerto', 'muerto': 'muerto'},
            'q1': {'D': 'q2', 'M': 'q3', 'm': 'q3', 'S': 'q3', 'muerto': 'muerto'},
            'q2': {'D': 'q4', 'M': 'q5', 'm': 'q5', 'S': 'q5', 'muerto': 'muerto'},
            'q3': {'D': 'q5', 'M': 'muerto', 'm': 'muerto', 'S': 'muerto', 'muerto': 'muerto'},
            'q4': {'D': 'q6', 'M': 'q6', 'm': 'q6', 'S': 'q6', 'muerto': 'muerto'},
            'q5': {'D': 'q6', 'M': 'muerto', 'm': 'muerto', 'S': 'muerto', 'muerto': 'muerto'},
            'q6': {'m': 'q7', 'D': 'muerto', 'M': 'muerto', 'S': 'muerto', 'muerto': 'muerto'},
            'q7': {'D': 'muerto', 'M': 'muerto', 'S': 'muerto', 'm': 'muerto', 'muerto': 'muerto'},
            'muerto': {'D': 'muerto', 'M': 'muerto', 'S': 'muerto', 'm': 'muerto', 'muerto': 'muerto'}
        }
    
    def reset(self):
        self.estado_actual = 'q0'
  
    def transformar_caracter(self, caracter):
        """Simbolos En ASCII: Del 33 al 47; 58 al 64; 91 al 96; 123 al 126"""
        if 33 <= ord(caracter) <= 47 or 58 <= ord(caracter) <= 64 or 91 <= ord(caracter) <= 96 or 123 <= ord(caracter) <= 126:
            return 'S'
        elif 'A' <= caracter <= 'Z' or caracter == 'Ñ':
            return 'M'
        elif 'a' <= caracter <= 'z' or caracter == 'ñ':
            return 'm'
        elif '0' <= caracter <= '9':
            return 'D'
        else:
            return 'muerto'

        
    def procesar(self, simbolo):
        #if simbolo in self.transiciones[self.estado_actual]:
        self.estado_actual = self.transiciones[self.estado_actual][simbolo]

    def acepta(self, cadena):
        self.reset()
        for simbolo in cadena:
            print(self.transformar_caracter(simbolo))
            self.procesar(self.transformar_caracter(simbolo))
            #print(f"Procesando símbolo: {simbolo}, Simbolo Transformado: {self.transformar_caracter(simbolo)}, Estado actual: {self.estado_actual}")
        return self.estado_actual in self.estado_final

afd = AFD()

c = input("Ingrese una cadena de 5 caracteres: ")
while c != "":
    c = input("Ingrese una cadena de 5 caracteres: ")
    if afd.acepta(c):
        print()
        print("-----------------------------")
        print("Cadena aceptada")
        print("-----------------------------")
    else:
        print()
        print("-----------------------------")
        print("Cadena no aceptada")
        print("-----------------------------")
    print()



