# Cargar las librerías
library(DBI)
library(RPostgres)

# Conectar a la base de datos
conexion <- dbConnect(
  RPostgres::Postgres(),
  dbname = "Examen",
  host = "localhost",
  port = 5432,
  user = "diego",
  password = "123456789"
)

# Obtener los datos
datos <- dbGetQuery(conexion, "SELECT * FROM prueba")
precios <- datos$precio

# Mostrar estadísticas en consola
cat("Media:", mean(precios), "\n")
cat("Varianza:", var(precios), "\n")
cat("Desviación estándar:", sd(precios), "\n\n")

# 1. Visualizar los datos (Guardar gráfica como imagen PNG)
png("evolucion_precios.png")
plot(datos$fecha, datos$precio, type="b", col="blue", pch=19,
     main="Evolución de Precios", xlab="Fecha", ylab="Precio")
dev.off()
cat("✓ Gráfica guardada exitosamente como 'evolucion_precios.png'\n")

# 2. Exportar los resultados (Guardar como archivo CSV)
write.csv(datos, "resultados_prueba.csv", row.names = FALSE)
cat("✓ Datos exportados exitosamente a 'resultados_prueba.csv'\n")

# Cerrar conexión
dbDisconnect(conexion)
