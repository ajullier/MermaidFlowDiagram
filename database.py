from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, GraphType  # Asegúrate de importar GraphType

DATABASE_URL = "sqlite:///diagram_app.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Crear todas las tablas
    Base.metadata.create_all(bind=engine)
    
    # Insertar datos iniciales para GraphType
    session = SessionLocal()
    try:
        # Verificar si la tabla GraphType está vacía
        if session.query(GraphType).count() == 0:
            # Definir datos iniciales
            initial_types = [
                GraphType(Code="TD", Description="Top - Down"),
                GraphType(Code="LR", Description="Left - Right"),
                GraphType(Code="RL", Description="Right - Left"),
                GraphType(Code="BT", Description="Botton - Top")
            ]
            
            # Insertar datos
            session.add_all(initial_types)
            session.commit()
            print("Datos iniciales para GraphType insertados correctamente")
    except Exception as e:
        session.rollback()
        print(f"Error al insertar datos iniciales: {e}")
    finally:
        session.close()