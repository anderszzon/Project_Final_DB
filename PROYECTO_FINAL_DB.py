import pandas as pd
import matplotlib.pyplot as plt
import sys
from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QPushButton
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sqlalchemy import create_engine
from sklearn import preprocessing
from pymongo import MongoClient
import pymysql
import sqlalchemy.exc
from sqlalchemy.exc import DatabaseError, DisconnectionError
from sqlalchemy import exc

#conn = create_engine('mysql+pymysql://root:@localhost:3306/proyecto_final')

# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = ''
host = 'localhost'
port = 3306
database = 'proyecto_final'

def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )

def get_connection_mongo():
    cliente = MongoClient('localhost', 27017)  # localhost predeterminado, 27017
    collection = cliente["ProyectoFinal"]["cultivos"]
    data = collection.find()
    # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
    data = list(data)
    #df = pd.DataFrame(data)  # leer la tabla completa (DataFrame)
    #print(df)
    return data


Formulario, Ventana = uic.loadUiType("Ej4.ui")
class Aplicacion(QtWidgets.QMainWindow, Formulario):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Formulario.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Mostrar_TablaCultivos)
        #self.pushButton_2.clicked.connect(self.Mostrar_Histograma)
        #self.pushButton_3.clicked.connect(self.ModeloSupervisado)
        #self.pushButton_4.clicked.connect(self.ModeloNoSupervisado)
###############################################################################
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(["Area Sembrada", "Area Cosechada", "Produccion", "Rendimiento", "Cultivo", "Municipio", "Periodo"])
        self.comboBox.move(50, 460)
        self.comboBox.iconSize()
        self.plainTextEdit.move(350, 460)

        button = QPushButton("Cargar Atributo", self)
        button.clicked.connect(self.display)
        button.move(200, 460)
#################################################################################
        self.comboBox1 = QComboBox(self)
        self.comboBox1.addItems(["Area Sembrada", "Area Cosechada", "Produccion", "Rendimiento", "Cultivo", "Municipio", "Periodo"])
        self.comboBox1.move(50, 535)
        self.comboBox1.iconSize()
        self.plainTextEdit_2.move(350, 535)

        #self.pushButton_2("Cargar Atributo", self)
        self.pushButton_2.clicked.connect(self.display1)
        self.pushButton_2.move(200, 535)
##################################################################################
        self.comboBox2 = QComboBox(self)
        self.comboBox2.addItems(["Area Sembrada", "Area Cosechada", "Produccion", "Rendimiento", "Cultivo", "Municipio", "Periodo"])
        self.comboBox2.move(50, 595)
        self.comboBox2.iconSize()
        self.comboBox3 = QComboBox(self)
        self.comboBox3.addItems(["Area Sembrada", "Area Cosechada", "Produccion", "Rendimiento", "Cultivo", "Municipio", "Periodo"])
        self.comboBox3.move(50, 633)
        self.comboBox3.iconSize()
        #self.plainTextEdit_3.move(350, 595)
        #self.plainTextEdit_4.move(350, 633)

        #self.pushButton_2("Cargar Atributo", self)
        self.pushButton_5.clicked.connect(self.display2)
        self.pushButton_5.move(200, 595)
####################################################################################

    def Mostrar_TablaCultivos(self):
        """df = pd.read_sql("SELECT * FROM cultivos", conn)
        print(df)
        tabla_html = df.to_html()  # Crear versión HTML del df
        self.textBrowser.setHtml(tabla_html)
        """""
        #print(e)
        if not e:
        #if e:
            df = pd.read_sql("SELECT * FROM cultivos", conn)
            print(df)
            tabla_html = df.to_html() #Crear versión HTML del df
            self.textBrowser.setHtml(tabla_html)
        else:
            tabla_html = df_mongo.to_html() #Crear versión HTML del df
            self.textBrowser.setHtml(tabla_html)


####################################################################################

    def display(self):
        self.plainTextEdit.clear()  # Borrar plainText
        print(self.comboBox.currentText(), f"({self.comboBox.currentIndex()})")
        if not e:
            if (self.comboBox.currentIndex() == 0):
                self.plainTextEdit.insertPlainText("Area Sembrada")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.read_sql_query("SELECT area sembrada FROM cultivos",conn)
                # Crear un histograma de la columna rendimiento
                df['area sembrada'].hist()
                # Agregar etiquetas al gráfico
                plt.title('Histograma de Area Sembrada')
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                # Mostrar el gráfico
                plt.show()
            elif(self.comboBox.currentIndex() == 1):
                self.plainTextEdit.insertPlainText("Area Cosechada")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.read_sql_query("SELECT area sembrada FROM cultivos",conn)
                # Crear un histograma de la columna rendimiento
                df['area cosechada'].hist()
                # Agregar etiquetas al gráfico
                plt.title('Histograma de Area Cosechada')
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                # Mostrar el gráfico
                plt.show()
            elif (self.comboBox.currentIndex() == 2):
                self.plainTextEdit.insertPlainText("Produccion")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.read_sql_query("SELECT area sembrada FROM cultivos",conn)
                # Crear un histograma de la columna rendimiento
                df['produccion'].hist()
                # Agregar etiquetas al gráfico
                plt.title('Histograma de Produccion')
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                # Mostrar el gráfico
                plt.show()
            if (self.comboBox.currentIndex() == 3):
                self.plainTextEdit.insertPlainText("Rendimiento")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.read_sql_query("SELECT area sembrada FROM cultivos",conn)
                # Crear un histograma de la columna rendimiento
                df['rendimiento'].hist()
                # Agregar etiquetas al gráfico
                plt.title('Histograma de Rendimiento')
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                # Mostrar el gráfico
                plt.show()
            elif(self.comboBox.currentIndex() == 4):
                self.plainTextEdit.insertPlainText("Cultivo")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.read_sql_query("SELECT area sembrada FROM cultivos",conn)
                # Crear un histograma de la columna rendimiento
                df['cultivo'].hist()
                # Agregar etiquetas al gráfico
                plt.title('Histograma de Cultivo')
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                # Mostrar el gráfico
                plt.show()
            elif (self.comboBox.currentIndex() == 5):
                self.plainTextEdit.insertPlainText("Municipio")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.read_sql_query("SELECT area sembrada FROM cultivos",conn)
                # Crear un histograma de la columna rendimiento
                df['municipio'].hist()
                # Agregar etiquetas al gráfico
                plt.title('Histograma de Municipio')
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                # Mostrar el gráfico
                plt.show()
            elif (self.comboBox.currentIndex() == 6):
                self.plainTextEdit.insertPlainText("Periodo")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.read_sql_query("SELECT area sembrada FROM cultivos",conn)
                # Crear un histograma de la columna rendimiento
                df['PERIODO'].hist()
                # Agregar etiquetas al gráfico
                plt.title('Histograma de Periodo')
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                # Mostrar el gráfico
                plt.show()
            else:
                self.plainTextEdit.insertPlainText("")
        else:
            if (self.comboBox.currentIndex() == 0):
                cliente = MongoClient('localhost', 27017)  # localhost predeterminado, 27017
                collection = cliente["ProyectoFinal"]["cultivos"]
                data = collection.find({})
                # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
                data = list(data)
                df_mongo = pd.DataFrame(data)  # leer la tabla completa (DataFrame)
                self.plainTextEdit.insertPlainText("Area Sembrada")
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.read_sql_query("SELECT area sembrada FROM cultivos",conn)
                # Crear un histograma de la columna rendimiento
                df_mongo['area sembrada'].hist()
                # Agregar etiquetas al gráfico
                plt.title('Histograma de Area Sembrada')
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                # Mostrar el gráfico
                plt.show()
            elif(self.comboBox.currentIndex() == 1):
                cliente = MongoClient('localhost', 27017)  # localhost predeterminado, 27017
                collection = cliente["ProyectoFinal"]["cultivos"]
                data = collection.find({})
                # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
                data = list(data)
                df_mongo = pd.DataFrame(data)  # leer la tabla completa (DataFrame)
                self.plainTextEdit.insertPlainText("Area Cosechada")
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.read_sql_query("SELECT area sembrada FROM cultivos",conn)
                # Crear un histograma de la columna rendimiento
                df_mongo['area cosechada'].hist()
                # Agregar etiquetas al gráfico
                plt.title('Histograma de Area Cosechada')
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                # Mostrar el gráfico
                plt.show()
            elif (self.comboBox.currentIndex() == 2):
                cliente = MongoClient('localhost', 27017)  # localhost predeterminado, 27017
                collection = cliente["ProyectoFinal"]["cultivos"]
                data = collection.find({})
                # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
                data = list(data)
                df_mongo = pd.DataFrame(data)  # leer la tabla completa (DataFrame)
                self.plainTextEdit.insertPlainText("Produccion")
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.read_sql_query("SELECT area sembrada FROM cultivos",conn)
                # Crear un histograma de la columna rendimiento
                df_mongo['produccion'].hist()
                # Agregar etiquetas al gráfico
                plt.title('Histograma de Produccion')
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                # Mostrar el gráfico
                plt.show()
            if (self.comboBox.currentIndex() == 3):
                cliente = MongoClient('localhost', 27017)  # localhost predeterminado, 27017
                collection = cliente["ProyectoFinal"]["cultivos"]
                data = collection.find({})
                # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
                data = list(data)
                df_mongo = pd.DataFrame(data)  # leer la tabla completa (DataFrame)
                self.plainTextEdit.insertPlainText("Rendimiento")
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.read_sql_query("SELECT area sembrada FROM cultivos",conn)
                # Crear un histograma de la columna rendimiento
                df_mongo['rendimiento'].hist()
                # Agregar etiquetas al gráfico
                plt.title('Histograma de Rendimiento')
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                # Mostrar el gráfico
                plt.show()
            elif(self.comboBox.currentIndex() == 4):
                cliente = MongoClient('localhost', 27017)  # localhost predeterminado, 27017
                collection = cliente["ProyectoFinal"]["cultivos"]
                data = collection.find({})
                # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
                data = list(data)
                df_mongo = pd.DataFrame(data)  # leer la tabla completa (DataFrame)
                self.plainTextEdit.insertPlainText("Cultivo")
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.read_sql_query("SELECT area sembrada FROM cultivos",conn)
                # Crear un histograma de la columna rendimiento
                df_mongo['cultivo'].hist()
                # Agregar etiquetas al gráfico
                plt.title('Histograma de Cultivo')
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                # Mostrar el gráfico
                plt.show()
            elif (self.comboBox.currentIndex() == 5):
                cliente = MongoClient('localhost', 27017)  # localhost predeterminado, 27017
                collection = cliente["ProyectoFinal"]["cultivos"]
                data = collection.find({})
                # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
                data = list(data)
                df_mongo = pd.DataFrame(data)  # leer la tabla completa (DataFrame)
                self.plainTextEdit.insertPlainText("Municipio")
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.read_sql_query("SELECT area sembrada FROM cultivos",conn)
                # Crear un histograma de la columna rendimiento
                df_mongo['municipio'].hist()
                # Agregar etiquetas al gráfico
                plt.title('Histograma de Municipio')
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                # Mostrar el gráfico
                plt.show()
            elif (self.comboBox.currentIndex() == 6):
                cliente = MongoClient('localhost', 27017)  # localhost predeterminado, 27017
                collection = cliente["ProyectoFinal"]["cultivos"]
                data = collection.find({})
                # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
                data = list(data)
                df_mongo = pd.DataFrame(data)  # leer la tabla completa (DataFrame)
                self.plainTextEdit.insertPlainText("Periodo")
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.read_sql_query("SELECT area sembrada FROM cultivos",conn)
                # Crear un histograma de la columna rendimiento
                df_mongo['PERIODO'].hist()
                # Agregar etiquetas al gráfico
                plt.title('Histograma de Periodo')
                plt.xlabel('Valor')
                plt.ylabel('Frecuencia')
                # Mostrar el gráfico
                plt.show()
            else:
                self.plainTextEdit.insertPlainText("")
####################################################################################

    def display1(self):
        self.plainTextEdit_2.clear()  # Borrar plainText
        print(self.comboBox1.currentText(), f"({self.comboBox1.currentIndex()})")
        if not e:
            if (self.comboBox1.currentIndex() == 0):
                self.plainTextEdit_2.insertPlainText("Area Sembrada")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.get_dummies(df, columns=['categoria'], prefix='', prefix_sep='').astype(bool)
                df = pd.get_dummies(df, columns=['cultivo', 'municipio', 'PERIODO']).astype(int)
                print(df)
                X = df.to_numpy()
                y = df['area sembrada'].to_numpy()
                """
                iris = load_iris()
                X = iris.data
                y = iris.target """
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
                lab_enc = preprocessing.LabelEncoder()
                logreg = LogisticRegression()
                encoded_train_Y = lab_enc.fit_transform(y_train)
                logreg.fit(X_train, encoded_train_Y)
                y_pred = logreg.predict(X_test)
                accuracy = np.mean(y_pred == y_test)
                print(f"Precisión del modelo: {accuracy:.2f}")
                """
                # Graficar los puntos de prueba con colores según la clase predicha
                colors = ['red', 'green', 'blue']
                markers = ['o', '^', 's']
    
                for i in range(3):
                    plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1],
                                color=colors[i], marker=markers[i], label=f'Clase {i}')
                """
                # Graficar los datos reales y predichos
                plt.figure(figsize=(10, 6))
                plt.scatter(X_train[:, 0], X_train[:, 1], marker='o',edgecolors='blue')
                plt.scatter(X_test[:, 0], X_test[:, 1], marker='s', alpha=0.4,edgecolors='red')
                plt.xlabel('')
                plt.ylabel('')
                plt.title('Datos reales (círculos) y predichos (cuadros)')
                plt.show()
            elif(self.comboBox1.currentIndex() == 1):
                self.plainTextEdit_2.insertPlainText("Area Cosechada")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                df = pd.get_dummies(df, columns=['cultivo', 'municipio', 'PERIODO']).astype(int)
                print(df)
                X = df.to_numpy()
                y = df['area cosechada'].to_numpy()
                """
                iris = load_iris()
                X = iris.data
                y = iris.target """
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
                lab_enc = preprocessing.LabelEncoder()
                logreg = LogisticRegression()
                encoded_train_Y = lab_enc.fit_transform(y_train)
                logreg.fit(X_train, encoded_train_Y)
                y_pred = logreg.predict(X_test)
                accuracy = np.mean(y_pred == y_test)
                print(f"Precisión del modelo: {accuracy:.2f}")
                """
                # Graficar los puntos de prueba con colores según la clase predicha
                colors = ['red', 'green', 'blue']
                markers = ['o', '^', 's']
    
                for i in range(3):
                    plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1],
                                color=colors[i], marker=markers[i], label=f'Clase {i}')
                """
                # Graficar los datos reales y predichos
                plt.figure(figsize=(10, 6))
                plt.scatter(X_train[:, 0], X_train[:, 1], marker='o',edgecolors='blue')
                plt.scatter(X_test[:, 0], X_test[:, 1], marker='s', alpha=0.4,edgecolors='red')
                plt.xlabel('')
                plt.ylabel('')
                plt.title('Datos reales (círculos) y predichos (cuadros)')
                plt.show()
            elif (self.comboBox1.currentIndex() == 2):
                self.plainTextEdit_2.insertPlainText("Produccion")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                df = pd.get_dummies(df, columns=['cultivo', 'municipio', 'PERIODO']).astype(int)
                print(df)
                X = df.to_numpy()
                y = df['produccion'].to_numpy()
                """
                iris = load_iris()
                X = iris.data
                y = iris.target """
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
                lab_enc = preprocessing.LabelEncoder()
                logreg = LogisticRegression()
                encoded_train_Y = lab_enc.fit_transform(y_train)
                logreg.fit(X_train, encoded_train_Y)
                y_pred = logreg.predict(X_test)
                accuracy = np.mean(y_pred == y_test)
                print(f"Precisión del modelo: {accuracy:.2f}")
                """
                # Graficar los puntos de prueba con colores según la clase predicha
                colors = ['red', 'green', 'blue']
                markers = ['o', '^', 's']
    
                for i in range(3):
                    plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1],
                                color=colors[i], marker=markers[i], label=f'Clase {i}')
                """
                # Graficar los datos reales y predichos
                plt.figure(figsize=(10, 6))
                plt.scatter(X_train[:, 0], X_train[:, 1], marker='o',edgecolors='blue')
                plt.scatter(X_test[:, 0], X_test[:, 1], marker='s', alpha=0.4,edgecolors='red')
                plt.xlabel('')
                plt.ylabel('')
                plt.title('Datos reales (círculos) y predichos (cuadros)')
                plt.show()
            if (self.comboBox1.currentIndex() == 3):
                self.plainTextEdit_2.insertPlainText("Rendimiento")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                df = pd.get_dummies(df, columns=['cultivo', 'municipio', 'PERIODO']).astype(int)
                print(df)
                X = df.to_numpy()
                y = df['rendimiento'].to_numpy()
                """
                iris = load_iris()
                X = iris.data
                y = iris.target """
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
                lab_enc = preprocessing.LabelEncoder()
                logreg = LogisticRegression()
                encoded_train_Y = lab_enc.fit_transform(y_train)
                logreg.fit(X_train, encoded_train_Y)
                y_pred = logreg.predict(X_test)
                accuracy = np.mean(y_pred == y_test)
                print(f"Precisión del modelo: {accuracy:.2f}")
                """
                # Graficar los puntos de prueba con colores según la clase predicha
                colors = ['red', 'green', 'blue']
                markers = ['o', '^', 's']
    
                for i in range(3):
                    plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1],
                                color=colors[i], marker=markers[i], label=f'Clase {i}')
                """
                # Graficar los datos reales y predichos
                plt.figure(figsize=(10, 6))
                plt.scatter(X_train[:, 0], X_train[:, 1], marker='o',edgecolors='blue')
                plt.scatter(X_test[:, 0], X_test[:, 1], marker='s', alpha=0.4,edgecolors='red')
                plt.xlabel('')
                plt.ylabel('')
                plt.title('Datos reales (círculos) y predichos (cuadros)')
                plt.show()
            """
            elif(self.comboBox1.currentIndex() == 4):
                self.plainTextEdit_2.insertPlainText("Cultivo")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                df = pd.get_dummies(df, columns=['cultivo', 'municipio', 'PERIODO']).astype(int)
                print(df)
                X = df.to_numpy()
                y = df['cultivo'].to_numpy()
                
                iris = load_iris()
                X = iris.data
                y = iris.target 
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
                lab_enc = preprocessing.LabelEncoder()
                logreg = LogisticRegression()
                encoded_train_Y = lab_enc.fit_transform(y_train)
                logreg.fit(X_train, encoded_train_Y)
                y_pred = logreg.predict(X_test)
                accuracy = np.mean(y_pred == y_test)
                print(f"Precisión del modelo: {accuracy:.2f}")
                
                # Graficar los puntos de prueba con colores según la clase predicha
                colors = ['red', 'green', 'blue']
                markers = ['o', '^', 's']
    
                for i in range(3):
                    plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1],
                                color=colors[i], marker=markers[i], label=f'Clase {i}')
                
                # Graficar los datos reales y predichos
                plt.figure(figsize=(10, 6))
                plt.scatter(X_train[:, 0], X_train[:, 1], marker='o',edgecolors='blue')
                plt.scatter(X_test[:, 0], X_test[:, 1], marker='s', alpha=0.4,edgecolors='red')
                plt.xlabel('')
                plt.ylabel('')
                plt.title('Datos reales (círculos) y predichos (cuadros)')
                plt.show()
            elif (self.comboBox1.currentIndex() == 5):
                self.plainTextEdit_2.insertPlainText("Municipio")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                df = pd.get_dummies(df, columns=['cultivo', 'municipio', 'PERIODO'])
                X = df.to_numpy()
                y = df['municipio'].to_numpy()
                
    
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
                lab_enc = preprocessing.LabelEncoder()
                logreg = LogisticRegression()
                encoded_train_Y = lab_enc.fit_transform(y_train)
                logreg.fit(X_train, encoded_train_Y)
                y_pred = logreg.predict(X_test)
                accuracy = np.mean(y_pred == y_test)
                print(f"Precisión del modelo: {accuracy:.2f}")
                
                # Graficar los puntos de prueba con colores según la clase predicha
                colors = ['red', 'green', 'blue']
                markers = ['o', '^', 's']
    
                for i in range(3):
                    plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1],
                                color=colors[i], marker=markers[i], label=f'Clase {i}')
                
                # Graficar los datos reales y predichos
                plt.figure(figsize=(10, 6))
                plt.scatter(X_train[:, 0], X_train[:, 1], marker='o',edgecolors='blue')
                plt.scatter(X_test[:, 0], X_test[:, 1], marker='s', alpha=0.4,edgecolors='red')
                plt.xlabel('')
                plt.ylabel('')
                plt.title('Datos reales (círculos) y predichos (cuadros)')
                plt.show()
            elif (self.comboBox1.currentIndex() == 6):
                self.plainTextEdit_2.insertPlainText("Periodo")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                df = pd.get_dummies(df, columns=['cultivo', 'municipio', 'PERIODO'])
                X = df.to_numpy()
                y = df['PERIODO'].to_numpy()
    
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
                lab_enc = preprocessing.LabelEncoder()
                logreg = LogisticRegression()
                encoded_train_Y = lab_enc.fit_transform(y_train)
                logreg.fit(X_train, encoded_train_Y)
                y_pred = logreg.predict(X_test)
                accuracy = np.mean(y_pred == y_test)
                print(f"Precisión del modelo: {accuracy:.2f}")
    
                # Graficar los datos reales y predichos
                plt.figure(figsize=(10, 6))
                plt.scatter(X_train[:, 0], X_train[:, 1], marker='o',edgecolors='blue')
                plt.scatter(X_test[:, 0], X_test[:, 1], marker='s', alpha=0.4,edgecolors='red')
                plt.xlabel('')
                plt.ylabel('')
                plt.title('Datos reales (círculos) y predichos (cuadros)')
                plt.show()
            else:
                self.plainTextEdit_2.insertPlainText("")
            """
        else:
            if (self.comboBox1.currentIndex() == 0):
                self.plainTextEdit_2.insertPlainText("Area Sembrada")
                cliente = MongoClient('localhost', 27017)  # localhost predeterminado, 27017
                collection = cliente["ProyectoFinal"]["cultivos"]
                data = collection.find({})
                # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
                data = list(data)
                df_mongo = pd.DataFrame(data)  # leer la tabla completa (DataFrame)
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                # df = pd.get_dummies(df, columns=['categoria'], prefix='', prefix_sep='').astype(bool)
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                #df = pd.get_dummies(df_mongo, columns=['cultivo', 'municipio', 'PERIODO']).astype(int)
                print(df)
                X = df.to_numpy()
                y = df['area sembrada'].to_numpy()
                """
                iris = load_iris()
                X = iris.data
                y = iris.target """
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
                lab_enc = preprocessing.LabelEncoder()
                logreg = LogisticRegression()
                encoded_train_Y = lab_enc.fit_transform(y_train)
                logreg.fit(X_train, encoded_train_Y)
                y_pred = logreg.predict(X_test)
                accuracy = np.mean(y_pred == y_test)
                print(f"Precisión del modelo: {accuracy:.2f}")
                """
                # Graficar los puntos de prueba con colores según la clase predicha
                colors = ['red', 'green', 'blue']
                markers = ['o', '^', 's']

                for i in range(3):
                    plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1],
                                color=colors[i], marker=markers[i], label=f'Clase {i}')
                """
                # Graficar los datos reales y predichos
                plt.figure(figsize=(10, 6))
                plt.scatter(X_train[:, 0], X_train[:, 1], marker='o', edgecolors='blue')
                plt.scatter(X_test[:, 0], X_test[:, 1], marker='s', alpha=0.4, edgecolors='red')
                plt.xlabel('')
                plt.ylabel('')
                plt.title('Datos reales (círculos) y predichos (cuadros)')
                plt.show()
            elif (self.comboBox1.currentIndex() == 1):
                self.plainTextEdit_2.insertPlainText("Area Cosechada")
                cliente = MongoClient('localhost', 27017)  # localhost predeterminado, 27017
                collection = cliente["ProyectoFinal"]["cultivos"]
                data = collection.find({})
                # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
                data = list(data)
                df_mongo = pd.DataFrame(data)  # leer la tabla completa (DataFrame)
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.get_dummies(df_mongo, columns=['cultivo', 'municipio', 'PERIODO']).astype(int)
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                print(df)
                X = df.to_numpy()
                y = df['area cosechada'].to_numpy()
                """
                iris = load_iris()
                X = iris.data
                y = iris.target """
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
                lab_enc = preprocessing.LabelEncoder()
                logreg = LogisticRegression()
                encoded_train_Y = lab_enc.fit_transform(y_train)
                logreg.fit(X_train, encoded_train_Y)
                y_pred = logreg.predict(X_test)
                accuracy = np.mean(y_pred == y_test)
                print(f"Precisión del modelo: {accuracy:.2f}")
                """
                # Graficar los puntos de prueba con colores según la clase predicha
                colors = ['red', 'green', 'blue']
                markers = ['o', '^', 's']

                for i in range(3):
                    plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1],
                                color=colors[i], marker=markers[i], label=f'Clase {i}')
                """
                # Graficar los datos reales y predichos
                plt.figure(figsize=(10, 6))
                plt.scatter(X_train[:, 0], X_train[:, 1], marker='o', edgecolors='blue')
                plt.scatter(X_test[:, 0], X_test[:, 1], marker='s', alpha=0.4, edgecolors='red')
                plt.xlabel('')
                plt.ylabel('')
                plt.title('Datos reales (círculos) y predichos (cuadros)')
                plt.show()
            elif (self.comboBox1.currentIndex() == 2):
                self.plainTextEdit_2.insertPlainText("Produccion")
                cliente = MongoClient('localhost', 27017)  # localhost predeterminado, 27017
                collection = cliente["ProyectoFinal"]["cultivos"]
                data = collection.find({})
                # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
                data = list(data)
                df_mongo = pd.DataFrame(data)  # leer la tabla completa (DataFrame)
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.get_dummies(df_mongo, columns=['cultivo', 'municipio', 'PERIODO']).astype(int)
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                print(df)
                X = df.to_numpy()
                y = df['produccion'].to_numpy()
                """
                iris = load_iris()
                X = iris.data
                y = iris.target """
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
                lab_enc = preprocessing.LabelEncoder()
                logreg = LogisticRegression()
                encoded_train_Y = lab_enc.fit_transform(y_train)
                logreg.fit(X_train, encoded_train_Y)
                y_pred = logreg.predict(X_test)
                accuracy = np.mean(y_pred == y_test)
                print(f"Precisión del modelo: {accuracy:.2f}")
                """
                # Graficar los puntos de prueba con colores según la clase predicha
                colors = ['red', 'green', 'blue']
                markers = ['o', '^', 's']

                for i in range(3):
                    plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1],
                                color=colors[i], marker=markers[i], label=f'Clase {i}')
                """
                # Graficar los datos reales y predichos
                plt.figure(figsize=(10, 6))
                plt.scatter(X_train[:, 0], X_train[:, 1], marker='o', edgecolors='blue')
                plt.scatter(X_test[:, 0], X_test[:, 1], marker='s', alpha=0.4, edgecolors='red')
                plt.xlabel('')
                plt.ylabel('')
                plt.title('Datos reales (círculos) y predichos (cuadros)')
                plt.show()
            if (self.comboBox1.currentIndex() == 3):
                self.plainTextEdit_2.insertPlainText("Rendimiento")
                cliente = MongoClient('localhost', 27017)  # localhost predeterminado, 27017
                collection = cliente["ProyectoFinal"]["cultivos"]
                data = collection.find({})
                # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
                data = list(data)
                df_mongo = pd.DataFrame(data)  # leer la tabla completa (DataFrame)
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                #df = pd.get_dummies(df_mongo, columns=['cultivo', 'municipio', 'PERIODO']).astype(int)
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                print(df)
                X = df.to_numpy()
                y = df['rendimiento'].to_numpy()
                """
                iris = load_iris()
                X = iris.data
                y = iris.target """
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
                lab_enc = preprocessing.LabelEncoder()
                logreg = LogisticRegression()
                encoded_train_Y = lab_enc.fit_transform(y_train)
                logreg.fit(X_train, encoded_train_Y)
                y_pred = logreg.predict(X_test)
                accuracy = np.mean(y_pred == y_test)
                print(f"Precisión del modelo: {accuracy:.2f}")
                """
                # Graficar los puntos de prueba con colores según la clase predicha
                colors = ['red', 'green', 'blue']
                markers = ['o', '^', 's']

                for i in range(3):
                    plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1],
                                color=colors[i], marker=markers[i], label=f'Clase {i}')
                """
                # Graficar los datos reales y predichos
                plt.figure(figsize=(10, 6))
                plt.scatter(X_train[:, 0], X_train[:, 1], marker='o', edgecolors='blue')
                plt.scatter(X_test[:, 0], X_test[:, 1], marker='s', alpha=0.4, edgecolors='red')
                plt.xlabel('')
                plt.ylabel('')
                plt.title('Datos reales (círculos) y predichos (cuadros)')
                plt.show()
            """
            elif(self.comboBox1.currentIndex() == 4):
                self.plainTextEdit_2.insertPlainText("Cultivo")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                df = pd.get_dummies(df, columns=['cultivo', 'municipio', 'PERIODO']).astype(int)
                print(df)
                X = df.to_numpy()
                y = df['cultivo'].to_numpy()

                iris = load_iris()
                X = iris.data
                y = iris.target 
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
                lab_enc = preprocessing.LabelEncoder()
                logreg = LogisticRegression()
                encoded_train_Y = lab_enc.fit_transform(y_train)
                logreg.fit(X_train, encoded_train_Y)
                y_pred = logreg.predict(X_test)
                accuracy = np.mean(y_pred == y_test)
                print(f"Precisión del modelo: {accuracy:.2f}")

                # Graficar los puntos de prueba con colores según la clase predicha
                colors = ['red', 'green', 'blue']
                markers = ['o', '^', 's']

                for i in range(3):
                    plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1],
                                color=colors[i], marker=markers[i], label=f'Clase {i}')

                # Graficar los datos reales y predichos
                plt.figure(figsize=(10, 6))
                plt.scatter(X_train[:, 0], X_train[:, 1], marker='o',edgecolors='blue')
                plt.scatter(X_test[:, 0], X_test[:, 1], marker='s', alpha=0.4,edgecolors='red')
                plt.xlabel('')
                plt.ylabel('')
                plt.title('Datos reales (círculos) y predichos (cuadros)')
                plt.show()
            elif (self.comboBox1.currentIndex() == 5):
                self.plainTextEdit_2.insertPlainText("Municipio")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                df = pd.get_dummies(df, columns=['cultivo', 'municipio', 'PERIODO'])
                X = df.to_numpy()
                y = df['municipio'].to_numpy()


                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
                lab_enc = preprocessing.LabelEncoder()
                logreg = LogisticRegression()
                encoded_train_Y = lab_enc.fit_transform(y_train)
                logreg.fit(X_train, encoded_train_Y)
                y_pred = logreg.predict(X_test)
                accuracy = np.mean(y_pred == y_test)
                print(f"Precisión del modelo: {accuracy:.2f}")

                # Graficar los puntos de prueba con colores según la clase predicha
                colors = ['red', 'green', 'blue']
                markers = ['o', '^', 's']

                for i in range(3):
                    plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1],
                                color=colors[i], marker=markers[i], label=f'Clase {i}')

                # Graficar los datos reales y predichos
                plt.figure(figsize=(10, 6))
                plt.scatter(X_train[:, 0], X_train[:, 1], marker='o',edgecolors='blue')
                plt.scatter(X_test[:, 0], X_test[:, 1], marker='s', alpha=0.4,edgecolors='red')
                plt.xlabel('')
                plt.ylabel('')
                plt.title('Datos reales (círculos) y predichos (cuadros)')
                plt.show()
            elif (self.comboBox1.currentIndex() == 6):
                self.plainTextEdit_2.insertPlainText("Periodo")
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                df = pd.get_dummies(df, columns=['cultivo', 'municipio', 'PERIODO'])
                X = df.to_numpy()
                y = df['PERIODO'].to_numpy()

                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
                lab_enc = preprocessing.LabelEncoder()
                logreg = LogisticRegression()
                encoded_train_Y = lab_enc.fit_transform(y_train)
                logreg.fit(X_train, encoded_train_Y)
                y_pred = logreg.predict(X_test)
                accuracy = np.mean(y_pred == y_test)
                print(f"Precisión del modelo: {accuracy:.2f}")

                # Graficar los datos reales y predichos
                plt.figure(figsize=(10, 6))
                plt.scatter(X_train[:, 0], X_train[:, 1], marker='o',edgecolors='blue')
                plt.scatter(X_test[:, 0], X_test[:, 1], marker='s', alpha=0.4,edgecolors='red')
                plt.xlabel('')
                plt.ylabel('')
                plt.title('Datos reales (círculos) y predichos (cuadros)')
                plt.show()
            else:
                self.plainTextEdit_2.insertPlainText("")
            """

    ####################################################################################

    def display2(self):
        print(self.comboBox2.currentText(), f"({self.comboBox2.currentIndex()})")
        print(self.comboBox3.currentText(), f"({self.comboBox3.currentIndex()})")
        if not e:
            if (self.comboBox2.currentIndex() == 0 and self.comboBox3.currentIndex() == 1):
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                X = df.iloc[:, 0:2].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif(self.comboBox2.currentIndex() == 1 and self.comboBox3.currentIndex() == 0):
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                X = df.iloc[:, 0:2].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif(self.comboBox2.currentIndex() == 0 and self.comboBox3.currentIndex() == 2):
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                X = df.iloc[:, [0, 2]].values


                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif(self.comboBox2.currentIndex() == 2 and self.comboBox3.currentIndex() == 0):
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                X = df.iloc[:, [0, 2]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif(self.comboBox2.currentIndex() == 0 and self.comboBox3.currentIndex() == 3):
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                X = df.iloc[:, [0, 3]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif(self.comboBox2.currentIndex() == 3 and self.comboBox3.currentIndex() == 0):
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                X = df.iloc[:, [0, 3]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif(self.comboBox2.currentIndex() == 1 and self.comboBox3.currentIndex() == 2):
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                X = df.iloc[:, [1, 2]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif(self.comboBox2.currentIndex() == 2 and self.comboBox3.currentIndex() == 1):
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                X = df.iloc[:, [1, 2]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif(self.comboBox2.currentIndex() == 1 and self.comboBox3.currentIndex() == 3):
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                X = df.iloc[:, [1, 3]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif(self.comboBox2.currentIndex() == 3 and self.comboBox3.currentIndex() == 1):
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                X = df.iloc[:, [1, 3]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif(self.comboBox2.currentIndex() == 2 and self.comboBox3.currentIndex() == 3):
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                X = df.iloc[:, [2, 3]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif(self.comboBox2.currentIndex() == 3 and self.comboBox3.currentIndex() == 2):
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                X = df.iloc[:, [2, 3]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif(self.comboBox2.currentIndex() == 2 and self.comboBox3.currentIndex() == 4):
                df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                X = df.iloc[:, [2, 4]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            """    
            else:
            """
        else:
            if (self.comboBox2.currentIndex() == 0 and self.comboBox3.currentIndex() == 1):
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                X = df.iloc[:, 0:2].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif (self.comboBox2.currentIndex() == 1 and self.comboBox3.currentIndex() == 0):
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                X = df.iloc[:, 0:2].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif (self.comboBox2.currentIndex() == 0 and self.comboBox3.currentIndex() == 2):
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                X = df.iloc[:, [0, 2]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif (self.comboBox2.currentIndex() == 2 and self.comboBox3.currentIndex() == 0):
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                X = df.iloc[:, [0, 2]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif (self.comboBox2.currentIndex() == 0 and self.comboBox3.currentIndex() == 3):
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                X = df.iloc[:, [0, 3]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif (self.comboBox2.currentIndex() == 3 and self.comboBox3.currentIndex() == 0):
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                X = df.iloc[:, [0, 3]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif (self.comboBox2.currentIndex() == 1 and self.comboBox3.currentIndex() == 2):
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                X = df.iloc[:, [1, 2]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif (self.comboBox2.currentIndex() == 2 and self.comboBox3.currentIndex() == 1):
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                X = df.iloc[:, [1, 2]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif (self.comboBox2.currentIndex() == 1 and self.comboBox3.currentIndex() == 3):
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                X = df.iloc[:, [1, 3]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif (self.comboBox2.currentIndex() == 3 and self.comboBox3.currentIndex() == 1):
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                X = df.iloc[:, [1, 3]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif (self.comboBox2.currentIndex() == 2 and self.comboBox3.currentIndex() == 3):
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                X = df.iloc[:, [2, 3]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif (self.comboBox2.currentIndex() == 3 and self.comboBox3.currentIndex() == 2):
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                X = df.iloc[:, [2, 3]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            elif (self.comboBox2.currentIndex() == 2 and self.comboBox3.currentIndex() == 4):
                #df = pd.read_sql("SELECT * FROM cultivos", conn)
                # iris = load_iris()
                # X = iris.data[:, :2]
                df = df_mongo.drop(['cultivo', 'municipio', 'PERIODO','_id'], axis=1)
                X = df.iloc[:, [2, 4]].values

                # Entrenar el modelo de clustering con KMeans
                kmeans = KMeans(n_clusters=10, random_state=42)
                kmeans.fit(X)

                # Obtener los centroides y las etiquetas de cada punto
                centroides = kmeans.cluster_centers_
                labels = kmeans.labels_

                # Visualizar los resultados
                plt.scatter(X[:, 0], X[:, 1], c=labels)
                plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                plt.title('KMeans Clustering')
                plt.xlabel('')
                plt.ylabel('')
                plt.show()

                # Evaluar los modelos con los datos de prueba
                print("Resultados de KMeans:")
                print(kmeans.predict(X))
            """    
            else:
            """

    ####################################################################################

    def Mostrar_Histograma(self):
        df = pd.read_sql("SELECT * FROM cultivos", conn)
        # Crear un histograma de la columna rendimiento
        df['rendimiento'].hist()
        # Agregar etiquetas al gráfico
        plt.title('Histograma de columna1')
        plt.xlabel('Valor')
        plt.ylabel('Frecuencia')
        # Mostrar el gráfico
        plt.show()

####################################################################################

    def ModeloSupervisado(self):
        df = pd.read_sql("SELECT * FROM cultivos", conn)
        df = pd.get_dummies(df, columns=['cultivo', 'municipio', 'PERIODO'])
        X = df.to_numpy()
        y = df['rendimiento'].to_numpy()

        print(X)
        print(y)
        print("hola")
        """
        iris = load_iris()
        X = iris.data
        y = iris.target """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
        lab_enc = preprocessing.LabelEncoder()
        logreg = LogisticRegression()
        encoded_train_Y = lab_enc.fit_transform(y_train)
        logreg.fit(X_train, encoded_train_Y)
        y_pred = logreg.predict(X_test)
        accuracy = np.mean(y_pred == y_test)
        print(f"Precisión del modelo: {accuracy:.2f}")
        """
        # Graficar los puntos de prueba con colores según la clase predicha
        colors = ['red', 'green', 'blue']
        markers = ['o', '^', 's']

        for i in range(3):
            plt.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1],
                        color=colors[i], marker=markers[i], label=f'Clase {i}')
        """
        # Graficar los datos reales y predichos
        plt.figure(figsize=(10, 6))
        plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, marker='o')
        plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, marker='s', alpha=0.4)
        plt.xlabel('Longitud del tallo')
        plt.ylabel('Ancho del tallo')
        plt.title('Datos reales (círculos) y predichos (cuadros)')
        plt.show()

####################################################################################

    def ModeloNoSupervisado(self):

        # Cargar el conjunto de datos iris
        iris = load_iris()
        # Seleccionar dos características
        X = iris.data[:, :2]

        #y = np.array(dataframe['categoria'])

        # Entrenar el modelo de clustering con KMeans
        kmeans = KMeans(n_clusters=10, random_state=42)
        kmeans.fit(X)

        # Obtener los centroides y las etiquetas de cada punto
        centroides = kmeans.cluster_centers_
        labels = kmeans.labels_

        # Visualizar los resultados
        plt.scatter(X[:, 0], X[:, 1], c=labels)
        plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
        plt.title('KMeans Clustering - Dataset Iris')
        plt.xlabel('longitud de tallo')
        plt.ylabel('ancho de tallo')
        plt.show()

        # Evaluar los modelos con los datos de prueba
        print("Resultados de KMeans:")
        print(kmeans.predict(X))

####################################################################################

if __name__=="__main__":
    while True:
        try:
            e=""
            if not e:
                #conn = get_connection()
                conn = pymysql.connect(host=str(host), port=port, user=user, passwd=password, db=database, charset='utf8mb4')
                print(f"Conexion Exitosa con bases de datos SQL")
                app = QtWidgets.QApplication(sys.argv)
                Vent = Aplicacion()
                Vent.show()
                app.exec()
            else:
                print(f"Se produjo una excepción: {e}")
                # print(dir(e))
                # print(f"Conexion Exitosa con bases de datos NOSQL")
                # Código a ejecutar si no se produce una excepción
                cliente = MongoClient('localhost', 27017)  # localhost predeterminado, 27017
                collection = cliente["ProyectoFinal"]["cultivos"]
                data = collection.find()

                # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
                data = list(data)
                df_mongo = pd.DataFrame(data)  # leer la tabla completa (DataFrame)
                print(df_mongo)
                app = QtWidgets.QApplication(sys.argv)
                Vent = Aplicacion()
                Vent.show()
                app.exec()

        except Exception as e:
            print(f"Se produjo una excepción: {e}")
            #print(dir(e))
            #print(f"Conexion Exitosa con bases de datos NOSQL")
            # Código a ejecutar si no se produce una excepción
            cliente = MongoClient('localhost', 27017)  # localhost predeterminado, 27017
            collection = cliente["ProyectoFinal"]["cultivos"]
            data = collection.find()

            # Al convertir a una lista, puede filtrar solo los datos que necesita según la situación. (para filtrado transversal)
            data = list(data)
            df_mongo = pd.DataFrame(data)  # leer la tabla completa (DataFrame)
            print(df_mongo)
            app = QtWidgets.QApplication(sys.argv)
            Vent = Aplicacion()
            Vent.show()
            app.exec()

"""
    try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        conn = get_connection()
        print(f"Connection to the host for user created successfully.")

    except DisconnectionError:
        print("Connection could not be made due to the following error")
"""
"""
    try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        conn = get_connection()
        print(f"Connection to the host for user created successfully.")
        app = QtWidgets.QApplication(sys.argv)
        Vent = Aplicacion()
        Vent.show()
        app.exec()
        data = get_connection_mongo()
    except DatabaseError:
        print("Connection could not be made due to the following error")
"""
"""
    try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        conn = get_connection()
        print(
            f"Connection to the host for user created successfully.")
        app = QtWidgets.QApplication(sys.argv)
        Vent = Aplicacion()
        Vent.show()
        app.exec()

        data = get_connection_mongo()

    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
"""


