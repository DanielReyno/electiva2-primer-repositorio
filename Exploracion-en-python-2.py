from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("netflix_titles.csv")


print("Primeras 10 filas")
print(data.head(10))

print("Ultimas 15 filas")
print(data.tail(15))

print("Generar las estadisticas basicas")
print(data.describe())

print("sustituir los registros que esten vacios(na) con 0")
print(data.fillna(0))

print(data["type"])

pelicula = data[data["type"] == "Movie"]
pelicula2 = pelicula[pelicula["release_year"] >= 2010]
pelicula3 = pelicula2.groupby('release_year').size()



serie = data[data["type"] == "TV Show"]
serie2 = serie[serie["release_year"] >= 2010]
serie3 = serie2.groupby('release_year').size()

indice = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]

grafico = {'Peliculas': pelicula3,'Series': serie3}

datos = pd.DataFrame(grafico,index=indice)

z = datos.plot.bar(rot=0)

plt.show()