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
import matplotlib.pyplot as plt

# Leer el archivo Excel y cargar los datos en un DataFrame
df = pd.read_excel("patron_letras_librerias_separado.xlsx", usecols="A")

# Tabla de los datos más comunes
datos_mas_comunes = df['categoria'].value_counts().head(5)
tabla_mas_comunes = pd.DataFrame({'Categoria': datos_mas_comunes.index, 'Cantidad': datos_mas_comunes.values})

# Tabla de los datos menos comunes
datos_menos_comunes = df['categoria'].value_counts().tail(5)
tabla_menos_comunes = pd.DataFrame({'Categoria': datos_menos_comunes.index, 'Cantidad': datos_menos_comunes.values})

# Visualización de los datos todo en una sola ventana
plt.figure(figsize=(18, 6))
plt.subplot(131)
plt.bar(tabla_mas_comunes['Categoria'], tabla_mas_comunes['Cantidad'])
plt.title('Datos Más Comunes')
plt.xlabel('Columna Categoría')
plt.ylabel('Cantidad')
plt.xticks(rotation=45, ha='right')
plt.subplot(132)
plt.bar(tabla_menos_comunes['Categoria'], tabla_menos_comunes['Cantidad'])
plt.title('Datos Menos Comunes')
plt.xlabel('Columna Categoría')
plt.ylabel('Cantidad')
plt.xticks(rotation=45, ha='right')
plt.subplot(133)
plt.bar(df['categoria'].value_counts().index, df['categoria'].value_counts().values)
plt.title('Distribución de Todos los Datos')
plt.xlabel('Columna Categoría')
plt.ylabel('Cantidad')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()

plt.show()
