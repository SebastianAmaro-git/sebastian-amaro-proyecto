class Recetas:
    def __init__(self, id, nombre, objetivo, reactivos_utilizados, procedimiento, valores_a_medir):
        self.id = id
        self.nombre = nombre
        self.obejtivo = objetivo
        self.reactivos_utilizados = reactivos_utilizados
        self.procedimiento = procedimiento
        self.valores_a_medir = valores_a_medir
    
    def mostrar_atr(self):
        print("\n-----------------------------------------")
        print("ID:", self.id)
        print("Nombre:", self.nombre)
        print("Objetivo:", self.obejtivo)
        print("\n--------------------------------------")
        print("Reactivos utilizados:")
        count = 0
        for reactivo in self.reactivos_utilizados:
            count += 1
            print(f"\n - Reactivo {count}: \nID: {reactivo['reactivo_id']}, \nCantidad Necesaria: {reactivo['cantidad_necesaria']}, \nUnidad de Medida: {reactivo['unidad_medida']}")
        print("\n--------------------------------------")
        print("Procedimiento:")
        count = 0
        for paso in self.procedimiento:
            count += 1
            print(f" - Paso {count}: {paso}")
        print("\n--------------------------------------")
        print("Valores a Medir:")
        count = 0
        for valor in self.valores_a_medir:
            count += 1
            print(f" -({count})- \nNombre: {valor['nombre']}, \nFormula: {valor['formula']}, \nMinimo: {valor['minimo']}, \nMaximo: {valor['maximo']}")

        
        


            