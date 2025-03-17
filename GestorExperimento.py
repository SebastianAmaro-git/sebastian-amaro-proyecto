from Experimentos import Experimentos
from Recetas import Recetas
from datetime import datetime
from random import random

class GestorExperimento:
    def mostrar_experimentos(self, experimentos):
        print("\n","~"*35)
        print("\nMostrando Experimentos:")
        for experimento in experimentos:
            atr = Experimentos(experimento['id'],
                               experimento['receta_id'],
                               experimento['personas_responsables'],
                               experimento['fecha'],
                               experimento['costo_asociado'],
                               experimento['resultado'])
            atr.mostrar_atr()
    
    def mostrar_receta(self, recetas):
        print("\n","~"*35)
        print("\nMostrando Receta:")
        for receta in recetas:
            atr = Recetas(receta['id'],
                          receta['nombre'],
                          receta['objetivo'],
                          receta['reactivos_utilizados'],
                          receta['procedimiento'],
                          receta['valores_a_medir'])
            atr.mostrar_atr()
    
    def crear_experimento(self, experimentos, recetas, reactivos,desperdicio):
        print("\n","~"*35)
        print("\nCreando Experimento:")
        while True:
            try:
                receta_id = int(input("Ingrese el ID de la receta: "))
                receta_seleccionada = None
                for receta in recetas:
                    if receta['id'] == receta_id:
                        receta_seleccionada = receta
                        break
                if receta_seleccionada:
                    break
                else:
                    print("Receta no encontrada. Por favor, ingrese un ID válido.")
                    continue
            except ValueError:
                print("ID inválido. Por favor, ingresa un número válido.")
        validacion, reactivos_a, falta = self.validar_reactivos(receta_seleccionada['reactivos_utilizados'], reactivos)
        if validacion:
            dict_experimento = {
                "id": len(experimentos) + 1,
                "receta_id": receta_id,
                "personas_responsables": [],
                "fecha": "",
                "costo_asociado": 0,
                "resultado": ''
            }
            agregar = input("Ingresa la cantidad de personas responsables que deseas agregar: ")
            while not(int(agregar) > 0 and agregar.isnumeric()):
                    print("Cantidad inválida. Por favor, ingresa un número válido.")
                    agregar = input("Ingresa la cantidad de personas responsables que deseas agregar: ")
            for i in range(int(agregar)):
                nombre = input("Ingrese el nombre de la persona responsable: ")
                dict_experimento['personas_responsables'].append(nombre)
            while True:
                fecha = input("Fecha del experimento (formato AAAA-MM-DD):")
                try:
                    fecha = datetime.strptime(fecha, "%Y-%m-%d") #Verifica formato válido
                    dict_experimento['fecha'] = fecha
                    break
                except ValueError:
                    print("Fecha inválido. Por favor, ingresa una fecha válido.")

            dict_experimento['costo_asociado'] = self.costo_calcular(reactivos_a, receta_seleccionada['reactivos_utilizados'])

            dict_experimento['resultado'] = self.resultado(receta_seleccionada['valores_a_medir'])

            for reactivo in reactivos_a:
                for r in receta_seleccionada['reactivos_utilizados']:
                    if reactivo['id'] == r['reactivo_id']:
                        descuento, error_aplicado = self.error_inventario(r['id'],r['cantidad_necesaria'], desperdicio)
                        reactivo['inventario_disponible'] -= descuento
                        print(f"!--->El reactivo {reactivo['id']} ha sido modificado con un descuento de {error_aplicado}%")
        else:
            falta_reactivo += falta
            return print("\nNo se puede realizar el experimento, es posible que falten reactivos.")
            
        experimentos.append(dict_experimento)
        return f"Experimento {dict_experimento['id']} creado con éxito."
    
    def modificar_experimento(self, experimentos, recetas, reactivos, falta_reactivo, desperdicio):
        print("\n","~"*35)
        print("\nModificando Experimento:")
        while True:
            try:
                experimento_id = int(input("Ingrese el ID del experimento a modificar: "))
                for experimento in experimentos:
                    if experimento['id'] == experimento_id:
                        experimento_encontrado = experimento
                        break
                if experimento_encontrado:
                    break
                else:
                    print("Experimento no encontrado. Por favor, ingrese un ID válido.")
                    continue
            except ValueError:
                print("ID inválido. Por favor, ingresa un número válido.")
            
        while True:
            try:
                receta_id = int(input("Ingrese el ID de la receta: "))
                receta_seleccionada = None
                for receta in recetas:
                    if receta['id'] == receta_id:
                        receta_seleccionada = receta
                        break
                if receta_seleccionada:
                    break
                else:
                    print("Receta no encontrada. Por favor, ingrese un ID válido.")
                    continue
            except ValueError:
                print("ID inválido. Por favor, ingresa un número válido.")

        validacion, reactivos_a, falta = self.validar_reactivos(receta_seleccionada['reactivos_utilizados'], reactivos)
        if validacion:
            experimento_encontrado['receta_id'] = receta_id
            agregar = input("Ingresa la cantidad de personas responsables que deseas agregar: ")
            while not(int(agregar) > 0 and agregar.isnumeric()):
                    print("Cantidad inválida. Por favor, ingresa un número válido.")
                    agregar = input("Ingresa la cantidad de personas responsables que deseas agregar: ")
            for i in range(int(agregar)):
                personas = []
                nombre = input("Ingrese el nombre de la persona responsable: ")
                personas.append(nombre)
            experimento_encontrado['personas_responsables'] = personas
            while True:
                fecha = input("Fecha del experimento (formato AAAA-MM-DD):")
                try:
                    fecha = datetime.strptime(fecha, "%Y-%m-%d") #Verifica formato válido
                    experimento_encontrado['fecha'] = fecha
                    break
                except ValueError:
                    print("Fecha inválido. Por favor, ingresa una fecha válido.")

            experimento_encontrado['costo_asociado'] = self.costo_calcular(reactivos_a, receta_seleccionada['reactivos_utilizados'])

            experimento_encontrado['resultado'] = self.resultado(receta_seleccionada['valores_a_medir'])

            for reactivo in reactivos_a:
                for r in receta_seleccionada['reactivos_utilizados']:
                    if reactivo['id'] == r['reactivo_id']:
                        descuento, error_aplicado = self.error_inventario(r['id'],r['cantidad_necesaria'], desperdicio)
                        reactivo['inventario_disponible'] -= descuento
                        print(f"!--->El reactivo {reactivo['id']} ha sido modificado con un descuento de {error_aplicado}%")
        else:
            falta_reactivo += falta
            return print("\nNo se puede realizar el experimento, es posible que falten reactivos.")
            
        return f"Experimento {experimento_encontrado['id']} modificado con éxito."
    
    def eliminar_experimento(self, experimentos):
        print("\n","~"*35)
        print("\nEliminando Experimento:")
        id_experimento = input("Ingrese el ID del reactivo que desea eliminar:")
        found = False
        for experimento in experimentos:
            if str(experimento['id']) == id_experimento:
                found = True
                experimentos.remove(experimento)
                print("\n->Experimento eliminado exitosamente.<-")
        if not found:
            print("Experimento no encontrado.")

    def validar_reactivos(self, reactivos_utilizados, reactivos):
        hoy = datetime.now().date()
        reactivos_a = [] #Guarda los reactivos validos
        falta_reactivo = 0
        for r in reactivos_utilizados:
            encontrado = None

            for reactivo in reactivos:
                if reactivo['id'] == r['reactivo_id']:
                    encontrado = reactivo
                    break
            # Verificar si el reactivo no existe, está agotado o caducado
            if not encontrado:
                return False
            if encontrado['inventario_disponible'] < r['cantidad_necesaria']:
                return False, reactivos_a, 1
            if datetime.strptime(encontrado['fecha_caducidad'], '%Y-%m-%d').date() < hoy:
                return False

            reactivos_a.append(encontrado)
        
        return True , reactivos_a, falta_reactivo
    
    def costo_calcular(self, reactivos_a, reactivos_utilizados):
        costo_total = 0
        for reactivo in reactivos_a:
            for r in reactivos_utilizados:
                if reactivo['id'] == r['reactivo_id']:
                    costo_total += reactivo['costo'] * r['cantidad_necesaria']

        return costo_total
     
    def resultado(self, valores_a_medir):
        r = ''
        for i in valores_a_medir:
            while True:
                try:
                    resultado = int(input("Ingrese el resultado del experimento: "))
                    if resultado > 0:
                        break
                    else:
                        print("Resultado inválido. Por favor, ingresa un número mayor a cero.")
                except ValueError:
                    print("Resultado inválido. Por favor, ingresa un número válido.")
            
            minimo = i['minimo']
            maximo = i['maximo']
            nombre = i['nombre']
            r += f'{nombre}: {resultado}.'

        if resultado < minimo or resultado > maximo:
            r += ' El experimento esta dentro de los parametros establecidos.'
        else:
            r += ' El experimento no esta dentro de los parametros establecidos.'

        return r
    
    def error_inventario(self,id,cantidad_necesaria, desperdicio):
        error_porcentaje = random.uniform(0.1, 22.5)/100
        descuento = cantidad_necesaria * error_porcentaje
        error_apliacado = error_porcentaje * 100
        
        for i in desperdicio:
            if i['id'] == id:
                i['cantidad'] += descuento
            else:
                desperdicio.append({'id': id, 'cantidad': descuento})
        

        return descuento, error_apliacado                 