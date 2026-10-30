import pandas as pd
from sqlalchemy import create_engine, Column, Integer, Date, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker

# Informacion de la conexión a la base de datos de postgreSQL
USER = "diego"
PASSWORD = "123456789"
HOST = "localhost"
PORT = "5432"
DB_NAME = "Examen"

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Definir la clase (tabla 'prueba')
class Prueba(Base):
    __tablename__ = "cotizaciones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    precio = Column(Numeric(10, 4), nullable=False)

# Crear una sesión para interactuar con la BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Rango de fechas basado en los datos insertados
fecha_inicio = "2012-01-01"
fecha_fin = "2018-31-12"

# Realizar la consulta
mi_query = session.query(Prueba).filter(Prueba.fecha.between(fecha_inicio, fecha_fin))
df = pd.read_sql(mi_query.statement, session.bind)

# Cerrar sesión
session.close()

# Calcular estadísticas
media = df['precio'].astype(float).mean()
varianza = df['precio'].astype(float).var()
desviacion_estandar = df['precio'].astype(float).std()

print("Datos recuperados:")
print(df)
print(f"\nMedia: {media:.4f}")
print(f"Varianza: {varianza:.4f}")
print(f"Desviación Estándar: {desviacion_estandar:.4f}")
