# 1. Datos simulados para los dos sexenios
sexenio_1 <- c(2.5, 3.1, 2.8, 4.0, 3.5, 2.9)
sexenio_2 <- c(1.5, 1.8, 1.2, 2.0, 1.7, 1.9)

# 2. Función para calcular todas las métricas solicitadas
calcular_metricas <- function(datos) {
  media <- mean(datos)
  varianza <- var(datos) # R calcula la varianza muestral por defecto
  desv_estandar <- sd(datos)
  maximo <- max(datos)
  minimo <- min(datos)
  rango <- maximo - minimo
  
  return(c(media, varianza, desv_estandar, maximo, minimo, rango))
}

# 3. Construir la tabla (Data Frame)
tabla_resultados <- data.frame(
  Metrica = c("Media", "Varianza", "Desviacion estandar", "Maximo", "Minimo", "Rango"),
  Sexenio_1 = calcular_metricas(sexenio_1),
  Sexenio_2 = calcular_metricas(sexenio_2)
)

# 4. Imprimir los resultados
cat("--- Tabla Comparativa ---\n")
print(tabla_resultados)

cat("\n¿Qué puedes determinar al comparar ambos periodos?\n")
cat("-> El Sexenio 1 presenta un indicador promedio más alto, pero también muestra mayor dispersión en sus datos (mayor varianza y rango) en comparación con el Sexenio 2.\n")
