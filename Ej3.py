import sys
from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QPixmap
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

dataset = pd.read_csv('cultivos.csv')
dataset.head()
dataset.info()
dataset.describe()
dataset = pd.get_dummies(dataset, columns=['cultivo','municipio','PERIODO'] )
print(dataset.shape)
dataset.hist(bins = 40)
sns.set(style='whitegrid', context='notebook')
cols = ['area sembrada','area cosechada','produccion', 'rendimiento']
sns.pairplot(dataset[cols], height=2.5)
plt.show()

Formulario, Ventana = uic.loadUiType("Ej2.ui")


class Aplicacion(QtWidgets.QMainWindow, Formulario):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Formulario.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.imagen)

    def imagen(self):
        plt.plot([1, 2, 3], [20, 10, 30])
        plt.savefig('Grafica.png')
        pixmap = QPixmap('Grafica.png')
        self.label.setPixmap(pixmap)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Vent = Aplicacion()
    Vent.show()
    app.exec()