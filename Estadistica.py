from collections import Counter
from datetime import datetime
from matplotlib import pyplot as plt

class Estadistica:
    def __init__(self):
        self.investigador = []
        self.mas_menos = []
        self.rotacion = []
        self.desperdicio = []
        self.vencidos = []

    def calculando_estatdistica(self, experimentos, recetas, reactivos, falta, desperdicio):
        #Extraer de todas las persona responsables
        investigadores = []
        for experimento in experimentos:
            for persona in experimento['personas_responsables']:
                investigadores.append(persona)
        
        #Contar cuantos investigadores hay
        c = Counter(investigadores)

        self.investigador = c

        nombre_experimento = []
        for experimento in experimentos:
            nombre_experimento.append(experimento['receta_id'])
        
        c = Counter()
        for i in nombre_experimento:
            c[int(i)] += 1

        receta_mas_usada = None
        frecuencia_mas = 0
        for receta, frecuencia in c.items():
            if frecuencia > frecuencia_mas:
                receta_mas_usada = receta
                frecuencia_mas = frecuencia

        receta_menos_usada = None
        frecuencia_menos = frecuencia_mas
        for receta, frecuencia in c.items():
            if frecuencia < frecuencia_mas:
                receta_menos_usada = receta
                frecuencia_mas = frecuencia

        receta_mas_nombre = None
        receta_menos_nombre = None
        for receta in recetas:
            if receta['id'] == receta_mas_usada:
                receta_mas_nombre = receta['nombre']
            if receta['id'] == receta_menos_usada:
                receta_menos_nombre = receta['nombre']
        
        dict_result = {receta_mas_nombre: frecuencia_mas, receta_menos_nombre: frecuencia_menos}
        self.mas_menos = dict_result

        c = Counter()
        for experimento in experimentos:
            for receta in recetas:
                if experimento['receta_id'] == receta['id']:
                    for reactivo in receta['reactivos_utilizados']:
                        reactivo_id = int(reactivo['reactivo_id'])
                        cantidad_necesaria = reactivo['cantidad_necesaria']
                        c[reactivo_id] += cantidad_necesaria
        
        reactivo_mas_rotacion = c.most_common(5)
        self.rotacion = reactivo_mas_rotacion
    
        fecha_vencimiento = datetime.now().date()
        c_vencido = Counter()

        for reactivo in reactivos:
            fecha_caducidad = datetime.strptime(reactivo['fecha_caducidad'], "%Y-%m-%d").date()
            if fecha_caducidad < fecha_vencimiento:
                c_vencido[int(reactivo['id'])] += 1

        reactivo_vencido = c_vencido.most_common(5)

        self.vencidos = reactivo_vencido

        self.grafica(falta, desperdicio)


#Aqui se grafican los datos obtenidos en la funcion calculando_estadistica 
    def grafica(self, falta_reactivos, desperdicio):
        plt.figure(figsize=(8, 6))
        plt.bar(self.investigador.keys(), self.investigador.values(), color='blue')
        plt.title('Investigadores que más usan el laboratorio')
        plt.xlabel('Investigadores')
        plt.ylabel('Frecuencia')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        plt.figure(figsize=(8, 6))
        count = 0
        recetas = list(self.mas_menos.keys())
        frecuencias = list(self.mas_menos.values())
        colores = ['green', 'red']
        plt.bar(recetas, frecuencias, color=colores)
        plt.title('Experimento mas y menos hecho')
        plt.xlabel('Recetas')
        plt.ylabel('Frecuencia')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        plt.figure(figsize=(8, 6))
        for reactivo, cantidad in self.rotacion:
            plt.bar(reactivo, cantidad, color='red')
        plt.title('Reactivos con más rotación')
        plt.xlabel('Reactivos')
        plt.ylabel('Cantidad')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        plt.figure(figsize=(8, 6))
        for id, cantidad in desperdicio:
            plt.bar(id, cantidad, color="purple")
        plt.title("Reactivo con más desperdicio")
        plt.xlabel("Reactivos")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        plt.figure(figsize=(8, 6))
        for reactivo, cantidad in self.vencidos:
            plt.bar(reactivo, cantidad, color="orange")
        plt.title("Reactivo que más se vencen")
        plt.xlabel("Reactivos")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
            
        plt.figure(figsize=(6, 6))
        plt.bar("Resultado", falta_reactivos, color="black")
        plt.title("Cantidad de veces que no se logro hacer un experimento por falta de reactivos")
        plt.xlabel("Resultado")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()