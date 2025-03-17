from Reactivos import Reactivos
from datetime import datetime
class GestorReactivo:
    def mostrar_reactivos(self, reactivos):
        print("\n","~"*35)
        print("\nMostrando reactivos:")
        for reactivo in reactivos:
            atr = Reactivos(reactivo['id'],
                            reactivo['nombre'], 
                            reactivo['descripcion'], 
                            reactivo['costo'], 
                            reactivo['categoria'], 
                            reactivo['inventario_disponible'], 
                            reactivo['unidad_medida'],
                            reactivo['fecha_caducidad'],
                            reactivo['minimo_sugerido'],
                            reactivo['conversiones_posibles'])
            atr.mostrar_atr()
    def crear_reactivo(self, reactivos): 
        print("\n","~"*35)
        print("\nCreando reactivo:")
        #Diccionario del reactivo creado
        dict_reactivo = {
            "id": len(reactivos) + 1,
            "nombre": input("Nombre: "),
            "descripcion": input("Descripción: "),
            "costo":  0,
            "categoria": input("Categoría: "),
            "inventario_disponible": 0,
            "unidad_medida": input("Unidad de medida: "),
            "fecha_caducidad": "",
            "minimo_sugerido": input("Mínimo sugerido: "),
            "conversiones_posibles": []
        }
        while True:
            fecha = input("Fecha de caducidad (formato AAAA-MM-DD):")
            try:
                fecha_caducidad = datetime.strptime(fecha, "%Y-%m-%d") #Verifica formato válido
                dict_reactivo["fecha_caducidad"] = fecha_caducidad
                break
            except ValueError:
                print("Fecha inválido. Por favor, ingresa una fecha válido.")
        while True:
            try:
                costo = float(input("Costo: ")) #Verifica costo válido
                if costo > 0:
                    dict_reactivo["costo"] = costo
                    break
                else:
                    print("Costo inválido. Por favor, ingresa un costo mayor a cero.")
            except ValueError:
                print("Costo inválido. Por favor, ingresa un costo válido.")

        while True:
            try:
                inventario = float(input("Inventario disponible: ")) #Verifica inventario válido
                if inventario > 0:
                    dict_reactivo["inventario_disponible"] = inventario
                    break
                else:
                    print("Inventario inválido. Por favor, ingresa un valor mayor a cero.")
            except ValueError:
                print("Inventario inválido. Por favor, ingresa un valor válido.")

        agregar = input("Ingresa la cantidad de conversiones posibles que deseas agregar: ")
        while not(agregar != "0" and agregar.isnumeric()): 
            print("Cantidad inválida. Por favor, ingresa un número válido.")
            agregar = input("Ingresa la cantidad de conversiones posibles que deseas agregar: ")
        for i in range(int(agregar)): #Itera la cantidad de conversiones posibles
            conversion = {
                "unidad": input("Unidad: "),
                "factor": 0
            }
            while True:
                try:
                    factor = float(input("Factor: ")) #Verifica factor válido
                    if factor > 0:
                        conversion['factor'] = factor
                        break
                    else: 
                        print("Factor inválido. Por favor, ingresa un valor mayor a cero.")
                except ValueError:
                    print("Factor inválido. Por favor, ingresa un valor válido.")

            dict_reactivo["conversiones_posibles"].append(conversion)
        
        reactivos.append(dict_reactivo) #Agrega el reactivo a la lista
        print("\n->Reactivo creado exitosamente.<-")

    def modificar_reactivo(self, reactivos):
        print("\n","~"*35)
        print("\nModoficando reactivo:")
        id_reactivo = input("Ingrese el ID del reactivo que desea modificar:")
        found = False #Creo una variable para evitar un bucle de else y verificar si el reactivo existe
        for reactivo in reactivos: #Itera la lista de reactivos
            if str(reactivo['id']) == id_reactivo: #Y luego verifica si el reactivo existe
                found = True
                reactivo['nombre'] = input("Nombre: ")
                reactivo['descripcion'] = input("Descripción: ") 
                while True:
                    try:
                        costo = float(input("Costo: "))
                        if costo > 0:
                            reactivo["costo"] = costo
                            break
                        else:
                            print("Costo inválido. Por favor, ingresa un costo mayor a cero.")
                    except ValueError:
                        print("Costo inválido. Por favor, ingresa un costo válido.")
                reactivo['categoria'] = input("Categoría: ")
                while True:
                    try:
                        inventario = float(input("Inventario disponible: "))
                        if inventario > 0:
                            reactivo["inventario_disponible"] = inventario
                            break
                        else:
                            print("Inventario inválido. Por favor, ingresa un valor mayor a cero.")
                    except ValueError:
                        print("Inventario inválido. Por favor, ingresa un valor válido.")
                reactivo['unidad_medida'] = input("Unidad de medida: ")
                while True:
                    fecha = input("Fecha de caducidad (formato AAAA-MM-DD):")
                    try:
                        fecha_caducidad = datetime.strptime(fecha, "%Y-%m-%d") #Verifica formato válido
                        reactivo["fecha_caducidad"] = fecha_caducidad
                        break
                    except ValueError:
                        print("Fecha inválido. Por favor, ingresa una fecha válido.")        
                while True:
                    try:
                        minimo = int(input("Inventario disponible: "))
                        if minimo > 0:
                            reactivo['minimo_sugerido'] = minimo
                            break
                        else:
                            print("Minimo sugerido inválido. Por favor, ingresa un valor mayor a cero.")
                    except ValueError:
                        print("Minimo sugerido inválido. Por favor, ingresa un valor válido.")
                reactivo["conversiones_posibles"] = []
                agregar = input("Ingresa la cantidad de conversiones posibles que deseas agregar: ")
                while not(agregar != "0" and agregar.isnumeric()):
                    print("Cantidad inválida. Por favor, ingresa un número válido.")
                    agregar = input("Ingresa la cantidad de conversiones posibles que deseas agregar: ")

                for i in range(int(agregar)):
                    conversion = {
                        "unidad": input("Unidad: "),
                        "factor": 0
                    }
                    while True:
                        try:
                            factor = float(input("Factor: "))
                            if factor > 0:
                                conversion['factor'] = factor
                                break
                            else: 
                                print("Factor inválido. Por favor, ingresa un valor mayor a cero.")
                        except ValueError:
                            print("Factor inválido. Por favor, ingresa un valor válido.")

                    reactivo["conversiones_posibles"].append(conversion)
        if not found: #---> False:Si no se encuentra el reactivo se imprime un mensaje
            print("Reactivo no encontrado.")

    def eliminar_reactivo(self, reactivos):
        print("\n","~"*35)
        print("\nEliminando reactivo:")
        id_reactivo = input("Ingrese el ID del reactivo que desea eliminar:")
        found = False
        for reactivo in reactivos:
            if str(reactivo['id']) == id_reactivo:
                found = True
                reactivos.remove(reactivo)
                print("\n->Reactivo eliminado exitosamente.<-")
        if not found:
            print("Reactivo no encontrado.")

    def conversion_unidades(self, reactivos):
        print("\n","~"*35)
        print("\nConvirtiendo unidades:")
        #Solicita al usuario el ID del reactivo que desea convertir
        id_reactivo = input("Ingrese el ID del reactivo que desea convertir:")
        found = False
        #Itera la lista de reactivos y luego verifica si el id del raectivo coincide
        for reactivo in reactivos:
            if str(reactivo['id']) == id_reactivo:
                found = True
                unidad_encontrada = False #Variable para verificar si la unidad de medida es valida
                unidad = input("Unidad de medida a la que desea convertir: ")
                for conversion in reactivo['conversiones_posibles']:
                    if conversion['unidad'] == unidad:
                        unidad_encontrada = True
                        factor = conversion['factor']
                        while True:
                            try:
                                cantidad = float(input("Cantidad a convertir: "))
                                if cantidad > 0:
                                    break
                                else:
                                    print("Cantidad inválida. Por favor, ingrese un valor mayor a cero.")
                            except ValueError:
                                print("Cantidad inválida. Por favor, ingrese un valor numérico.")
                        print(f"{cantidad} {reactivo['unidad_medida']} equivale a {cantidad * factor} {unidad}.")
                        return
                if not unidad_encontrada:
                    print('Unidad de medida no encontrada.')
                    return
        if not found:
            print("Reactivo no encontrado.") 
    
    def verificar_minimo_sugerido(self, reactivos):
        for reactivo in reactivos:
            if reactivo['inventario_disponible'] <= reactivo['minimo_sugerido']:
                print("\n","-"*35)
                print(f"""El reactivo {reactivo['id']} ({reactivo['nombre']}) 
                      ha llegado al minimo sugerido {reactivo['minimo_sugerido']}. 
                      Es necesario reponerlo""")