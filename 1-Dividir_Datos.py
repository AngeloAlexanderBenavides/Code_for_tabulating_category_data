"""
Bibliotecas Necesarias
# Instalar Panda 
#        pip install pandas
# En la consola.
# Instalar matplotlib 
#        pip install matplotlib
# En la consola.
# 
# """

import pandas as pd


#Nombre del documento y su denominacion de archivo ".xlsx"
#Columna que se desea extraer a otro exel
df = pd.read_excel("AnalizarDatos.xlsx", usecols="I")


#Separeacion y elimacion de espacios en blanco
columna_datos = df["categoria"].str.split(",").apply(lambda x: [item.strip() for item in x])
df_separado = pd.DataFrame({'categoria': [item for sublist in columna_datos for item in sublist]})

#Nombre del documento final.
df_separado.to_excel("patron_letras_librerias_separado.xlsx", index=False)
print("Separación completada y archivo guardado.")
