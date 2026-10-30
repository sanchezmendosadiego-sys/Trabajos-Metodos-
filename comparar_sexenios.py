import pandas as pd

# 1. Datos simulados para los dos sexenios
datos = {
    'Sexenio 1': [2.5, 3.1, 2.8, 4.0, 3.5, 2.9],
    'Sexenio 2': [1.5, 1.8, 1.2, 2.0, 1.7, 1.9]
}
df_datos = pd.DataFrame(datos)

# 2. Calcular las métricas para cada columna
def calcular_metricas(serie):
    return [
        serie.mean(),
        serie.var(ddof=0), # Varianza poblacional
        serie.std(ddof=0), # Desviación estándar poblacional
        serie.max(),
        serie.min(),
        serie.max() - serie.min() # Rango
    ]

# 3. Construir la tabla final
tabla_resultados = {
    'Métrica': ['Media', 'Varianza', 'Desviación estándar', 'Máximo', 'Mínimo', 'Rango'],
    'Sexenio 1': calcular_metricas(df_datos['Sexenio 1']),
    'Sexenio 2': calcular_metricas(df_datos['Sexenio 2'])
}

df_final = pd.DataFrame(tabla_resultados)

# 4. Imprimir los resultados
print("--- Tabla Comparativa ---")
print(df_final.to_string(index=False))

print("\n¿Qué puedes determinar al comparar ambos periodos?")
print("-> (Ejemplo de análisis): El Sexenio 1 presenta un indicador promedio más alto, pero también muestra mayor dispersión y volatilidad en sus datos (mayor varianza y rango) en comparación con el Sexenio 2.")
