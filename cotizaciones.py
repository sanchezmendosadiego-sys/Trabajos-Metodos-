import pandas as pd
from sqlalchemy import create_engine, Column, Integer, Date, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Información de la conexión
USER = "diego"
PASSWORD = "123456789"
HOST = "localhost"
PORT = "5432"
DB_NAME = "cotizacion"

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# 2. Definir la tabla
class Prueba(Base):
    __tablename__ = "cotizaciones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    precio = Column(Numeric(10, 4), nullable=False)

# 3. Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# 4. Realizar la consulta (SIN FILTRO DE FECHAS para traer TODO)
mi_query = session.query(Prueba)
df = pd.read_sql(mi_query.statement, session.bind)

session.close()

# 5. Calcular estadísticas
# dropna() asegura que si hay algún dato vacío en el CSV, no arruine el cálculo
media = df['precio'].dropna().astype(float).mean()
varianza = df['precio'].dropna().astype(float).var()
desviacion_estandar = df['precio'].dropna().astype(float).std()

# 6. Mostrar resultados
print(f"Total de datos recuperados: {len(df)}")
print("\nPrimeras 5 filas de tu tabla:")
print(df.head())

print(f"\n=== RESULTADOS ESTADÍSTICOS ===")
print(f"Media: {media:.4f}")
print(f"Varianza: {varianza:.4f}")
print(f"Desviación Estándar: {desviacion_estandar:.4f}")
