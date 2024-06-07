from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONFIG_PATH = "app/database/config"


engine = create_engine(
    "sqlite:///./sql_app.db",
    connect_args={
        "check_same_thread": False,
    },
)

LocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()
Base.metadata.create_all(bind=engine)
