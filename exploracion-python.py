from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

#Autor: Daniel Sebastian Reynoso Feliz
#Matricula: 2021-1571


#Leer el archivo csv 
data = pd.read_csv("avocado.csv")

#1. Obtener Cuantas filas y cuantas columnas tiene el conjunto de datos
Columnas = data.shape[1]
Filas = data.shape[0]

print("")
print("")

print("La tabla de datos tiene "+str(Filas)+" Filas, y "+str(Columnas)+" Columnas")

print("")
print("")

#2. Mostrar los primeros 100 registros
print("imprimir los primeros 100 registros")
print(data.head(100))

print("")
print("")

#3. Mostrar los últimos 20 registros
print("Imprimir los ultimos 20 registros")
print(data.tail(20))

print("")
print("")

#4. Cual es el precio mínimo, máximo y promedio del aguacate en ese conjunto de datos
PrecioAlto = data["AveragePrice"].max()
PrecioBajo = data["AveragePrice"].min()
PrecioPromedio = data["AveragePrice"].mean()

print("Maximo: "+str(PrecioAlto))
print("Minimo: "+str(PrecioBajo))
print("Promedio: "+str(PrecioPromedio))

#5.Generar un gráfico de tipo scatter usando  para la x la variable 'year' y  para y la variable 'AveragePrice' para 3 regiones (las que usted elija), 
#los 3 sub-conjuntos deben mostrarse en el mismo gráfico.
Albany = data[data["region"] == "Albany"]
Boston = data[data["region"] == "Boston"]
California = data[data["region"] == "California"]

x1 = plt.subplot()

g_Albany = Albany.plot(x="year", y="AveragePrice", kind="scatter", color="blue", ax=x1, label="Albany")
g_Boston = Boston.plot(x="year", y="AveragePrice", kind="scatter", color="green", ax=x1, label="Boston")
g_California = California.plot(x="year", y="AveragePrice", kind="scatter", color="red", ax=x1, label="California")

plt.show()

print("hola gitS")


