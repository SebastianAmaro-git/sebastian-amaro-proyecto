class Reactivos:
    def __init__(self, id, nombre, descripcion, costo, categoria, inventario_disponible, unidad_medida, fecha_caducidad, minimo_sugerido, conversiones_posibles):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.categoria = categoria
        self.inventario_disponible = inventario_disponible
        self.unidad_medida = unidad_medida
        self.fecha_caducidad = fecha_caducidad
        self.minimo_sugerido = minimo_sugerido
        self.conversiones_posibles = conversiones_posibles
    
    def mostrar_atr(self):
        print("\n------------------------------------------------------")
        print("[ID:", self.id,"]")
        print("Nombre:", self.nombre)
        print("Descripción:", self.descripcion)
        print("Costo:", self.costo)
        print("Categoría:", self.categoria)
        print("Inventario disponible:", self.inventario_disponible)
        print("Unidad de medida:", self.unidad_medida)
        print("Fecha de caducidad:", self.fecha_caducidad)
        print("Mínimo sugerido:", self.minimo_sugerido)
        print("Conversiones disponibles:")
        for conversion in self.conversiones_posibles:
            print(f" - Unidad: {conversion['unidad']}, Factor: {conversion['factor']}")