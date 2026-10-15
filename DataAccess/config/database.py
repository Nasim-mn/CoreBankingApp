from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


load_dotenv()


def build_connection_string():
    server = os.getenv("DB_SERVER")
    database_name = os.getenv("CoreBanking")
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    driver = os.getenv("DB_DRIVER")
    return(
        f"mssql+pymssql://{username}:{password}@{server}/{database_name}"
        f"?driver={driver}"
        f"&TrustServerCertificate=yes"

    )

connection_string = build_connection_string()
engine = create_engine(connection_string , echo = True)


sessionmaker = sessionmaker(engine)

@contextmanager
def create_session():
    session = sessionmaker()

    try:
        yield session

    except Exception as ex:
        print(f"Database Exceotion -> {ex.args[0]}")
        raise

    else :
        session.commit()

    finally :
        session.close()
