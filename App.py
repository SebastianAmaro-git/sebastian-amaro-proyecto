from GestorReactivo import GestorReactivo
from GestorExperimento import GestorExperimento
from Estadistica import Estadistica
import requests

class App:
    def __init__(self):
        self.reactivos = []
        self.recetas = []
        self.experimentos = []
        self.falta_reactivos = 0
        self.desperdicio = []
    
    def inicio(self):
        self.cargar_api()
    
    def menu(self):
        while True:
           print("\n","-"*35)
           print()
           print("       -----------------------")
           print("            MENU PRINCIPAL     ")
           print("       -----------------------")
           print(" - Bienvenido al laboratorio de química - \n")
           print("1. Gestionar Reactivos")
           print("2. Gestionar Experimentos")
           print("3. Estadisticas")
           print("4. Salir")
           opcion = input("Seleccione una opción: ")
           if opcion == "1":
               self.menu_reactivos()
           elif opcion == "2":
               self.menu_experimentos()
           elif opcion == "3":
               Estadistica().calculando_estatdistica(self.experimentos, self.recetas, self.reactivos, self.falta_reactivos, self.desperdicio)
           elif opcion == "4":
               print("¡Hasta luego!")
               break
           else:
               print("Opción no válida. Por favor, seleccione una opción válida.")
               continue
    
    def menu_reactivos(self):
        while True:
            GestorReactivo().verificar_minimo_sugerido(self.reactivos)
            print("\n","-"*35)
            print("       -----------------------")
            print("            MENU REACTIVOS     ")
            print("       -----------------------\n")
            print("1. Mostrar Reactivos")
            print("2. Crear Reactivo")
            print("3. Modificar Reactivo")
            print("4. Eliminar Reactivo")
            print("5. Conversion de Unidades")
            print("6. Regresar al Menu Principal")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
               GestorReactivo().mostrar_reactivos(self.reactivos)
            elif opcion == "2":
               GestorReactivo().crear_reactivo(self.reactivos)
            elif opcion == "3":
               GestorReactivo().modificar_reactivo(self.reactivos)
            elif opcion == "4":
               GestorReactivo().eliminar_reactivo(self.reactivos)
            elif opcion == "5":
               GestorReactivo().conversion_unidades(self.reactivos)
            elif opcion == "6":
               self.menu()
               
            else:
               print("Opción no válida. Por favor, seleccione una opción válida.")
               continue
    
    def menu_experimentos(self):
        while True:
            print("\n","-"*35)
            print("       -----------------------")
            print("          MENU EXPERIMENTOS  ")
            print("       -----------------------\n")
            print("1. Mostrar Experimentos")
            print("2. Mostrar Recetas")
            print("3. Crear Experimentos")
            print("4. Modificar Experimentos")
            print("5. Eliminar Experimentos")
            print("6. Regresar al Menu Principal")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                GestorExperimento().mostrar_experimentos(self.experimentos)
            elif opcion == "2":
               GestorExperimento().mostrar_receta(self.recetas)
            elif opcion == "3":
               GestorExperimento().crear_experimento(self.experimentos, self.recetas, self.reactivos, self.desperdicio)
            elif opcion == "4":
               GestorExperimento().modificar_experimento(self.experimentos, self.recetas, self.reactivos, self.desperdicio)
            elif opcion == "5":
               GestorExperimento().eliminar_experimento(self.experimentos)
            elif opcion == "6":
               self.menu()
               
            else:
               print("Opción no válida. Por favor, seleccione una opción válida.")
               continue
    
    def cargar_api(self):
        base_url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main"
        response = requests.get(f"{base_url}/reactivos.json")
        if response.status_code == 200:
            reactivos = response.json()
            self.reactivos = reactivos
        else:
            print("Error al obtener los reactivos.")
        response = requests.get(f"{base_url}/recetas.json")
        if response.status_code == 200:
            recetas = response.json()
            self.recetas = recetas
        else:
            print("Error al obtener las recetas.")
        response = requests.get(f"{base_url}/experimentos.json")
        if response.status_code == 200:
            experimentos = response.json()
            self.experimentos = experimentos
        else:
            print("Error al obtener los experimentos.")

        self.menu()