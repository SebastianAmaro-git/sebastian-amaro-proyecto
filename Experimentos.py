class Experimentos:
    def __init__(self, id, receta_id, personas_responsables, fecha, costo_asociado, resultado):
        self.id = id
        self.receta_id = receta_id
        self.personas_responsables = personas_responsables
        self.fecha = fecha
        self.costo_asociado = costo_asociado
        self.resultado = resultado
    def mostrar_atr(self): #muestra los atributos de la clase Experimentos
        print("\n---------------------------------------------------")
        print("[ID:", self.id,"]")
        print("Receta ID:", self.receta_id)
        print("Personas Responsables:")
        for persona in self.personas_responsables:
            print(" -", persona)
        print("Fecha:", self.fecha)
        print("Costo Asociado:", self.costo_asociado)
        print("Resultado:", self.resultado)