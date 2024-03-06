import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget
import matplotlib.pyplot as plt

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lista_numeros = []
        self.setWindowTitle("Búsqueda de Elementos")
        self.setGeometry(100, 100, 400, 200)  # Tamaño y posición de la ventana

        # Widget para el gráfico
        self.widget_grafico = QWidget(self)
        self.setCentralWidget(self.widget_grafico)
        
        # Widgets
        self.label_instrucciones1 = QLabel("Ingrese una lista de números separados por comas:", self)
        self.label_instrucciones1.setGeometry(20, 360, 400, 20)
        self.label_instrucciones1.move(20, 20)

        self.input_lista = QLineEdit(self)
        self.input_lista.setGeometry(20, 50, 360, 30)

        self.label_instrucciones2 = QLabel("Ingrese el número a buscar:", self)
        self.label_instrucciones2.setGeometry(20, 360, 400, 20)
        self.label_instrucciones2.move(20, 90)

        self.input_buscar = QLineEdit(self)
        self.input_buscar.setGeometry(20, 120, 200, 30)

        self.boton_buscar = QPushButton("Buscar", self)
        self.boton_buscar.setGeometry(240, 120, 140, 30)
        self.boton_buscar.clicked.connect(self.realizar_busqueda)

        self.boton_buscar_binaria = QPushButton("Buscar (Binaria)", self)
        self.boton_buscar_binaria.setGeometry(240, 150, 140, 30)
        self.boton_buscar_binaria.clicked.connect(self.realizar_busqueda_binaria)


        # Botón para mostrar el gráfico
        self.boton_mostrar = QPushButton("Mostrar Gráfico", self)
        self.boton_mostrar.setGeometry(240, 90, 140, 30)
        self.boton_mostrar.clicked.connect(self.mostrar_grafico)

    def busqueda_lineal(self, elemento):
        for i in range(len(self.lista_numeros)):
            if self.lista_numeros[i] == elemento:
                return i 
        return -1

    def busqueda_binaria(self, elemento):
        inicio = 0
        fin = len(self.lista_numeros) - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self.lista_numeros[medio] == elemento:
                return medio
            elif self.lista_numeros[medio] < elemento:
                inicio = medio + 1
            else:
                fin = medio - 1
        return -1
    
    def realizar_busqueda(self):
        
        self.lista_numeros = self.input_lista.text().split(",")
        elemento_buscar = self.input_buscar.text()

        # Validar la self.lista_numeros
        if not self.lista_numeros:
            self.mostrar_alerta("Error", "La lista de numeros está vacía. Ingrese al menos un número.")
            return

        # Validar que sean números
        if not all(num.isdigit() for num in self.lista_numeros):
            self.mostrar_alerta("Error", "La lista de numeros debe contener solo números enteros separados por comas.")
            return

        # Realizar búsqueda lineal
        resultado_lineal = self.busqueda_lineal(elemento_buscar)
        if resultado_lineal != -1:
            self.mostrar_alerta("Resultado", f"El elemento {elemento_buscar} se encuentra en la posición {resultado_lineal}.")
        else:
            self.mostrar_alerta("Resultado", f"El elemento {elemento_buscar} no se encuentra en la lista de números.")

    def realizar_busqueda_binaria(self):
        
        self.lista_numeros = self.input_lista.text().split(",")
        elemento_buscar = self.input_buscar.text()
        
        # Validar la self.lista_numeros
        if not self.lista_numeros:
            self.mostrar_alerta("Error", "La lista de numeros está vacía. Ingrese al menos un número.")
            return
        
        # Realizar búsqueda binaria (requiere una lista de numeros ordenada)
        lista_ordenada = sorted(self.lista_numeros)
        resultado_binaria = self.busqueda_binaria(elemento_buscar)
        
        if resultado_binaria != -1:
            self.mostrar_alerta("Resultado", f"El elemento {elemento_buscar} se encuentra en la posición {resultado_binaria} (búsqueda binaria).")
        else:
            self.mostrar_alerta("Resultado", f"El elemento {elemento_buscar} no se encuentra en la lista de números (búsqueda binaria).")

    def mostrar_alerta(self, titulo, mensaje):
        alerta = QMessageBox(self)
        alerta.setWindowTitle(titulo)
        alerta.setText(mensaje)
        alerta.exec_()

    def mostrar_grafico(self):
        self.lista_numeros = [int(num) for num in self.input_lista.text().split(",")]

        if not self.lista_numeros:
            self.mostrar_alerta("Error", "La lista de numeros está vacía. Ingrese al menos un número.")
            return

        # Crear el gráfico de líneas
        plt.plot(self.lista_numeros)
        plt.xlabel("Índice")
        plt.ylabel("Valor")
        plt.title("Gráfico de Líneas")
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())

